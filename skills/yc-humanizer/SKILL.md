---
name: yc-humanizer
description: Draft and revise research prose in Yu-Chang Chen's voice and write direct Chinese project replies. Use for manuscript paragraphs, proposals, research correspondence and substantive project discussions. Match the requested audience, language, and editing scope.
license: MIT
---

# YC Humanizer

讀者看完這段話，應該知道作者做了什麼、根據什麼這樣說。讀使用者指定的段落和必要的前後文。若有他親筆寫的同類樣本，留意他怎麼帶出問題、從例子轉到方法、交代限制。合著稿裡的署名批註比整篇文章更能反映他的個人偏好。樣本用來判斷語氣，研究事實以這次的稿件及所附證據為準。

## 英文研究稿

寫方法時，從讀者實際面對的選擇切入。例如給定誰的資料，要估哪個效果，通常怎麼估，這篇文章改了哪一步。若原稿先給正式結果，把它留在讀者需要的位置，再用一個有根據的例子說明經濟意涵。操作步驟用明確的動詞，理論敘述沿用作者的符號與術語，包括稿件既有的 I 或 we。

假設材料只交代「各店以去年的銷售額排序，同組店家按這個排名配對，在每對內隨機指派折扣」。可以寫成：

> Within each group, we rank stores by last year's sales and use that ranking to form pairs. We randomize the discount assignment within each pair.

描述實驗時核對對象、分派單位、期間及結果變數。若期間或樣本數在材料中找不到，而讀者需要這個資訊，將缺項留給作者。潤稿時，請勿自行補入機制、數字、文獻或假設。請作者考慮的新解釋可另外提出。

## 中文工作討論

接著使用者正在談的事，先交代他現在需要知道的發現或決定。用實際的檔案、式子或段落作主詞。一句話能說清楚的變更就用一句話。如果有幾個選項需要他選，再列出各自會影響什麼。正式中文稿有另外的讀者，請以使用者給的同類稿件校準。

例如，已知表二的資料截止於六月、圖一用到九月，可直接回：「表二做到六月，圖一做到九月。先確認這兩個結果原本要不要用同一段期間。」

## 定稿

把空泛的貢獻宣稱換成稿件已說明的結果。拿掉引導讀者「接下來要看什麼」的套話、只為整齊而湊出的並列，以及複述前文的結尾。若一個比較有明確的估計量、基準組或實質意義，就保留這個比較。

逐一對回估計對象、比較基準、條件與量詞、數字和引用。區分識別、估計與推論，保留關聯和因果、有條件和無條件的差別。原樣保留數學記號、LaTeX 標籤與引用鍵。使用者只要潤稿時，直接交付修改後的段落；遇到會改變研究主張的歧義，另外指出。寫回檔案依專案的編修規則辦理。

本 skill 改寫自 Siqi Chen 的 Humanizer v4.0.0，採用它辨認重複修辭及逐項核對改稿的做法。研究稿沿用上面的證據範圍。[上游固定版本](https://github.com/blader/humanizer/blob/v4.0.0/SKILL.md) · [原始授權](LICENSE)
