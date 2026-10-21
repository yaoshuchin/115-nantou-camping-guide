# -*- coding: utf-8 -*-
"""
生成南投國中 115 二年級隔宿露營網頁式簡報 index.html
1. 移除去個資切換按鈕，直接固化所有姓名第二字為 "O"
2. 童軍知識卡（營地建設與屋式帳、八大繩結、自然方向辨識、簡易急救、臺灣六大毒蛇與五要五不）均配置圖片與影片連結
3. 頂部提供切換至「📖 手冊網頁版 (handbook.html)」的連結
"""
import json

with open("students_data.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for s in students:
    assert s["name"][1] == "O", f"Error in masking: {s['name']}"

students_js = json.dumps(students, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>南投國中 115 學年度二年級戶外教育（隔宿露營）教學簡報</title>
  <style>
    :root, [data-theme="green"] {{
      --primary: #15803d;
      --primary-light: #22c55e;
      --primary-dark: #14532d;
      --accent: #16a34a;
      --accent-light: #4ade80;
      --gold: #d97706;
      --bg: #f2fbf5;
      --body-gradient: radial-gradient(circle at 10% 10%, #dcfce7 0%, #f0fdf4 60%, #ecfdf5 100%);
      --card-bg: #ffffff;
      --card-border: #bbf7d0;
      --card-shadow: 0 15px 35px -5px rgba(22, 101, 52, 0.08);
      --text: #14532d;
      --text-body: #1e293b;
      --text-muted: #4b6b55;
      --topbar-bg: rgba(240, 253, 244, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    [data-theme="purple"] {{
      --primary: #7e22ce;
      --primary-light: #a855f7;
      --primary-dark: #581c87;
      --accent: #9333ea;
      --accent-light: #c084fc;
      --gold: #d97706;
      --bg: #faf5ff;
      --body-gradient: radial-gradient(circle at 10% 10%, #f3e8ff 0%, #faf5ff 60%, #f5f3ff 100%);
      --card-bg: #ffffff;
      --card-border: #e9d5ff;
      --card-shadow: 0 15px 35px -5px rgba(126, 34, 206, 0.08);
      --text: #581c87;
      --text-body: #1e293b;
      --text-muted: #6b21a8;
      --topbar-bg: rgba(250, 245, 255, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    [data-theme="red"] {{
      --primary: #e11d48;
      --primary-light: #fb7185;
      --primary-dark: #9f1239;
      --accent: #be123c;
      --accent-light: #fda4af;
      --gold: #d97706;
      --bg: #fff1f2;
      --body-gradient: radial-gradient(circle at 10% 10%, #ffe4e6 0%, #fff1f2 60%, #fff5f5 100%);
      --card-bg: #ffffff;
      --card-border: #fecdd3;
      --card-shadow: 0 15px 35px -5px rgba(225, 29, 72, 0.08);
      --text: #9f1239;
      --text-body: #1e293b;
      --text-muted: #881337;
      --topbar-bg: rgba(255, 241, 242, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    [data-theme="blue"] {{
      --primary: #0284c7;
      --primary-light: #38bdf8;
      --primary-dark: #0369a1;
      --accent: #0284c7;
      --accent-light: #7dd3fc;
      --gold: #d97706;
      --bg: #f0f9ff;
      --body-gradient: radial-gradient(circle at 10% 10%, #e0f2fe 0%, #f0f9ff 60%, #e0f7fa 100%);
      --card-bg: #ffffff;
      --card-border: #bae6fd;
      --card-shadow: 0 15px 35px -5px rgba(3, 105, 161, 0.08);
      --text: #0369a1;
      --text-body: #1e293b;
      --text-muted: #075985;
      --topbar-bg: rgba(240, 249, 255, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    [data-theme="gray"] {{
      --primary: #475569;
      --primary-light: #94a3b8;
      --primary-dark: #1e293b;
      --accent: #334155;
      --accent-light: #cbd5e1;
      --gold: #d97706;
      --bg: #f8fafc;
      --body-gradient: radial-gradient(circle at 10% 10%, #f1f5f9 0%, #f8fafc 60%, #e2e8f0 100%);
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --card-shadow: 0 15px 35px -5px rgba(30, 41, 59, 0.08);
      --text: #1e293b;
      --text-body: #1e293b;
      --text-muted: #475569;
      --topbar-bg: rgba(248, 250, 252, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    [data-theme="orange"] {{
      --primary: #d97706;
      --primary-light: #fbbf24;
      --primary-dark: #92400e;
      --accent: #b45309;
      --accent-light: #fde68a;
      --gold: #b45309;
      --bg: #fffbeb;
      --body-gradient: radial-gradient(circle at 10% 10%, #fef3c7 0%, #fffbeb 60%, #fff7ed 100%);
      --card-bg: #ffffff;
      --card-border: #fde68a;
      --card-shadow: 0 15px 35px -5px rgba(180, 83, 9, 0.08);
      --text: #92400e;
      --text-body: #1e293b;
      --text-muted: #78350f;
      --topbar-bg: rgba(255, 251, 235, 0.95);
      --highlight: #0284c7;
      --danger: #dc2626;
      --success: #16a34a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-main);
      background: var(--body-gradient);
      color: var(--text-body);
      min-height: 100vh;
      overflow-x: hidden;
      transition: background 0.3s ease;
    }}

    /* Top Header Bar */
    header.top-bar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 60px;
      background: var(--topbar-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.25rem;
      z-index: 1000;
      transition: all 0.3s ease;
    }}

    .logo-group {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .badge-tag {{
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      color: #fff;
      font-size: 0.75rem;
      font-weight: bold;
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      letter-spacing: 0.5px;
    }}
    .header-title {{
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--primary-dark);
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .btn {{
      background: #ffffff;
      border: 1.5px solid var(--card-border);
      color: var(--primary-dark);
      padding: 0.4rem 0.8rem;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }}
    .btn:hover {{
      background: var(--bg);
      border-color: var(--primary);
      transform: translateY(-1px);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, var(--primary-light), var(--primary));
      border: 1px solid var(--primary);
      color: #fff;
      font-weight: 600;
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, var(--primary), var(--primary-dark));
      color: #fff;
    }}

    /* Floating Navigation Controls */
    .side-nav-btn {{
      position: fixed;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 80px;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(8px);
      border: 1.5px solid var(--card-border);
      color: var(--primary-dark);
      font-size: 1.5rem;
      font-weight: 900;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1050;
      transition: all 0.25s ease;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
      user-select: none;
    }}
    .side-nav-prev {{ left: 16px; }}
    .side-nav-next {{ right: 16px; }}
    .side-nav-btn:hover {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary-light);
      transform: translateY(-50%) scale(1.08);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.18);
    }}

    .btn-video {{
      background: #fef2f2;
      border: 1px solid #fecaca;
      color: #dc2626;
      font-weight: 600;
      font-size: 0.8rem;
      padding: 0.3rem 0.65rem;
      border-radius: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      transition: all 0.2s ease;
      margin-top: 0.45rem;
    }}
    .btn-video:hover {{
      background: #dc2626;
      color: #fff;
      border-color: #dc2626;
    }}

    /* Progress bar */
    .progress-bar-container {{
      position: fixed;
      top: 60px;
      left: 0;
      right: 0;
      height: 4px;
      background: #dcfce7;
      z-index: 999;
    }}
    .progress-bar-fill {{
      height: 100%;
      width: 6.25%;
      background: linear-gradient(90deg, #16a34a, #22c55e);
      transition: width 0.3s ease;
    }}

    /* Main Viewport Container */
    main.viewport {{
      margin-top: 64px;
      min-height: calc(100vh - 64px);
      position: relative;
    }}

    /* Presentation Slide Deck */
    .slide-deck {{
      position: relative;
      width: 100vw;
      min-height: calc(100vh - 124px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem 2rem 5rem 2rem;
    }}

    .slide {{
      display: none;
      width: 100%;
      max-width: 1200px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 2.2rem 2.8rem;
      box-shadow: 0 15px 40px rgba(22, 101, 52, 0.08);
      animation: fadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .slide.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(14px) scale(0.99); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    /* Slide Header */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #e2f5e9;
      padding-bottom: 1rem;
      margin-bottom: 1.5rem;
    }}
    .slide-category {{
      font-size: 0.85rem;
      text-transform: uppercase;
      color: var(--accent);
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 0.25rem;
    }}
    .slide-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #14532d;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .slide-num {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #166534;
      background: #dcfce7;
      padding: 0.3rem 0.8rem;
      border-radius: 8px;
    }}

    /* Grids & Cards */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-top: 1rem;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.2rem;
      margin-top: 1rem;
    }}
    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 1rem;
      margin-top: 1rem;
    }}

    .card {{
      background: #f8fdf9;
      border: 1px solid #dcfce7;
      border-radius: 12px;
      padding: 1.15rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .card:hover {{
      background: #ffffff;
      border-color: #86efac;
      box-shadow: 0 6px 16px rgba(22, 101, 52, 0.08);
      transform: translateY(-2px);
    }}
    .card-highlight {{
      border-left: 4px solid var(--accent);
    }}
    .card-info {{
      border-left: 4px solid var(--highlight);
    }}
    .card-success {{
      border-left: 4px solid var(--success);
    }}
    .card-danger {{
      border-left: 4px solid var(--danger);
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #14532d;
      margin-bottom: 0.4rem;
    }}

    /* Media Box */
    .media-box {{
      width: 100%;
      height: 140px;
      border-radius: 8px;
      overflow: hidden;
      background: #f0fdf4;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0.6rem 0;
      border: 1px solid var(--card-border);
    }}
    .media-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}

    /* Tables */
    .table-responsive {{
      width: 100%;
      overflow-x: auto;
      margin: 1rem 0;
      border-radius: 10px;
      border: 1px solid var(--card-border);
    }}
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }}
    table.data-table th {{
      background: #dcfce7;
      color: #14532d;
      padding: 0.8rem 1rem;
      font-weight: 700;
      border-bottom: 2px solid #86efac;
      white-space: nowrap;
    }}
    table.data-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #e2e8f0;
      color: var(--text-body);
    }}
    table.data-table tr:hover td {{
      background: #f0fdf4;
    }}

    /* Pills & Badges */
    .pill {{
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 6px;
      margin: 0.15rem 0.2rem;
      background: #dcfce7;
      color: #14532d;
    }}
    .pill-boy {{
      background: #e0f2fe;
      border: 1px solid #bae6fd;
      color: #0369a1;
    }}
    .pill-girl {{
      background: #fce7f3;
      border: 1px solid #fbcfe8;
      color: #be185d;
    }}
    .pill-veg {{
      background: #dcfce7;
      border: 1px solid #86efac;
      color: #15803d;
    }}
    .pill-accent {{
      background: #fef3c7;
      border: 1px solid #fde68a;
      color: #b45309;
    }}

    /* Bottom Navigation Bar */
    .bottom-nav {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 60px;
      background: rgba(240, 253, 244, 0.94);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 1000;
    }}

    .nav-btn-group {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .slide-indicator {{
      font-weight: 600;
      font-size: 0.9rem;
      color: #166534;
    }}

    /* Teacher notes drawer */
    .notes-drawer {{
      position: fixed;
      bottom: 60px;
      left: 0;
      right: 0;
      background: #ffffff;
      border-top: 3px solid #16a34a;
      padding: 1.25rem 2rem;
      max-height: 250px;
      overflow-y: auto;
      z-index: 998;
      display: none;
      box-shadow: 0 -10px 30px rgba(22, 101, 52, 0.1);
      color: #1e293b;
    }}
    .notes-drawer.open {{
      display: block;
      animation: slideUp 0.25s ease;
    }}
    @keyframes slideUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}
    .notes-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #15803d;
      margin-bottom: 0.4rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* Modal Directory */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 2000;
      padding: 1.5rem;
    }}
    .modal-overlay.open {{
      display: flex;
    }}
    .modal-box {{
      background: #ffffff;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      width: 100%;
      max-width: 900px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 2rem;
      box-shadow: 0 25px 50px -12px rgba(22, 101, 52, 0.15);
      color: #1e293b;
    }}
    .modal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    .modal-card {{
      background: #f0fdf4;
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 1rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .modal-card.current-active {{
      background: var(--bg) !important;
      border: 2px solid var(--primary) !important;
      box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.2);
    }}
    .modal-card:hover {{
      background: #dcfce7;
      border-color: #16a34a;
      transform: translateY(-2px);
    }}

    /* Search & Filter Component */
    .search-bar-wrap {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      align-items: center;
      background: #f0fdf4;
      padding: 1rem;
      border-radius: 12px;
      margin-bottom: 1.25rem;
      border: 1px solid var(--card-border);
    }}
    .input-text {{
      background: #ffffff;
      border: 1.5px solid #86efac;
      color: #14532d;
      padding: 0.6rem 1rem;
      border-radius: 8px;
      font-size: 0.95rem;
      min-width: 220px;
      flex: 1;
    }}
    .input-text:focus {{
      outline: none;
      border-color: #16a34a;
      box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2);
    }}
    .select-dropdown {{
      background: #ffffff;
      border: 1.5px solid #86efac;
      color: #14532d;
      padding: 0.6rem 0.9rem;
      border-radius: 8px;
      font-size: 0.9rem;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- Top Bar -->
  <header class="top-bar">
    <div class="logo-group">
      <span class="badge-tag">教學簡報版</span>
      <span class="header-title">南投國中 115 學年度二年級隔宿露營簡報</span>
    </div>
    <div class="header-controls">
      <!-- 🎨 背景主題切換 -->
      <div style="display:flex; align-items:center; gap:0.35rem; background:rgba(255,255,255,0.85); padding:0.25rem 0.6rem; border-radius:8px; border:1px solid var(--card-border);">
        <span style="font-size:0.85rem; font-weight:700; color:var(--primary-dark);">🎨 背景：</span>
        <select id="themeSelector" onchange="changeTheme(this.value)" style="border:none; background:transparent; font-size:0.85rem; font-weight:700; color:var(--primary-dark); cursor:pointer; outline:none;">
          <option value="green">🌿 淡綠 (預設)</option>
          <option value="purple">🍇 淡紫</option>
          <option value="red">🌸 淡紅</option>
          <option value="blue">🌊 淡藍</option>
          <option value="gray">🌫️ 淺灰</option>
          <option value="orange">🍊 淺橙</option>
        </select>
      </div>

      <!-- 快速上一頁與下一頁功能鍵 -->
      <div style="display:flex; align-items:center; gap:0.25rem;">
        <button class="btn" onclick="prevSlide()" title="上一張 (←)" style="padding:0.4rem 0.65rem; font-weight:700;">◀ 上一頁</button>
        <button class="btn" onclick="nextSlide()" title="下一張 (→)" style="padding:0.4rem 0.65rem; font-weight:700;">下一頁 ▶</button>
      </div>

      <a href="handbook.html" class="btn">📖 前往手冊網頁版</a>
      <button class="btn" id="btnOpenIndex" onclick="openDirectory()">📑 目錄總覽</button>
      <button class="btn" id="btnNotes" onclick="toggleNotes()">💡 教學重點</button>
      <button class="btn btn-primary" id="btnFullscreen" onclick="toggleFullscreen()">⛶ 全螢幕放映</button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="progressBar"></div>
  </div>

  <!-- Viewport Slide Deck -->
  <main class="viewport">
    <div class="slide-deck" id="slideDeck">

      <!-- SLIDE 1: 封面 -->
      <section class="slide active" id="slide-1">
        <div class="slide-header">
          <div>
            <div class="slide-category">南投縣立南投國民中學 115 學年度</div>
            <div class="slide-title">🏕️ 二年級戶外教育活動（隔宿露營）手冊與教學簡報</div>
          </div>
          <div class="slide-num">01 / 17</div>
        </div>
        <div style="text-align: center; padding: 2rem 1rem;">
          <h2 style="font-size: 2.2rem; color: var(--gold); margin-bottom: 1rem; font-weight: 800;">
            ～好 戲 開 鑼・探 索 自 我～
          </h2>
          <p style="font-size: 1.25rem; color: #334155; max-width: 800px; margin: 0 auto 2rem auto; line-height: 1.8;">
            在做中學（Learning by Doing）實踐童軍互助精神，淬鍊自立自強生活體驗，凝聚班級榮譽與團隊默契！
          </p>
          <div class="grid-3" style="max-width: 950px; margin: 0 auto;">
            <div class="card card-highlight">
              <div class="card-title">📅 活動日期</div>
              <p style="font-size: 1.15rem; font-weight: 700; color: #fff;">115 年 10 月 27 日（二）<br>至 10 月 28 日（三）</p>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.4rem;">兩天一夜露營體驗</p>
            </div>
            <div class="card card-info">
              <div class="card-title">📍 活動地點</div>
              <p style="font-size: 1.15rem; font-weight: 700; color: #fff;">台南-尖山埤露營區</p>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.4rem;">柳營區旭山里 60 號 (06-6233888)</p>
            </div>
            <div class="card card-success">
              <div class="card-title">👥 參與規模</div>
              <p style="font-size: 1.15rem; font-weight: 700; color: #fff;">師生共計 117 人</p>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.4rem;">學生 107 人（男 48、女 59）+ 師長 10 人</p>
            </div>
          </div>
          <div style="margin-top: 2.5rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <span class="pill pill-accent" style="font-size: 0.95rem; padding: 0.5rem 1rem;">主辦單位：南投縣立南投國中</span>
            <span class="pill pill-accent" style="font-size: 0.95rem; padding: 0.5rem 1rem;">承辦單位：中國青年旅行社中部分公司</span>
            <span class="pill pill-accent" style="font-size: 0.95rem; padding: 0.5rem 1rem;">團控經理：邱O凱 0972-721756</span>
          </div>
        </div>
      </section>

      <!-- SLIDE 2: 實施計畫與重要須知 -->
      <section class="slide" id="slide-2">
        <div class="slide-header">
          <div>
            <div class="slide-category">活動方針與規範</div>
            <div class="slide-title">📋 隔宿露營實施計畫與教育宗旨</div>
          </div>
          <div class="slide-num">02 / 17</div>
        </div>
        <div class="grid-2">
          <div class="card card-highlight">
            <div class="card-title">🎯 活動三大教育主軸</div>
            <ul style="padding-left: 1.4rem; line-height: 1.9; font-size: 1rem;">
              <li><strong>生活教育</strong>：實踐國民須知，培養勤儉、服務、守法、合群與自我打理精神。</li>
              <li><strong>技能教育</strong>：落實童軍實作技能（生火、野炊、帳棚搭設、繩結、急救包紮）。</li>
              <li><strong>團體活動</strong>：小隊聯誼、團隊探索教育、山訓垂降挑戰、營火晚會凝聚向心力。</li>
            </ul>
          </div>
          <div class="card card-info">
            <div class="card-title">⏱️ 集合與返校作息</div>
            <ul style="padding-left: 1.4rem; line-height: 1.9; font-size: 1rem;">
              <li><strong>出發報到</strong>：115 年 10 月 27 日（二）上午 <strong>07:30 校園集合</strong>，08:00 準時出發。</li>
              <li><strong>集合演練</strong>：921 地震公園暨南投國際會展中心園區逃生避難演練。</li>
              <li><strong>活動賦歸</strong>：115 年 10 月 28 日（三）下午 <strong>16:20 預計返抵南投國中</strong>。</li>
              <li><strong>服裝規範</strong>：請一律著學校規定之運動服裝、運動球鞋。</li>
            </ul>
          </div>
        </div>
        <div class="card card-success" style="margin-top: 1.25rem;">
          <div class="card-title">🛡️ 安全管理與平安守則</div>
          <p style="line-height: 1.7; font-size: 0.95rem;">
            活動採中隊競賽與班級小隊自治管理，落實「全員投保平安保險」、「乘車安全檢查」、「活動場域排查」與「醫護急救站隨行常駐」。各小隊活動嚴禁脫隊、私自離營或前往非指定水域，時時刻刻以安全為第一優先！
          </p>
        </div>
      </section>

            <!-- SLIDE 3: 10/23 行前說明會重點宣導 -->
      <section class="slide" id="slide-3">
        <div class="slide-header">
          <div>
            <div class="slide-category">重要生活紀律宣導</div>
            <div class="slide-title">📢 10/23（五）隔宿露營行前說明會四大重點</div>
          </div>
          <div class="slide-num">03 / 17</div>
        </div>
        <div class="grid-2">
          <!-- Card 1: 違禁品清查 -->
          <div class="card card-danger">
            <div class="card-title">🚫 一、違禁品嚴格清查（出發前務必再檢查一次）</div>
            <p style="line-height: 1.7; font-size: 0.95rem; margin-top: 0.3rem;">
              • <strong>嚴禁攜帶物品</strong>：菸品、電子菸、酒精飲品、檳榔、各類刀械利器、打火機、煙火爆竹或具危險性之物品。<br>
              • <strong>行前再次清查</strong>：10/23 說明會後及出發前，請導師與家長協助再次徹底檢查學生背包行李，入營後亦會實施嚴密安全檢查。
            </p>
          </div>
          <!-- Card 2: 個人物品與手機保管 -->
          <div class="card card-info">
            <div class="card-title">📱 二、個人隨身物品規範與手機統一保管</div>
            <p style="line-height: 1.7; font-size: 0.95rem; margin-top: 0.3rem;">
              • <strong>個人必帶物品</strong>：健保 IC 卡、個人常備醫藥、<strong>零用錢限制在 600 元以內</strong>（切勿帶過多現鈔）、<strong>學校體育服（供晚上洗澡後就寢穿著）</strong>。<br>
              • <strong>手機集中保管</strong>：活動期間手機一律由學校與隨車導師集中統一保管，<strong>每晚預計開放約 1 小時</strong>讓同學向家長撥打電話報平安，通話後立即繳回。
            </p>
          </div>
          <!-- Card 3: 服裝儀容規定 -->
          <div class="card card-highlight">
            <div class="card-title">👕 三、服裝儀容規定（畢旅服裝看本次表現！）</div>
            <p style="line-height: 1.7; font-size: 0.95rem; margin-top: 0.3rem;">
              • <strong>日間活動穿著</strong>：穿著休閒便服或各班班服，下半身一律穿著「<strong>深色長褲</strong>」（防蚊蟲叮咬與林間攀爬劃傷），嚴禁穿著拖鞋或涼鞋走動。<br>
              • <strong>與畢業旅行連動</strong>：本次隔宿露營的全校生活常規與紀律遵守狀況，將作為<strong>三年級畢業旅行服裝穿著開放之重要評估指標</strong>（畢旅服裝看表現）！
            </p>
          </div>
          <!-- Card 4: 機動車即刻送回學校 -->
          <div class="card card-danger" style="border: 2px solid #ef4444; background: #fff5f5;">
            <div class="card-title" style="color: #b91c1c;">🚨 四、機動車即刻遣返機制（記大過處分！）</div>
            <p style="line-height: 1.7; font-size: 0.95rem; margin-top: 0.3rem; color: #7f1d1d;">
              • <strong>嚴厲紀律底線</strong>：露營期間凡違犯重大校規之行為（包含：<strong>打架滋事、抽菸、喝酒、嚼食檳榔等</strong>），營區將一律啟動「<strong>機動車即刻送回學校</strong>」！<br>
              • <strong>家長帶回管教</strong>：立即通知家長親自到校帶回管教，並依校規召開學生獎懲委員會，<strong>一律予以「記大過處分」</strong>，絕不寬貸！
            </p>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 攜帶裝備自我檢核清單 -->
      <section class="slide" id="slide-4">
        <div class="slide-header">
          <div>
            <div class="slide-category">行前準備 CheckList</div>
            <div class="slide-title">🎒 想一想，準備好了，出發！攜帶物品自我檢核</div>
          </div>
          <div class="slide-num">04 / 17</div>
        </div>
        <div class="grid-4">
          <div class="card">
            <div class="card-title">🪪 重要證件</div>
            <ul style="list-style: none; line-height: 1.8; font-size: 0.95rem;">
              <li>☑️ <strong>健保 IC 卡（必備首選）</strong></li>
              <li>☑️ 少許零錢（勿帶過多現鈔）</li>
              <li>☑️ 備用電話卡 / 學生證</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-title">👕 衣物與穿著</div>
            <ul style="list-style: none; line-height: 1.8; font-size: 0.95rem;">
              <li>☑️ 學校規定運動服裝一套</li>
              <li>☑️ 換洗衣物 1~2 套、內衣褲</li>
              <li>☑️ 保暖薄外套、禦寒防風衣</li>
              <li>☑️ 運動鞋（禁皮鞋/涼鞋）、拖鞋</li>
              <li>☑️ 多備 2~3 雙透氣襪子</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-title">🧴 盥洗與個人衛生</div>
            <ul style="list-style: none; line-height: 1.8; font-size: 0.95rem;">
              <li>☑️ 牙刷、牙膏、洗臉毛巾</li>
              <li>☑️ 衛生紙、隨身濕紙巾</li>
              <li>☑️ 乾淨塑膠袋 3~5 個（裝髒衣物）</li>
              <li>☑️ 隨身防護口罩 2~3 片</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-title">🔦 防護與生活備品</div>
            <ul style="list-style: none; line-height: 1.8; font-size: 0.95rem;">
              <li>☑️ <strong>手電筒（夜間查舖與安全必備）</strong></li>
              <li>☑️ 輕便型雨衣、折疊雨傘</li>
              <li>☑️ 遮陽帽、防曬用品</li>
              <li>☑️ 水壺 / 環保隨手杯</li>
              <li>☑️ 個人常用藥品（暈車藥、過敏藥）</li>
            </ul>
          </div>
        </div>
        <div class="card card-danger" style="margin-top: 1.25rem;">
          <div class="card-title">⚠️ 攜帶管制注意事項（嚴格禁止攜帶）</div>
          <p style="font-size: 0.92rem; line-height: 1.6;">
            ❌ 嚴禁穿戴有礙活動進行之飾品：項鍊、戒指、手鐲、長垂耳環、皮鞋、裙子。<br>
            ❌ 嚴禁攜帶危險物品（打火機、刀械、煙火炮竹）、菸酒、高額現金與昂貴電子遊戲機。手機請依學校管理辦法配合導師統一保管。
          </p>
        </div>
      </section>

      <!-- SLIDE 17: 活動日程表 -->
      <section class="slide" id="slide-5">
        <div class="slide-header">
          <div>
            <div class="slide-category">兩天一夜精實行程</div>
            <div class="slide-title">📅 活動日程與課程時刻總表</div>
          </div>
          <div class="slide-num">05 / 17</div>
        </div>
        <div class="grid-2">
          <!-- Day 1 -->
          <div class="card card-highlight">
            <div class="card-title">🌄 第一天：115 年 10 月 27 日（二）</div>
            <div class="table-responsive" style="margin: 0.5rem 0;">
              <table class="data-table">
                <tr><th>時間</th><th>活動項目</th><th>備註與內容</th></tr>
                <tr><td>07:30-08:00</td><td>學校集合</td><td>921地震公園逃生演練</td></tr>
                <tr><td>08:00-10:00</td><td>乘車出發</td><td>國道行車、安全檢查</td></tr>
                <tr><td>10:00-11:00</td><td>喜相逢</td><td>營地環境認識、小隊編組</td></tr>
                <tr><td>11:00-12:00</td><td>始業式</td><td>營規介紹、工作人員介紹</td></tr>
                <tr><td>12:00-13:00</td><td>午餐時間</td><td>中式美味便當</td></tr>
                <tr><td>13:00-14:00</td><td>野營常識</td><td>搭帳教學、器材使用領取</td></tr>
                <tr><td>14:00-17:00</td><td><strong>童軍技能教育</strong></td><td>生火烹調、繩結、毒蛇、偽裝</td></tr>
                <tr><td>17:00-19:00</td><td><strong>晚餐(野炊)</strong></td><td>炊事競賽、小隊互助合作</td></tr>
                <tr><td>19:10-21:30</td><td><strong>營火晚會</strong></td><td>班級節目、隊輔熱舞、燭光夜語</td></tr>
                <tr><td>21:30-22:30</td><td>盥洗、宵夜</td><td>整理儀容、享用宵夜</td></tr>
                <tr><td>22:30-----</td><td>就寢＆查舖</td><td>清點人數、熄燈安歇</td></tr>
              </table>
            </div>
          </div>
          <!-- Day 2 -->
          <div class="card card-info">
            <div class="card-title">🌅 第二天：115 年 10 月 28 日（三）</div>
            <div class="table-responsive" style="margin: 0.5rem 0;">
              <table class="data-table">
                <tr><th>時間</th><th>活動項目</th><th>備註與內容</th></tr>
                <tr><td>06:00-06:30</td><td>起床號</td><td>做個跟太陽賽跑的人</td></tr>
                <tr><td>06:30-07:20</td><td>活力有氧</td><td>早操晨檢、內務檢查</td></tr>
                <tr><td>07:20-08:00</td><td>美味早餐</td><td>中式合菜元氣早餐</td></tr>
                <tr><td>08:00-11:30</td><td><strong>山訓與探索教育</strong></td><td>垂降、攀岩、水彈、獨木橋、跳繩</td></tr>
                <tr><td>11:30-14:00</td><td>BBQ 烤肉午餐</td><td>戶外野趣烤肉餐</td></tr>
                <tr><td>14:00-15:00</td><td><strong>結訓典禮</strong></td><td>炊事、晚會、生活教育、總錦標頒獎</td></tr>
                <tr><td>15:00-16:20</td><td>平安抵校</td><td>互道珍重，預計抵校 16:20</td></tr>
              </table>
            </div>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 工作人員一覽表 -->
      <section class="slide" id="slide-6">
        <div class="slide-header">
          <div>
            <div class="slide-category">行政隨隊與導師陣容</div>
            <div class="slide-title">👨‍🏫 工作人員與隨隊導師一覽表</div>
          </div>
          <div class="slide-num">06 / 17</div>
        </div>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>職稱</th><th>師長姓名</th><th>男生</th><th>女生</th><th>合計</th><th>乘車車次</th><th>職掌與守則</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><strong>校長</strong></td><td>劉O彥</td><td>-</td><td>-</td><td>-</td><td><span class="pill pill-accent">全校巡察</span></td><td>整體活動最高指揮與巡視關懷</td></tr>
              <tr><td><strong>學務主任</strong></td><td>董O遠</td><td>-</td><td>-</td><td>-</td><td><span class="pill pill-accent">1 車</span></td><td>第 1 車隨車總指揮、全隊秩序與安全督導</td></tr>
              <tr><td><strong>訓育組長</strong></td><td>姚O勤</td><td>-</td><td>-</td><td>-</td><td><span class="pill pill-accent">丁 車</span></td><td>第 丁 車隨車主管、活動時程與行程協調</td></tr>
              <tr><td><strong>801 導師</strong></td><td>黃O月</td><td>10</td><td>7</td><td>17</td><td><span class="pill">3 車</span></td><td>801 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>802 導師</strong></td><td>黃O君</td><td>6</td><td>13</td><td>19</td><td><span class="pill">2 車</span></td><td>802 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>803 導師</strong></td><td>林O玟</td><td>6</td><td>9</td><td>15</td><td><span class="pill">3 車</span></td><td>803 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>804 導師</strong></td><td>李O儒</td><td>7</td><td>8</td><td>15</td><td><span class="pill">2 車</span></td><td>804 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>805 導師</strong></td><td>林O銓</td><td>7</td><td>4</td><td>11</td><td><span class="pill">1 車</span></td><td>805 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>806 導師</strong></td><td>許O玉</td><td>4</td><td>5</td><td>9</td><td><span class="pill">1 車</span></td><td>806 班生活照護、點名查舖、野炊指導</td></tr>
              <tr><td><strong>807 導師</strong></td><td>黃O慧</td><td>8</td><td>13</td><td>21</td><td><span class="pill">丁 車</span></td><td>807 班生活照護、點名查舖、野炊指導</td></tr>
              <tr style="background: rgba(255, 255, 255, 0.08); font-weight: bold;">
                <td><strong>團控經理</strong></td><td>邱O凱</td><td>48</td><td>59</td><td>107</td><td><span class="pill pill-accent">全隊機動</span></td><td>旅行社領隊、隊輔調度、安全戒護總負責</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">
          * 學生合計 107 人（男生 48 人、女生 59 人），隨隊教職員合計 10 人。所有師生姓名第二個字均已寫為「O」。
        </p>
      </section>

      <!-- SLIDE 17: 車次分配表 -->
      <section class="slide" id="slide-7">
        <div class="slide-header">
          <div>
            <div class="slide-category">交通乘車編組</div>
            <div class="slide-title">🚌 車次分配與隨車配置表</div>
          </div>
          <div class="slide-num">07 / 17</div>
        </div>
        <div class="grid-4">
          <!-- 車次 1 -->
          <div class="card card-highlight">
            <div class="card-title">🚍 第 1 車（共 20 學生）</div>
            <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>隨車師長：</strong>董O遠主任、林O銓老師、許O玉老師</p>
            <div style="background: rgba(0,0,0,0.2); padding: 0.75rem; border-radius: 8px; font-size: 0.88rem; line-height: 1.6;">
              <strong>805 班（11 人）</strong>：男 7、女 4<br>
              <strong>806 班（9 人）</strong>：男 4、女 5
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">亮點：含全校 1 位素食同學（805班 張O瑜）</p>
          </div>
          <!-- 車次 2 -->
          <div class="card card-info">
            <div class="card-title">🚍 第 2 車（共 34 學生）</div>
            <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>隨車師長：</strong>黃O君老師、李O儒老師</p>
            <div style="background: rgba(0,0,0,0.2); padding: 0.75rem; border-radius: 8px; font-size: 0.88rem; line-height: 1.6;">
              <strong>802 班（19 人）</strong>：男 6、女 13<br>
              <strong>804 班（15 人）</strong>：男 7、女 8
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">人數最多車輛之一，配置兩位隨車導師全權照護</p>
          </div>
          <!-- 車次 3 -->
          <div class="card card-success">
            <div class="card-title">🚍 第 3 車（共 32 學生）</div>
            <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>隨車師長：</strong>黃O月老師、林O玟老師</p>
            <div style="background: rgba(0,0,0,0.2); padding: 0.75rem; border-radius: 8px; font-size: 0.88rem; line-height: 1.6;">
              <strong>801 班（17 人）</strong>：男 10、女 7<br>
              <strong>803 班（15 人）</strong>：男 6、女 9
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">男生人數達 16 人，童軍生火與帳棚搭建主力車隊</p>
          </div>
          <!-- 車次 丁 -->
          <div class="card card-accent">
            <div class="card-title">🚍 第 丁 車（共 21 學生）</div>
            <p style="font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>隨車師長：</strong>姚O勤組長、黃O慧老師</p>
            <div style="background: rgba(0,0,0,0.2); padding: 0.75rem; border-radius: 8px; font-size: 0.88rem; line-height: 1.6;">
              <strong>807 班（21 人）</strong>：男 8、女 13
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">全班獨立成車，由訓育組長親自隨隊督導</p>
          </div>
        </div>
        <div class="card" style="margin-top: 1.25rem;">
          <div class="card-title">📢 乘車安全規範</div>
          <p style="font-size: 0.92rem; line-height: 1.6;">
            1. 上車依編定座位依序就坐，<strong>全程繫妥安全帶</strong>，非必要不得隨意離座走動。<br>
            2. 車內禁止大聲喧嘩、飲食請保持車廂整潔；頭手切勿伸出窗外；遇突發狀況聽從隨車師長與導隊輔引導。
          </p>
        </div>
      </section>

      <!-- SLIDE 17: 男生帳棚清冊 A01~A13 -->
      <section class="slide" id="slide-8">
        <div class="slide-header">
          <div>
            <div class="slide-category">營地夜宿分配</div>
            <div class="slide-title">⛺ 男生帳棚分配清冊（A01 ~ A13 共 13 頂）</div>
          </div>
          <div class="slide-num">08 / 17</div>
        </div>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr><th>帳號</th><th>班級</th><th>人數</th><th>入住學生名單</th><th>乘車</th></tr>
            </thead>
            <tbody>
              <tr><td><span class="pill pill-boy">A01</span></td><td>801</td><td>5人</td><td>林O諼、張O鈞、張O偉、吳O岷、谷O恩</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-boy">A02</span></td><td>801</td><td>5人</td><td>湯O丞、陳O廷、許O瑋、陳O宗、賴O豪</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-boy">A03</span></td><td>802</td><td>3人</td><td>黃O睿、葉O毅、廖O惟</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-boy">A04</span></td><td>802</td><td>3人</td><td>劉O宇、張O瑋、簡O宸</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-boy">A05</span></td><td>803</td><td>3人</td><td>許O煜、陳O熙、蔡O呈</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-boy">A06</span></td><td>803</td><td>3人</td><td>陳O天、陳O瑜、李O成</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-boy">A07</span></td><td>804</td><td>3人</td><td>陳O光、蕭O皓、陳O昇</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-boy">A08</span></td><td>804</td><td>4人</td><td>林O澄、許O翔、劉O振、張O帆</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-boy">A09</span></td><td>805</td><td>4人</td><td>林O竹、郭O佑、陳O庭、嚴O諭</td><td>1 車</td></tr>
              <tr><td><span class="pill pill-boy">A10</span></td><td>805</td><td>3人</td><td>吳O鋒、簡O宇、張O瑜 <span class="pill pill-veg">素食</span></td><td>1 車</td></tr>
              <tr><td><span class="pill pill-boy">A11</span></td><td>806</td><td>4人</td><td>吳O文、曾O承、洪O倫、張O棋</td><td>1 車</td></tr>
              <tr><td><span class="pill pill-boy">A12</span></td><td>807</td><td>4人</td><td>吳O霆、洪O熙、張O睿、黃O壬</td><td>丁 車</td></tr>
              <tr><td><span class="pill pill-boy">A13</span></td><td>807</td><td>4人</td><td>呂O辰、林O福、林O旻、許O瀚</td><td>丁 車</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">
          * 男生共 48 人，分配於 13 頂屋式帳。每帳設室長 1 名負責內務整潔與就寢點名。
        </p>
      </section>

      <!-- SLIDE 17: 女生帳棚清冊 B01~B14 -->
      <section class="slide" id="slide-9">
        <div class="slide-header">
          <div>
            <div class="slide-category">營地夜宿分配</div>
            <div class="slide-title">⛺ 女生帳棚分配清冊（B01 ~ B14 共 14 頂）</div>
          </div>
          <div class="slide-num">09 / 17</div>
        </div>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr><th>帳號</th><th>班級</th><th>人數</th><th>入住學生名單</th><th>乘車</th></tr>
            </thead>
            <tbody>
              <tr><td><span class="pill pill-girl">B01</span></td><td>801</td><td>3人</td><td>林O言、劉O含、藍O詒</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-girl">B02</span></td><td>801</td><td>4人</td><td>林O嫻、江O婷、陳O翎、陳O涵</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-girl">B03</span></td><td>802</td><td>4人</td><td>李O妮、李O甯、鄭O琳、黃O蒂</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-girl">B04</span></td><td>802</td><td>4人</td><td>簡O懿、黃O薇、賴O其、鐘O彤</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-girl">B05</span></td><td>802</td><td>5人</td><td>郭O琪、廖O昕、胡O薰、張O桔、詹O彤</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-girl">B06</span></td><td>803</td><td>5人</td><td>王O芝、石O芳、吳O恩、吳O蓉、潘O汝</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-girl">B07</span></td><td>803</td><td>4人</td><td>邱O慈、陳O羽、謝O璇、沈O愉</td><td>3 車</td></tr>
              <tr><td><span class="pill pill-girl">B08</span></td><td>804</td><td>4人</td><td>王O涵、陳O妘、張O晴、劉O硯 <span class="pill pill-accent">804</span></td><td>2 車</td></tr>
              <tr><td><span class="pill pill-girl">B09</span></td><td>804</td><td>4人</td><td>羅O茜、簡O璇、余O婷、洪O瑄</td><td>2 車</td></tr>
              <tr><td><span class="pill pill-girl">B10</span></td><td>805</td><td>4人</td><td>劉O硯 <span class="pill pill-accent">805</span>、吳O瑜、黃O薇、鄭O妮</td><td>1 車</td></tr>
              <tr><td><span class="pill pill-girl">B11</span></td><td>806</td><td>5人</td><td>陳O臻、李O榕、林O妤、范O英、廖O慈</td><td>1 車</td></tr>
              <tr><td><span class="pill pill-girl">B12</span></td><td>807</td><td>4人</td><td>張O瑄、郭O岑、黃O浠、詹O靜</td><td>丁 車</td></tr>
              <tr><td><span class="pill pill-girl">B13</span></td><td>807</td><td>5人</td><td>林O妤、吳O桐、陳O錥、蕭O晨、簡O緹</td><td>丁 車</td></tr>
              <tr><td><span class="pill pill-girl">B14</span></td><td>807</td><td>4人</td><td>廖O涵、陳O伶、古O潼、胡O熙</td><td>丁 車</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card card-info" style="margin-top: 0.8rem; padding: 0.75rem 1rem;">
          <p style="font-size: 0.88rem; line-height: 1.5;">
            💡 <strong>名冊查核備註</strong>：B08 帳（804班）與 B10 帳（805班）各有一位女同學名為「<strong>劉O硯</strong>」，經學籍底冊校對，804 班為座號 11 號、805 班為座號 13 號，身分證與學號皆相異，確認為兩位同名同姓同學，手冊資料完全無誤。
          </p>
        </div>
      </section>

      <!-- SLIDE 17: 野炊膳食分組 1~15 組 -->
      <section class="slide" id="slide-10">
        <div class="slide-header">
          <div>
            <div class="slide-category">野炊與烤肉小隊</div>
            <div class="slide-title">🍲 膳食野炊與烤肉編組名單（第 1 組 ～ 第 15 組）</div>
          </div>
          <div class="slide-num">10 / 17</div>
        </div>
        <div class="grid-3" style="max-height: 520px; overflow-y: auto; padding-right: 0.5rem;">
          <div class="card"><div class="card-title">🥢 第 1 組（801 班，9人）</div><p style="font-size: 0.9rem;">劉O含、林O言、谷O恩、張O鈞、張O偉、林O諼、陳O宗、賴O豪、藍O詒</p></div>
          <div class="card"><div class="card-title">🥢 第 2 組（801 班，8人）</div><p style="font-size: 0.9rem;">林O嫻、陳O翎、江O婷、陳O涵、湯O丞、吳O岷、許O瑋、陳O廷</p></div>
          <div class="card"><div class="card-title">🥢 第 3 組（802 班，6人）</div><p style="font-size: 0.9rem;">黃O薇、廖O惟、賴O其、簡O懿、鐘O彤、張O瑋</p></div>
          <div class="card"><div class="card-title">🥢 第 4 組（802 班，6人）</div><p style="font-size: 0.9rem;">葉O毅、李O甯、李O妮、鄭O琳、黃O蒂、黃O睿</p></div>
          <div class="card"><div class="card-title">🥢 第 5 組（802 班，7人）</div><p style="font-size: 0.9rem;">廖O昕、胡O薰、郭O琪、張O桔、簡O宸、劉O宇、詹O彤</p></div>
          <div class="card"><div class="card-title">🥢 第 6 組（803 班，8人）</div><p style="font-size: 0.9rem;">王O芝、石O芳、吳O恩、吳O蓉、潘O汝、許O煜、陳O熙、蔡O呈</p></div>
          <div class="card"><div class="card-title">🥢 第 7 組（803 班，7人）</div><p style="font-size: 0.9rem;">邱O慈、陳O羽、謝O璇、沈O愉、陳O天、陳O瑜、李O成</p></div>
          <div class="card"><div class="card-title">🥢 第 8 組（804 班，7人）</div><p style="font-size: 0.9rem;">陳O光、張O帆、林O澄、劉O振、許O翔、蕭O皓、陳O昇</p></div>
          <div class="card"><div class="card-title">🥢 第 9 組（804 班，8人）</div><p style="font-size: 0.9rem;">張O晴、洪O瑄、余O婷、簡O璇、陳O妘、羅O茜、王O涵、劉O硯</p></div>
          <div class="card card-highlight"><div class="card-title">🥢 第 10 組（805 班，7人）</div><p style="font-size: 0.9rem;">林O竹、吳O鋒、簡O宇、郭O佑、陳O庭、嚴O諭、<strong>張O瑜 <span class="pill pill-veg">素食</span></strong></p></div>
          <div class="card"><div class="card-title">🥢 第 11 組（805 班，4人）</div><p style="font-size: 0.9rem;">劉O硯、吳O瑜、黃O薇、鄭O妮</p></div>
          <div class="card"><div class="card-title">🥢 第 12 組（806 班，9人）</div><p style="font-size: 0.9rem;">廖O慈、洪O倫、范O英、林O妤、張O棋、吳O文、陳O臻、李O榕、曾O承</p></div>
          <div class="card"><div class="card-title">🥢 第 13 組（807 班，7人）</div><p style="font-size: 0.9rem;">郭O岑、黃O浠、詹O靜、張O瑄、胡O熙、古O潼、陳O伶</p></div>
          <div class="card"><div class="card-title">🥢 第 14 組（807 班，6人）</div><p style="font-size: 0.9rem;">吳O桐、林O妤、陳O錥、廖O涵、蕭O晨、簡O緹</p></div>
          <div class="card"><div class="card-title">🥢 第 15 組（807 班，8人）</div><p style="font-size: 0.9rem;">吳O霆、呂O辰、林O福、林O旻、洪O熙、張O睿、許O瀚、黃O壬</p></div>
        </div>
      </section>

      <!-- SLIDE 17: 【教學參考 1】營地建設與屋式帳 -->
      <section class="slide" id="slide-11">
        <div class="slide-header">
          <div>
            <div class="slide-category">童軍知識卡 ①</div>
            <div class="slide-title">🏕️ 營地建設與屋式帳搭設解析（圖文與影音）</div>
          </div>
          <div class="slide-num">11 / 17</div>
        </div>
        <div class="grid-4">
          <div class="card">
            <div>
              <div class="card-title">1. 營地五大分區規劃</div>
              <p style="font-size: 0.85rem; color: #334155;">搭帳區門口順風、炊事區靠水下風處、活動場、WC、垃圾場。</p>
              <div class="media-box"><img src="assets/p13_img3.jpeg" alt="營地分區"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+營地建設+LNT" target="_blank" class="btn-video">▶ 觀看營地建設教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">2. 屋式帳結構與器材</div>
              <p style="font-size: 0.85rem; color: #334155;">營釘14支、主繩2條、副繩16條、營柱、雷管雷帽、內外帳。</p>
              <div class="media-box"><img src="assets/camp_setup_page13.png" alt="屋式帳器材"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+屋式帳+結構+營柱營釘" target="_blank" class="btn-video">▶ 觀看器材構造解說</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">3. 帳棚搭設圖文四步驟</div>
              <p style="font-size: 0.85rem; color: #334155;">鋪平內帳 ➔ 組合四柱 ➔ 釘四角撐起 ➔ 短營柱穿外帳組合。</p>
              <div class="media-box"><img src="assets/tent_pitching_page14.png" alt="搭帳步驟"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+帳篷搭設教學+步驟" target="_blank" class="btn-video">▶ 觀看步驟示範影片</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">4. 搭收口訣與防蛇曬帳</div>
              <p style="font-size: 0.85rem; color: #334155;">口訣：一拉對角二立中柱...；收外帳：一拜天地二拜高堂...。</p>
              <div class="media-box"><img src="assets/p14_img7.jpeg" alt="搭收口訣"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+搭帳口訣+一拉對角+收外帳" target="_blank" class="btn-video">▶ 觀看搭帳口訣示範</a>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 【教學參考 2】童軍常用八大繩結 -->
      <section class="slide" id="slide-12">
        <div class="slide-header">
          <div>
            <div class="slide-category">童軍知識卡 ②</div>
            <div class="slide-title">🪢 童軍常用八大繩結圖解與影音教學</div>
          </div>
          <div class="slide-num">12 / 17</div>
        </div>
        <div class="grid-4" style="max-height: 520px; overflow-y: auto;">
          <div class="card">
            <div>
              <div class="card-title">1. 單結 (Overhand)</div>
              <p style="font-size: 0.82rem; color: #334155;">基礎繩端防脫結眼，防止繩頭脫落。</p>
              <div class="media-box"><img src="assets/knot_1_single.png" alt="單結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+單結+Overhand+Knot" target="_blank" class="btn-video">▶ 觀看單結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">2. 八字結 (Figure-8)</div>
              <p style="font-size: 0.82rem; color: #334155;">比單結大、易解，登山防墜必備。</p>
              <div class="media-box"><img src="assets/knot_2_figure8.png" alt="八字結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+八字結+Figure+Eight+Knot" target="_blank" class="btn-video">▶ 觀看八字結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">3. 活結 (Slip Knot)</div>
              <p style="font-size: 0.82rem; color: #334155;">拉單端即解開，臨時牽繫與快拆首選。</p>
              <div class="media-box"><img src="assets/knot_3_slip.png" alt="活結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+活結+Slip+Knot" target="_blank" class="btn-video">▶ 觀看活結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">4. 平結 (Reef Knot)</div>
              <p style="font-size: 0.82rem; color: #334155;">接等粗繩，急救三角巾包紮首選。</p>
              <div class="media-box"><img src="assets/knot_4_square.png" alt="平結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+平結+Square+Knot+Reef+Knot" target="_blank" class="btn-video">▶ 觀看平結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">5. 接繩結 (Sheet Bend)</div>
              <p style="font-size: 0.82rem; color: #334155;">專門連接兩條不同粗細或材質繩索。</p>
              <div class="media-box"><img src="assets/knot_5_sheetbend.png" alt="接繩結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+接繩結+Sheet+Bend" target="_blank" class="btn-video">▶ 觀看接繩結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">6. 雙套結 (Clove Hitch)</div>
              <p style="font-size: 0.82rem; color: #334155;">工程結之母！繫營柱雷管、開頭與收尾。</p>
              <div class="media-box"><img src="assets/knot_6_clovehitch.png" alt="雙套結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+雙套結+Clove+Hitch" target="_blank" class="btn-video">▶ 觀看雙套結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">7. 雙半結 (Two Half)</div>
              <p style="font-size: 0.82rem; color: #334155;">繞樹幹打兩次半結，緊密栓繫不滑脫。</p>
              <div class="media-box"><img src="assets/knot_7_twohalf.png" alt="雙半結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+雙半結+Two+Half+Hitches" target="_blank" class="btn-video">▶ 觀看雙半結教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">8. 營繩結 (Taut-Line)</div>
              <p style="font-size: 0.82rem; color: #334155;">滑動調長度，拉緊自動卡死微調張力。</p>
              <div class="media-box"><img src="assets/knot_8_tautline.png" alt="營繩結"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=童軍+營繩結+營釘結+Taut-line+Hitch" target="_blank" class="btn-video">▶ 觀看營繩結教學</a>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 【教學參考 3】自然方向辨識 -->
      <section class="slide" id="slide-13">
        <div class="slide-header">
          <div>
            <div class="slide-category">童軍知識卡 ③</div>
            <div class="slide-title">🧭 自然方向辨識（圖文與影音教學）</div>
          </div>
          <div class="slide-num">13 / 17</div>
        </div>
        <div class="grid-4">
          <div class="card">
            <div>
              <div class="card-title">1. 指南針與 16 方位盤</div>
              <p style="font-size: 0.85rem; color: #334155;">紅針指北（磁北），標準 16 方位判讀。</p>
              <div class="media-box"><img src="assets/dir_compass_rose.png" alt="指南針方位"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=指北針+指南針+16方位+地圖定向" target="_blank" class="btn-video">▶ 觀看指北針定位</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">2. 手錶時針太陽法</div>
              <p style="font-size: 0.85rem; color: #334155;">時針對太陽，時針與 12 點角平分線為正南。</p>
              <div class="media-box"><img src="assets/direction_page17.png" alt="手錶太陽法"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=手錶+太陽+方向辨識" target="_blank" class="btn-video">▶ 觀看手錶太陽法</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">3. 夜間北極星定位</div>
              <p style="font-size: 0.85rem; color: #334155;">北斗七星勺口延伸 5 倍；仙后座 W 開口法。</p>
              <div class="media-box"><img src="assets/p17_img3.jpeg" alt="北極星"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=北極星+尋找+北斗七星+仙后座" target="_blank" class="btn-video">▶ 觀看北極星定位</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">4. 樹木年輪與向日葵</div>
              <p style="font-size: 0.85rem; color: #334155;">年輪密者為北；向日葵午前向東南午後向西南。</p>
              <div class="media-box"><img src="assets/worksheet_page22.png" alt="自然特徵定向"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=野外求生+自然方位辨識+年輪" target="_blank" class="btn-video">▶ 觀看自然定向教學</a>
          </div>
        </div>

        <!-- 🌕 延伸教學工具：月相模擬器 -->
        <div class="card card-highlight" style="margin-top: 1.25rem; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem; background: linear-gradient(135deg, rgba(2,132,199,0.08), rgba(217,119,6,0.08)); border: 1.5px dashed var(--accent);">
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-size: 2.3rem;">🌕</div>
            <div>
              <div class="card-title" style="margin-bottom: 0.25rem; font-size: 1.15rem; color: var(--text);">
                🔭 延伸童軍野營教學：月相模擬器 (Moon Phase Simulator)
              </div>
              <p style="font-size: 0.9rem; color: #334155;">
                野營夜間辨位與觀星輔助！透過 Gemini 互動工具即時觀察月球公轉軌跡、日地月相對位置與初一至三十月相盈虧變化。
              </p>
            </div>
          </div>
          <a href="https://gemini.google.com/share/90fe02a031a5?social_preview=false&skid=498c1de2-4192-4fb7-9b14-92d3a058c761" target="_blank" class="btn btn-primary" style="padding: 0.75rem 1.4rem; font-size: 0.95rem; font-weight: bold; border-radius: 9999px; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 14px rgba(2,132,199,0.25);">
            <span>🌕 開啟月相模擬器</span>
            <span style="font-size: 0.8rem; opacity: 0.9;">(點擊新分頁開啟 ↗)</span>
          </a>
        </div>
      </section>

      <!-- SLIDE 17: 【教學參考 4】野外簡易急救處置 -->
      <section class="slide" id="slide-14">
        <div class="slide-header">
          <div>
            <div class="slide-category">童軍知識卡 ④</div>
            <div class="slide-title">🩹 野外簡易急救處置（圖文與影音教學）</div>
          </div>
          <div class="slide-num">14 / 17</div>
        </div>
        <div class="grid-4">
          <div class="card">
            <div>
              <div class="card-title">1. 意外割傷處理</div>
              <p style="font-size: 0.85rem; color: #334155;">清水沖洗、無菌紗布直接加壓止血、抬高傷肢。</p>
              <div class="media-box"><img src="assets/fa_cuts.png" alt="割傷加壓止血"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=外傷出血+加壓止血+包紮教學" target="_blank" class="btn-video">▶ 觀看加壓止血教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">2. 肌肉抽筋處理</div>
              <p style="font-size: 0.85rem; color: #334155;">反向伸展大原則：小腿抽筋將腳掌向上扳屈。</p>
              <div class="media-box"><img src="assets/fa_cramps.png" alt="抽筋處理"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=小腿抽筋+急救處理+伸展" target="_blank" class="btn-video">▶ 觀看抽筋處理教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">3. 流鼻血緊急處置</div>
              <p style="font-size: 0.85rem; color: #334155;">坐下頭微前傾（切忌後仰防嗆血），捏鼻翼軟骨。</p>
              <div class="media-box"><img src="assets/fa_nosebleed.png" alt="流鼻血處置"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=流鼻血+正確急救姿勢+頭前傾" target="_blank" class="btn-video">▶ 觀看流鼻血處置教學</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">4. 骨折固定處置</div>
              <p style="font-size: 0.85rem; color: #334155;">切勿推拿，就地取材夾板超過上下兩關節固定。</p>
              <div class="media-box"><img src="assets/fa_fracture.png" alt="骨折夾板固定"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=骨折+夾板固定+急救教學" target="_blank" class="btn-video">▶ 觀看骨折固定教學</a>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 【教學參考 5】臺灣六大毒蛇與急救「五要五不」 -->
      <section class="slide" id="slide-15">
        <div class="slide-header">
          <div>
            <div class="slide-category">童軍知識卡 ⑤</div>
            <div class="slide-title">🐍 臺灣六大毒蛇與急救「五要五不」（圖文與影音）</div>
          </div>
          <div class="slide-num">15 / 17</div>
        </div>
        <div class="grid-4">
          <div class="card">
            <div>
              <div class="card-title">1. 出血性毒蛇：百步蛇</div>
              <p style="font-size: 0.85rem; color: #334155;">吻端尖翹、黑色三角形側斑，劇痛腫脹出血。</p>
              <div class="media-box"><img src="assets/p16_img3.jpeg" alt="百步蛇"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=百步蛇+出血性毒蛇+介紹" target="_blank" class="btn-video">▶ 觀看百步蛇生態</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">2. 神經性毒蛇：雨傘節</div>
              <p style="font-size: 0.85rem; color: #334155;">黑白環紋、致死率極高，引起呼吸麻痺衰竭。</p>
              <div class="media-box"><img src="assets/p16_img4.jpeg" alt="雨傘節"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=雨傘節+神經性毒蛇+介紹" target="_blank" class="btn-video">▶ 觀看雨傘節生態</a>
          </div>
          <div class="card">
            <div>
              <div class="card-title">3. 毒蛇圖鑑綜合鑑別</div>
              <p style="font-size: 0.85rem; color: #334155;">龜殼花、赤尾青竹絲、眼鏡蛇、鎖鏈蛇辨別。</p>
              <div class="media-box"><img src="assets/snakes_cards.png" alt="毒蛇圖鑑"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=臺灣六大毒蛇+辨識教學" target="_blank" class="btn-video">▶ 觀看六大毒蛇鑑別</a>
          </div>
          <div class="card card-highlight">
            <div>
              <div class="card-title">4. 蛇傷急救「五要五不」</div>
              <p style="font-size: 0.85rem; color: #334155;">五要：視為毒蛇、記特徵、脫飾品、包紮、送醫；五不：不割、不吸、不冰、不紮死、不喝酒！</p>
              <div class="media-box"><img src="assets/snakes_safety_page16.png" alt="五要五不"></div>
            </div>
            <a href="https://www.youtube.com/results?search_query=疾管署+毒蛇咬傷+五要五不" target="_blank" class="btn-video">▶ 觀看疾管署五要五不</a>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 營火晚會・學習單與自我檢核 -->
      <section class="slide" id="slide-16">
        <div class="slide-header">
          <div>
            <div class="slide-category">情感昇華與反思總結</div>
            <div class="slide-title">🔥 營火晚會精神・學習單指引與自我檢核指標</div>
          </div>
          <div class="slide-num">16 / 17</div>
        </div>
        <div class="grid-2">
          <div class="card card-highlight">
            <div class="card-title">🔥 超ㄅ一ㄤˋ的營火晚會～燭光夜語</div>
            <p style="line-height: 1.8; font-size: 0.95rem;">
              營火象徵熱情、團結與生命力！在熊熊火光中，各班展現自編隊呼與動感歌舞競賽，隊輔勁歌熱舞嗨翻全場。<br>
              <strong>薪火相傳儀式</strong>：晚會尾聲轉入「燭光夜語」，師長點燃象徵智慧與關懷的心燈，傳遞到每一位同學手中。靜下心來回顧國中成長點滴，感恩師長的諄諄教誨，同儕彼此互許承諾，將這份溫暖深植心底。
            </p>
          </div>
          <div class="card card-success">
            <div class="card-title">📝 學習單核心題庫指導</div>
            <ul style="padding-left: 1.25rem; line-height: 1.8; font-size: 0.92rem;">
              <li><strong>露營反原則辨別</strong>：營帳不可搭在枯樹下或低窪處、生火不可緊貼帳篷、水桶與砂土需備妥。</li>
              <li><strong>繩結配對</strong>：平結包紮傷口、八字結防止脫繩、雙套結綁營柱、營繩結調鬆緊。</li>
              <li><strong>中暑急救流程</strong>：移至陰涼通風處 ➔ 冷水擦拭降溫 ➔ 平躺抬高腳部 ➔ 補充水分 ➔ 儘速送醫。</li>
            </ul>
          </div>
        </div>
        <div class="card" style="margin-top: 1.25rem;">
          <div class="card-title">⭐ 學生自我檢核 13 大指標（手冊第 23 頁）</div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.6rem; font-size: 0.88rem; line-height: 1.5; margin-top: 0.5rem;">
            <div>• 能學習規劃童軍體驗生活</div>
            <div>• 能運用資訊做好行前準備</div>
            <div>• 每個單元課程都能仔細觀察</div>
            <div>• 能認真完成學習手冊</div>
            <div>• 體會「行萬里路勝讀萬卷書」</div>
            <div>• 集合能守時，遵守作息規定</div>
            <div>• 能熟讀生活須知並確實遵守</div>
            <div>• 能遵守團體紀律維護榮譽</div>
            <div>• 能聽從帶隊師長指導不私自行動</div>
            <div>• 能與同學互助合作互相照顧</div>
            <div>• 能傾聽發表與同學分享心得</div>
            <div>• 能夠尊重生命愛惜大自然</div>
            <div style="color: var(--gold); font-weight: bold;">• 遊必有方，每天向家人報平安！</div>
          </div>
        </div>
      </section>

      <!-- SLIDE 17: 智慧名冊速查系統 -->
      <section class="slide" id="slide-17">
        <div class="slide-header">
          <div>
            <div class="slide-category">現場執行與導師工具</div>
            <div class="slide-title">👥 二年級隔宿露營 107 位學生名冊速查系統</div>
          </div>
          <div class="slide-num">17 / 17</div>
        </div>
        
        <!-- Search & Filter Controls -->
        <div class="search-bar-wrap">
          <input type="text" id="searchInput" class="input-text" placeholder="🔍 輸入學生姓名（例：林O諼、劉O硯）或帳號..." oninput="filterStudents()">
          <select id="filterClass" class="select-dropdown" onchange="filterStudents()">
            <option value="ALL">全部班級 (801~807)</option>
            <option value="801">801 班 (17人)</option>
            <option value="802">802 班 (19人)</option>
            <option value="803">803 班 (15人)</option>
            <option value="804">804 班 (15人)</option>
            <option value="805">805 班 (11人)</option>
            <option value="806">806 班 (9人)</option>
            <option value="807">807 班 (21人)</option>
          </select>
          <select id="filterBus" class="select-dropdown" onchange="filterStudents()">
            <option value="ALL">全部車次</option>
            <option value="1">1 車 (805, 806)</option>
            <option value="2">2 車 (802, 804)</option>
            <option value="3">3 車 (801, 803)</option>
            <option value="丁">丁 車 (807)</option>
          </select>
          <select id="filterGender" class="select-dropdown" onchange="filterStudents()">
            <option value="ALL">全部性別</option>
            <option value="男">男生 (48人)</option>
            <option value="女">女生 (59人)</option>
          </select>
          <button class="btn btn-primary" onclick="resetFilters()">重設篩選</button>
          <span id="resultCount" style="font-size: 0.9rem; font-weight: bold; color: var(--gold); margin-left: auto;">
            共 107 筆資料
          </span>
        </div>

        <!-- Student Table -->
        <div class="table-responsive" style="max-height: 480px; overflow-y: auto;">
          <table class="data-table" id="studentTable">
            <thead>
              <tr>
                <th>序號</th>
                <th>班級</th>
                <th>學生姓名</th>
                <th>性別</th>
                <th>車次</th>
                <th>帳棚編號</th>
                <th>膳食野炊組別</th>
                <th>備註</th>
              </tr>
            </thead>
            <tbody id="studentTbody">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </section>

    </div>
  </main>

  <!-- Bottom Navigation Bar (Presentation Mode) -->
  <footer class="bottom-nav">
    <div class="nav-btn-group">
      <button class="btn" onclick="prevSlide()">◀ 上一張 (←)</button>
      <button class="btn" onclick="nextSlide()">下一張 (→) ▶</button>
      <span class="slide-indicator" id="slideIndicator">投影片 1 / 16</span>
    </div>
    <div style="display: flex; align-items: center; gap: 0.5rem;">
      <span style="font-size: 0.8rem; color: var(--text-muted);">快捷鍵: 方向鍵 [←] [→] / 空白鍵 [Space] / 全螢幕 [F]</span>
    </div>
  </footer>

  <!-- Teacher Notes Drawer -->
  <div class="notes-drawer" id="notesDrawer">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
      <div class="notes-title">💡 隨身引導與教學備忘錄 (Teacher's Guide Notes)</div>
      <button class="btn" style="padding: 0.2rem 0.5rem;" onclick="toggleNotes()">關閉 ✖</button>
    </div>
    <div id="notesContent" style="font-size: 0.95rem; line-height: 1.7; color: #e2e8f0;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <!-- Modal Index / Directory -->
  <div class="modal-overlay" id="directoryModal" onclick="closeDirectory(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--card-border); padding-bottom: 0.8rem;">
        <div>
          <h3 style="font-size: 1.35rem; color: var(--primary-dark); font-weight: 800;">📑 投影片章節目錄總覽</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.2rem;">點擊任一章節卡片即可快速跳轉至該投影片（共 17 頁，支援鍵盤 ESC 關閉）</p>
        </div>
        <button class="btn btn-primary" onclick="closeDirectory()" style="padding: 0.4rem 1rem;">關閉 ✖</button>
      </div>
      <div class="modal-grid" id="modalDirectoryGrid">
        <!-- Injected via JS -->
      </div>
    </div>
  </div>

  <!-- Application Script -->
  <script>
    const studentsData = {students_js};

    const slideTitles = [
      "01. 封面：南投國中 115 二年級隔宿露營",
      "02. 活動實施計畫與教育宗旨",
      "03. 📢 10/23（五）行前說明會四大重點宣導",
      "04. 想一想，準備好了！行前裝備檢核清單",
      "05. 兩天一夜精實行程日程表",
      "06. 工作人員職掌與隨隊名冊",
      "07. 交通乘車編組與車次分配表",
      "08. 男生帳棚住宿清冊（A01~A13）",
      "09. 女生帳棚住宿清冊（B01~B14）",
      "10. 膳食野炊與烤肉小隊編組名冊",
      "11. 童軍知識卡 ① 營地建設與屋式帳",
      "12. 童軍知識卡 ② 童軍常用八大繩結",
      "13. 童軍知識卡 ③ 自然方向辨識",
      "14. 童軍知識卡 ④ 野外簡易急救處置",
      "15. 童軍知識卡 ⑤ 臺灣六大毒蛇與急救五要五不",
      "16. 營火晚會精神・學習單指引與自我檢核",
      "17. 👥 隔宿露營 107 位學生名冊速查系統"
    ];

    const teacherNotes = [
      "【開場引導】：請導師提醒學生集合時間為 10/27（二）上午 07:30，於校園集合後前往 921 地震公園進行逃生演練。",
      "【計畫說明】：向家長與學生強調團隊生活、做中學與生活教育核心價值。請導師協助催繳 15 位尚未入帳學生之收據。",
      "【行前宣導】：10/23 說明會請各班導師特別強調 4 大生活常規：出發前清查違禁品、零錢限 600 元內、體育服晚上穿、手機每晚約 1 小時報平安、日間著便服/班服+深色長褲（畢旅服裝連動）、重大違規立即由機動車遣返並記大過！",
      "【行李提醒】：手電筒與健保卡為第一要件！再次提醒學生不可穿著裙子、涼鞋與貴重飾品。",
      "【日程重點】：第一天野炊競賽與營火晚會為活動高峰，第二天上午山訓垂降攀岩為意志挑戰，下午 16:20 準時返校接送。",
      "【人員職掌】：董主任隨 1 車、姚組長隨丁車、劉校長與邱經理全場巡察支援。注意隨時回報各班身心狀況。",
      "【車次指引】：1 車(805+806)、2 車(802+804)、3 車(801+803)、丁車(807)。上下車請各班隨車導師親自清點人數。",
      "【男帳要點】：男帳共 13 頂。A01 與 A02 均為 5 人大帳，A10 帳張O瑜同學為素食。指定每帳室長保管內務與門簾關閉。",
      "【女帳要點】：女帳共 14 頂。特別注意 804 班與 805 班各有一位「劉O硯」同學，兩人分別住 B08 與 B10 帳，非誤植。",
      "【野炊指引】：全校共 15 組。第 10 組張O瑜為素食，營區已單獨配置素食材料包與專用煎炒鍋具。",
      "【搭帳教學】：熟記口訣「一拉對角、二立中柱、三拉角繩、四拉邊繩、五加外帳膨內帳」。提醒鞋子倒放外帳下防蛇防潮！各卡片均有影音連結。",
      "【繩結教學】：八大繩結中平結、雙套結與營繩結為必考驗收項目。可帶領小隊進行 1 分鐘計時結繩賽，點擊卡片影片觀看教學。",
      "【定向教學】：手錶太陽法與樹木年輪為生活常見辨位法。提醒學生在野外若迷途切勿慌張，留在原地或順水流而下。",
      "【急救教學】：割傷加壓止血、抽筋反向伸展、流鼻血頭微前傾捏鼻翼軟骨、骨折超關節夾板固定，點擊影片可加深印象。",
      "【毒蛇防護】：強調「五要五不」，絕對嚴禁切開吸血或冰敷！記下毒蛇特徵外觀送尖山埤醫護站迅速轉診施打血清。",
      "【晚會與檢核】：燭光夜語是班級情感凝聚核心。回校後請導師批閱學習單與自我檢核表，作為綜合活動評量依據。",
      "【現場速查】：現場可用平板或手機在此頁輸入學生姓名快速查出帳號、車次與野炊組別，即時處理換組或走失問題。"
    ];

    let currentSlide = 1;
    const totalSlides = 17;

    function updateSlide() {{
      document.querySelectorAll('.slide').forEach((slide, idx) => {{
        if (idx + 1 === currentSlide) {{
          slide.classList.add('active');
        }} else {{
          slide.classList.remove('active');
        }}
      }});

      document.getElementById('slideIndicator').innerText = `投影片 ${{currentSlide}} / ${{totalSlides}}`;
      document.getElementById('progressBar').style.width = `${{(currentSlide / totalSlides) * 100}}%`;
      document.getElementById('notesContent').innerHTML = `<strong>${{slideTitles[currentSlide - 1]}}</strong><br>${{teacherNotes[currentSlide - 1]}}`;
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        currentSlide++;
        updateSlide();
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        currentSlide--;
        updateSlide();
      }}
    }}

    function goToSlide(n) {{
      currentSlide = n;
      updateSlide();
      closeDirectory();
    }}

    function toggleNotes() {{
      const drawer = document.getElementById('notesDrawer');
      drawer.classList.toggle('open');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{
          console.log(err);
        }});
      }} else {{
        document.exitFullscreen();
      }}
    }}

    // 主題背景切換
    function changeTheme(themeName) {{
      document.body.setAttribute('data-theme', themeName);
      localStorage.setItem('nantouCampingTheme', themeName);
      const selector = document.getElementById('themeSelector');
      if (selector) selector.value = themeName;
    }}

    // 目錄總覽功能修正
    function openDirectory() {{
      const modal = document.getElementById('directoryModal');
      const grid = document.getElementById('modalDirectoryGrid');
      grid.innerHTML = '';
      slideTitles.forEach((title, idx) => {{
        const card = document.createElement('div');
        const isCurrent = (idx + 1 === currentSlide);
        card.className = 'modal-card' + (isCurrent ? ' current-active' : '');
        card.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="color:var(--primary); font-size:1.15rem;">#${{String(idx+1).padStart(2, '0')}}</strong>
            ${{isCurrent ? '<span style="background:var(--primary); color:#fff; font-size:0.75rem; padding:0.15rem 0.5rem; border-radius:9999px; font-weight:bold;">📍 當前頁面</span>' : ''}}
          </div>
          <div style="margin-top:0.4rem; font-size:0.92rem; font-weight:600; color:#1e293b; line-height:1.4;">${{title}}</div>
        `;
        card.onclick = () => goToSlide(idx + 1);
        grid.appendChild(card);
      }});
      modal.classList.add('open');
    }}

    function closeDirectory(e) {{
      document.getElementById('directoryModal').classList.remove('open');
    }}

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        prevSlide();
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'n' || e.key === 'N') {{
        toggleNotes();
      }} else if (e.key === 'Escape') {{
        closeDirectory();
      }}
    }});

    // Populate Student Table
    function renderStudents(list) {{
      const tbody = document.getElementById('studentTbody');
      tbody.innerHTML = '';
      list.forEach((s, idx) => {{
        const tr = document.createElement('tr');
        const genderClass = s.gender === '男' ? 'pill-boy' : 'pill-girl';
        const vegBadge = s.note && s.note.includes('素食') ? '<span class="pill pill-veg">素食</span>' : '';
        const noteBadge = s.note && s.note.includes('同名') ? `<span class="pill pill-accent">${{s.note}}</span>` : vegBadge;
        
        tr.innerHTML = `
          <td>${{idx + 1}}</td>
          <td><strong>${{s.clazz}} 班</strong></td>
          <td><strong style="color:#fff;">${{s.name}}</strong></td>
          <td><span class="pill ${{genderClass}}">${{s.gender}}</span></td>
          <td><span class="pill pill-accent">${{s.bus}} 車</span></td>
          <td><span class="pill">${{s.tent}}</span></td>
          <td>第 ${{s.mealGroup}} 組</td>
          <td>${{noteBadge}}</td>
        `;
        tbody.appendChild(tr);
      }});
      document.getElementById('resultCount').innerText = `共 ${{list.length}} 筆資料`;
    }}

    function filterStudents() {{
      const query = document.getElementById('searchInput').value.trim().toLowerCase();
      const cls = document.getElementById('filterClass').value;
      const bus = document.getElementById('filterBus').value;
      const gender = document.getElementById('filterGender').value;

      const filtered = studentsData.filter(s => {{
        const matchQuery = !query || s.name.toLowerCase().includes(query) || s.tent.toLowerCase().includes(query) || s.clazz.includes(query);
        const matchClass = cls === 'ALL' || s.clazz === cls;
        const matchBus = bus === 'ALL' || s.bus === bus;
        const matchGender = gender === 'ALL' || s.gender === gender;
        return matchQuery && matchClass && matchBus && matchGender;
      }});

      renderStudents(filtered);
    }}

    function resetFilters() {{
      document.getElementById('searchInput').value = '';
      document.getElementById('filterClass').value = 'ALL';
      document.getElementById('filterBus').value = 'ALL';
      document.getElementById('filterGender').value = 'ALL';
      renderStudents(studentsData);

    // 初始化讀取背景主題
    const savedTheme = localStorage.getItem('nantouCampingTheme') || 'green';
    changeTheme(savedTheme);
    }}

    // Initialization
    updateSlide();
    renderStudents(studentsData);

    // 初始化讀取背景主題
    const savedTheme = localStorage.getItem('nantouCampingTheme') || 'green';
    changeTheme(savedTheme);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Updated index.html: added images & videos to scout cards, linked to handbook.html, and solidified all names with second char 'O'!")
