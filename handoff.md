# 南投國中 115 二年級隔宿露營專案交接與進度紀錄 (handoff.md)

- **更新日期**：115 年 10 月 19 日（2026-10-19）
- **專案路徑**：`D:\antigravity\1151019二年級隔宿露營`
- **核心來源**：`1151019-115南投國二露營手冊.pdf`（共 26 頁）
- **線上發布網址**：
  - **GitHub 倉庫**：[https://github.com/yaoshuchin/115-nantou-camping-guide](https://github.com/yaoshuchin/115-nantou-camping-guide)
  - **GitHub Pages 線上簡報版**：[https://yaoshuchin.github.io/115-nantou-camping-guide/](https://yaoshuchin.github.io/115-nantou-camping-guide/)
  - **GitHub Pages 露營手冊網頁版**：[https://yaoshuchin.github.io/115-nantou-camping-guide/handbook.html](https://yaoshuchin.github.io/115-nantou-camping-guide/handbook.html)
  - **Netlify 發布站點**：[http://stirring-sunflower-3236f7.netlify.app](http://stirring-sunflower-3236f7.netlify.app)（手冊網頁版：[http://stirring-sunflower-3236f7.netlify.app/handbook.html](http://stirring-sunflower-3236f7.netlify.app/handbook.html)，預設存取密碼：`My-Drop-Site`）

---

## 📌 一、當前進度與成果紀錄

1. **露營手冊網頁版 (`handbook.html`) 與教學簡報版 (`index.html`) 雙向串聯**：
   - 頂部導覽列提供一鍵跨頁互相切換按鈕。
   - 手冊網頁版採沉浸式雙欄/行動單欄卡片式架構，含快速章節錨點跳轉、浮動回頂部、手冊 PDF 下載按鈕。
   - 包含完整活動日程、隨隊師長、車次配置、27 頂帳篷住宿名單、15 組野炊分組、手冊學習單（含水彈體驗心得分隊檢視表、行前檢查表）。

2. **徹底固化去識別化（完全移除切換按鈕）**：
   - 全體 106 位學生與 11 位教職員姓名第 2 字皆硬編碼為大寫「O」（例：`林O諼`、`劉O彥`）。
   - 完全移除頁面上任何「去個資/解除遮蔽」切換開關，不可從前端還原真實姓名，確保個資 100% 安全合規。

3. **童軍知識卡 5 大單元全面增補圖影教學資源**：
   - **營地建設與屋式帳**：配置營地分區俯瞰圖、帳篷營釘 45 度力學圖，附「屋式帳搭設教學」與「外帳收折口訣教學」YouTube 影片。
   - **童軍常用八大繩結**：
     - 單結、八字結、活結、平結、接繩結、雙套結、雙半結、營繩結等 8 個子單元。
     - 各配 1 張高清線條/結法圖解與 1 個對應結法 YouTube 教學影片。
   - **自然方向辨識**：
     - 指南針 16 方位盤、手錶太陽時針折半法、北極星（北斗七星/仙后座）定向法、年輪與向日葵向光性 4 個子單元。
     - 各配 1 張圖解與 1 個野外定向 YouTube 教學影片。
   - **野外簡易急救處置**：
     - 割傷加壓止血、小腿抽筋反向伸展、流鼻血頭微前傾捏鼻翼、骨折超關節夾板固定 4 個子單元。
     - 各配 1 張急救步驟圖解與 1 個紅十字會急救 SOP YouTube 影片。
   - **臺灣六大毒蛇與急救「五要五不」**：
     - 百步蛇外觀鑑別、雨傘節外觀鑑別、六大毒蛇圖鑑、毒蛇咬傷五要五不 SOP 4 個子單元。
     - 各配 1 張毒蛇實照/圖鑑與 1 個毒蛇急救宣導 YouTube 影片。

4. **雲端同步與雙重發布**：
   - **GitHub**：更新已推送至遠端 `main` 分支，GitHub Pages 已更新上線。
   - **Netlify**：靜態資源（含 `assets/` 70 餘張圖片圖鑑）已完整上傳部署至最新站點。

---

## 🎯 二、後續可擴充項目

1. 匯出 Excel 全功能行政彙整總表（.xlsx）。
2. 匯出各班導師隨身手冊與點名簽到單（.docx / PDF）。
3. 建立行前家長須知與活動推播通知圖卡。
