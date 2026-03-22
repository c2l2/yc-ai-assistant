#!/usr/bin/env python3

"""Generate and optionally send the next task prompt to Codex CLI."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = REPO_ROOT / "TASKS.md"
SESSION_PATH = REPO_ROOT / "SESSION.md"
DEFAULT_MODEL = os.environ.get("CODEX_MODEL", "")
DEFAULT_CODEX_BIN = os.environ.get("CODEX_BIN", "")


@dataclass
class TaskRow:
    task_id: str
    status: str
    task: str
    output: str
    notes: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pick a task from TASKS.md and send it to Codex CLI."
    )
    parser.add_argument(
        "--task-id",
        help="Run a specific task ID. Defaults to the first in_progress task, then the first todo task.",
    )
    parser.add_argument(
        "--mode",
        choices=["print", "exec", "resume-last"],
        default="print",
        help="Print the prompt, run codex exec, or run codex resume --last.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Optional Codex model name.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        help="Sandbox mode passed to Codex CLI.",
    )
    parser.add_argument(
        "--approval",
        default="on-request",
        help="Approval policy passed to Codex CLI.",
    )
    parser.add_argument(
        "--full-auto",
        action="store_true",
        help="Pass --full-auto to Codex CLI instead of explicit sandbox/approval flags.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def parse_task_rows(markdown: str) -> list[TaskRow]:
    rows: list[TaskRow] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        parts = [part.strip() for part in stripped.split("|")[1:-1]]
        if len(parts) != 5:
            continue
        if parts[0] in {"ID", "---"}:
            continue
        if not re.fullmatch(r"T\d+", parts[0]):
            continue
        rows.append(
            TaskRow(
                task_id=parts[0],
                status=parts[1],
                task=parts[2],
                output=parts[3],
                notes=parts[4],
            )
        )
    return rows


def pick_task(rows: Iterable[TaskRow], requested_id: str | None) -> TaskRow:
    task_rows = list(rows)
    if not task_rows:
        raise ValueError("No task rows found in TASKS.md.")

    if requested_id:
        for row in task_rows:
            if row.task_id == requested_id:
                return row
        raise ValueError(f"Task ID {requested_id} was not found in TASKS.md.")

    for preferred_status in ("in_progress", "todo"):
        for row in task_rows:
            if row.status == preferred_status:
                return row

    raise ValueError("No task with status in_progress or todo is available.")


def extract_recommended_prompt(session_text: str) -> str:
    marker = "## Recommended Next Prompt"
    if marker not in session_text:
        return ""
    section = session_text.split(marker, 1)[1].strip()
    lines = []
    in_fence = False
    for line in section.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            lines.append(line.rstrip())
    return "\n".join(line for line in lines if line).strip()


def build_prompt(task: TaskRow, session_text: str) -> str:
    previous_recommendation = extract_recommended_prompt(session_text)
    lines = [
        "Read TASKS.md and SESSION.md first.",
        f"Work only on {task.task_id} in TASKS.md.",
        f"Task summary: {task.task}",
        f"Expected output or deliverable: {task.output}",
        f"Notes: {task.notes}",
        "If the task is still marked `todo`, mark it `in_progress` when you begin.",
        "When finished, update TASKS.md and SESSION.md.",
        "In SESSION.md, record files changed, decisions made, blockers, and the single best next prompt.",
        "Do not batch other tasks unless TASKS.md explicitly says this task depends on doing so.",
    ]
    if previous_recommendation:
        lines.append("")
        lines.append("Previous recommended prompt from SESSION.md:")
        lines.append(previous_recommendation)
    return "\n".join(lines)


def codex_command(args: argparse.Namespace, prompt: str) -> list[str]:
    codex_bin = resolve_codex_binary()

    command = [codex_bin]
    is_resume = args.mode == "resume-last"
    if is_resume:
        command.extend(["resume", "--last"])
    else:
        command.append("exec")

    command.extend(["-C", str(REPO_ROOT)])

    if args.full_auto:
        command.append("--full-auto")
    else:
        command.extend(["-s", args.sandbox])
        if is_resume:
            command.extend(["-a", args.approval])

    if args.model:
        command.extend(["-m", args.model])

    command.append(prompt)
    return command


def candidate_codex_paths() -> list[Path]:
    candidates: list[Path] = []

    if DEFAULT_CODEX_BIN:
        candidates.append(Path(DEFAULT_CODEX_BIN).expanduser())

    # Common install location when Codex comes from the VS Code extension.
    vscode_root = Path.home() / ".vscode" / "extensions"
    if vscode_root.exists():
        candidates.extend(
            sorted(
                vscode_root.glob(
                    "openai.chatgpt-*/bin/macos-aarch64/codex"
                ),
                reverse=True,
            )
        )
    return candidates


def resolve_codex_binary() -> str:
    if DEFAULT_CODEX_BIN:
        expanded = str(Path(DEFAULT_CODEX_BIN).expanduser())
        if os.path.isfile(expanded) and os.access(expanded, os.X_OK):
            return expanded

    from_path = shutil.which("codex")
    if from_path:
        return from_path

    for candidate in candidate_codex_paths():
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    checked = [str(path) for path in candidate_codex_paths()]
    details = [
        "Could not find `codex`.",
        "Tried PATH lookup and common VS Code extension locations.",
    ]
    if checked:
        details.append("Checked candidates:")
        details.extend(f"- {path}" for path in checked)
    details.append(
        "Set CODEX_BIN=/absolute/path/to/codex if your installation lives elsewhere."
    )
    raise FileNotFoundError("\n".join(details))


def main() -> int:
    args = parse_args()

    try:
        tasks_text = read_text(TASKS_PATH)
        session_text = read_text(SESSION_PATH)
        task = pick_task(parse_task_rows(tasks_text), args.task_id)
        prompt = build_prompt(task, session_text)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.mode == "print":
        print(prompt)
        return 0

    command = codex_command(args, prompt)
    completed = subprocess.run(command, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
