## Why

研究者想讓助手辨認自己怎麼寫不同類型的文章，也希望助手能在證明進稿前與模擬設計階段指出具體問題。

## What Changes

- 將四篇指定作品的寫法及作者日後實際採用的改稿納入寫作校準。
- 在理論工作中提供獨立複核，在正式模擬中先指定要檢查的研究主張與真值。

## Capabilities

### New Capabilities

- `proof-second-reader`: 對指定命題提供獨立複核，指出可查核的推導步驟。
- `simulation-evidence`: 讓正式數值結果可對回估計對象、生成過程和重跑方式。

### Modified Capabilities

- `research-writing-voice`: 根據不同文類的成稿與作者有意採用的改法校準語氣。

## Impact

更新共用源碼中的 `yc-humanizer`、`theory-workbench` 和 `simulation-runner`。各研究專案延後升版。
