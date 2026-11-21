# research-writing-voice Specification

## Purpose

研究者將草稿交給助手潤稿時，得到符合文類與個人語氣的文句，也能核對原有證據與研究結論。

## Requirements

### Requirement: 依研究者語氣編輯並保留證據

寫作 skill 必須（SHALL）按讀者、文類及作者樣本調整行文，只使用原稿或所附材料支持的事實，保留估計對象、適用條件、數字、引用與主張的強度。

#### Scenario: 調整有條件的研究陳述

- **WHEN** 理論結果依賴指明的識別或抽樣條件
- **THEN** 改稿仍寫出該條件、估計對象及結論的種類。

##### Example: 核對未作為範例的段落

- **GIVEN** 一段同時說明估計步驟、GMM 條件與 delta method 的方法段落
- **WHEN** 研究者要求改得容易讀
- **THEN** 段落仍可對回每個步驟、條件及參數，並保留各段推論方法。

#### Scenario: 中文協作需要作者裁決

- **WHEN** 中文工作訊息需要作者決定表格或圖形到底應採哪個期間
- **THEN** 改稿保留已知月份，直接說明待決選擇。

##### Example: 編輯圖表說明

- **GIVEN** 數據說明列出兩個不同的截止月，尚無核定的共同截止月
- **WHEN** 研究者要一段簡短的工作訊息
- **THEN** 訊息分別寫出兩個截止月，請作者決定是否統一。

<!-- @trace
source: add-yc-humanizer
updated: 2026-11-21
code:
  - skills/yc-humanizer/LICENSE
  - TASKS.md
  - docs/spectra-research.md
  - skills/finalize-weekly-meeting/SKILL.md
  - skills/submission-check/SKILL.md
  - AGENTS.md
  - .spectra.yaml
  - WORKFLOW.md
  - skills/yc-humanizer/SKILL.md
-->

---
### Requirement: 從指定作品與作者改稿校準寫作

寫作助手必須（SHALL）按文類參照指定作品，分辨獨著、合著及可歸屬作者的親筆修改。日後從一篇稿件抽出的通則，須有作者明示或有重複改稿作為提議依據；共用指南的更新依使用者授權辦理。

#### Scenario: 辨認改稿的適用範圍

- **WHEN** 作者修改了研究敘述，而該段也包含本篇專用的符號或結果
- **THEN** 助手區分可跨稿使用的表達習慣和僅適用本案的內容，再依證據與授權決定是否更新共用規則。

##### Example: 調整實證段落

- **GIVEN** 作者多次把空泛的表現描述換成原資料支持的比較，這次也修改本篇特有的變數名稱
- **WHEN** 作者要求整理日後潤稿習慣
- **THEN** 可將交代比較對象及證據列為寫作指引，符號約定留在本篇。

<!-- @trace
source: strengthen-research-skills
updated: 2026-11-21
code:
  - skills/theory-workbench/SKILL.md
  - skills/simulation-runner/SKILL.md
  - skills/yc-humanizer/SKILL.md
  - skills/yc-humanizer/references/research-voice.md
-->