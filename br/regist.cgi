#! /usr/bin/perl

#■□■□■□■□■□■□■□■□■□■□■
#□ 	-  BR REGISTRATION PROGRAM  - 	 □
#■ 									 ■
#□ 		扔皮伙□民件域厖			 □
#■ 									 ■
#□ checker			-		Checker		 □
#■ MAIN			-		丟奶件		 ■
#□ 瓚狤質咥		-		REGIST		 □
#■ INFO			-		濩抸質咥	 ■
#□ CLUBMAKE		-		弁仿皮綜嶽	 □
#■□■□■□■□■□■□■□■□■□■□■

#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
require "pref.cgi";

&DECODE;
&CREAD ;

if ($mode eq "regist"){&REGIST;}
elsif ($mode eq "info"){&INFO;}
elsif ($mode eq "info2"){&INFO2;}
else { &MAIN; }
&UNLOCK;
exit;

#==================#
# □ Checker       #
#==================#
sub checker {
if(($limit == "")||($limit == 0)){ $limit = 7;}local($t_limit) = ($limit * 3) + 1;

if (($fl =~ /終了/)||($ar >= $t_limit)){&ERROR("遊戲登錄數已滿。<br><br>　請等待下次遊戲開始再行登錄。") ;}

$chktim = $c_endtime + (1*60*60*2) ;	#死亡時間取得ぜ
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($chktim);
$year+=1900; $month++;

if ($chktim > $now) {&ERROR("伽羅死亡確認後，2小時不能再登記。<br><br>　次回登錄可能時間：$year/$month/$mday $hour:$min:$sec") ;}#登記時間錯誤？

#用戶文件取得
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$listnum = @userlist;
if (($userlist - $npc_num) >= $maxmem) {&ERROR("申請登錄失敗，遊戲最高接受 ($maxmem諦) 名玩家登錄。") ;}#最大人數超過？

#重複核對
foreach $userlist(@userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
	if (($c_id eq $w_id) && ($c_password eq $w_password) && ($w_sts ne "死亡")) {&ERROR("名字或ID禁止重複登記。請檢查清楚或向管理員詢問。HOST ID:$IPAdd-$w_f_name-$w_l_name") ;}#同一ID or 同姓同名？
	if (($w_sts ne "死亡")&&($host eq $w_IP)&&($host ne "209.137.141.2")) {&ERROR("名字或ID禁止重複登記。請檢查清楚或向管理員詢問。COMMENT:USED SAME PC HOST:$host") ;}#同一ID or 同姓同名？
}
}
#==================#
# ■main		   #
#==================#
sub MAIN {
$hostchk = 0;
if (($SubServer)&&($host eq "209.137.141.2")){$hostchk=1;$host = $IPAdd;if ($IPAdd eq ""){&ERROR("慶應生請從TOP PAGE訪問")};}
if ($host eq "209.137.141.2"){$hostchk=1;}
&checker;&HEADER;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">轉校手續</span></font></center>
<BR><BR><img border="0" src="img/i_hayashida.jpg" width="70" height="70"><BR><BR>
你是轉校生？我是擔當者林田。<BR>嘿，你還很懂挑學校 (露出邪惡的笑容)，<BR>無論如何你先填好你的資料吧。<BR><BR>首先，在這裡寫上你的姓名，記上性別！<BR>再向我提交就可以了。
<FORM METHOD="POST"  ACTION="regist.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="regist">
<INPUT TYPE="HIDDEN" NAME="IP" VALUE="$host">
姓：<INPUT size="16" type="text" name="F_Name" maxlength="6"><BR>
名：<INPUT size="16" type="text" name="L_Name" maxlength="6"><BR>
(姓,名全角6個字以內)
<BR><BR>
性別：<SELECT name="Sex">
<OPTION value="NOSEX" selected>- 性別 -</OPTION>
<OPTION value="男生">男生</OPTION>
<OPTION value="女生">女生</OPTION>
</SELECT>
_HERE_
print "　頭像：<SELECT name=\"Icon\">\n";
print "<OPTION value=\"NOICON\" selected>-頭像-</OPTION><OPTION value=\"NOICON\">男生</OPTION>\n";
	for ($i=0;$i<$icon_check1;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
print "<OPTION value=\"NOICON\">女生</OPTION>";
	for ($i;$i<$icon_check2;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
#print "<OPTION value=\"NOICON\">特殊</OPTION>";
#for ($i;$i<$icon_check3;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
print "</SELECT>\n";
print <<"_HERE_";
[<a href="view.htm" target="_blank">頭像一覽</a>]<BR><BR>
ID：<INPUT size="8" type="text" name="Id" maxlength="8">　密碼：<INPUT size="8" type="text" name="Password" maxlength="8"><BR>
(ID，密碼半角英數字8個字以內)<BR><BR>
<Table border="0" cellspacing="0" cellpadding="0">
<tr><td align="right">口頭語：</td><td><INPUT size="32" type="text" name="Message" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">殺害對手時的台詞</td></tr>
<tr><td align="right">遺　言：</td><td><INPUT size="32" type="text" name="Message2" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">不幸死亡時的台詞</td>
<tr><td align="right">代表句：</td><td><INPUT size="32" type="text" name="Comment" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">(代表性語句。記載於生存者一覽表。)<BR>(32個字限定)</td></tr>
</table><BR>
<FONT color="yellow" size="2"><B>
相同IP複數登錄完全禁止；其它網站盜連本站遊戲完全禁止；<BR>
玩家名字及遊戲內是完全禁止不雅字眼的；如發現以上破壞守則玩家，<BR>
Withlove管理員將會強制刪除遊戲人物及禁止進入Withlove Server，<BR>
將會完全禁止享用Withlove提供的一切免費服務，請遵守這小小遊戲守則，謝謝。<BR>
_HERE_
if($hostchk){print "慶應生不必用真實姓名，遊戲只是純屬虛構。<BR>";}
print <<"_HERE_";
</U></B></FONT><BR>
<INPUT type="submit" name="Enter" value="確定">　<INPUT type="reset" name="Reset" value="重寫"><BR></FORM></CENTER>
<P align="center"><A href="index.cgi"><B><FONT color="#ff0000" size="4">返回</FONT></B></A></P>
_HERE_
&FOOTER;
}
#==================#
# ■登錄處理       #
#==================#
sub REGIST {
$host = $IP;
&checker;
#輸入信息核對
if ($f_name2 eq '') { &ERROR("姓氏未輸入。") ; }
if (length($f_name2) > 12) { &ERROR("姓氏輸入字數超出限制 (最多6個中文字)") ; }
if ($f_name2 =~ m/[>]/) { &ERROR("最多6個中文字") ; }
if ($l_name2 eq '') { &ERROR("名字未輸入。") ; }
if (length($l_name2) > 12) { &ERROR("名字輸入字數超出限制 (最多6個中文字)") ; }
if ($l_name2 =~ m/[>]/) { &ERROR("最多6個中文字") ; }
if ($sex2 eq "NOSEX") { &ERROR("性別未選擇。") ; }
if (length($id2) > 8) { &ERROR("ID的字數超出限制。(最多輸入8個半形字)") ; }
if ($id2 eq '') { &ERROR("ID未輸入。") ; }
if ($id2 =~ m/[^0-9a-zA-Z]/) { &ERROR("ID請用半形字輸入。(最多輸入8個半形字)") ; }
if ($password2 eq '') { &ERROR("密碼未輸入。") ; }
if (length($password2) > 8) { &ERROR("密碼的字數超出限制。(最多輸入8個半形字)") ; }
if ($password2 =~ m/[^0-9a-zA-Z]/) { &ERROR("密碼請用半形字輸入。(最多輸入8個半形字)") ; }
if ($icon2 eq "NOICON") { &ERROR("頭像未選擇。") ; }
if (($id2 =~ /$password2/)||($password2 =~ /$id2/)) { &ERROR("密碼不能與ID相同。") ; }
if (length($msg2) > 64) { &ERROR("口頭語的文字數超出限制。(最多輸入32個全角字)") ; }
if (length($dmes2) > 64) { &ERROR("遺言的文字數超出限制。(最多輸入32個全角字)") ; }
if (length($com2) > 64) { &ERROR("代表句的文字數超出限制。(最多輸入32個全角字)") ; }
if ($msg2 eq "") { &ERROR("請輸入口頭語。(最多輸入32個全角字)") ; }
if ($dmes2 eq "") { &ERROR("請輸入遺言。(最多輸入32個全角字)") ; }
if ($com2 eq "") { &ERROR("請輸入代表句。(最多輸入32個全角字)") ; }
if(($sex2 =~ /男生/)&&($icon2 >= $icon_check1 )) { &ERROR("不能選擇與性別不同的頭像。") ; }
if(($sex2 =~ /女生/)&&($icon2 < $icon_check1 )){ &ERROR("不能選擇與性別不同的頭像。") ; }

@word = (" ","　","on9","西","狗","屌","撚","柒","76","仆","老母","老豆","幹","鳩","臭","含","蕭","家產","做愛","蕉","fuck","ｆｕｃｋ","fxck","fuxk");
for ($i = 0;$i < 24;$i++)
{
if ($f_name2 =~ /@word[$i]/) {
print &ERROR("注意姓氏欄位，禁止輸入不雅字眼或空字符。");
exit();
}
if ($l_name2 =~ /@word[$i]/) {
print &ERROR("注意名稱欄位，禁止輸入不雅字眼或空字符。");
exit();
}
if ($msg2 =~ /@word[$i]/) {
print &ERROR("注意口頭語欄位，禁止輸入不雅字眼或空字符。");
exit();
}
if ($dmes2 =~ /@word[$i]/) {
print &ERROR("注意遺言欄位，禁止輸入不雅字眼或空字符。");
exit();
}
if ($com2 =~ /@word[$i]/) {
print &ERROR("注意代表句欄位，禁止輸入不雅字眼或空字符。");
exit();
}
}

#get User file
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
#Same Name and ID check
foreach $userlist(@userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
	if (($id2 eq $w_id) || (($f_name2 eq $w_f_name)&&($l_name2 eq $w_l_name))) {&ERROR("同樣的ID或同姓同名的字符已經存在。") ;}#同樣的ID或同姓同名？
}

#支付武器文件
open(DB,"$wep_file") || exit; seek(DB,0,0); @weplist=<DB>; close(DB);

#個人私有物文件
open(DB,"$stitem_file") || exit; seek(DB,0,0); @stitemlist=<DB>; close(DB);

#學生號碼文件
open(DB,"$member_file") || exit; seek(DB,0,0); $memberlist=<DB>; close(DB);
($m,$f,$mc,$fc) = split(/,/, $memberlist);

#性別人數核對
if ($sex2 eq "男生") {
	if ($mc >= $clmax) { &ERROR("男生數目超出限定不能登記。") ;}#登錄不能？
	$m+=1;$no=$m;$cl=$clas[$mc];
	if ($m >= $manmax) {$m=0;$mc+=1;}#(班)級更新？
} else {
	if ($fc >= $clmax) {&ERROR("女生數目超出限定不能登記。") ;}#登錄不能？
	$f+=1;$no=$f;$cl=$clas[$fc];
	if ($f >= $manmax) {$f=0;$fc+=1;}#(班)級更新？
}

#學生號碼文件更新
$memberlist="$m,$f,$mc,$fc,\n" ;
open(DB,">$member_file"); seek(DB,0,0); print DB $memberlist; close(DB);

#初期散發武器名單取得
$index = int(rand($#weplist));
($w_wep,$w_att,$w_tai) = split(/,/, $weplist[$index]);

#個人私有物條款名單取得
$index = int(rand($#stitemlist));
local($st_item,$st_eff,$st_tai) = split(/,/, $stitemlist[$index]);
$index = int(rand($#stitemlist));
local($st_item2,$st_eff2,$st_tai2) = split(/,/, $stitemlist[$index]);

#所持品初期化
for ($i=0; $i<6; $i++) {$item[$i] = "無"; $eff[$i]=$itai[$i]=0;}

#初期能力
$rand = int(rand(25));
$att = $rand + 50;
$def = 100 - $rand;
$hit = 100;
$mhit = $hit ;$kill=0;$sta = $maxsta ;$level=1;
#經驗值
$exp=0;
$reg_exp = $ar;
if ($reg_exp >= 4){$reg_exp-=4;$exp = ($ar * 10);}

$death = $msg = "";$sts = "正常"; $pls=0;$tactics = "通常" ;
$endtime = 0 ;$log = "";$dmes = "" ; $bid = "" ; $inf = "" ;

#初期道具及初期散發的武器
$item[0] = "麵包<>SH"; $eff[0] = 50; $itai[0] = 2;
$item[1] = "水<>HH"; $eff[1] = 50; $itai[1] = 2;
$item[2] = $w_wep; $eff[2] = $w_att; $itai[2] = $w_tai;

$wep = "空手<>WP";
$watt = 0;
$wtai = "∞" ;

if ($sex2 eq "男生" ) {$bou = "校服<>DBN";}
else {$bou = "水兵服<>DBN";}
local($bou_reg,$bou_regi) = split(/<>,/, $bou);
$bdef = 5;
$btai = 30;

$bou_h = $bou_f = $bou_a = "無" ;
$bdef_h = $bdef_f = $bdef_a = 0;
$btai_h = $btai_f = $btai_a = 0 ;

#子彈又箭支付
if ($w_wep =~ /<>WG/) {$item[3] = "子彈<>Y"; $eff[3] = 10; $itai[3] = 1;$item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;}#彈
elsif ($w_wep =~ /<>WA/) {$item[3] = "箭<>Y"; $eff[3] = 12; $itai[3] = 1;$item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;}#箭
else {$item[3] = $st_item; $eff[3] = $st_eff; $itai[3] = $st_tai;$item[4] = $st_item2; $eff[4] = $st_eff2; $itai[4] = $st_tai2;}

&CLUBMAKE ; #學部作成

#User File
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$seikaku = "無";#seikaku
$sinri = "無";#sinri
$teamID = "無";#TeamID
$teamPass = "無";#TeamPass
$ousen = "通常";#Ousen
$item_get = "無";
$eff_get = "0";
$itai_get = "0";
$newuser = "$id2,$password2,$f_name2,$l_name2,$sex2,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg2,$sts,$pls,$kill,$icon2,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes2,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com2,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n" ;

#New User Save
open(DB,">>$user_file"); seek(DB,0,0); print DB $newuser; close(DB);

#New User Log
&LOGSAVE("NEWENT") ;

$id=$id2; $password=$password2;

&CSAVE ;	#Cokie Save

($w_name,$w_kind) = split(/<>/, $w_wep);
($b_name,$b_kind) = split(/<>/, $bou_reg);

&HEADER;

print <<"_HERE_";
<center><B><FONT color="#ff0000" size="+3" face="Verdana">轉校手續完成</FONT></B><BR><BR></center>
<TABLE border="1" width="222" cellspacing="0">
  <TBODY>
	<TR><TD width="36" class="b1">(班)級</TD><TD colspan="3" class="b3">$cl</TD></TR>
	<TR><TD class="b1">姓名</TD><TD colspan="3" class="b3">$f_name2 $l_name2</TD></TR>
	<TR><TD class="b1">編號</TD><TD colspan="3" class="b3">$sex2$no��</TD></TR>
	<TR><TD class="b1">學部</TD><TD colspan="3" class="b3">$club</TD></TR>
	<TR><TD class="b1">體力</TD><TD class="b3">$hit/$mhit</TD><TD width="39" class="b1">能量</TD><TD class="b3">$sta</TD></TR>
	<TR><TD class="b1">攻擊力</TD><TD class="b3">$att</TD><TD class="b1">武器</TD><TD class="b3">$w_name</TD></TR>
	<TR><TD class="b1">防御力</TD><TD class="b3">$def</TD><TD class="b1">防具</TD><TD class="b3">$b_name</TD></TR>
  </TBODY>
</TABLE>
<P align="center">
_HERE_

if ($sex2 eq "男生") {print "$f_name2 $l_name2決定了吧？<BR>\n" ;}
else {print "$f_name2 $l_name2是嗎？<BR>\n" ;}

print <<"_HERE_";

轉校急急忙忙，不過，明天是修學旅行。<BR><BR>
你也真幸運，千萬記著不要遲到！<BR><BR>
<A href="regist.cgi?mode=info&Id=$id2&Password=$password2"><B><FONT color="#ff0000" size="+2">修學旅行出發</FONT></B></A><BR>
</P>
_HERE_
&FOOTER;
}

#===================#
# ■說明處理		#
#===================#
sub INFO {

&HEADER;

print <<"_HERE_";
<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">登錄完成</FONT></B><BR><BR>
張開眼睛後，發現自己在一個像教室的地方。我不是應該去了修學旅行嗎···？<BR>
「對了，在去修學旅行的巴士中忽然睡意襲來···」<BR>
縱覽四周，看見其他的學生好像也在。用心地看的話，發現了大家的頸上套上了銀色項圈，<BR>
用手碰自己的頸，也感覺到冷冷的金屬觸感。<BR>
正在疑惑大家為什麼都套上同樣的那個銀色項圈的時候...<BR><BR>
突然，從前面的門，一個男人全副武裝裝備的軍人走了進來···。<BR><BR>
<img border="0" src="img/i_sakamochi.jpg" width="70" height="70"><BR><BR>
「大家好，一年前的時候我也是這次計劃的擔當者。很榮幸能再擔任此次計劃的任務。很好！<BR>
隨著時間日子人民越來越安於現狀，過著幸福日子的時候，相信各位已經忘記了國家曾多努力多辛苦才能建成今天的社會地位，<BR>
如今國家開始衰退，想再振興，但人們已經再沒有自信，這是很危險的。因此，偉大的人們商量製定了這個計劃。<BR><BR>
<p align="center"><font color="#FF0000" face="Verdana" size="6">
<span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">
■ BATTLE ROYALE ■</span></font></p><BR>
今天起開始，在這裡諸位要開始互相殺害對方。<BR>
如果你想取下那個項圈，嘗試打算逃走的話，你將會立即被殺。<BR><BR>
直到剩下一人生存為止，乖乖遵守別犯規。<BR>
哎呀，老師都忘記了說，這裡是一個四面環海的荒島。<BR><BR>
而這裡是這個島的分校。<BR>
老師會一直在這裡看著各位努力。<BR><BR>
那麼，開始說這個計劃如何執行。你從這裡出去後去哪裡也可以。<BR>
每天8小時 (0點和8點和6點)，做全島廣播。一日三回。<BR><BR>
在那裡，大家會看到地圖，這個區域什麼時候危險老師會告知。<BR>
好好地了解地圖，離開那一個區域，<BR>
要很快地從那個區域出來喔。<BR><BR>
為何會這樣說呢，不逃離廣播危險區域的範圍，那個項圈是會爆炸的。<BR><BR>
因此呀，潛伏在該區域中的建築物中也是不行。<BR>
就算挖洞隱藏無線電波也會找到你引爆喔。<BR>
對了，建築物平常是可以讓你任意隱藏的。<BR><BR>
但還是你要知道。計劃有時間限制。你只有<B><font color="yellow">一週</font></B>時間去完成。<BR><BR>
時間夠如果還留下不止一人，剩下的那些人的項圈一樣會爆炸。因為冠軍只能夠存活<u>—人</u>。<BR><BR>
既然參加了游戲就要全力以赴，老師可不想看到沒勝利者呢！<BR>
你們每個人將被派發到一個物品包，裡面有食物和水，指南針，以及一件武器。<BR><BR>
下面開始，按照學號，拿好你們的東西，一個個離開這裡！<BR><BR>
<FORM METHOD="POST"  ACTION="battle.cgi" style="MARGIN: 0px">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="main">
<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
<center>
<INPUT type="submit" name="Enter" value="從教室出去">
</center>
</FORM>
_HERE_
&FOOTER;
}
#==================#
# ■學部作成     #
#==================#
sub CLUBMAKE {
$wa=$wg=$wb=$wc=$wd=$ws=$wn=$wf=$wp=$we=0 ;
#    複      髑  ⑻      痿      澎

local($dice) = int(rand(95)) ;

if		($dice < 10)	{$club = "射擊部";$wg = 1 * $BASE;}
elsif	($dice < 20)	{$club = "空手部";$wp = 1 * $BASE;}
elsif	($dice < 30)	{$club = "棒球部";$wc = 1 * $BASE;}
elsif	($dice < 40)	{$club = "科學部";$wd = 1 * $BASE;}
elsif	($dice < 50)	{$club = "劍擊部";$ws = 1 * $BASE;}
elsif	($dice < 60)	{$club = "劍道部";$ws = 1 * $BASE;}
elsif	($dice < 70)	{$club = "拳擊部";$wp = 1 * $BASE;}
elsif	($dice < 80)	{$club = "電腦部";}
elsif	($dice < 90)	{$club = "田徑部";}
elsif	($dice < 100)	{$club = "料理部";}
}
