# -*- coding: utf-8 -*-
"""
生成南投國中 115 學年度二年級隔宿露營「手冊網頁版」 handbook.html
1. 嚴格採用「淺藍色系（Light Blue Theme）」設計
2. 頂部提供切換至「🖥️ 教學簡報版 (index.html)」連結
3. 採用標籤列型式（Tab-based navigation）呈現各部份內容（完全比照使用者截圖模式）：
   - 📅 行程總覽 (含 Day 1 / Day 2 雙日行程切換卡片、三餐標籤與詳細時程)
   - 🔍 查帳分車 (即時速查系統，班級/車次/性別篩選，姓名第2字固化為 "O")
   - 🚌 團務車次 (4 輛專車編制、各車班級名額與隨車導師名單卡片)
   - ⛺ 帳棚住宿 (27 頂屋式帳篷住宿名單，營地圖解與搭帳步驟)
   - 🍲 野炊膳食 (15 組炊事競賽分組名冊與素食標註)
   - ⚜️ 童軍技能 (營地屋式帳、八大繩結、自然定向、簡易急救、六大毒蛇辨識，每項均附圖片與 YouTube 教學影片按鈕)
   - 🧗 山訓探索 (垂降、攀岩、解手結、水彈生存對抗與安全守則)
   - 🎯 露營學習單 (互動是非挑戰題：點選即時驗證、水彈分隊檢核、心得自我省思)
   - 🎒 行李清單 (可互動勾選之行前裝備清單)
   - ⚠️ 生活須知 (營地生活守則、乘車安全與緊急聯絡網絡)
"""
import json

with open("students_data.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# Double verify every student name second char is 'O'
for s in students:
    assert s["name"][1] == "O", f"Error in masking: {s['name']}"

students_js = json.dumps(students, ensure_ascii=False)

# 1. Pre-render Scout items
scout_items = [
    {
        "cat": "tent",
        "tag": "營地建設與屋式帳",
        "title": "營地分區規劃與環境維護",
        "subtitle": "帳篷區、炊事區、活動區分明，落實無痕山林 (LNT)",
        "img": "assets/p13_img3.jpeg",
        "desc": "營地建設首重排水良好、地勢平坦且背風。帳棚區、野炊炊事區與衛生洗滌區需明確劃分，避免帳內受油煙與水漬污染。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E9%9C%B2%E7%87%9F",
        "webTitle": "📖 推薦教學：露營營地規範",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍露營+營地建設與規劃",
        "videoTitle": "🎬 推薦影片：營地建設教學"
    },
    {
        "cat": "tent",
        "tag": "營地建設與屋式帳",
        "title": "屋式帳搭設五步驟與力學原理",
        "subtitle": "45° 倒勾營釘斜角受力，外帳收折趣味口訣",
        "img": "assets/tent_pitching_page14.png",
        "desc": "搭帳口訣：鋪底布、立內帳營柱、固定內帳營釘、覆蓋外帳拉水線、打外帳營釘（營釘與地面呈 45° 背向帳篷）。外帳收折口訣：「一折二抱三大笑」。",
        "webUrl": "https://www.youtube.com/results?search_query=屋式帳搭設示範",
        "webTitle": "📖 推薦教學：屋式帳步驟指南",
        "videoUrl": "https://www.youtube.com/results?search_query=屋式帳搭設示範",
        "videoTitle": "🎬 推薦影片：屋式帳搭設示範"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "01. 單結 (Overhand Knot)",
        "subtitle": "最基礎結繩入門，防滑防脫落終端結",
        "img": "assets/knot_1_single.png",
        "desc": "所有複雜繩結的基礎。繩端穿過單一繩圈拉緊即成，常用於防止繩頭鬆散或作為粗繩末端制動防滑結。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%96%AE%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：單結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+單結教學",
        "videoTitle": "🎬 推薦影片：單結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "02. 八字結 (Figure-Eight Knot)",
        "subtitle": "比單結更大且易解開，登山攀岩必備",
        "img": "assets/knot_2_figure8.png",
        "desc": "外形酷似數字「8」，耐拉力強且受大重力拉扯後依然極易解開。常用於滑輪終端、登山安全吊帶終端固定。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%85%AB%E5%AD%97%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：八字結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+八字結教學",
        "videoTitle": "🎬 推薦影片：八字結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "03. 活結 (Slip Knot)",
        "subtitle": "輕拉單側短繩即可瞬間秒解，綑紮牲畜便利結",
        "img": "assets/knot_3_slip.png",
        "desc": "具備受力時可拉緊、需要鬆開時只需輕拉活繩頭即可瞬間解開的特性。常用於包裹綑綁或營地暫時繫留。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E6%B4%BB%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：活結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+活結教學",
        "videoTitle": "🎬 推薦影片：活結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "04. 平結 (Square Knot)",
        "subtitle": "童軍最通用結，連接粗細相同繩索與急救三角巾",
        "img": "assets/knot_4_square.png",
        "desc": "口訣：「左在右之上，右在左之上」。結形扁平不壓迫傷口，常用於急救三角巾包紮、包裹綑紮及等粗繩索連接。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%B9%B3%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：平結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+平結教學",
        "videoTitle": "🎬 推薦影片：平結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "05. 接繩結 (Sheet Bend)",
        "subtitle": "連接粗細不同兩條繩索的最佳選擇",
        "img": "assets/knot_5_sheetbend.png",
        "desc": "以粗繩折成Ｕ型圈、細繩穿入並繞壓鎖緊。粗細不同繩子互接時，細繩不易滑脫，強度遠勝平結。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E6%8E%A5%E7%B9%A9%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：接繩結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+接繩結教學",
        "videoTitle": "🎬 推薦影片：接繩結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "06. 雙套結 (Clove Hitch)",
        "subtitle": "摩擦力極大越拉越緊，營柱營木固定工程核心",
        "img": "assets/knot_6_clovehitch.png",
        "desc": "將繩子於柱狀物上纏繞兩圈交叉鎖緊。越拉越緊且固定牢固，為搭設木橋、瞭望台等童軍先鋒工程起結結尾必備。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E9%9B%99%E5%A5%97%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：雙套結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+雙套結教學",
        "videoTitle": "🎬 推薦影片：雙套結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "07. 雙半結 (Two Half Hitches)",
        "subtitle": "固定於樹幹或圓環，容易解開不易滑脫",
        "img": "assets/knot_7_twohalf.png",
        "desc": "在主繩身連續打兩次單半結。受力時穩定不脫落，解開輕鬆自如，常用於繫船纜、拴扣牲畜或帳篷營柱固定。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E9%9B%99%E5%8D%8A%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：雙半結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+雙半結教學",
        "videoTitle": "🎬 推薦影片：雙半結教學"
    },
    {
        "cat": "knots",
        "tag": "童軍常用八大繩結",
        "title": "08. 營繩結 (Taut-Line Hitch)",
        "subtitle": "自由滑動調節繩索鬆緊，露營防風拉水線神技",
        "img": "assets/knot_8_tautline.png",
        "desc": "能在繩身前後滑動調整繩索鬆緊度，受力時立即咬死固定。戶外露營外帳抗風拉緊、晾衣繩調節不可或缺。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E7%87%9F%E7%B9%A9%E7%B5%90",
        "webTitle": "📖 繩結圖鑑：營繩結百科",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍八大繩結+營繩結教學",
        "videoTitle": "🎬 推薦影片：營繩結教學"
    },
    {
        "cat": "direction",
        "tag": "自然方向辨識",
        "title": "指南針 16 方位盤與度數判讀",
        "subtitle": "紅針對準北方，精準判讀東南西北與度數",
        "img": "assets/dir_compass_rose.png",
        "desc": "指南針基準點為北方（0°/360°）、東方 90°、南方 180°、西方 270°。水平手持避開金屬干擾即可精準導航。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E7%BD%97%E7%9B%98",
        "webTitle": "📖 定向百科：羅盤與方位判讀",
        "videoUrl": "https://www.youtube.com/results?search_query=童軍定向越野+指北針使用教學",
        "videoTitle": "🎬 推薦影片：指南針使用教學"
    },
    {
        "cat": "direction",
        "tag": "自然方向辨識",
        "title": "手錶時針對準太陽折半法",
        "subtitle": "時針指太陽，時針與 12 點刻度夾角平分線為南方",
        "img": "assets/p17_img3.jpeg",
        "desc": "在北半球，將指針手錶水平放置，時針對準太陽方向，時針與手錶 12 點刻度之間的角平分線所指方向即為「南方」。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%A4%AA%E9%98%B3%E6%96%B9%E4%BD%8D%E8%A7%92",
        "webTitle": "📖 定向原理：太陽定向法",
        "videoUrl": "https://www.youtube.com/results?search_query=手錶太陽辨識方向教學",
        "videoTitle": "🎬 推薦影片：手錶太陽定向法"
    },
    {
        "cat": "direction",
        "tag": "自然方向辨識",
        "title": "北極星星座定向法",
        "subtitle": "北斗七星勺口延伸 5 倍，夜間不滅指南針",
        "img": "assets/direction_page17.png",
        "desc": "春夏尋找大熊座北斗七星，將天璇天樞連線往勺口方向延長 5 倍；秋冬尋找仙后座「W」形兩側延長交點，延長 5 倍皆可覓得正北方北極星。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%8C%97%E6%9E%81%E6%98%9F",
        "webTitle": "📖 觀星定向：北極星百科",
        "videoUrl": "https://www.youtube.com/results?search_query=北斗七星尋找北極星教學",
        "videoTitle": "🎬 推薦影片：北極星辨識法"
      },
    {
        "cat": "direction",
        "tag": "自然方向辨識・天文互動",
        "title": "月相模擬器 (Moon Phase Simulator)",
        "subtitle": "日地月相對位置、月球公轉與月相盈虧即時互動模擬",
        "img": "assets/p17_img3.jpeg",
        "desc": "露營夜間辨認方位與觀測夜空的必備互動工具！模擬月球繞地球公轉時的受光面與在地球上所見的月相變化（新月、上弦月、滿月、下弦月）。",
        "webUrl": "https://gemini.google.com/share/90fe02a031a5?social_preview=false&skid=498c1de2-4192-4fb7-9b14-92d3a058c761",
        "webTitle": "🌕 開啟月相模擬器 (Gemini 互動工具)",
        "videoUrl": "https://www.youtube.com/results?search_query=月相變化+動畫模擬+地球月球太陽",
        "videoTitle": "🎬 推薦影片：月相變化原理"
    },
    {
        "cat": "direction",
        "tag": "自然方向辨識",
        "title": "年輪疏密與植物向光性",
        "subtitle": "年輪朝南稀疏朝北密集，向日葵清晨向東黃昏向西",
        "img": "assets/p13_img2.jpeg",
        "desc": "樹木南面陽光充足生長旺盛，年輪間距較寬疏；北面受光少，年輪較細密。向日葵與青苔（向陰面較潮濕茂密）亦為自然定向指標。",
        "webUrl": "https://zh.wikipedia.org/zh-tw/%E5%B9%B4%E8%BD%AE",
        "webTitle": "📖 自然觀察：樹木年輪向陽性",
        "videoUrl": "https://www.youtube.com/results?search_query=自然界辨識方向+年輪+植物",
        "videoTitle": "🎬 推薦影片：自然界辨識方向"
    },
    {
        "cat": "firstaid",
        "tag": "野外簡易急救處置",
        "title": "割傷與擦傷：直接加壓止血",
        "subtitle": "乾淨敷料緊壓傷口 5~10 分鐘，抬高患肢",
        "img": "assets/fa_cuts.png",
        "desc": "用無菌紗布或乾淨手帕直接覆蓋傷口加壓止血。傷口先以生理食鹽水沖洗乾淨，抬高患肢高於心臟位置以減少出血。",
        "webUrl": "https://www.redcross.org.tw/",
        "webTitle": "📖 紅十字會：止血處置指引",
        "videoUrl": "https://www.youtube.com/results?search_query=急救加壓止血教學",
        "videoTitle": "🎬 推薦影片：加壓止血法"
    },
    {
        "cat": "firstaid",
        "tag": "野外簡易急救處置",
        "title": "小腿肌肉抽筋：反向緩慢伸展",
        "subtitle": "膝蓋伸直，腳板腳趾朝向身體緩慢勾起",
        "img": "assets/fa_cramps.png",
        "desc": "切勿大力捶打或揉捏。應坐平將膝蓋伸直，將腳趾朝身體方向緩慢反向勾拉伸展，放鬆小腿腓腸肌，並適量補充溫開水及電解質。",
        "webUrl": "https://health.tvbs.com.tw/",
        "webTitle": "📖 衛教專欄：抽筋急救四步驟",
        "videoUrl": "https://www.youtube.com/results?search_query=小腿抽筋急救伸展教學",
        "videoTitle": "🎬 推薦影片：小腿抽筋自救"
    },
    {
        "cat": "firstaid",
        "tag": "野外簡易急救處置",
        "title": "流鼻血處置：頭微前傾捏鼻翼",
        "subtitle": "禁止仰頭防血倒流，緊捏兩側鼻翼 10 分鐘",
        "img": "assets/fa_nosebleed.png",
        "desc": "坐直身軀、頭部「微微向前傾」，用拇指與食指緊緊捏住兩側鼻翼軟骨處 10~15 分鐘，以口呼吸，額頭可冰敷促進血管收縮。",
        "webUrl": "https://www.mohw.gov.tw/",
        "webTitle": "📖 衛福部：流鼻血正確急救",
        "videoUrl": "https://www.youtube.com/results?search_query=流鼻血正確急救捏鼻翼",
        "videoTitle": "🎬 推薦影片：流鼻血正確處理"
    },
    {
        "cat": "firstaid",
        "tag": "野外簡易急救處置",
        "title": "疑似骨折：副木夾板超關節固定",
        "subtitle": "就地取材固定，副木長度須超過上下兩關節",
        "img": "assets/fa_fracture.png",
        "desc": "切勿試圖整復移位骨頭。就地取材（樹枝、硬紙板或雨傘）襯以軟墊，以繃帶或三角巾固定，夾板長度必須超越骨折處上下兩關節。",
        "webUrl": "https://www.redcross.org.tw/",
        "webTitle": "📖 紅十字會：骨折夾板包紮",
        "videoUrl": "https://www.youtube.com/results?search_query=骨折夾板固定教學+紅十字會",
        "videoTitle": "🎬 推薦影片：骨折副木固定教學"
    },
    {
        "cat": "snakes",
        "tag": "臺灣六大毒蛇與急救",
        "title": "百步蛇辨識（出血性劇毒）",
        "subtitle": "三角鼻吻向上翹，兩側有顯著暗褐色三角形花斑",
        "img": "assets/p16_img3.jpeg",
        "desc": "體型粗壯，吻端尖向上翹。背部兩側有排列對稱之三角形深褐色斑紋。被咬傷後局部劇痛、嚴重腫脹腫大並迅速組織壞死出血。",
        "webUrl": "https://e-info.org.tw/node/216259",
        "webTitle": "📖 生態科普：臺灣百步蛇圖鑑",
        "videoUrl": "https://www.youtube.com/results?search_query=百步蛇生態介紹+辨識",
        "videoTitle": "🎬 推薦影片：百步蛇生態辨識"
    },
    {
        "cat": "snakes",
        "tag": "臺灣六大毒蛇與急救",
        "title": "雨傘節辨識（神經性劇毒）",
        "subtitle": "黑白相間環紋，背脊中央顯著隆起成脊狀",
        "img": "assets/p16_img4.jpeg",
        "desc": "全身黑白相間寬度大致均勻之橫帶環紋，背脊微呈三角形。神經毒素致傷口通常不痛不腫，但數小時內會引發眼皮下垂、呼吸衰竭衰竭。",
        "webUrl": "https://e-info.org.tw/node/216260",
        "webTitle": "📖 生態科普：臺灣雨傘節圖鑑",
        "videoUrl": "https://www.youtube.com/results?search_query=雨傘節生態介紹+辨識",
        "videoTitle": "🎬 推薦影片：雨傘節生態辨識"
    },
    {
        "cat": "snakes",
        "tag": "臺灣六大毒蛇與急救",
        "title": "臺灣六大毒蛇全鑑別",
        "subtitle": "出血性（百步、赤尾青竹絲、龜殼花）、神經性（雨傘節、眼鏡蛇）、混合性（鎖鏈蛇）",
        "img": "assets/snakes_cards.png",
        "desc": "台灣常見六大毒蛇：青竹絲尾紅身綠、龜殼花背有碎花斑紋、眼鏡蛇頸部膨大呈眼鏡狀、鎖鏈蛇背有圓形鏈狀鎖斑。戶外活動打草驚蛇方為上策。",
        "webUrl": "https://www.cdc.gov.tw/Category/Page/i7s3v766jP_mK18V_w450Q",
        "webTitle": "📖 疾管署：六大毒蛇抗蛇毒血清",
        "videoUrl": "https://www.youtube.com/results?search_query=臺灣六大毒蛇全辨識+疾管署",
        "videoTitle": "🎬 推薦影片：六大毒蛇辨識全覽"
    },
    {
        "cat": "snakes",
        "tag": "臺灣六大毒蛇與急救",
        "title": "毒蛇咬傷急救「五要五不」SOP",
        "subtitle": "五要：要記、要脫、要包、要低、要送；五不：不割、不吸、不冰、不酒、不跑",
        "img": "assets/snakes_safety_page16.png",
        "desc": "五要：①要記住蛇外觀 ②要脫下戒指手鐲束縛物 ③要包紮壓迫固定 ④要將患肢低於心臟 ⑤要盡速送醫施打血清。五不：不切開、不用口吸、不冰敷、不喝酒刺激、不慌張跑步。",
        "webUrl": "https://www.cdc.gov.tw/",
        "webTitle": "📖 疾管署：蛇傷五要五不指引",
        "videoUrl": "https://www.youtube.com/results?search_query=毒蛇咬傷五要五不教學+宣導",
        "videoTitle": "🎬 推薦影片：蛇傷急救五要五不"
    }
]

scout_cards_html = ""
for item in scout_items:
    scout_cards_html += f"""
    <div class="scout-item-card" data-cat="{item['cat']}">
      <div>
        <span class="scout-tag">{item['tag']}</span>
        <div class="scout-title">{item['title']}</div>
        <div class="scout-subtitle">{item['subtitle']}</div>
        <div class="scout-img-box">
          <img src="{item['img']}" alt="{item['title']}">
        </div>
        <div class="scout-desc">{item['desc']}</div>
      </div>
      <div class="scout-links-row">
        <a href="{item['webUrl']}" target="_blank" class="btn-scout-web">{item['webTitle']}</a>
        <a href="{item['videoUrl']}" target="_blank" class="btn-scout-video">{item['videoTitle']}</a>
      </div>
    </div>
    """

# 2. Pre-render Tents
tent_list = [
    {"id": "A01", "type": "A", "clazz": "801", "count": 5, "members": ["林O諼", "張O鈞", "張O偉", "吳O岷", "谷O恩"]},
    {"id": "A02", "type": "A", "clazz": "801", "count": 5, "members": ["湯O丞", "陳O廷", "許O瑋", "陳O宗", "賴O豪"]},
    {"id": "A03", "type": "A", "clazz": "802", "count": 3, "members": ["黃O睿", "葉O毅", "廖O惟"]},
    {"id": "A04", "type": "A", "clazz": "802", "count": 3, "members": ["劉O宇", "張O瑋", "簡O宸"]},
    {"id": "A05", "type": "A", "clazz": "803", "count": 3, "members": ["許O煜", "陳O熙", "蔡O呈"]},
    {"id": "A06", "type": "A", "clazz": "803", "count": 3, "members": ["陳O天", "陳O瑜", "李O成"]},
    {"id": "A07", "type": "A", "clazz": "804", "count": 3, "members": ["陳O光", "蕭O皓", "陳O昇"]},
    {"id": "A08", "type": "A", "clazz": "804", "count": 4, "members": ["林O澄", "許O翔", "劉O振", "張O帆"]},
    {"id": "A09", "type": "A", "clazz": "805", "count": 4, "members": ["林O竹", "郭O佑", "陳O庭", "嚴O諭"]},
    {"id": "A10", "type": "A", "clazz": "805", "count": 3, "members": ["吳O鋒", "簡O宇", "張O瑜"]},
    {"id": "A11", "type": "A", "clazz": "806", "count": 4, "members": ["吳O文", "曾O承", "洪O倫", "張O棋"]},
    {"id": "A12", "type": "A", "clazz": "807", "count": 4, "members": ["吳O霆", "洪O熙", "張O睿", "黃O壬"]},
    {"id": "A13", "type": "A", "clazz": "807", "count": 4, "members": ["呂O辰", "林O福", "林O旻", "許O瀚"]},
    {"id": "B01", "type": "B", "clazz": "801", "count": 3, "members": ["林O言", "劉O含", "藍O諒"]},
    {"id": "B02", "type": "B", "clazz": "801", "count": 4, "members": ["林O嫻", "江O婷", "陳O翎", "陳O涵"]},
    {"id": "B03", "type": "B", "clazz": "802", "count": 4, "members": ["李O妮", "李O甯", "鄭O琳", "黃O蒂"]},
    {"id": "B04", "type": "B", "clazz": "802", "count": 4, "members": ["簡O懿", "黃O薇", "賴O其", "鐘O彤"]},
    {"id": "B05", "type": "B", "clazz": "802", "count": 5, "members": ["郭O琪", "廖O昕", "胡O薰", "張O桔", "詹O彤"]},
    {"id": "B06", "type": "B", "clazz": "803", "count": 5, "members": ["王O芝", "石O芳", "吳O恩", "吳O蓉", "潘O汝"]},
    {"id": "B07", "type": "B", "clazz": "803", "count": 4, "members": ["邱O慈", "陳O羽", "謝O璇", "沈O愉"]},
    {"id": "B08", "type": "B", "clazz": "804", "count": 4, "members": ["王O涵", "陳O妘", "張O晴", "劉O硯"]},
    {"id": "B09", "type": "B", "clazz": "804", "count": 4, "members": ["羅O茜", "簡O璇", "余O婷", "洪O瑄"]},
    {"id": "B10", "type": "B", "clazz": "805", "count": 4, "members": ["劉O硯", "吳O瑜", "黃O薇", "鄭O妮"]},
    {"id": "B11", "type": "B", "clazz": "806", "count": 5, "members": ["陳O臻", "李O榕", "林O妤", "范O英", "廖O慈"]},
    {"id": "B12", "type": "B", "clazz": "807", "count": 4, "members": ["張O瑄", "郭O岑", "黃O浠", "詹O靜"]},
    {"id": "B13", "type": "B", "clazz": "807", "count": 5, "members": ["林O妤", "吳O桐", "陳O錥", "蕭O晨", "簡O緹"]},
    {"id": "B14", "type": "B", "clazz": "807", "count": 4, "members": ["廖O涵", "陳O伶", "古O潼", "胡O熙"]}
]

tents_cards_html = ""
for t in tent_list:
    pill_style = "background:#e0f2fe; color:#0369a1;" if t["type"] == "A" else "background:#fce7f3; color:#be185d;"
    tent_title = f"⛺ {t['id']} (男生帳)" if t["type"] == "A" else f"⛺ {t['id']} (女生帳)"
    members_spans = "".join([f'<span style="display:inline-block; background:#f1f5f9; padding:0.2rem 0.5rem; border-radius:6px; margin:0.15rem 0.25rem 0.15rem 0; font-weight:600;">{m}</span>' for m in t["members"]])
    tents_cards_html += f"""
    <div class="bus-card tent-card" data-tent-type="{t['type']}">
      <div class="bus-card-header">
        <div class="bus-card-title">{tent_title}</div>
        <span class="bus-student-pill" style="{pill_style}">{t['clazz']} 班・{t['count']} 人</span>
      </div>
      <div style="font-size:0.95rem; color:#1e293b; line-height:1.7; margin-top:0.4rem;">
        {members_spans}
      </div>
    </div>
    """

# 3. Pre-render Meals
meal_list = [
    {"group": 1, "clazz": "801", "count": 9, "members": ["劉O含", "林O言", "谷O恩", "張O鈞", "張O偉", "林O諼", "陳O宗", "賴O豪", "藍O諒"], "note": ""},
    {"group": 2, "clazz": "801", "count": 8, "members": ["林O嫻", "陳O翎", "江O婷", "陳O涵", "湯O丞", "吳O岷", "許O瑋", "陳O廷"], "note": ""},
    {"group": 3, "clazz": "802", "count": 6, "members": ["黃O薇", "廖O惟", "賴O其", "簡O懿", "鐘O彤", "張O瑋"], "note": ""},
    {"group": 4, "clazz": "802", "count": 6, "members": ["葉O毅", "李O甯", "李O妮", "鄭O琳", "黃O蒂", "黃O睿"], "note": ""},
    {"group": 5, "clazz": "802", "count": 7, "members": ["廖O昕", "胡O薰", "郭O琪", "張O桔", "簡O宸", "劉O宇", "詹O彤"], "note": ""},
    {"group": 6, "clazz": "803", "count": 8, "members": ["王O芝", "石O芳", "吳O恩", "吳O蓉", "潘O汝", "許O煜", "陳O熙", "蔡O呈"], "note": ""},
    {"group": 7, "clazz": "803", "count": 7, "members": ["邱O慈", "陳O羽", "謝O璇", "沈O愉", "陳O天", "陳O瑜", "李O成"], "note": ""},
    {"group": 8, "clazz": "804", "count": 7, "members": ["陳O光", "張O帆", "林O澄", "劉O振", "許O翔", "蕭O皓", "陳O昇"], "note": ""},
    {"group": 9, "clazz": "804", "count": 8, "members": ["張O晴", "洪O瑄", "余O婷", "簡O璇", "陳O妘", "羅O茜", "王O涵", "劉O硯"], "note": ""},
    {"group": 10, "clazz": "805", "count": 7, "members": ["林O竹", "吳O鋒", "簡O宇", "郭O佑", "陳O庭", "嚴O諭", "張O瑜(素)"], "note": "張O瑜 (素食 1 份)"},
    {"group": 11, "clazz": "805", "count": 4, "members": ["劉O硯", "吳O瑜", "黃O薇", "鄭O妮"], "note": ""},
    {"group": 12, "clazz": "806", "count": 9, "members": ["廖O慈", "洪O倫", "范O英", "林O妤", "張O棋", "吳O文", "陳O臻", "李O榕", "曾O承"], "note": ""},
    {"group": 13, "clazz": "807", "count": 7, "members": ["郭O岑", "黃O浠", "詹O靜", "張O瑄", "胡O熙", "古O潼", "陳O伶"], "note": ""},
    {"group": 14, "clazz": "807", "count": 6, "members": ["吳O桐", "林O妤", "陳O錥", "廖O涵", "蕭O晨", "簡O緹"], "note": ""},
    {"group": 15, "clazz": "807", "count": 8, "members": ["吳O霆", "呂O辰", "林O福", "林O旻", "洪O熙", "張O睿", "許O瀚", "黃O壬"], "note": ""}
]

meals_cards_html = ""
for m in meal_list:
    members_spans = "".join([f'<span style="display:inline-block; background:#f1f5f9; padding:0.2rem 0.5rem; border-radius:6px; margin:0.15rem 0.25rem 0.15rem 0; font-weight:600;">{mb}</span>' for mb in m["members"]])
    veg_badge = f'<div class="bus-veg-badge" style="margin-top:0.8rem;">🥗 {m["note"]}</div>' if m["note"] else ""
    meals_cards_html += f"""
    <div class="bus-card">
      <div class="bus-card-header">
        <div class="bus-card-title">🍲 第 {m['group']} 組 ({m['clazz']} 班)</div>
        <span class="bus-student-pill">{m['count']} 人</span>
      </div>
      <div style="font-size:0.95rem; color:#1e293b; line-height:1.7; margin-top:0.4rem;">
        {members_spans}
      </div>
      {veg_badge}
    </div>
    """

# 4. Pre-render Quiz Questions
quiz_list = [
    {
        "num": "01",
        "q": "屋式帳的營釘打入地面時，角度應與地面呈 45 度角，且釘尖朝向帳篷？",
        "ans": False,
        "correct": "⭕ 答對了！釘尖應背向帳篷、受力方向相反，方能產生最大拉力固定外帳。",
        "wrong": "❌ 答錯囉！營釘打入時，釘尖應「背向帳篷」，與拉繩呈 90 度受力，而非釘尖朝向帳篷。"
    },
    {
        "num": "02",
        "q": "連接兩條粗細相同的繩子時，童軍最推薦使用的繩結是平結？",
        "ans": True,
        "correct": "⭕ 答對了！平結扁平且對稱，專門用於連接粗細相同的兩條繩索或急救包紮。",
        "wrong": "❌ 答錯囉！平結確實是最適合連接粗細相同的兩條繩索之繩結。"
    },
    {
        "num": "03",
        "q": "雙套結越拉越緊，常用於將繩索固定在圓木或營柱上？",
        "ans": True,
        "correct": "⭕ 答對了！雙套結摩擦力大且固定牢靠，是營地工程與先鋒工程的核心繩結。",
        "wrong": "❌ 答錯囉！雙套結確實越拉越緊，是固定於圓木與營柱最重要的繩結。"
    },
    {
        "num": "04",
        "q": "在野外用手錶定向時，將手錶時針對準太陽，時針與 12 點刻度的夾角平分線指向北方？",
        "ans": False,
        "correct": "⭕ 答對了！在北半球，時針對準太陽，時針與 12 點的角平分線所指方向是「南方」。",
        "wrong": "❌ 答錯囉！時針與 12 點刻度的夾角平分線指向「南方」，背對南方才是北方。"
    },
    {
        "num": "05",
        "q": "被毒蛇咬傷時，應立即用嘴將毒血吸出以減少毒液在體內擴散？",
        "ans": False,
        "correct": "⭕ 答對了！絕對不可用嘴吸或切開傷口，應牢記「五要五不」，保持冷靜盡速送醫。",
        "wrong": "❌ 答錯囉！切忌用嘴吸或刀割傷口，口腔黏膜微創可能導致施救者中毒並引發嚴重感染。"
    },
    {
        "num": "06",
        "q": "疑似骨折時，使用副木夾板固定範圍必須超過骨折部位的上、下兩個關節？",
        "ans": True,
        "correct": "⭕ 答對了！副木長度必須超越上下兩個關節，才能完全限制活動防止骨折端二次位移刺傷神經血管。",
        "wrong": "❌ 答錯囉！夾板固定確實必須超越骨折處「上、下兩關節」，此為急救標準固定規範。"
    },
    {
        "num": "07",
        "q": "流鼻血時應將頭部盡量往後仰，以防止血液流到衣服上？",
        "ans": False,
        "correct": "⭕ 答對了！頭後仰易使血液倒流嗆入氣管或吞入胃部引起嘔吐，應「頭微前傾」捏住鼻翼止血。",
        "wrong": "❌ 答錯囉！流鼻血千萬不能後仰，應保持「頭微前傾」，以口呼吸並緊捏鼻翼 10 分鐘。"
    },
    {
        "num": "08",
        "q": "營繩結可以在不解開繩索的情況下，自由在繩身前後滑動以調節營繩鬆緊度？",
        "ans": True,
        "correct": "⭕ 答對了！營繩結具備可滑動調節特點，受力時立即咬死，是外帳抗風拉緊必備技能。",
        "wrong": "❌ 答錯囉！營繩結確實可以在主繩身滑動調節長度，是露營外帳抗風神技。"
    }
]

quiz_cards_html = ""
for idx, q in enumerate(quiz_list):
    quiz_cards_html += f"""
    <div class="question-card" id="quizCard_{idx}">
      <div class="question-prompt">{q['num']}. {q['q']}</div>
      <div class="question-options-row">
        <button class="btn-choice" onclick="checkQuizAnswer({idx}, true, this)">⭕ 是</button>
        <button class="btn-choice" onclick="checkQuizAnswer({idx}, false, this)">❌ 否</button>
      </div>
      <div class="explanation-box" id="quizExp_{idx}"></div>
    </div>
    """

# 5. Pre-render Students Table Rows
student_rows_html = ""
for s in students:
    gender_class = "gender-boy" if s["gender"] == "男" else "gender-girl"
    gender_icon = "👦 男" if s["gender"] == "男" else "👧 女"
    note_html = f'<span style="color:#15803d; font-weight:700;">{s["note"]}</span>' if s.get("note") else "-"
    student_rows_html += f"""
    <tr data-class="{s['clazz']}" data-bus="{s['bus']}" data-gender="{s['gender']}" data-search="{s['name']}{s['clazz']}{s['bus']}{s['tent']}{s['mealGroup']}{s.get('note', '')}">
      <td><strong>{s['clazz']} 班</strong></td>
      <td><strong style="color:#0f172a; font-size:1.05rem;">{s['name']}</strong></td>
      <td><span class="{gender_class}">{gender_icon}</span></td>
      <td><span class="pill-bus">🚌 {s['bus']} 車</span></td>
      <td><span class="pill-tent">⛺ {s['tent']}</span></td>
      <td><span class="pill-meal">🍲 第 {s['mealGroup']} 組</span></td>
      <td>{note_html}</td>
    </tr>
    """

quiz_json = json.dumps(quiz_list, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>南投國中 115 學年度二年級戶外教育（隔宿露營）行動手冊・網頁版</title>
  <style>
    :root {{
      --sky-50: #f0f9ff;
      --sky-100: #e0f2fe;
      --sky-200: #bae6fd;
      --sky-300: #7dd3fc;
      --sky-400: #38bdf8;
      --sky-500: #0ea5e9;
      --sky-600: #0284c7;
      --sky-700: #0369a1;
      --sky-800: #075985;
      --sky-900: #0c4a6e;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: #e0f2fe;
      --accent: #f97316;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --card-border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-main);
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.65;
    }}

    /* Top Hero Header (Light Blue Banner) */
    .hero-header {{
      background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 60%, #38bdf8 100%);
      color: #ffffff;
      padding: 2.2rem 2rem 2.8rem 2rem;
      position: relative;
    }}
    .hero-container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    .hero-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      align-items: center;
      margin-bottom: 1rem;
    }}
    .pill-tag {{
      background: rgba(255, 255, 255, 0.22);
      backdrop-filter: blur(4px);
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 0.3rem 0.8rem;
      border-radius: 9999px;
      letter-spacing: 0.5px;
      border: 1px solid rgba(255, 255, 255, 0.35);
    }}
    .pill-orange {{
      background: #f97316;
      border-color: #ea580c;
      font-weight: 700;
    }}
    .hero-title {{
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
      text-shadow: 0 2px 4px rgba(2, 132, 199, 0.3);
    }}
    .hero-subtitle {{
      font-size: 1rem;
      color: rgba(255, 255, 255, 0.95);
      margin-bottom: 1.75rem;
    }}
    .hero-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
    }}
    .hero-info-card {{
      background: rgba(255, 255, 255, 0.16);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.32);
      border-radius: 14px;
      padding: 1.15rem 1.4rem;
      color: #ffffff;
    }}
    .hero-info-tag {{
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      opacity: 0.9;
      margin-bottom: 0.3rem;
    }}
    .hero-info-name {{
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
    }}
    .hero-info-meta {{
      font-size: 0.9rem;
      opacity: 0.92;
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
    }}
    .btn-hero-action {{
      background: #ffffff;
      color: #0284c7;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.9rem;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      cursor: pointer;
      border: none;
    }}
    .btn-hero-action:hover {{
      background: #e0f2fe;
      transform: translateY(-1px);
    }}

    /* Sticky Tab Navigation Bar */
    .tab-nav-bar {{
      position: sticky;
      top: 0;
      background: #ffffff;
      border-bottom: 2px solid #e0f2fe;
      box-shadow: 0 4px 15px rgba(14, 165, 233, 0.08);
      z-index: 1000;
      overflow-x: auto;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
    }}
    .tab-nav-container {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0 1rem;
      height: 60px;
    }}
    .btn-to-slide {{
      background: #0284c7;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      flex-shrink: 0;
      margin-right: 0.5rem;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
    }}
    .btn-to-slide:hover {{
      background: #0369a1;
      transform: translateY(-1px);
    }}
    .tab-btn {{
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      color: #64748b;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0 0.9rem;
      height: 60px;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      cursor: pointer;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}
    .tab-btn:hover {{
      color: #0284c7;
      background: #f0f9ff;
    }}
    .tab-btn.active {{
      color: #0284c7;
      border-bottom-color: #0284c7;
      font-weight: 700;
      background: #f0f9ff;
    }}

    /* Main Container & Panes */
    .main-content {{
      max-width: 1200px;
      margin: 2rem auto;
      padding: 0 1.25rem 4rem 1.25rem;
    }}
    .tab-pane {{
      display: none;
      animation: fadeIn 0.25s ease;
    }}
    .tab-pane.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Section Headers */
    .section-header {{
      margin-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: flex-end;
      gap: 1rem;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 0.9rem;
    }}
    .section-title {{
      font-size: 1.65rem;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}
    .section-subtitle {{
      font-size: 0.95rem;
      color: #64748b;
      margin-top: 0.25rem;
    }}

    /* Sub-tabs / Day Pills (Reference Image 1) */
    .day-selector-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}
    .day-card-btn {{
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 12px;
      padding: 1rem 1.5rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      color: #475569;
    }}
    .day-card-btn:hover {{
      border-color: #0284c7;
      background: #f0f9ff;
    }}
    .day-card-btn.active {{
      background: #0284c7;
      border-color: #0284c7;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
    }}
    .day-card-btn .day-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.2rem;
    }}
    .day-card-btn .day-date {{
      font-size: 0.95rem;
      opacity: 0.9;
    }}

    /* Day Banner & Meals Card (Image 1 Style) */
    .day-banner-card {{
      background: #ffffff;
      border: 1px solid #e0f2fe;
      border-radius: 16px;
      padding: 1.5rem 1.75rem;
      box-shadow: 0 4px 15px rgba(14, 165, 233, 0.06);
      margin-bottom: 1.5rem;
    }}
    .day-banner-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }}
    .day-banner-title {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0369a1;
    }}
    .meal-badges-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.85rem;
      margin-top: 1rem;
    }}
    .meal-badge-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 0.75rem 1rem;
      font-size: 0.9rem;
      font-weight: 600;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    /* Timeline List */
    .timeline-wrap {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}
    .timeline-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 1.1rem 1.4rem;
      display: flex;
      flex-wrap: wrap;
      align-items: flex-start;
      gap: 1.25rem;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }}
    .timeline-card:hover {{
      border-color: #38bdf8;
      box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);
      transform: translateY(-1px);
    }}
    .time-badge {{
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 700;
      font-size: 0.88rem;
      padding: 0.35rem 0.85rem;
      border-radius: 8px;
      flex-shrink: 0;
      min-width: 135px;
      text-align: center;
    }}
    .timeline-info {{
      flex: 1;
      min-width: 250px;
    }}
    .timeline-title {{
      font-size: 1.08rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.25rem;
    }}
    .timeline-desc {{
      font-size: 0.92rem;
      color: #475569;
      line-height: 1.55;
    }}

    /* Search & Lookup (Image 2 Style) */
    .search-panel {{
      background: #ffffff;
      border: 1px solid #e0f2fe;
      border-radius: 16px;
      padding: 1.5rem;
      box-shadow: 0 4px 18px rgba(14, 165, 233, 0.06);
      margin-bottom: 1.5rem;
    }}
    .search-input-wrap {{
      position: relative;
      margin-bottom: 1.2rem;
    }}
    .search-input {{
      width: 100%;
      background: #ffffff;
      border: 2px solid #bae6fd;
      border-radius: 12px;
      padding: 0.9rem 1.25rem 0.9rem 2.8rem;
      font-size: 1.05rem;
      color: #0f172a;
      outline: none;
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: #0284c7;
      box-shadow: 0 0 0 4px rgba(2, 132, 199, 0.15);
    }}
    .search-icon-inside {{
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.15rem;
      color: #64748b;
    }}
    .filter-group-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .filter-label {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #334155;
      min-width: 80px;
    }}
    .filter-pill-btn {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      color: #475569;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-pill-btn:hover {{
      background: #e2e8f0;
      color: #0284c7;
    }}
    .filter-pill-btn.active {{
      background: #0284c7;
      border-color: #0284c7;
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
    }}

    /* Student & Staff Table */
    .table-container {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      overflow-x: auto;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }}
    table.custom-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }}
    table.custom-table th {{
      background: #f0f9ff;
      color: #0369a1;
      padding: 0.85rem 1rem;
      font-weight: 700;
      border-bottom: 2px solid #bae6fd;
      white-space: nowrap;
    }}
    table.custom-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    table.custom-table tr:hover td {{
      background: #f8fafc;
    }}
    .pill-bus {{
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      display: inline-block;
      font-size: 0.82rem;
    }}
    .pill-tent {{
      background: #fef3c7;
      color: #b45309;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      display: inline-block;
      font-size: 0.82rem;
    }}
    .pill-meal {{
      background: #dcfce7;
      color: #15803d;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      display: inline-block;
      font-size: 0.82rem;
    }}
    .gender-boy {{
      color: #0284c7;
      font-weight: 700;
    }}
    .gender-girl {{
      color: #db2777;
      font-weight: 700;
    }}

    /* Buses Cards Grid (Image 3 Style) */
    .buses-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.35rem;
    }}
    .bus-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 1.4rem;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .bus-card:hover {{
      border-color: #38bdf8;
      box-shadow: 0 6px 20px rgba(14, 165, 233, 0.1);
      transform: translateY(-2px);
    }}
    .bus-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.8rem;
    }}
    .bus-card-title {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .bus-student-pill {{
      background: #e0f2fe;
      color: #0369a1;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
    }}
    .bus-class-line {{
      font-size: 1rem;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 0.3rem;
    }}
    .bus-breakdown {{
      font-size: 0.88rem;
      color: #64748b;
      margin-bottom: 1rem;
    }}
    .bus-teachers-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 0.85rem 1rem;
      margin-bottom: 0.75rem;
    }}
    .bus-teachers-label {{
      font-size: 0.78rem;
      font-weight: 700;
      color: #0284c7;
      text-transform: uppercase;
      margin-bottom: 0.4rem;
    }}
    .bus-teacher-item {{
      display: flex;
      justify-content: space-between;
      font-size: 0.92rem;
      color: #334155;
      padding: 0.2rem 0;
      border-bottom: 1px dashed #e2e8f0;
    }}
    .bus-teacher-item:last-child {{
      border-bottom: none;
    }}
    .bus-veg-badge {{
      background: #f0fdf4;
      border: 1px solid #86efac;
      color: #15803d;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 0.4rem 0.75rem;
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* Scout Cards (Image 4 Style) */
    .scout-nav-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1.5rem;
    }}
    .scout-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.5rem;
    }}
    .scout-item-card {{
      background: #ffffff;
      border: 1px solid #e0f2fe;
      border-radius: 16px;
      padding: 1.4rem;
      box-shadow: 0 4px 18px rgba(14, 165, 233, 0.06);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .scout-item-card:hover {{
      border-color: #38bdf8;
      box-shadow: 0 8px 25px rgba(14, 165, 233, 0.12);
      transform: translateY(-2px);
    }}
    .scout-tag {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      color: #0284c7;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 0.5rem;
    }}
    .scout-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 0.25rem;
    }}
    .scout-subtitle {{
      font-size: 0.9rem;
      color: #64748b;
      margin-bottom: 0.85rem;
    }}
    .scout-img-box {{
      width: 100%;
      height: 180px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1rem;
    }}
    .scout-img-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .scout-desc {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.6;
      margin-bottom: 1rem;
    }}
    .scout-links-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-top: auto;
      border-top: 1px dashed #e2e8f0;
      padding-top: 0.85rem;
    }}
    .btn-scout-web {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      color: #0284c7;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }}
    .btn-scout-web:hover {{
      background: #0284c7;
      color: #ffffff;
    }}
    .btn-scout-video {{
      background: #fef2f2;
      border: 1px solid #fecaca;
      color: #dc2626;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }}
    .btn-scout-video:hover {{
      background: #dc2626;
      color: #ffffff;
    }}

    /* Interactive Worksheet (Image 5 Style) */
    .worksheet-container {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .question-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 1.4rem;
      box-shadow: 0 3px 12px rgba(0,0,0,0.03);
      transition: all 0.2s ease;
    }}
    .question-card:hover {{
      border-color: #38bdf8;
    }}
    .question-prompt {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 1rem;
    }}
    .question-options-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 0.75rem;
    }}
    .btn-choice {{
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 10px;
      padding: 0.75rem 1rem;
      font-size: 1.05rem;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }}
    .btn-choice:hover {{
      border-color: #0284c7;
      background: #f0f9ff;
    }}
    .btn-choice.selected-correct {{
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      color: #15803d !important;
    }}
    .btn-choice.selected-wrong {{
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #b91c1c !important;
    }}
    .explanation-box {{
      display: none;
      background: #f8fafc;
      border-left: 4px solid #0284c7;
      border-radius: 8px;
      padding: 0.85rem 1.15rem;
      font-size: 0.92rem;
      color: #334155;
      margin-top: 0.75rem;
      animation: fadeIn 0.2s ease;
    }}

    /* Checklist */
    .checklist-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
    }}
    .checklist-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 1.25rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }}
    .checklist-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #0369a1;
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      border-bottom: 2px solid #e0f2fe;
      padding-bottom: 0.4rem;
    }}
    .check-item {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.45rem 0;
      border-bottom: 1px dashed #f1f5f9;
      font-size: 0.95rem;
      color: #334155;
      cursor: pointer;
    }}
    .check-item:last-child {{
      border-bottom: none;
    }}
    .check-item input[type="checkbox"] {{
      width: 18px;
      height: 18px;
      accent-color: #0284c7;
      cursor: pointer;
    }}
    .check-item.checked span {{
      text-decoration: line-through;
      color: #94a3b8;
    }}

    /* Floating Navigation Controls */
    .floating-tools {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      z-index: 990;
    }}
    .btn-fab {{
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: #ffffff;
      border: 1px solid #bae6fd;
      color: #0284c7;
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .btn-fab:hover {{
      background: #0284c7;
      color: #ffffff;
      transform: translateY(-2px);
    }}

    /* Print styles */
    @media print {{
      .hero-header, .tab-nav-bar, .floating-tools, .btn-to-slide {{
        display: none !important;
      }}
      .tab-pane {{
        display: block !important;
        page-break-after: always;
      }}
      body {{
        background: #fff;
        color: #000;
      }}
    }}
  
    /* Sub-tab Navigation (Level 2 Nested Tabs) */
    .sub-tab-nav-bar {{
      background: #ffffff;
      border: 1.5px solid #bae6fd;
      border-radius: 14px;
      padding: 0.75rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.8rem;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.06);
    }}
    .sub-tab-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #0369a1;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .sub-tab-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .sub-tab-btn {{
      padding: 0.45rem 1.15rem;
      border-radius: 9999px;
      border: 1.5px solid #bae6fd;
      background: #f0f9ff;
      color: #0369a1;
      font-size: 0.92rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .sub-tab-btn:hover {{
      background: #e0f2fe;
      border-color: #0284c7;
    }}
    .sub-tab-btn.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
    }}
    .sub-pane {{
      display: none;
    }}
    .sub-pane.active {{
      display: block;
      animation: fadeIn 0.25s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

  </style>
</head>
<body>

  <!-- Top Hero Header (Light Blue Banner matching Image 1) -->
  <header class="hero-header">
    <div class="hero-container">
      <div class="hero-pills">
        <span class="pill-tag">🏫 南投縣立南投國民中學</span>
        <span class="pill-tag pill-orange">兩天一夜</span>
        <span class="pill-tag">115.10.27(二) ~ 10.28(三)</span>
        <span class="pill-tag">共 107 位同學・10 位隨隊師長</span>
      </div>
      <h1 class="hero-title">115學年度 二年級戶外教育（隔宿露營）行動手冊</h1>
      <p class="hero-subtitle">集合出發：10/27 (二) 07:30 學校集合（921地震公園逃生演練） | 尖山埤野營・童軍分站技能・營火晚會・山訓攀岩垂降</p>
      
      <div class="hero-cards-grid">
        <!-- Camp Location Card -->
        <div class="hero-info-card">
          <div class="hero-info-tag">第一晚 (10/27 二) 住宿營地</div>
          <div class="hero-info-name">台南・尖山埤渡假村露營區</div>
          <div class="hero-info-meta">📍 台南市柳營區旭山里 60 號</div>
          <div class="hero-actions">
            <a href="tel:066233888" class="btn-hero-action">📞 打電話 (06-6233888)</a>
            <a href="https://maps.google.com/?q=台南市柳營區旭山里60號尖山埤渡假村" target="_blank" class="btn-hero-action">🗺️ 地圖導航</a>
          </div>
        </div>

        <!-- Agency & Emergency Card -->
        <div class="hero-info-card">
          <div class="hero-info-tag">承辦旅行社與應變小組</div>
          <div class="hero-info-name">中國青年旅行社中部分公司</div>
          <div class="hero-info-meta">👤 團控經理：邱O凱 (0972-721756) | 學校電話：049-2222549</div>
          <div class="hero-actions">
            <a href="tel:0972721756" class="btn-hero-action">📞 打電話 (邱O凱 經理)</a>
            <button onclick="switchTab('briefing')" class="btn-hero-action" style="background:#fee2e2; color:#b91c1c; border:1px solid #fca5a5; font-weight:700;">📢 10/23線上說明會</button>
            <button onclick="switchTab('notices')" class="btn-hero-action">🚑 緊急通訊網</button>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Sticky Tab Bar (Reference Images 1~5) -->
  <nav class="tab-nav-bar" id="tabNavBar">
    <div class="tab-nav-container">
      <a href="index.html" class="btn-to-slide">🖥️ 切換至教學簡報</a>
      <button class="tab-btn" data-tab="briefing" onclick="switchTab('briefing')" style="background:#fff1f2; border:1.5px solid #fecdd3; color:#be123c; font-weight:800;">📢 10/23線上說明會</button>
      <button class="tab-btn active" data-tab="schedule" onclick="switchTab('schedule')">📅 行程總覽</button>
      <button class="tab-btn" data-tab="lookup" onclick="switchTab('lookup')">🔍 查帳分車</button>
      <button class="tab-btn" data-tab="buses" onclick="switchTab('buses')">🚌 團務車次</button>
      <button class="tab-btn" data-tab="camp-cook" onclick="switchTab('camp-cook')">⛺ 帳棚・野炊</button>
      <button class="tab-btn" data-tab="scout-mountain" onclick="switchTab('scout-mountain')">⚜️ 童軍・山訓</button>
      <button class="tab-btn" data-tab="worksheet" onclick="switchTab('worksheet')">🎯 露營學習單</button>
      <button class="tab-btn" data-tab="pack-rules" onclick="switchTab('pack-rules')">🎒 行李・生活</button>
    </div>
  </nav>

  <!-- Main Content Panes -->
  <main class="main-content">

    <!-- ==================== TAB 0: 📢 10/23 線上說明會 ==================== -->
    <section class="tab-pane" id="pane-briefing">
      <div class="section-header">
        <div>
          <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.3rem; flex-wrap:wrap;">
            <span style="background:#ef4444; color:#fff; font-size:0.75rem; font-weight:bold; padding:0.2rem 0.6rem; border-radius:9999px;">重要行前宣導</span>
            <span style="background:#2563eb; color:#fff; font-size:0.75rem; font-weight:bold; padding:0.2rem 0.6rem; border-radius:9999px;">線上確認單</span>
            <span style="background:#0284c7; color:#fff; font-size:0.75rem; font-weight:bold; padding:0.2rem 0.6rem; border-radius:9999px;">21頁完整簡報</span>
            <span style="background:#16a34a; color:#fff; font-size:0.75rem; font-weight:bold; padding:0.2rem 0.6rem; border-radius:9999px;">海報公告</span>
          </div>
          <h2 class="section-title">📢 10/23 二年級隔宿露營行前線上說明會</h2>
          <p class="section-subtitle">家長與同學行前必看！涵蓋四大重點叮嚀、說明會錄影、21頁圖文簡報、重點海報，以及最下方「線上確認簽名單」</p>
          <div style="margin-top:0.6rem;">
            <a href="#briefing-form-card" style="display:inline-flex; align-items:center; gap:0.4rem; background:#eff6ff; border:1px solid #93c5fd; color:#1d4ed8; padding:0.35rem 0.85rem; border-radius:9999px; font-size:0.88rem; font-weight:700; text-decoration:none;">
              ✍️ 點此快速跳至頁面最下方填寫「線上確認單」 ➔
            </a>
          </div>
        </div>
      </div>

      <!-- 10/23 行前說明會四大重點宣導 -->
      <div style="background:#fff1f2; border:2px solid #fecdd3; border-radius:16px; padding:1.5rem; margin-bottom:1.5rem; box-shadow:0 4px 15px rgba(225, 29, 72, 0.08);">
        <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:1rem;">
          <span style="background:#e11d48; color:#fff; font-size:0.85rem; font-weight:700; padding:0.3rem 0.8rem; border-radius:9999px;">重要行前宣導</span>
          <h3 style="font-size:1.35rem; font-weight:800; color:#9f1239; margin:0;">📢 10/23（五）隔宿露營行前說明會四大重點</h3>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem;">
          <div style="background:#ffffff; border:1px solid #fecdd3; border-radius:12px; padding:1.1rem;">
            <div style="font-weight:700; color:#be123c; font-size:1.05rem; margin-bottom:0.4rem;">🚫 一、違禁品出發前再檢查</div>
            <p style="font-size:0.92rem; color:#4c0519; line-height:1.65; margin:0;">
              嚴禁攜帶菸酒、檳榔、各類刀械利器、打火機及危險物品。<strong>出發前請家長與導師務必再徹底檢查一次行李！</strong>
            </p>
          </div>
          <div style="background:#ffffff; border:1px solid #fecdd3; border-radius:12px; padding:1.1rem;">
            <div style="font-weight:700; color:#be123c; font-size:1.05rem; margin-bottom:0.4rem;">📱 二、個人物品與手機統一保管</div>
            <p style="font-size:0.92rem; color:#4c0519; line-height:1.65; margin:0;">
              健保卡、個人醫藥必帶；<strong>零用錢限制在 600 元以內</strong>；<strong>學校體育服供晚上洗澡後就寢穿著</strong>。手機由學校導師統一保管，<strong>晚上約有 1 小時開放向家長打電話報平安</strong>。
            </p>
          </div>
          <div style="background:#ffffff; border:1px solid #fecdd3; border-radius:12px; padding:1.1rem;">
            <div style="font-weight:700; color:#be123c; font-size:1.05rem; margin-bottom:0.4rem;">👕 三、服裝儀容與畢旅連動</div>
            <div style="font-size:0.92rem; color:#4c0519; line-height:1.75; margin:0;">
              <div>1. <strong>晚上一律穿體育服</strong></div>
              <div>2. <strong>白天由老師自行決定（班服或便服）（下身一律著深色長褲）</strong></div>
              <div>3. <strong>第一天表現不好，第二天將穿體育服</strong></div>
              <div>4. <strong>本次露營生活常規表現將作為三年級畢業旅行服裝規定之重要評量依據（畢旅服裝看表現！）</strong></div>
            </div>
          </div>
          <div style="background:#ffffff; border:2px solid #ef4444; border-radius:12px; padding:1.1rem; background:#fff5f5;">
            <div style="font-weight:700; color:#b91c1c; font-size:1.05rem; margin-bottom:0.4rem;">🚨 四、機動車即刻送回學校</div>
            <p style="font-size:0.92rem; color:#7f1d1d; line-height:1.65; margin:0;">
              活動期間凡違犯校規之<strong>打架、抽菸、喝酒、吃檳榔等重大偏差行為，一律由「機動車即刻送回學校，通知家長帶回家管教」，並依校規予以「記大過處分」！</strong>
            </p>
          </div>
        </div>
      </div>

      <!-- 1. 嵌入 YouTube 說明會影片 -->
      <div class="briefing-video-card" style="background:#ffffff; border:1.5px solid #bae6fd; border-radius:16px; padding:1.25rem; box-shadow:0 4px 20px rgba(2,132,199,0.08); margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.85rem; flex-wrap:wrap; gap:0.5rem;">
          <div style="display:flex; align-items:center; gap:0.5rem;">
            <span style="font-size:1.3rem;">🎬</span>
            <h3 style="font-size:1.15rem; color:#0369a1; font-weight:800; margin:0;">說明會線上錄影完整重溫</h3>
          </div>
          <a href="https://youtu.be/Q81Z1Sxl0_0" target="_blank" class="btn-hero-action" style="background:#fef2f2; border:1px solid #fecaca; color:#dc2626; font-weight:700; text-decoration:none; padding:0.35rem 0.85rem; border-radius:8px; font-size:0.85rem; display:inline-flex; align-items:center; gap:0.35rem;">
            ▶ 在 YouTube 開啟播放 ↗
          </a>
        </div>
        <div style="position:relative; width:100%; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:12px; background:#0f172a; box-shadow:0 6px 18px rgba(0,0,0,0.15);">
          <iframe src="https://www.youtube-nocookie.com/embed/Q81Z1Sxl0_0" title="1151023投中隔宿露營行前說明會" style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <p style="font-size:0.88rem; color:#64748b; margin-top:0.75rem; line-height:1.6;">
          📌 <strong>影片導讀</strong>：請同學與家長在出發前完整觀看說明會錄影，詳細了解各班集合時間、乘車秩序、活動流程、違禁品管制與生活常規要求。
        </p>
      </div>

      <!-- 2. 21 張投影片簡報播放器 -->
      <div class="briefing-slideshow-card" style="background:#ffffff; border:1.5px solid #bae6fd; border-radius:16px; padding:1.25rem; box-shadow:0 4px 20px rgba(2,132,199,0.08); margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.6rem;">
          <div>
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <span style="font-size:1.3rem;">📑</span>
              <h3 style="font-size:1.15rem; color:#0369a1; font-weight:800; margin:0;">1151023 二年級隔宿露營行前須知簡報 (21 頁)</h3>
            </div>
            <p style="font-size:0.85rem; color:#64748b; margin-top:0.25rem;">支援上一頁、下一頁按鈕切換、縮圖快速跳轉，點擊大圖可開啟全螢幕高解析放大檢視</p>
          </div>
          <div style="display:flex; align-items:center; gap:0.5rem; background:#f0f9ff; padding:0.35rem 0.75rem; border-radius:10px; border:1px solid #bae6fd;">
            <button class="sub-tab-btn" onclick="prevBriefingSlide()" style="padding:0.35rem 0.85rem; font-weight:bold; font-size:0.88rem;">◀ 上一張</button>
            <span id="briefingSlideIndicator" style="font-size:0.95rem; font-weight:800; color:#0284c7; min-width:90px; text-align:center;">第 1 / 21 頁</span>
            <button class="sub-tab-btn" onclick="nextBriefingSlide()" style="padding:0.35rem 0.85rem; font-weight:bold; font-size:0.88rem;">下一張 ▶</button>
          </div>
        </div>

        <!-- 播放器主畫面 (大圖) -->
        <div style="position:relative; background:#0f172a; border-radius:12px; overflow:hidden; text-align:center; min-height:300px; display:flex; align-items:center; justify-content:center; box-shadow:inset 0 0 25px rgba(0,0,0,0.5);">
          <img id="briefingMainImg" src="assets/briefing/slide_1.jpg" alt="行前須知投影片 1" style="max-width:100%; max-height:560px; width:auto; height:auto; object-fit:contain; border-radius:8px; cursor:zoom-in; transition:opacity 0.2s ease;" onclick="openLightbox(this.src, '行前須知投影片 第 ' + currentBriefingSlide + ' 頁')">
          
          <!-- 左右浮動翻頁按鈕 -->
          <button onclick="prevBriefingSlide()" style="position:absolute; left:12px; top:50%; transform:translateY(-50%); background:rgba(0,0,0,0.65); color:#fff; border:1.5px solid rgba(255,255,255,0.4); border-radius:50%; width:46px; height:46px; font-size:1.3rem; font-weight:bold; cursor:pointer; display:flex; align-items:center; justify-content:center; backdrop-filter:blur(6px); transition:all 0.2s; box-shadow:0 4px 12px rgba(0,0,0,0.3);" title="上一張 (←)">◀</button>
          <button onclick="nextBriefingSlide()" style="position:absolute; right:12px; top:50%; transform:translateY(-50%); background:rgba(0,0,0,0.65); color:#fff; border:1.5px solid rgba(255,255,255,0.4); border-radius:50%; width:46px; height:46px; font-size:1.3rem; font-weight:bold; cursor:pointer; display:flex; align-items:center; justify-content:center; backdrop-filter:blur(6px); transition:all 0.2s; box-shadow:0 4px 12px rgba(0,0,0,0.3);" title="下一張 (→)">▶</button>
        </div>

        <!-- 底部 21 張微縮圖滑軌 -->
        <div style="margin-top:0.85rem;">
          <div style="font-size:0.82rem; font-weight:700; color:#64748b; margin-bottom:0.35rem;">縮圖快速瀏覽（點擊任一頁立即切換）：</div>
          <div style="display:flex; gap:0.5rem; overflow-x:auto; padding-bottom:0.6rem; scrollbar-width:thin;" id="briefingThumbnailsStrip">
            <img src="assets/briefing/slide_1.jpg" alt="投影片 1" class="briefing-thumb-item" onclick="goToBriefingSlide(1)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #0284c7; flex-shrink:0; transition:all 0.2s;" title="跳至第 1 頁">
            <img src="assets/briefing/slide_2.jpg" alt="投影片 2" class="briefing-thumb-item" onclick="goToBriefingSlide(2)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 2 頁">
            <img src="assets/briefing/slide_3.jpg" alt="投影片 3" class="briefing-thumb-item" onclick="goToBriefingSlide(3)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 3 頁">
            <img src="assets/briefing/slide_4.jpg" alt="投影片 4" class="briefing-thumb-item" onclick="goToBriefingSlide(4)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 4 頁">
            <img src="assets/briefing/slide_5.jpg" alt="投影片 5" class="briefing-thumb-item" onclick="goToBriefingSlide(5)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 5 頁">
            <img src="assets/briefing/slide_6.jpg" alt="投影片 6" class="briefing-thumb-item" onclick="goToBriefingSlide(6)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 6 頁">
            <img src="assets/briefing/slide_7.jpg" alt="投影片 7" class="briefing-thumb-item" onclick="goToBriefingSlide(7)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 7 頁">
            <img src="assets/briefing/slide_8.jpg" alt="投影片 8" class="briefing-thumb-item" onclick="goToBriefingSlide(8)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 8 頁">
            <img src="assets/briefing/slide_9.jpg" alt="投影片 9" class="briefing-thumb-item" onclick="goToBriefingSlide(9)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 9 頁">
            <img src="assets/briefing/slide_10.jpg" alt="投影片 10" class="briefing-thumb-item" onclick="goToBriefingSlide(10)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 10 頁">
            <img src="assets/briefing/slide_11.jpg" alt="投影片 11" class="briefing-thumb-item" onclick="goToBriefingSlide(11)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 11 頁">
            <img src="assets/briefing/slide_12.jpg" alt="投影片 12" class="briefing-thumb-item" onclick="goToBriefingSlide(12)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 12 頁">
            <img src="assets/briefing/slide_13.jpg" alt="投影片 13" class="briefing-thumb-item" onclick="goToBriefingSlide(13)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 13 頁">
            <img src="assets/briefing/slide_14.jpg" alt="投影片 14" class="briefing-thumb-item" onclick="goToBriefingSlide(14)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 14 頁">
            <img src="assets/briefing/slide_15.jpg" alt="投影片 15" class="briefing-thumb-item" onclick="goToBriefingSlide(15)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 15 頁">
            <img src="assets/briefing/slide_16.jpg" alt="投影片 16" class="briefing-thumb-item" onclick="goToBriefingSlide(16)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 16 頁">
            <img src="assets/briefing/slide_17.jpg" alt="投影片 17" class="briefing-thumb-item" onclick="goToBriefingSlide(17)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 17 頁">
            <img src="assets/briefing/slide_18.jpg" alt="投影片 18" class="briefing-thumb-item" onclick="goToBriefingSlide(18)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 18 頁">
            <img src="assets/briefing/slide_19.jpg" alt="投影片 19" class="briefing-thumb-item" onclick="goToBriefingSlide(19)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 19 頁">
            <img src="assets/briefing/slide_20.jpg" alt="投影片 20" class="briefing-thumb-item" onclick="goToBriefingSlide(20)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 20 頁">
            <img src="assets/briefing/slide_21.jpg" alt="投影片 21" class="briefing-thumb-item" onclick="goToBriefingSlide(21)" style="width:72px; height:42px; object-fit:cover; border-radius:6px; cursor:pointer; border:2px solid #e2e8f0; flex-shrink:0; transition:all 0.2s;" title="跳至第 21 頁">
          </div>
        </div>
      </div>

      <!-- 3. 最下方 2 張海報與須知重點圖片 -->
      <div class="briefing-posters-card" style="background:#ffffff; border:1.5px solid #bae6fd; border-radius:16px; padding:1.25rem; box-shadow:0 4px 20px rgba(2,132,199,0.08);">
        <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:1rem;">
          <span style="font-size:1.3rem;">📌</span>
          <h3 style="font-size:1.15rem; color:#0369a1; font-weight:800; margin:0;">行前須知海報與重點公告圖檔</h3>
        </div>
        
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.25rem;">
          <!-- 海報 -->
          <div style="border:1.5px solid #e0f2fe; border-radius:12px; padding:1rem; background:#f8fafc; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem;">
              <h4 style="font-size:1rem; color:#0f172a; font-weight:700; margin:0;">📄 1151023 二年級隔宿露營行前須知海報</h4>
              <button onclick="openLightbox('assets/briefing/briefing_poster.jpg', '二年級隔宿露營行前須知海報')" class="sub-tab-btn" style="padding:0.25rem 0.6rem; font-size:0.8rem;">🔍 放大</button>
            </div>
            <div style="overflow:hidden; border-radius:8px; background:#fff; box-shadow:0 4px 14px rgba(0,0,0,0.08); cursor:zoom-in;" onclick="openLightbox('assets/briefing/briefing_poster.jpg', '二年級隔宿露營行前須知海報')">
              <img src="assets/briefing/briefing_poster.jpg" alt="行前須知海報" style="width:100%; height:auto; display:block; transition:transform 0.25s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <p style="font-size:0.85rem; color:#64748b; margin-top:0.6rem;">點擊圖片可開啟全螢幕高解析度檢視</p>
          </div>

          <!-- 行前須知 4 -->
          <div style="border:1.5px solid #e0f2fe; border-radius:12px; padding:1rem; background:#f8fafc; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem;">
              <h4 style="font-size:1rem; color:#0f172a; font-weight:700; margin:0;">📋 1151023 二年級隔宿露營行前須知 4</h4>
              <button onclick="openLightbox('assets/briefing/briefing_notice4.png', '二年級隔宿露營行前須知 4')" class="sub-tab-btn" style="padding:0.25rem 0.6rem; font-size:0.8rem;">🔍 放大</button>
            </div>
            <div style="overflow:hidden; border-radius:8px; background:#fff; box-shadow:0 4px 14px rgba(0,0,0,0.08); cursor:zoom-in;" onclick="openLightbox('assets/briefing/briefing_notice4.png', '二年級隔宿露營行前須知 4')">
              <img src="assets/briefing/briefing_notice4.png" alt="行前須知 4" style="width:100%; height:auto; display:block; transition:transform 0.25s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <p style="font-size:0.85rem; color:#64748b; margin-top:0.6rem;">點擊圖片可開啟全螢幕高解析度檢視</p>
          </div>
        </div>
      </div>

      <!-- 4. 最下方：南投國中隔宿露營行前宣導線上確認單 (Google Apps Script) -->
      <div class="briefing-form-card" id="briefing-form-card" style="background:#ffffff; border:2px solid #3b82f6; border-radius:16px; padding:1.5rem; box-shadow:0 6px 24px rgba(37,99,235,0.12); margin-top:1.75rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.8rem;">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <span style="font-size:1.6rem;">✍️</span>
            <div>
              <h3 style="font-size:1.25rem; color:#1d4ed8; font-weight:800; margin:0;">南投國中隔宿露營行前宣導線上確認單</h3>
              <p style="font-size:0.88rem; color:#64748b; margin:0.2rem 0 0 0;">請全體二年級同學與家長於詳閱上方四大重點與行前須知後，於下方完成線上簽名與資料送出</p>
            </div>
          </div>
          <a href="https://script.google.com/macros/s/AKfycbwAqWNLvsp72k-TDaxTZVDHuYEzZ3S0pseO1e1T_ImAdDonx-Lkp_0i1ANFQKQ5csmCqg/exec" target="_blank" class="btn-hero-action" style="background:#2563eb; color:#ffffff; font-weight:700; text-decoration:none; padding:0.5rem 1.25rem; border-radius:10px; font-size:0.95rem; display:inline-flex; align-items:center; gap:0.4rem; box-shadow:0 4px 12px rgba(37,99,235,0.25);">
            ↗ 在新視窗開啟確認單（全螢幕填寫）
          </a>
        </div>

        <!-- Google Apps Script 直接嵌入視窗 -->
        <div style="position:relative; width:100%; height:860px; border-radius:12px; overflow:hidden; border:1.5px solid #cbd5e1; background:#f8fafc; box-shadow:inset 0 2px 6px rgba(0,0,0,0.03);">
          <iframe src="https://script.google.com/macros/s/AKfycbwAqWNLvsp72k-TDaxTZVDHuYEzZ3S0pseO1e1T_ImAdDonx-Lkp_0i1ANFQKQ5csmCqg/exec" title="南投國中隔宿露營行前宣導確認單" style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" allowfullscreen></iframe>
        </div>

        <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:0.85rem 1.15rem; margin-top:0.85rem; font-size:0.88rem; color:#1e40af; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem;">
          <span>📌 <strong>填寫說明</strong>：填寫年級、班級、座號、姓名及聯絡 Email 並勾選確認後送出，系統將自動寄送確認信留存。若因瀏覽器安全限制未直接顯示上方表格，請點擊上方或右方按鈕直接開啟填寫。</span>
          <a href="https://script.google.com/macros/s/AKfycbwAqWNLvsp72k-TDaxTZVDHuYEzZ3S0pseO1e1T_ImAdDonx-Lkp_0i1ANFQKQ5csmCqg/exec" target="_blank" style="font-weight:700; color:#2563eb; text-decoration:underline; white-space:nowrap;">點此直接開啟填寫 ↗</a>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 1: 📅 行程總覽 ==================== -->
    <section class="tab-pane active" id="pane-schedule">
      <div class="section-header">
        <div>
          <h2 class="section-title">📅 兩日行程時間與路線</h2>
          <p class="section-subtitle">點選下方天數切換行程細節、用餐安排與重點時間</p>
        </div>
      </div>

      <!-- Day Switch Buttons (Image 1 Style) -->
      <div class="day-selector-grid">
        <div class="day-card-btn active" id="dayBtn1" onclick="switchDay(1)">
          <div class="day-title">第 1 天</div>
          <div class="day-date">115/10/27 (星期二)</div>
        </div>
        <div class="day-card-btn" id="dayBtn2" onclick="switchDay(2)">
          <div class="day-title">第 2 天</div>
          <div class="day-date">115/10/28 (星期三)</div>
        </div>
      </div>

      <!-- Day 1 Content -->
      <div id="dayContent1">
        <div class="day-banner-card">
          <div class="day-banner-header">
            <span style="font-size:1.5rem;">☀️</span>
            <div>
              <div class="day-banner-title">Day 1：啟程出發・營地建設・技能教育・營火晚會</div>
              <div style="font-size:0.92rem; color:#64748b;">⛺ 營地：尖山埤露營區（屋式帳） | 📅 日期：115/10/27 (星期二)</div>
            </div>
          </div>
          <div class="meal-badges-row">
            <div class="meal-badge-box">🥣 早餐：自理</div>
            <div class="meal-badge-box">🍱 午餐：美味中式便當</div>
            <div class="meal-badge-box">🍲 晚餐：炊事競賽・野炊實作</div>
          </div>
        </div>

        <div class="timeline-wrap">
          <div class="timeline-card">
            <div class="time-badge">07:30 - 08:00</div>
            <div class="timeline-info">
              <div class="timeline-title">學校集合・逃生避難演練</div>
              <div class="timeline-desc">921 地震公園暨南投國際會展中心園區集合，實施人員點名與大客車逃生演練。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">08:00 - 10:00</div>
            <div class="timeline-info">
              <div class="timeline-title">快樂啟程・國道風光・行車安全宣導</div>
              <div class="timeline-desc">分乘 4 輛專車南下台南尖山埤，車上宣導乘車安全、繫妥安全帶並完成安全檢查。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">10:00 - 11:00</div>
            <div class="timeline-info">
              <div class="timeline-title">喜相逢～環境認識・安全檢查</div>
              <div class="timeline-desc">抵達尖山埤露營區，活動小隊編組、營地環境巡禮與個人違禁品安全檢查。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">11:00 - 12:00</div>
            <div class="timeline-info">
              <div class="timeline-title">開訓始業式～營規介紹・隊輔亮相</div>
              <div class="timeline-desc">師長致詞勉勵、營規與生活公約宣誓、值星官交接與隨隊隊輔熱情見面會。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">12:00 - 13:00</div>
            <div class="timeline-info">
              <div class="timeline-title">午餐饗宴～活力補給</div>
              <div class="timeline-desc">享用營養美味中式便當，各班稍作休息補充足沛水分。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">13:00 - 14:00</div>
            <div class="timeline-info">
              <div class="timeline-title">野營常識介紹～帳棚搭設示範</div>
              <div class="timeline-desc">屋式帳結構解析、搭帳五步驟、外帳收折口訣、營釘 45° 倒勾力學講解與各班領取搭帳器材。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">14:00 - 17:00</div>
            <div class="timeline-info">
              <div class="timeline-title">分站技能教育 Part 1：童軍核心技能</div>
              <div class="timeline-desc">五大專業關卡輪番闖關：① 生火技巧與炊具運用 ② 戰術偽裝與自然方位判讀 ③ 常用八大繩結生活應用 ④ 台灣六大毒蛇辨識與五要五不急救 ⑤ 晚會預習與音樂律動。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">17:00 - 19:00</div>
            <div class="timeline-info">
              <div class="timeline-title">炊事競賽～野炊廚藝大比拚</div>
              <div class="timeline-desc">全團 15 組分工合作生火、洗切、掌廚配菜，實踐做中學並評比班級炊事總錦標。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">19:10 - 21:30</div>
            <div class="timeline-info">
              <div class="timeline-title">營火晚會～燭光夜語・薪火相傳</div>
              <div class="timeline-desc">狂歡營火點燃、班級才藝創意競賽、隊輔群勁歌熱舞，最後於柔美燭光中感性對話、凝聚師生情誼。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">21:30 - 22:30</div>
            <div class="timeline-info">
              <div class="timeline-title">盥洗沐浴・暖心宵夜</div>
              <div class="timeline-desc">依分流順序盥洗，享用熱騰騰宵夜點心，回帳篷準備就寢。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">22:30 - 就寢</div>
            <div class="timeline-info">
              <div class="timeline-title">熄燈就寢・導師查舖點名</div>
              <div class="timeline-desc">營地全面熄燈安靜，鞋子倒放防蛇蟲入內，隨隊導師查房查帳確保安全。</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Day 2 Content -->
      <div id="dayContent2" style="display:none;">
        <div class="day-banner-card">
          <div class="day-banner-header">
            <span style="font-size:1.5rem;">🌅</span>
            <div>
              <div class="day-banner-title">Day 2：活力晨操・山訓探索・烤肉BBQ・平安賦歸</div>
              <div style="font-size:0.92rem; color:#64748b;">⛺ 活動地點：尖山埤渡假村山訓區 | 📅 日期：115/10/28 (星期三)</div>
            </div>
          </div>
          <div class="meal-badges-row">
            <div class="meal-badge-box">🥣 早餐：活力中式早餐・合菜</div>
            <div class="meal-badge-box">🍖 午餐：歡樂 BBQ 烤肉餐</div>
            <div class="meal-badge-box">🏠 晚餐：返家溫馨晚餐</div>
          </div>
        </div>

        <div class="timeline-wrap">
          <div class="timeline-card">
            <div class="time-badge">06:00 - 06:30</div>
            <div class="timeline-info">
              <div class="timeline-title">晨喚起床～做個跟太陽賽跑的人</div>
              <div class="timeline-desc">整理內務、收拾行囊裝備，實施晨間曬帳防潮。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">06:30 - 07:20</div>
            <div class="timeline-info">
              <div class="timeline-title">活力有氧～晨操動一動</div>
              <div class="timeline-desc">全體同學集合大草坪，跟隨隊輔進行活力晨間有氧體操，喚醒身心能量。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">07:20 - 08:00</div>
            <div class="timeline-info">
              <div class="timeline-title">享用早餐～中式美味合菜</div>
              <div class="timeline-desc">享用營養滿分熱食中式早餐合菜，儲備整日上午山訓挑戰體能。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">08:00 - 11:30</div>
            <div class="timeline-info">
              <div class="timeline-title">分站教育 Part 2：山訓與探索教育</div>
              <div class="timeline-desc">五大挑戰極限關卡：① 膽量大考驗・進擊の垂降 ② 解手結與團隊跳繩挑戰 ③ 超級蜘蛛人・攀岩絕技 ④ 生存遊戲水彈射擊競賽 ⑤ 信心考驗獨木橋。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">11:30 - 14:00</div>
            <div class="timeline-info">
              <div class="timeline-title">午餐約會～歡樂 BBQ 烤肉饗宴</div>
              <div class="timeline-desc">全團各組分工生火烤肉，享用豐盛 BBQ 食材，互道兩天一夜合作情誼。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">14:00 - 15:00</div>
            <div class="timeline-info">
              <div class="timeline-title">結訓典禮～榮耀加冕與收心反思</div>
              <div class="timeline-desc">頒發炊事錦標、晚會節目優勝、晨檢整潔獎、分站探索榮譽與全校精神總錦標，校長師長勉勵。</div>
            </div>
          </div>
          <div class="timeline-card">
            <div class="time-badge">15:00 - 16:20</div>
            <div class="timeline-info">
              <div class="timeline-title">滿載收穫・平安賦歸</div>
              <div class="timeline-desc">整理環境無痕山林，專車踏上歸途，預計 16:20 返抵南投國中校門。</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 2: 🔍 查帳分車 ==================== -->
    <section class="tab-pane" id="pane-lookup">
      <div class="section-header">
        <div>
          <h2 class="section-title">🔍 帳號、桌次與車次即時速查</h2>
          <p class="section-subtitle">輸入同學姓名、帳號、班級（801~807）或桌次即可秒查！姓名第二字固化遮蔽確保個資安全。</p>
        </div>
        <button class="btn-hero-action" onclick="window.print()">🖨️ 列印查帳名冊</button>
      </div>

      <!-- Search Panel (Image 2 Style) -->
      <div class="search-panel">
        <div class="search-input-wrap">
          <span class="search-icon-inside">🔍</span>
          <input type="text" id="searchInput" class="search-input" placeholder="輸入同學姓名、帳號、班級（801~807）或桌次關鍵字..." oninput="filterStudents()">
        </div>

        <div class="filter-group-row">
          <span class="filter-label">班級篩選：</span>
          <button class="filter-pill-btn active" data-type="class" data-val="all" onclick="setFilter('class', 'all', this)">全部對象</button>
          <button class="filter-pill-btn" data-type="class" data-val="801" onclick="setFilter('class', '801', this)">801班</button>
          <button class="filter-pill-btn" data-type="class" data-val="802" onclick="setFilter('class', '802', this)">802班</button>
          <button class="filter-pill-btn" data-type="class" data-val="803" onclick="setFilter('class', '803', this)">803班</button>
          <button class="filter-pill-btn" data-type="class" data-val="804" onclick="setFilter('class', '804', this)">804班</button>
          <button class="filter-pill-btn" data-type="class" data-val="805" onclick="setFilter('class', '805', this)">805班</button>
          <button class="filter-pill-btn" data-type="class" data-val="806" onclick="setFilter('class', '806', this)">806班</button>
          <button class="filter-pill-btn" data-type="class" data-val="807" onclick="setFilter('class', '807', this)">807班</button>
        </div>

        <div class="filter-group-row">
          <span class="filter-label">車次篩選：</span>
          <button class="filter-pill-btn active" data-type="bus" data-val="all" onclick="setFilter('bus', 'all', this)">全部車次</button>
          <button class="filter-pill-btn" data-type="bus" data-val="1" onclick="setFilter('bus', '1', this)">1車</button>
          <button class="filter-pill-btn" data-type="bus" data-val="2" onclick="setFilter('bus', '2', this)">2車</button>
          <button class="filter-pill-btn" data-type="bus" data-val="3" onclick="setFilter('bus', '3', this)">3車</button>
          <button class="filter-pill-btn" data-type="bus" data-val="丁" onclick="setFilter('bus', '丁', this)">丁車</button>
        </div>

        <div class="filter-group-row" style="margin-bottom:0;">
          <span class="filter-label">性別篩選：</span>
          <button class="filter-pill-btn active" data-type="gender" data-val="all" onclick="setFilter('gender', 'all', this)">全部性別</button>
          <button class="filter-pill-btn" data-type="gender" data-val="男" onclick="setFilter('gender', '男', this)">男生</button>
          <button class="filter-pill-btn" data-type="gender" data-val="女" onclick="setFilter('gender', '女', this)">女生</button>
          <span id="resultCountBadge" style="margin-left:auto; font-size:0.88rem; font-weight:700; color:#0284c7;">共 107 筆資料</span>
        </div>
      </div>

      <!-- Result Table -->
      <div class="table-container">
        <table class="custom-table">
          <thead>
            <tr>
              <th>班級</th>
              <th>學生姓名</th>
              <th>性別</th>
              <th>分配車次</th>
              <th>帳篷編號</th>
              <th>野炊組別</th>
              <th>重要備註</th>
            </tr>
          </thead>
          <tbody id="studentTableBody">
            {student_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- ==================== TAB 3: 🚌 團務車次 ==================== -->
    <section class="tab-pane" id="pane-buses">
      <div class="section-header">
        <div>
          <h2 class="section-title">🚌 團務編組與隨車師長</h2>
          <p class="section-subtitle">全團 4 輛專車編制、各車班級名額與隨車導師名單</p>
        </div>
      </div>

      <div class="buses-grid">
        <!-- 1 車 (Image 3 Style) -->
        <div class="bus-card">
          <div>
            <div class="bus-card-header">
              <div class="bus-card-title">🚌 1 車</div>
              <span class="bus-student-pill">學生 20 人</span>
            </div>
            <div class="bus-class-line">班級分配：805 (全部) + 806 (全部)</div>
            <div class="bus-breakdown">805班：男7、女4 (11人) | 806班：男4、女5 (9人)</div>
            
            <div class="bus-teachers-box">
              <div class="bus-teachers-label">隨車師長</div>
              <div class="bus-teacher-item">
                <span>學務主任</span>
                <span style="font-weight:700;">董O遠</span>
              </div>
              <div class="bus-teacher-item">
                <span>805 班導師</span>
                <span style="font-weight:700;">林O銓</span>
              </div>
              <div class="bus-teacher-item">
                <span>806 班導師</span>
                <span style="font-weight:700;">許O玉</span>
              </div>
            </div>
          </div>
          <div class="bus-veg-badge">
            <span>🥗</span>
            <span>本車含素食餐食：1 位 (805班 15號 張O瑜)</span>
          </div>
        </div>

        <!-- 2 車 -->
        <div class="bus-card">
          <div>
            <div class="bus-card-header">
              <div class="bus-card-title">🚌 2 車</div>
              <span class="bus-student-pill">學生 34 人</span>
            </div>
            <div class="bus-class-line">班級分配：802 (全部) + 804 (全部)</div>
            <div class="bus-breakdown">802班：男6、女13 (19人) | 804班：男7、女8 (15人)</div>
            
            <div class="bus-teachers-box">
              <div class="bus-teachers-label">隨車師長</div>
              <div class="bus-teacher-item">
                <span>802 班導師</span>
                <span style="font-weight:700;">黃O君</span>
              </div>
              <div class="bus-teacher-item">
                <span>804 班導師</span>
                <span style="font-weight:700;">李O儒</span>
              </div>
            </div>
          </div>
          <div style="font-size:0.85rem; color:#64748b; margin-top:0.5rem;">
            📌 備註：804班 11號女同學 劉O硯 於本車，與805班同名同學分屬不同車次。
          </div>
        </div>

        <!-- 3 車 -->
        <div class="bus-card">
          <div>
            <div class="bus-card-header">
              <div class="bus-card-title">🚌 3 車</div>
              <span class="bus-student-pill">學生 32 人</span>
            </div>
            <div class="bus-class-line">班級分配：801 (全部) + 803 (全部)</div>
            <div class="bus-breakdown">801班：男10、女7 (17人) | 803班：男6、女9 (15人)</div>
            
            <div class="bus-teachers-box">
              <div class="bus-teachers-label">隨車師長</div>
              <div class="bus-teacher-item">
                <span>801 班導師</span>
                <span style="font-weight:700;">黃O月</span>
              </div>
              <div class="bus-teacher-item">
                <span>803 班導師</span>
                <span style="font-weight:700;">林O玟</span>
              </div>
            </div>
          </div>
          <div style="font-size:0.85rem; color:#64748b; margin-top:0.5rem;">
            📌 備註：801班男女人數平衡，本車含第 1、2、6、7 野炊小隊。
          </div>
        </div>

        <!-- 丁 車 -->
        <div class="bus-card">
          <div>
            <div class="bus-card-header">
              <div class="bus-card-title">🚌 丁 車</div>
              <span class="bus-student-pill">學生 21 人</span>
            </div>
            <div class="bus-class-line">班級分配：807 (全部)</div>
            <div class="bus-breakdown">807班：男8、女13 (全班 21人)</div>
            
            <div class="bus-teachers-box">
              <div class="bus-teachers-label">隨車師長</div>
              <div class="bus-teacher-item">
                <span>訓育組長</span>
                <span style="font-weight:700;">姚O勤</span>
              </div>
              <div class="bus-teacher-item">
                <span>807 班導師</span>
                <span style="font-weight:700;">黃O慧</span>
              </div>
            </div>
          </div>
          <div style="font-size:0.85rem; color:#64748b; margin-top:0.5rem;">
            📌 備註：全班單獨成車，含第 13、14、15 野炊小隊及帳棚 A12~A13、B12~B14。
          </div>
        </div>

        <!-- 公務指揮車 -->
        <div class="bus-card" style="border-left: 4px solid #f97316;">
          <div>
            <div class="bus-card-header">
              <div class="bus-card-title">🚗 公務機動指揮車</div>
              <span class="bus-student-pill" style="background:#ffedd5; color:#c2410c;">巡迴督導</span>
            </div>
            <div class="bus-class-line">任務職掌：全校行車戒護、緊急應變與醫療支援</div>
            <div class="bus-breakdown">機動巡迴 4 輛遊覽車前後，掌握路況與隨隊安全</div>
            
            <div class="bus-teachers-box">
              <div class="bus-teachers-label">巡查人員名冊</div>
              <div class="bus-teacher-item">
                <span>南投國中校長</span>
                <span style="font-weight:700;">劉O彥</span>
              </div>
              <div class="bus-teacher-item">
                <span>中國青年旅行社團控經理</span>
                <span style="font-weight:700;">邱O凱 (0972-721756)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 4: ⛺ 帳棚・野炊 (二階層次標籤) ==================== -->
    <section class="tab-pane" id="pane-camp-cook">
      <div class="sub-tab-nav-bar">
        <div class="sub-tab-title">⛺ 帳棚住宿與野炊膳食管理專區</div>
        <div class="sub-tab-pills">
          <button class="sub-tab-btn active" id="subbtn-tents" onclick="switchSubTab('camp-cook', 'tents')">⛺ 帳棚住宿編組</button>
          <button class="sub-tab-btn" id="subbtn-meals" onclick="switchSubTab('camp-cook', 'meals')">🍲 野炊膳食編組</button>
        </div>
      </div>

      <!-- 二階子區域 1: 帳棚住宿 -->
      <div class="sub-pane active" id="subpane-tents">
        <!-- ==================== TAB 4: ⛺ 帳棚住宿 ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">⛺ 營地配置與帳棚住宿編組</h2>
          <p class="section-subtitle">全團共 27 頂屋式帳篷（男生帳 A01~A13 共 13 頂、女生帳 B01~B14 共 14 頂），依班級性別集中搭設</p>
        </div>
        <div style="display:flex; gap:0.5rem;">
          <button class="filter-pill-btn active" onclick="filterTents('all', this)">全部帳篷 (27頂)</button>
          <button class="filter-pill-btn" onclick="filterTents('A', this)">男生帳 A01~A13</button>
          <button class="filter-pill-btn" onclick="filterTents('B', this)">女生帳 B01~B14</button>
        </div>
      </div>

      <!-- Camp Image Banner -->
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; padding:0.5rem; text-align:center;">
          <img src="assets/camp_setup_page13.png" style="max-width:100%; height:auto; border-radius:8px;" alt="營地配置">
          <div style="font-size:0.85rem; color:#64748b; margin-top:0.3rem;">手冊第 13 頁：營地配置與搭帳要領</div>
        </div>
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; padding:0.5rem; text-align:center;">
          <img src="assets/tent_pitching_page14.png" style="max-width:100%; height:auto; border-radius:8px;" alt="帳篷搭設圖解">
          <div style="font-size:0.85rem; color:#64748b; margin-top:0.3rem;">手冊第 14 頁：屋式帳搭設五步驟與力學原理</div>
        </div>
      </div>

      <!-- Tents Grid -->
      <div class="buses-grid" id="tentsContainer">
        {tents_cards_html}
      </div>
      </div>

      <!-- 二階子區域 2: 野炊膳食 -->
      <div class="sub-pane" id="subpane-meals">
        <!-- ==================== TAB 5: 🍲 野炊膳食 ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">🍲 炊事競賽與野炊烤肉分組</h2>
          <p class="section-subtitle">全團 15 組炊事實作編組，分工掌理掌廚、生火、配菜、洗滌與場地收拾</p>
        </div>
      </div>

      <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:12px; padding:1.2rem; margin-bottom:1.5rem; display:flex; flex-wrap:wrap; gap:1.5rem; align-items:center;">
        <div>
          <div style="font-weight:700; color:#15803d; font-size:1.05rem; margin-bottom:0.25rem;">🔥 野炊安全與生火三大守則</div>
          <div style="font-size:0.92rem; color:#334155;">① 生火三部曲：先易燃火種引燃，次鋪細柴樹枝，待火旺後加入粗柴維持炭火。 ② 鍋具取放一律使用乾抹布或隔熱手套，防止熱油熱水噴濺。 ③ 炊事完畢必須落實灰燼澆水完全降溫滅火。</div>
        </div>
        <div style="margin-left:auto; background:#ffffff; border:1px solid #86efac; border-radius:8px; padding:0.5rem 1rem; color:#15803d; font-weight:700; font-size:0.9rem;">
          🥗 第 10 組含素食 1 份 (805班 張O瑜)
        </div>
      </div>

      <div class="buses-grid" id="mealsContainer">
        {meals_cards_html}
      </div>
      </div>
    </section>

    </section>

    <!-- ==================== TAB 5: ⚜️ 童軍・山訓 (二階層次標籤) ==================== -->
    <section class="tab-pane" id="pane-scout-mountain">
      <div class="sub-tab-nav-bar">
        <div class="sub-tab-title">⚜️ 童軍技能教育與山訓探索活動專區</div>
        <div class="sub-tab-pills">
          <button class="sub-tab-btn active" id="subbtn-scout" onclick="switchSubTab('scout-mountain', 'scout')">⚜️ 童軍技能圖鑑</button>
          <button class="sub-tab-btn" id="subbtn-mountain" onclick="switchSubTab('scout-mountain', 'mountain')">🧗 山訓探索教育</button>
        </div>
      </div>

      <!-- 二階子區域 1: 童軍技能 -->
      <div class="sub-pane active" id="subpane-scout">
        <!-- ==================== TAB 6: ⚜️ 童軍技能 (Image 4 Style) ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">⚜️ 童軍技能教育圖鑑與教學影片</h2>
          <p class="section-subtitle">營地建設、常用八大繩結、自然定向、簡易急救、六大毒蛇辨識完整圖文與影音教學</p>
        </div>
      </div>

      <!-- Scout Category Nav Pills -->
      <div class="scout-nav-pills">
        <button class="filter-pill-btn active" onclick="filterScout('all', this)">全部單元 (22項)</button>
        <button class="filter-pill-btn" onclick="filterScout('tent', this)">⛺ 營地建設與屋式帳</button>
        <button class="filter-pill-btn" onclick="filterScout('knots', this)">🪢 童軍常用八大繩結</button>
        <button class="filter-pill-btn" onclick="filterScout('direction', this)">🧭 自然方向辨識</button>
        <button class="filter-pill-btn" onclick="filterScout('firstaid', this)">🩹 野外簡易急救處置</button>
        <button class="filter-pill-btn" onclick="filterScout('snakes', this)">🐍 臺灣六大毒蛇與急救</button>
      </div>

      <!-- Scout Cards Grid -->
      <div class="scout-grid" id="scoutCardsContainer">
        {scout_cards_html}
      </div>
      </div>

      <!-- 二階子區域 2: 山訓探索 -->
      <div class="sub-pane" id="subpane-mountain">
        <!-- ==================== TAB 7: 🧗 山訓探索 ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">🧗 山訓與探索教育活動</h2>
          <p class="section-subtitle">進擊の垂降、解手結、攀岩蜘蛛人、水彈生存戰、信心獨木橋</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem; margin-bottom:1.5rem;">
        <div class="scout-item-card">
          <div>
            <span class="scout-tag">探索項目 01</span>
            <div class="scout-title">進擊の垂降・膽量大考驗</div>
            <div class="scout-subtitle">克服高度恐懼，學習正確坐姿與制動手握繩姿勢</div>
            <div class="scout-img-box">
              <img src="assets/p21_img6.jpeg" alt="垂降活動">
            </div>
            <div class="scout-desc">
              穿戴專業坐式吊帶與安全頭盔，雙腳微開成外八字貼緊塔壁，右手制動手緊握煞車繩於右臀後方，平穩後仰踏步而下。
            </div>
          </div>
          <div class="scout-links-row">
            <a href="https://www.youtube.com/results?search_query=童軍山訓+垂降教學" target="_blank" class="btn-scout-video">🎬 觀看垂降教學影片</a>
          </div>
        </div>

        <div class="scout-item-card">
          <div>
            <span class="scout-tag">探索項目 02</span>
            <div class="scout-title">攀岩絕技・超級蜘蛛人</div>
            <div class="scout-subtitle">三點不動一點動，專注與肢體平衡的極致挑戰</div>
            <div class="scout-img-box">
              <img src="assets/p21_img3.jpeg" alt="攀岩絕技">
            </div>
            <div class="scout-desc">
              遵循「三點不動、一點動」攀爬金科玉律，利用大腿肌力向上推蹬，雙臂保持伸直放鬆省力，尋找最穩固的岩點攀上頂峰。
            </div>
          </div>
          <div class="scout-links-row">
            <a href="https://www.youtube.com/results?search_query=人工岩場+攀岩初學技巧" target="_blank" class="btn-scout-video">🎬 觀看攀岩技巧影片</a>
          </div>
        </div>

        <div class="scout-item-card">
          <div>
            <span class="scout-tag">探索項目 03</span>
            <div class="scout-title">水彈生存對抗競賽</div>
            <div class="scout-subtitle">團隊戰術引導、通訊呼叫與掩體戰術轉移</div>
            <div class="scout-img-box">
              <img src="assets/mountain_waterbullet_page21.png" alt="水彈生存競賽">
            </div>
            <div class="scout-desc">
              使用安全吸水軟彈，全副護目全罩面罩，在掩體沙包林立的場域進行小隊對抗，考驗小隊默契、掩護與冷靜抗壓能力。
            </div>
          </div>
          <div class="scout-links-row">
            <a href="https://www.youtube.com/results?search_query=水彈槍+射擊安全守則" target="_blank" class="btn-scout-video">🎬 觀看水彈安全守則影片</a>
          </div>
        </div>
      </div>

      <!-- Water Bullet Safety Rules Box -->
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:1.5rem; box-shadow:0 2px 8px rgba(0,0,0,0.02);">
        <h3 style="font-size:1.15rem; color:#b91c1c; font-weight:800; margin-bottom:0.75rem;">⚠️ 手冊第 21 頁：水彈射擊 13 大絕對安全守則</h3>
        <ul style="font-size:0.92rem; color:#334155; line-height:1.7; padding-left:1.5rem;">
          <li><strong>一、面罩全程不脫：</strong>進入射擊場域後，無論發生任何狀況，絕對不得私自脫卸防護面罩。</li>
          <li><strong>二、槍口朝下關保險：</strong>非射擊時刻，槍口一律朝下 45 度，手指不得扣在扳機內。</li>
          <li><strong>三、三公尺內禁止射擊：</strong>敵我距離小於 3 公尺時不得開槍射擊，應口頭判定出局。</li>
          <li><strong>四、不可瞄準非護具部位：</strong>禁止蓄意瞄準頸部、後腦或近距離連續射擊。</li>
          <li><strong>五、出局立即高舉雙手：</strong>被擊中者應大聲喊出「陣亡」並高舉雙手迅速離開火線至安全區。</li>
        </ul>
      </div>
      </div>
    </section>

    </section>

    <!-- ==================== TAB 8: 🎯 露營學習單 (Image 5 Style) ==================== -->
    <section class="tab-pane" id="pane-worksheet">
      <div class="section-header">
        <div>
          <h2 class="section-title">🎯 隔宿露營・互動學習單</h2>
          <p class="section-subtitle">在營地或車上測試露營與童軍小知識！點選按鈕或點擊卡片查看解答與解析</p>
        </div>
      </div>

      <div style="margin-bottom:1.5rem;">
        <h3 style="font-size:1.25rem; font-weight:800; color:#0369a1; margin-bottom:1rem;">一、是非挑戰題 (點選即時驗證)</h3>
        
        <div class="worksheet-container" id="quizContainer">
          {quiz_cards_html}
        </div>
      </div>

      <!-- Worksheet Paper Image Preview -->
      <div style="background:#ffffff; border:1px solid #e0f2fe; border-radius:14px; padding:1.5rem; margin-top:2rem;">
        <h3 style="font-size:1.15rem; color:#0369a1; font-weight:700; margin-bottom:1rem;">📝 手冊紙本學習單（手冊第 22~23 頁存檔對照）</h3>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem;">
          <div style="text-align:center;">
            <img src="assets/worksheet_page22.png" style="max-width:100%; height:auto; border-radius:8px; border:1px solid #cbd5e1;" alt="學習單第22頁">
            <div style="font-size:0.85rem; color:#64748b; margin-top:0.3rem;">手冊第 22 頁：野營心得與營火反思</div>
          </div>
          <div style="text-align:center;">
            <img src="assets/worksheet_page23.png" style="max-width:100%; height:auto; border-radius:8px; border:1px solid #cbd5e1;" alt="學習單第23頁">
            <div style="font-size:0.85rem; color:#64748b; margin-top:0.3rem;">手冊第 23 頁：探索活動心得與自我評量</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TAB 7: 🎒 行李・生活 (二階層次標籤) ==================== -->
    <section class="tab-pane" id="pane-pack-rules">
      <div class="sub-tab-nav-bar">
        <div class="sub-tab-title">🎒 行程裝備檢核與生活須知手冊</div>
        <div class="sub-tab-pills">
          <button class="sub-tab-btn active" id="subbtn-packing" onclick="switchSubTab('pack-rules', 'packing')">🎒 行李清單檢核</button>
          <button class="sub-tab-btn" id="subbtn-notices" onclick="switchSubTab('pack-rules', 'notices')">⚠️ 生活公約與須知</button>
        </div>
      </div>

      <!-- 二階子區域 1: 行李清單 -->
      <div class="sub-pane active" id="subpane-packing">
        <!-- ==================== TAB 9: 🎒 行李清單 ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">🎒 行前裝備與行李攜帶清單</h2>
          <p class="section-subtitle">出發前請逐項核對整理，點擊方框可即時打勾標記！落實 10/23 行前說明會各項規定。</p>
        </div>
      </div>

      <div class="checklist-grid">
        <div class="checklist-card">
          <div class="checklist-title">🪪 重要必備證件與藥品</div>
          <label class="check-item"><input type="checkbox"><span>全民健康保險卡（必帶，裝入夾鏈袋）</span></label>
          <label class="check-item"><input type="checkbox"><span>個人常備藥品（氣喘吸入劑、過敏藥、暈車藥）</span></label>
          <label class="check-item"><input type="checkbox"><span><strong>零用錢限 600 元以內</strong>（切勿帶過多現鈔）</span></label>
          <label class="check-item"><input type="checkbox"><span>本活動手冊與文具筆（寫學習單用）</span></label>
        </div>

        <div class="checklist-card">
          <div class="checklist-title">👕 換洗衣物與服儀規定</div>
          <label class="check-item"><input type="checkbox"><span><strong>日間著便服或班服（下身一律著深色長褲）</strong></span></label>
          <label class="check-item"><input type="checkbox"><span><strong>學校體育服一套（供晚上洗澡後就寢穿著）</strong></span></label>
          <label class="check-item"><input type="checkbox"><span>內衣褲、襪子 2 雙</span></label>
          <label class="check-item"><input type="checkbox"><span>薄防風外套一件（夜間戶外與清晨溫差大）</span></label>
          <label class="check-item"><input type="checkbox"><span>舒適運動布鞋（禁止穿著拖鞋涼鞋進行活動）</span></label>
        </div>

        <div class="checklist-card">
          <div class="checklist-title">🪥 個人衛生與盥洗用品</div>
          <label class="check-item"><input type="checkbox"><span>毛巾、牙刷、牙膏</span></label>
          <label class="check-item"><input type="checkbox"><span>旅行裝沐浴乳、洗髮精</span></label>
          <label class="check-item"><input type="checkbox"><span>衛生紙、隨身濕紙巾</span></label>
          <label class="check-item"><input type="checkbox"><span>髒衣物塑膠收納袋 2~3 個</span></label>
        </div>

        <div class="checklist-card">
          <div class="checklist-title">📱 管制物品與違禁品宣導</div>
          <label class="check-item"><input type="checkbox"><span><strong>手機集中保管</strong>（每晚約 1 小時報平安）</span></label>
          <label class="check-item"><input type="checkbox"><span>小型手電筒或頭燈（夜間帳棚照明）</span></label>
          <label class="check-item"><input type="checkbox"><span>環保水壺、輕便雨衣、防蚊液</span></label>
          <label class="check-item"><input type="checkbox"><span><strong>出發前再次清查違禁品</strong>（禁菸酒檳榔刀械）</span></label>
        </div>
      </div>
      </div>

      <!-- 二階子區域 2: 生活須知 -->
      <div class="sub-pane" id="subpane-notices">
        <!-- ==================== TAB 10: ⚠️ 生活須知 ==================== -->
    
      <div class="section-header">
        <div>
          <h2 class="section-title">⚠️ 營規生活守則與安全應變須知</h2>
          <p class="section-subtitle">落實團隊紀律、注意個人安全、維護環境衛生</p>
        </div>
      </div>

      <!-- 10/23 行前說明會四大重點連結 -->
      <div style="background:#fff1f2; border:1.5px solid #fecdd3; border-radius:12px; padding:0.9rem 1.25rem; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem;">
        <div style="display:flex; align-items:center; gap:0.6rem;">
          <span style="font-size:1.3rem;">📢</span>
          <div>
            <strong style="color:#9f1239; font-size:1rem;">10/23（五）隔宿露營行前說明會四大重點宣導與線上說明會</strong>
            <p style="font-size:0.85rem; color:#881337; margin:0.15rem 0 0 0;">違禁品檢查・手機集中保管・服裝畢旅連動・機動車遣返</p>
          </div>
        </div>
        <button onclick="switchTab('briefing')" class="btn-hero-action" style="background:#e11d48; color:#fff; border:none; padding:0.4rem 1rem; border-radius:8px; font-weight:700; font-size:0.88rem; cursor:pointer;">
          查看 10/23 說明會專區 ➔
        </button>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:1.25rem;">
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:1.5rem;">
          <h3 style="font-size:1.15rem; color:#0369a1; font-weight:700; margin-bottom:0.75rem;">🏕️ 營地生活十項守則</h3>
          <ol style="font-size:0.92rem; color:#334155; line-height:1.75; padding-left:1.2rem;">
            <li>遵守值星官及隨隊師長指示，切勿私自脫隊單獨行動。</li>
            <li>活動期間一律穿著運動服裝與運動鞋，禁止穿著拖鞋走出帳棚。</li>
            <li>愛惜營區各項公物，營帳搭設牢固，勿在帳棚內點燃明火。</li>
            <li>晚上熄燈後，全營區保持肅靜，嚴禁跨帳或串班查房。</li>
            <li>鞋子入睡前務必「倒扣」或置入帳內，防止夜間蛇蟲躲藏。</li>
            <li>確實做好垃圾分類，貫徹無痕山林（LNT）環保精神。</li>
          </ol>
        </div>

        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:14px; padding:1.5rem;">
          <h3 style="font-size:1.15rem; color:#dc2626; font-weight:700; margin-bottom:0.75rem;">🚑 緊急就醫路線與通訊網絡</h3>
          <p style="font-size:0.92rem; color:#334155; line-height:1.7; margin-bottom:0.8rem;">
            活動期間如遇緊急傷病，立即通報隨隊師長與醫護小組，後送配合醫院：
          </p>
          <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:10px; padding:0.85rem 1rem; margin-bottom:0.85rem;">
            <div style="font-weight:700; color:#b91c1c;">柳營奇美醫院（急診醫學中心）</div>
            <div style="font-size:0.88rem; color:#450a0a;">地址：台南市柳營區太康里 201 號</div>
            <div style="font-size:0.88rem; color:#450a0a;">電話：06-6226999（車程約 15 分鐘）</div>
          </div>
          <ul style="font-size:0.9rem; color:#475569; line-height:1.6; padding-left:1.2rem;">
            <li>南投國中學務處電話：049-2222549 轉 202</li>
            <li>團控經理 邱O凱：0972-721756</li>
            <li>尖山埤渡假村服務中心：06-6233888</li>
          </ul>
        </div>
      </div>
      </div>
    </section>

  </main>

  <!-- Floating Tools (Bottom-right) -->
  <div class="floating-tools">
    <button class="btn-fab" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="回到頂部">🔝</button>
    <button class="btn-fab" onclick="window.print()" title="列印手冊">🖨️</button>
    <a href="1151019-115南投國二露營手冊.pdf" download class="btn-fab" title="下載原始 PDF 手冊">📥</a>
  </div>

  <script>
    // 二階層次標籤映射表
    const tabMapping = {{
      'briefing': {{ main: 'briefing', sub: null }},
      'online-briefing': {{ main: 'briefing', sub: null }},
      'tents': {{ main: 'camp-cook', sub: 'tents' }},
      'meals': {{ main: 'camp-cook', sub: 'meals' }},
      'camp-cook': {{ main: 'camp-cook', sub: 'tents' }},
      'scout': {{ main: 'scout-mountain', sub: 'scout' }},
      'mountain': {{ main: 'scout-mountain', sub: 'mountain' }},
      'scout-mountain': {{ main: 'scout-mountain', sub: 'scout' }},
      'packing': {{ main: 'pack-rules', sub: 'packing' }},
      'notices': {{ main: 'pack-rules', sub: 'notices' }},
      'pack-rules': {{ main: 'pack-rules', sub: 'packing' }}
    }};

    // 主標籤切換
    function switchTab(tabId) {{
      let mainTab = tabId;
      let subTab = null;

      if (tabMapping[tabId]) {{
        mainTab = tabMapping[tabId].main;
        subTab = tabMapping[tabId].sub;
      }}

      // 更新主標籤高亮
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        if (btn.getAttribute('data-tab') === mainTab) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      // 切換主區域
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const targetPane = document.getElementById('pane-' + mainTab);
      if (targetPane) {{
        targetPane.classList.add('active');
      }}

      // 若指定二階子標籤，切換子標籤
      if (subTab) {{
        switchSubTab(mainTab, subTab);
      }}

      // 平滑滾動至導覽列
      const navBar = document.getElementById('tabNavBar');
      if (navBar) {{
        window.scrollTo({{ top: navBar.offsetTop - 10, behavior: 'smooth' }});
      }}
    }}

    // 二階子標籤切換
    function switchSubTab(mainId, subId) {{
      const pane = document.getElementById('pane-' + mainId);
      if (!pane) return;

      // 更新子按鈕高亮
      pane.querySelectorAll('.sub-tab-btn').forEach(btn => {{
        if (btn.id === 'subbtn-' + subId) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      // 切換子區域
      pane.querySelectorAll('.sub-pane').forEach(sp => {{
        if (sp.id === 'subpane-' + subId) {{
          sp.classList.add('active');
        }} else {{
          sp.classList.remove('active');
        }}
      }});
    }}

    // 10/23 線上說明會簡報輪播器邏輯
    let currentBriefingSlide = 1;
    const totalBriefingSlides = 21;

    function updateBriefingSlide() {{
      const img = document.getElementById('briefingMainImg');
      const indicator = document.getElementById('briefingSlideIndicator');
      if (img) {{
        img.style.opacity = '0.3';
        setTimeout(() => {{
          img.src = `assets/briefing/slide_${{currentBriefingSlide}}.jpg`;
          img.alt = `行前須知投影片 ${{currentBriefingSlide}}`;
          img.style.opacity = '1';
        }}, 100);
      }}
      if (indicator) {{
        indicator.innerText = `第 ${{currentBriefingSlide}} / ${{totalBriefingSlides}} 頁`;
      }}
      // 更新縮圖外框高亮
      document.querySelectorAll('.briefing-thumb-item').forEach((thumb, idx) => {{
        if (idx + 1 === currentBriefingSlide) {{
          thumb.style.borderColor = '#0284c7';
          thumb.style.boxShadow = '0 0 0 2px rgba(2,132,199,0.4)';
          thumb.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
        }} else {{
          thumb.style.borderColor = '#e2e8f0';
          thumb.style.boxShadow = 'none';
        }}
      }});
    }}

    function nextBriefingSlide() {{
      if (currentBriefingSlide < totalBriefingSlides) {{
        currentBriefingSlide++;
      }} else {{
        currentBriefingSlide = 1;
      }}
      updateBriefingSlide();
    }}

    function prevBriefingSlide() {{
      if (currentBriefingSlide > 1) {{
        currentBriefingSlide--;
      }} else {{
        currentBriefingSlide = totalBriefingSlides;
      }}
      updateBriefingSlide();
    }}

    function goToBriefingSlide(n) {{
      currentBriefingSlide = n;
      updateBriefingSlide();
    }}

    // Lightbox 大圖預覽
    function openLightbox(src, caption) {{
      const modal = document.getElementById('lightboxModal');
      const img = document.getElementById('lightboxImg');
      const cap = document.getElementById('lightboxCaption');
      if (modal && img) {{
        img.src = src;
        if (cap) cap.innerText = caption || '';
        modal.style.display = 'flex';
      }}
    }}

    function closeLightbox() {{
      const modal = document.getElementById('lightboxModal');
      if (modal) modal.style.display = 'none';
    }}

    // 鍵盤導航支援
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeLightbox();
      const briefingPane = document.getElementById('pane-briefing');
      if (briefingPane && briefingPane.classList.contains('active')) {{
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextBriefingSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevBriefingSlide();
      }}
    }});


    // Day 1 / Day 2 Switcher in Schedule Tab
    function switchDay(day) {{
      const b1 = document.getElementById('dayBtn1');
      const b2 = document.getElementById('dayBtn2');
      const c1 = document.getElementById('dayContent1');
      const c2 = document.getElementById('dayContent2');

      if (day === 1) {{
        b1.classList.add('active');
        b2.classList.remove('active');
        c1.style.display = 'block';
        c2.style.display = 'none';
      }} else {{
        b2.classList.add('active');
        b1.classList.remove('active');
        c2.style.display = 'block';
        c1.style.display = 'none';
      }}
    }}

    // Current Search Filters for Table
    let curClass = 'all';
    let curBus = 'all';
    let curGender = 'all';

    function setFilter(type, val, btn) {{
      const siblings = btn.parentElement.querySelectorAll('.filter-pill-btn');
      siblings.forEach(s => s.classList.remove('active'));
      btn.classList.add('active');

      if (type === 'class') curClass = val;
      if (type === 'bus') curBus = val;
      if (type === 'gender') curGender = val;

      filterStudents();
    }}

    function filterStudents() {{
      const kw = document.getElementById('searchInput').value.trim().toLowerCase();
      const rows = document.querySelectorAll('#studentTableBody tr');
      let matched = 0;

      rows.forEach(r => {{
        const rClass = r.getAttribute('data-class');
        const rBus = r.getAttribute('data-bus');
        const rGender = r.getAttribute('data-gender');
        const rSearch = r.getAttribute('data-search').toLowerCase();

        let show = true;
        if (curClass !== 'all' && rClass !== curClass) show = false;
        if (curBus !== 'all' && rBus !== curBus) show = false;
        if (curGender !== 'all' && rGender !== curGender) show = false;
        if (kw && !rSearch.includes(kw)) show = false;

        if (show) {{
          r.style.display = '';
          matched++;
        }} else {{
          r.style.display = 'none';
        }}
      }});

      document.getElementById('resultCountBadge').innerText = `共找到 ${{matched}} / 107 筆資料`;
    }}

    // Filter Tents
    function filterTents(type, btn) {{
      if (btn) {{
        const siblings = btn.parentElement.querySelectorAll('.filter-pill-btn');
        siblings.forEach(s => s.classList.remove('active'));
        btn.classList.add('active');
      }}
      const cards = document.querySelectorAll('.tent-card');
      cards.forEach(c => {{
        const cType = c.getAttribute('data-tent-type');
        if (type === 'all' || cType === type) {{
          c.style.display = 'flex';
        }} else {{
          c.style.display = 'none';
        }}
      }});
    }}

    // Filter Scout Cards
    function filterScout(cat, btn) {{
      if (btn) {{
        const siblings = btn.parentElement.querySelectorAll('.filter-pill-btn');
        siblings.forEach(s => s.classList.remove('active'));
        btn.classList.add('active');
      }}
      const cards = document.querySelectorAll('.scout-item-card');
      cards.forEach(c => {{
        const cCat = c.getAttribute('data-cat');
        if (cat === 'all' || cCat === cat) {{
          c.style.display = 'flex';
        }} else {{
          c.style.display = 'none';
        }}
      }});
    }}

    // Quiz Checking Logic
    const quizData = {quiz_json};

    function checkQuizAnswer(idx, userChoice, btn) {{
      const q = quizData[idx];
      const card = document.getElementById('quizCard_' + idx);
      const expBox = document.getElementById('quizExp_' + idx);
      const buttons = card.querySelectorAll('.btn-choice');

      buttons.forEach(b => {{
        b.classList.remove('selected-correct');
        b.classList.remove('selected-wrong');
      }});

      const isCorrect = (userChoice === q.ans);

      if (isCorrect) {{
        btn.classList.add('selected-correct');
        expBox.style.display = 'block';
        expBox.style.borderLeftColor = '#16a34a';
        expBox.innerHTML = `<strong>${{q.correct}}</strong>`;
      }} else {{
        btn.classList.add('selected-wrong');
        expBox.style.display = 'block';
        expBox.style.borderLeftColor = '#dc2626';
        expBox.innerHTML = `<strong>${{q.wrong}}</strong>`;
      }}
    }}

    // Checklist interactive toggle
    document.addEventListener('DOMContentLoaded', () => {{
      document.querySelectorAll('.check-item input[type="checkbox"]').forEach(cb => {{
        cb.addEventListener('change', (e) => {{
          if (e.target.checked) {{
            e.target.parentElement.classList.add('checked');
          }} else {{
            e.target.parentElement.classList.remove('checked');
          }}
        }});
      }});
    }});
  </script>
  <!-- Lightbox Modal for Fullscreen Image Preview -->
  <div id="lightboxModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.88); backdrop-filter:blur(8px); z-index:3000; align-items:center; justify-content:center; padding:1.5rem;" onclick="closeLightbox()">
    <div style="position:relative; max-width:94vw; max-height:94vh; text-align:center;" onclick="event.stopPropagation()">
      <img id="lightboxImg" src="" style="max-width:100%; max-height:86vh; border-radius:8px; box-shadow:0 25px 50px rgba(0,0,0,0.6);">
      <div id="lightboxCaption" style="color:#ffffff; font-weight:700; margin-top:0.75rem; font-size:1.05rem; text-shadow:0 2px 4px rgba(0,0,0,0.8);"></div>
      <button onclick="closeLightbox()" style="position:absolute; top:-16px; right:-16px; background:#ef4444; color:#fff; border:2px solid #fff; border-radius:50%; width:38px; height:38px; font-size:1.2rem; font-weight:bold; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3);">✖</button>
    </div>
  </div>

</body>
</html>
"""

with open("handbook.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("handbook.html generated successfully with pre-rendered HTML cards & Light Blue Theme!")
