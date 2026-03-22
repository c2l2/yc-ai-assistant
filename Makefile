.PHONY: codex-task-prompt codex-task-next codex-task-resume

TASK ?=
MODEL ?=
RUNNER = python3 scripts/codex_task_runner.py

codex-task-prompt:
	@$(RUNNER) --mode print $(if $(TASK),--task-id $(TASK),) $(if $(MODEL),--model $(MODEL),)

codex-task-next:
	@$(RUNNER) --mode exec $(if $(TASK),--task-id $(TASK),) $(if $(MODEL),--model $(MODEL),)

codex-task-resume:
	@$(RUNNER) --mode resume-last $(if $(TASK),--task-id $(TASK),) $(if $(MODEL),--model $(MODEL),)
