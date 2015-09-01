## ----------------------------------------------------------------------------+
## BATTLE ROYALE CGI
##   (C) 2000 by Happy Ice.
##   E-MAIL: webmaster@happy-ice.com
##   HomePage: http://www.happy-ice.com/battle/
##
## Re-Edited By 2Y (Yuta Yamashita)
##	(C) 2003 by - 2Y -
##	E-MAIL:	2Y@mindspring.com
##	HP:		http://2Y.on.to
##■ 遊戲版本※變更嚴禁※
$ver = "V01.19";$ver2y = "1β4";
## ---[注意事項]---------------------------------------------------------------+
## 1. 對用這個遊戲程式令安裝或遊玩者有任何的損失，作者不承擔一切的責任。
##											      
## 2. 表示時候的TAB是4空間。文本請用編輯器設定。
##				
## 3. 有關設置的問題及改造的問題請到相公告板請助。
##    對於郵件的問題未必能回答，不過，如用MSN，問題應能有效的回答。
##											
## 4. 關於入門性的遊戲問題，這個主頁也有簡單的說明。
##														 
## 5. 如果有錯誤報告，或要求等，主頁的管理員公告牌寫上。
##														        		- 2Y -
## ----------------------------------------------------------------------------+
#■ 遊戲標題
$game = "■ BATTLE ROYALE ■ ($ver) [BRU Ver. $ver2y] 遊戲提供：Withlove -- 夢幻學園 (http://withlove.no-ip.com)";
#■ 下次遊戲召開預定日(未完成．動．不穩定？)
$start_mon = "3";$start_day = "4";$start_hour = "24";$start_min = "0";$start_sec = "0";
#------- 基本設定 ---------
#■ 管理者??&密碼
# 因為可能令user log崩潰的原因，「,」(小數點)請別用。
$a_id = "BR" ; # 變成NPC使用時的ID。
$a_pass = "12341234" ;
$a_pass_npc = "ADMIN_NPC";#兵士的密碼
$a_group_id = "ADMIN_GROUP";#兵士的小組名
$a_group_pass = "ADMIN_PASS";#兵士的小組密碼
#■ 目錄(最後/不閉上)
# 防止數據窺視必定變更。
$LOG_DIR = "log9428" ;
$DAT_DIR = "dat2ksi9" ;
$LIB_DIR = "lib812add" ;
#■ 鏈接處(對各CGI的鏈接．追加可能)
# 畫面上部被表示的鏈接。
@links = (
    '>><A href="index.htm">HOME</A>',
    '>><A href="rule.htm" target="_blank">RULE</A>',
    '>><A href="rank.cgi" target="_blank">RANKING</A>',
    '>><A href="map.cgi" target="_blank">MAP</A>',
    '>><A href="news.cgi" target="_blank">NEWS</A>',
    '>><A href="admin.cgi">ADMIN</A>'
    );
# 管理方式用的鏈接。
$home = "http://withlove.no-ip.com/br/"; #設定對首頁的鏈接
#■ 個別存檔
$u_save_dir = "$LOG_DIR/users_save/"; #用戶存檔目錄
$u_save_file = "_back.log"; #ID附加的字符串
#■ 用戶文件
# 因為數據窺視防止$LOG_DIR/以下請必定變更。
$user_file = "$LOG_DIR/userdatfile_1234.log" ;
$back_file = "$LOG_DIR/da23fd8s91k29kd91.log" ;
#■ log file
$log_file = "$LOG_DIR/newsfile1283dseie983.log" ;
#■ lockfile名
$lockf = "lock/dummydjwow839.txt";
#■ 文件鎖形式
# → 0=no 1=symlink函數 2=mkdir函數 3=Tripod用(暫定)
# 局部測試時候到服務器提高mkdir函數的，時候要是使用可能
# 使用symlink函數。
$lkey = 2;
#■ 用戶數文件
$member_file = "$LOG_DIR/memberfile938s9d9k.log" ;
#■ 禁止區域文件
$area_file = "$LOG_DIR/areafiledis83929.log" ;
#■ 支付武器文件
$wep_file = "$DAT_DIR/wepfile823829ksks.dat" ;
#■ 個人私有物道具文件
$stitem_file = "$DAT_DIR/stitemfile3928skso9.dat" ;
#■ 取得道具文件
$item_file = "itemfile.log" ;
#■ 時間管理文件
$time_file = "$LOG_DIR/timefile.log" ;
#■ 槍聲log file
$gun_log_file = "$LOG_DIR/gunlog.log" ;
#■ 結束
$end_flag_file = "$LOG_DIR/e_flag.txt" ;
#■ 天氣
@weather = ("快晴","晴","變陰","雨","豪雨","台風","雷雨","雪","霧","濃霧");
#■ 班級號碼
@clas = ("3年A組","3年B組","3年C組","3年D組","3年E組","3年F組","3年G組","3年H組","3年I組","3年J組");
$clmax = 10;#班級數
$manmax= 21;#性別最大數
$maxmem=$clmax*$manmax*2; #最大登錄數
#■ 場所
@place = ("分校","北之岬","北村住宅街","北村役場","郵便局","消防署","關公堂","清水池","西村神社","遺跡","山岳地帶","隧道","西村住宅街","寺","荒校","南村神社","森林地帶","源二郎池","南村住宅街","診療所","燈台","南之岬");
# SU=發現增加 SD:發現減少 DU:防禦增加 DD:防禦減少 AU:攻擊增加 AD:攻擊減少
@arsts = ("SU","DD","DU","SU","SD","SU","AU","SU","SD","AD","SU","DD","DU","SD","AD","SD","SD","SD","AU","SU","DU","SU");
@area = ("D-6","A-2","B-4","C-3","C-4","C-5","C-6","D-3","E-2","E-4","E-5","E-7","F-2","F-9","G-3","G-6","H-4","H-6","I-6","I-7","I-10","J-6");
@arno = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21");
@arinfo = (
	"分校。這裡不久會成為禁止區域。<BR>如果不快點離開，項圈將會爆炸…。",
	"望向海沒有船隻可以看得見。<BR>監視打算逃脫學生們的政府船或者…。",
	"以前也有人在這裡居住吧。<BR>如今已變成廢墟。",
	"這裡是村的中心嗎？<BR>現在變成誰都不在…。",
	"這裡顯然沒有任何東西…。",
	"雖說這裡是消防站，但是連消防車也沒有。",
	"大小各種各樣的佛像被供奉著。<BR>夜晚令人毛骨悚然。",
	"這裡的水很清澈。",
	"大概是學問的神被祭奠的火山灰。",
	"這樣的地方會有幽靈出現嗎？<BR>幽靈之說雖然不太相信，不過…。",
	"能夠一望這個島的高地。<BR>當然，如果在這裡站立著，<BR>被其他的夥伴找到的可能性也很高。",
	"真黑暗。<BR>如果在這樣的地方被襲擊，相信會是相當危險。",
	"這裡與其他的住宅街差不多，<BR>完全與廢墟無疑…。",
	"完全荒廢了的地方。",
	"白天的學校看上去感覺也沒什麼，但是，<BR>夜晚的學校就不一樣了，尤其是在這裡…。",
	"曝曬著的牌坊，感覺也很淒慘的…。",
	"鬱鬱蔥蔥的樹木多而茂盛。<BR>若從草叢突然被襲擊防備也來不及就…。",
	"這裡與其說是池子不如說是沼澤。<BR>完全令人毛骨悚然的地方…。",
	"這裡，比其他住宅街的商店特別多。<BR>是商店街還是什麼吧。",
	"寂靜地帶，<BR>如果尋找藥草就要快點行動了…。",
	"如果作為要塞立充滿，快要成為堅牢的城寨了。<BR>地板別有大量的幹的血痕。有什麼？",
	"兵士的船和…優勝者乘坐的船嗎？<BR>數艘船浮沉著。",
);
#■ 遊戲數據有效期限。以日數為單位。默認1星期。
$save_limit = 7;
#■ 等級提升基本經驗值
$baseexp = 9;
#■ 基本熟練度
$BASE = 20 ;
#■ 遊戲最低開催日數
# 用活動．陷阱等最後的一人決定，要是這個日數以下遊戲仍會繼續執行。
# 0的話1日。
$battle_limit = 3;
#■ 遊戲接待合計日數
$limit = 3;
#■ 體力最大數
$maxsta = 100;
#■ 應急措施指令的能量消費
$okyu_sta = 50;
#■ 毒見指令的能量消費
$dokumi_sta = 30;
#■ 恢復量的設定
$kaifuku_time = 10; # 能量恢復時間(秒):60秒1點恢復
$kaifuku_rate = 2;  # 體力恢複比率：能量的二分之一(不設定時設為0)
#■ 時刻 (海外服務器的時候、$now=time+請(9*60*60);例子:9時間差)
$now=time;

#------- 使用者設定 ---------
#訊息保存的文件名
$mes_file = "$LOG_DIR/mes.log";
#保存的消息的數
$listmax = 100;
#訊息表示數
$mesmax = 5;
#成員數保存文件
$memberfile = "$LOG_DIR/member.log";
#成員點數持續賠掉的時間
$mem_time = 120;
#訊息的顏色
$col_to = "red";
#送出訊息的顏色
$col_from = "blue";
#全員發送的訊息顏色
$col_all = "green";


#------- 安全性關聯設定 ---------

#■ 訪問禁止
@kick = ("218.188.104.92","TANATOS","TANATOS","TANATOS");
#■ 訪問承認
@oklist = ("TANATOS","TANATOS","TANATOS","TANATOS");
# 關於訪問禁止
# 名字不能取得的情況排除。
# 不想排除的情況，請把ＩＰ地址放入訪問承認。
# 例：@oklist = ("127.0.0","TANATOS","TANATOS","TANATOS");
# 這樣做，127.0.0.*** 的IP地址不被拒絕。
# 如果利用，pref.cgi的7-21行。

#■ method=POST 限定 (0=no 1=yes) →安全性對策
$Met_Post = 1;

#■ 從其他站點投稿排除時指定
$base_url = 0; #如果使用排除機能請設定為1

#接受設定輸入的地址(從http://寫)．可複數設定
@base_list = ("dummy","dummy");


#------- 安全性關聯設定．選擇機能 ---------

#■ 同一登記禁止((0=no 1=yes)
# 如果用這個機能的話，變得不能來自CATV等環境的登記
# 設定時候請注意。
$IP_deny = 0;

#■ 使用(0=no 1=yes)
# 設定成0的話變成在ＩＰ地址的表示。
$IP_host = 0;

#■ 准許來自同樣主人的登記orIP地址
# 省略的話能地址和主人名的範圍指定。
# 例子1) hogehoge.ne.如果jp 的話*．hogehoge.ne.jp 的主人被准許。
# 例子2)192.168.0的話192.168.0.*的地址被准許。
# 注意：這個設定做為空的話全部的主人(地址)成為許可對象。
@IP_ok = ("dummy","dummy");

#■ 在進行狀況裡(上)表示主人信息(0=no 1=yes)
# 設為1的話新規章登記時ＩＰ地址將被表示。
$host_view = 0;


#------- 選擇機能 ---------

# NPC設置有無(0=no 1=yes)
# 如果設置請在base.dat製作NPC數據。
$npc_mode = 1;
$npc_num = 26;	# Number of NPC
$npc_file = "$DAT_DIR/base.dat"; #NPC DATA FILE
$BOSS = "擔任";$KANN = "監查員";$ZAKO = "兵士";
# 頭像方式(0=no 1=yes)
$icon_mode = 1;
# 頭像畫像的「目錄」
# → 要是從http:// URL請注明
# → 最後必定加上 /
$imgurl = "img/";
# map的畫像「目錄」
# → 要是從http:// URL請注明
# → 最後必定加上 /
$map = "map";#		
# Meter的圖像文件
$blue = "img/blue.PNG";$gold = "img/gold.PNG";$green = "img/green.PNG";$pink = "img/pink.PNG";$red = "img/red.PNG";$yellow = "img/yellow.PNG";
# 狀態的圖像文件
$fine = "img/fine.swf";$caution = "img/caution.swf";$danger = "img/danger.swf";$dead = "img/dead.swf";$poison = "img/poison.swf";
# 定義(上下設定必定相對。上為男生，下為女生)
# 男生學生頭像
@m_icon_file = ('i_akamatsu.jpg','i_keita.jpg','i_ooki.jpg','i_oda.jpg','i_kawada.jpg','i_kiriyama.jpg','i_kuninobu.jpg','i_kuramoto.jpg','i_kuronaga.jpg','i_sasagawa.jpg','i_sugimura.jpg','i_yutaka.jpg','i_takiguchi.jpg','i_duki.jpg','i_nanahara.jpg','i_niida.jpg','i_numai.jpg','i_hatagami.jpg','i_mimura.jpg','i_motobuchi.jpg','i_yamamoto.jpg');
@m_icon_name = ('1番 赤松義生','2番 飯島敬太','3番 大木立道','4番 織田敏憲','5番 川田章吾','6番 桐山和雄','7番 國信慶時','8番 倉元洋二','9番 黑長博','10番 世川龍平','11番 杉村弘樹','12番 瀨戶豐','13番 瀧口優一朗','14番 月岡彰','15番 七原秋也','16番 新井田和志','17番 沼井充','18番 旗上忠勝','19番 三村信史','20番 元滌恭一','21番 山本和彥');
# 女生學生頭像
@f_icon_file = ('i_inada.jpg','i_utsumi.jpg','i_eto.jpg','i_sakura.jpg','i_kanai.jpg','i_yukiko.jpg','i_yumiko.jpg','i_kotohiki.jpg','i_sakaki.jpg','i_hirono.jpg','i_souma.jpg','i_haruka.jpg','i_takako.jpg','i_tendo.jpg','i_noriko.jpg','i_yuka.jpg','i_noda.jpg','i_fujiyoshi.jpg','i_matsui.jpg','i_minami.jpg','i_yahagi.jpg');
@f_icon_name = ('1番 稻田瑞穗','2番 內海幸枝','3番 江藤惠','4番 小川 兒','5番 金井泉','6番 北野雪子','7番 日下友美子','8番 琴彈加代子','9番 神祐子','10番 清水比呂乃','11番 相馬光子','12番 谷澤鈴','13番 千草貴子','14番 天堂真弓','15番 中川典子','16番 中川有香','17番 野田聰美','18番 藤吉文世','19番 松井知里','20番 南佳織','21番 矢作好美');
# NPC用頭像
@n_icon_file = ('i_sakamochi.jpg','i_tahara.jpg','i_kondou.jpg','i_nomura.jpg','i_kato.jpg','i_hayashida.jpg','i_ocha.jpg','i_bus.jpg');
@n_icon_name = ('板持金發 先生','兵士 田原','兵士 近藤','兵士 野村','兵士 加藤','林田昌朗 先生','司機','那個人');
# 特殊頭像
@s_icon_file = ('GPO3.gif','i_ana.jpg','i_anna.jpg','i_anno.jpg','i_ikumi.jpg','i_junya.jpg','i_kazumi.jpg','i_keiko.jpg','i_uncle.jpg');
@s_icon_name = ('GPO3','廣播員','北川安奈','安野良子','三村郁美','劍崎順矢','新谷和美','大貫慶子','三村叔父');
@s_icon_pass = ('GPO3pass','','','','','','','','');
# 頭像定義(沒必要請別變更)
#-----------從這裡-----------------
@icon_file = (@m_icon_file,@f_icon_file,@n_icon_file,@s_icon_file);
@icon_name = (@m_icon_name,@f_icon_name,@n_icon_name,@s_icon_name);
$icon_check1 = $#m_icon_file + 1;
$icon_check2 = $icon_check1 + $#f_icon_file + 1;
$icon_check3 = $icon_check2 + $#n_icon_file + 1;
$icon_check4 = $icon_check3 + $#s_icon_file + 1;
#-----------到這裡-----------------
#========== 設定到這裡 ===============
1;
