# 研究工作流程驗證

| 請求或操作 | 核對結果 |
| --- | --- |
| 只要求討論方法 | 獨立情境測試得到聊天答覆，未啟動檔案修改。 |
| 授權執行，研究工作區已有相同 change | 接續原研究 change。助手自身的工作區未被選為研究工作區。 |
| 修正單一錯字；另有一項新的跨檔案研究工作 | 前者直接修改；後者委由 AI 決定在使用專案新開 change。 |
| 研究專案第一次使用 Spectra | 在有助手副本的暫存專案中，於論文子目錄實際執行 `spxa init . --tools codex` 和 `spxa list --json`。初始化成功，論文工作區的初始變更清單為空。 |
| 專案初始化和升版 | 將此次 Post-EB 的 `Makefile`、根目錄與論文的 `AGENTS.md` 放入隔離的 Git 專案，設定有兩個版本的本機上游。先將 submodule 取消初始化，執行 `make ai-template-setup` 後核對為指定的第一版。接著在上游建立第二版，再執行 `make ai-template-update`，核對 submodule 已前進至第二版。兩次操作前後，根目錄與論文的指令檔均逐位元相符。 |

`spxa analyze delegate-research-changes --json` 回報零項發現；`spxa validate delegate-research-changes --json` 回報有效且無警告。專案正式釘選的提交由發布程序逐案核對。
