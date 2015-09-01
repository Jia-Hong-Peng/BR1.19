#! /usr/bin/perl

#□■□■□■□■□■□■□■□■□■□■□
#■ 	- BR ADMINISTRATOR SCRIPT  - 	 ■
#□ 									 □
#■     	   	子程序一覽	    	 	 ■
#□ 									 □
#■ 		-     整理中     -			 ■
#□										 □
#■□■□■□■□■□■□■□■□■□■□■

#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
require "pref.cgi";

open(DB,"$admin_file");seek(DB,0,0); @admin=<DB>;close(DB);

&ADMDECODE ;
# GET 拒絕方法
$a_pass = crypt($a_pass,"2Y");

if(($Command eq "LOCKOFF")&&($id eq "@admin"))	{&LOCKOFF;&UNLOCK;exit;}		#鎖取下

if(!$p_flag){&ERROR("不正當的訪問。");}

if ($admpas ne ""){$admpass = crypt($admpas,"2Y");}
if ($admpass eq $a_pass){
	if	 ($Command eq "MAIN")			{&MENU;}	#菜單
	elsif($Command eq "BSAVE")		{&BACKSAVE;}	#接應保存
	elsif($Command eq "BREAD")		{&BACKREAD;}	#接應讀入
	elsif($Command eq "RESET")		{&RESET;}		#復位
	elsif($Command eq "ITEMLIST")	{&ITEMLIST;}	#道具名單
	elsif($Command eq "RESETACC")	{&DATARESET;}	#數據復位
	elsif($Command eq "USERLIST")	{&USERLIST;}	#用戶名單一覽
	elsif($Command eq "USERDEL")	{&USERDEL;}		#用戶刪掉
	elsif($Command eq "USERCHG")	{&USERCHG;}		#用戶變更
	elsif($Command eq "USERCHG3")	{&USERCHG3;}	#用戶變更
	elsif($Command eq "ENTER")		{&ENTER;}		#Admin Entrance
	elsif($Command eq "LOGON")		{&MAIN;}		#main
	elsif($Command eq "ITEMCHG")	{&ITEMCHG;}		#道具變更
	elsif($Command eq "LOCKOFF")	{&LOCKOFF;}		#鎖取下
	else { &MENU; }
}else{&MAIN;&UNLOCK;exit;}

&UNLOCK;
exit;
#==================#
# ■ Item Changer  #
#==================#
sub LOCKOFF {
local($xx, $name, $value);
for $xx (split(/; */, $ENV{'HTTP_COOKIE'})) {
	if ($xx =~ /BR/){
		$cooks = $xx;
		$cooks =~ s/BR=//;
		$cooks =~ s/([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $cooks);
	}
}
$cook = "";
$cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
print "Set-Cookie: BR=$cook; expires=$expires\n";

$new = rand($now);

open(DB,"$admin_file");seek(DB,0,0); @admin=<DB>;close(DB);
$admin[0] = "$new";
open(DB,">$admin_file"); seek(DB,0,0); print DB @admin; close(DB);


&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
LOCK 取下了。<br>
<br><B><FONT color="#ff0000">>><a href="index.cgi">HOME</a> >><a href="admin.cgi">ADMIN</a></b></FONT>
_HERE_
&FOOTER;
}

#==================#
# ■ Item Changer  #
#==================#
sub ITEMCHG {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if($w_sts ne "NPC"){$w_pls = 3;}
	$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
}
open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
OK<br>
<br><B><FONT color="#ff0000">>><a href="index.cgi">HOME</a> >><a href="admin.cgi">ADMIN</a></b></FONT>
_HERE_
&FOOTER;
}
#==================#
# ■ ITEM一覽	   #
#==================#
sub ITEMLIST {
&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<TABLE border="1" class="b3">
_HERE_
#Del Area Item
for ($j=0; $j<$#area+1; $j++) {
	$filename = "$LOG_DIR/$j$item_file";
	open(DB,"$filename");@itemlist=<DB>;close(DB);
	print "<TR><TD colspan=\"12\" class=\"b1\"><font size=\"+2\" color=\"yellow\">$place[$j]</font></TD></TR><TR><TD class=\"b2\">道具名<>種類</TD><TD class=\"b2\">種類</TD><TD class=\"b2\">效果</TD><TD class=\"b2\">數量</TD><TD class=\"b2\">道具名<>種類</TD><TD class=\"b2\">種類</TD><TD class=\"b2\">效果</TD><TD class=\"b2\">數量</TD><TD class=\"b2\">道具名<>種類</TD><TD class=\"b2\">種類</TD><TD class=\"b2\">效果</TD><TD class=\"b2\">數量</TD></TR>";
	for ($i=0;$i<$#itemlist+1;$i+=3) {
		($w_i,$w_e,$w_t) = split(/,/, $itemlist[$i]);
		($i_name,$i_kind) = split(/<>/, $w_i);
		if ($i_kind =~ /HH|HD/) {$itemtype = "【體力恢復】";}
		elsif ($i_kind =~ /SH|SD/) {$itemtype = "【能量恢復】";}
		elsif ($i_kind eq TN) {$itemtype = "【陷阱】";}
		elsif ($i_kind =~ /W/) {$itemtype = "【武器";
			if ($i_kind =~ /G/)  {$itemtype = ($itemtype . "(鎗)");}
			if ($i_kind =~ /N|S/)  {$itemtype = ($itemtype . "(ERROR)");}
			if ($i_kind =~ /K/)  {$itemtype = ($itemtype . "(劍)");}
			if ($i_kind =~ /C/)  {$itemtype = ($itemtype . "(投)");}
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(毆)");}
			if ($i_kind =~ /D/)  {$itemtype = ($itemtype . "(爆)");}
			$itemtype = ($itemtype . "】");}
		elsif ($i_kind =~ /D/)  {$itemtype = "【防具";
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(體)");}
			if ($i_kind =~ /H/)  {$itemtype = ($itemtype . "(頭)");}
			if ($i_kind =~ /F/)  {$itemtype = ($itemtype . "(足)");}
			if ($i_kind =~ /A/)  {$itemtype = ($itemtype . "(腕)");}
			$itemtype = ($itemtype . "】");}
		elsif (($i_kind eq R1)||($i_kind eq R2)) {$itemtype = "【雷達】";}
		elsif ($i_kind eq Y) {
			if (($i_name eq "假遊戲解除鑰匙")||($i_name eq "遊戲解除鑰匙")) {$itemtype = "【解除鑰匙】";}
			elsif ($i_name eq "【子彈】") {$itemtype = "【彈】";}
			else {$itemtype = "【道具】";}}
		elsif ($i_kind eq A) {$itemtype = "【裝飾品】";}
		elsif ($item[$i] eq "無") {$itemtype = "【無】";}
		else {$itemtype = "【不明】";}
		print "<TR><TD class=\"b3\">$w_i</TD><TD><font color=\"00ffff\">$itemtype</font></TD><TD class=\"b3\">$w_e</TD><TD class=\"b3\">$w_t</TD>";
		($w_i,$w_e,$w_t) = split(/,/, $itemlist[$i+1]);
		($i_name,$i_kind) = split(/<>/, $w_i);
		if ($i_kind =~ /HH|HD/) {$itemtype = "【體力恢復】";}
		elsif ($i_kind =~ /SH|SD/) {$itemtype = "【能量恢復】";}
		elsif ($i_kind eq TN) {$itemtype = "【陷阱】";}
		elsif ($i_kind =~ /W/) {$itemtype = "【武器";
			if ($i_kind =~ /G/)  {$itemtype = ($itemtype . "(鎗)");}
			if ($i_kind =~ /N|S/)  {$itemtype = ($itemtype . "(ERROR)");}
			if ($i_kind =~ /K/)  {$itemtype = ($itemtype . "(劍)");}
			if ($i_kind =~ /C/)  {$itemtype = ($itemtype . "(投)");}
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(毆)");}
			if ($i_kind =~ /D/)  {$itemtype = ($itemtype . "(爆)");}
			$itemtype = ($itemtype . "】");}
		elsif ($i_kind =~ /D/)  {$itemtype = "【防具";
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(體)");}
			if ($i_kind =~ /H/)  {$itemtype = ($itemtype . "(頭)");}
			if ($i_kind =~ /F/)  {$itemtype = ($itemtype . "(足)");}
			if ($i_kind =~ /A/)  {$itemtype = ($itemtype . "(腕)");}
			$itemtype = ($itemtype . "】");}
		elsif (($i_kind eq R1)||($i_kind eq R2)) {$itemtype = "【雷達】";}
		elsif ($i_kind eq Y) {
			if (($i_name eq "假遊戲解除鑰匙")||($i_name eq "遊戲解除鑰匙")) {$itemtype = "【解除鑰匙】";}
			elsif ($i_name eq "【子彈】") {$itemtype = "【彈】";}
			else {$itemtype = "【道具】";}}
		elsif ($i_kind eq A) {$itemtype = "【裝飾品】";}
		elsif ($item[$i] eq "無") {$itemtype = "【無】";}
		else {$itemtype = "【不明】";}
		print "<TD class=\"b3\">$w_i</TD><TD><font color=\"00ffff\">$itemtype</font></TD><TD class=\"b3\">$w_e</TD><TD class=\"b3\">$w_t</TD>";
		($w_i,$w_e,$w_t) = split(/,/, $itemlist[$i+2]);
		($i_name,$i_kind) = split(/<>/, $w_i);
		if ($i_kind =~ /HH|HD/) {$itemtype = "【體力恢復】";}
		elsif ($i_kind =~ /SH|SD/) {$itemtype = "【能量恢復】";}
		elsif ($i_kind eq TN) {$itemtype = "【陷阱】";}
		elsif ($i_kind =~ /W/) {$itemtype = "【武器";
			if ($i_kind =~ /G/)  {$itemtype = ($itemtype . "(鎗)");}
			if ($i_kind =~ /N|S/)  {$itemtype = ($itemtype . "(ERROR)");}
			if ($i_kind =~ /K/)  {$itemtype = ($itemtype . "(劍)");}
			if ($i_kind =~ /C/)  {$itemtype = ($itemtype . "(投)");}
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(毆)");}
			if ($i_kind =~ /D/)  {$itemtype = ($itemtype . "(爆)");}
			$itemtype = ($itemtype . "】");}
		elsif ($i_kind =~ /D/)  {$itemtype = "【防具";
			if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(體)");}
			if ($i_kind =~ /H/)  {$itemtype = ($itemtype . "(頭)");}
			if ($i_kind =~ /F/)  {$itemtype = ($itemtype . "(足)");}
			if ($i_kind =~ /A/)  {$itemtype = ($itemtype . "(腕)");}
			$itemtype = ($itemtype . "】");}
		elsif (($i_kind eq R1)||($i_kind eq R2)) {$itemtype = "【雷達】";}
		elsif ($i_kind eq Y) {
			if (($i_name eq "假遊戲解除鑰匙")||($i_name eq "遊戲解除鑰匙")) {$itemtype = "【解除鑰匙】";}
			elsif ($i_name eq "【子彈】") {$itemtype = "【彈】";}
			else {$itemtype = "【道具】";}}
		elsif ($i_kind eq A) {$itemtype = "【裝飾品】";}
		elsif ($item[$i] eq "無") {$itemtype = "【無】";}
		else {$itemtype = "【不明】";}
		print "<TD class=\"b3\">$w_i</TD><TD><font color=\"00ffff\">$itemtype</font></TD><TD class=\"b3\">$w_e</TD><TD class=\"b3\">$w_t</TD></TR>";
	}
}
print <<"_HERE_";
</TABLE>
<BR>
_HERE_
&FOOTER;
}
#==================#
# ■ 初期化Main畫面#
#==================#
sub RESET {
&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<FORM METHOD="POST">
<TABLE border="0">
<TR><TD>
<INPUT type="hidden" name="Password" value="$admpass">
<INPUT type="hidden" name="Command" value="RESETACC">
<font color="00FFFF"><b><center><font size="+3" color="blue">※警告※</font><br><br>這裡是做信息操作的CORE部分。<BR>沒有Administrator的權限請立刻離開<br>如果隨意地刪掉資料，就需要面對法律責任。<br></Center><BR>
<input type=checkbox name=RESET0 value="1" class="b4"> NPC 初始化<br>
<input type=checkbox name=RESET1 value="1" class="b4"> 時間初始化<br>
<input type=checkbox name=RESET2 value="1" class="b4"> 學生號碼初始化<br>
<input type=checkbox name=RESET3 value="1" class="b4"> 禁止區域初始化<br>
<input type=checkbox name=RESET4 value="1" class="b4"> 初始化狀態及遊戲開始狀態追加<br>
<input type=checkbox name=RESET5 value="1" class="b4"> 道具初始化狀態<br>
<input type=checkbox name=RESET6 value="1" class="b4"> 鎗聲初始化狀態<br>
<input type=checkbox name=RESET7 value="1" class="b4"> 用戶保存數據文件夾刪掉<br>
<input type=checkbox name=RESET8 value="1" class="b4"> Flag文件更新<br>
<input type=checkbox name=RESET10 value="1" class="b4"> BR開催回數數值UP<br>
<hr>
<input type=checkbox name=RESET9 value="1" class="b4">警告同意及刪除開始<br>
</b></FONT>
</TD></TR>
</TABLE>
<BR><INPUT type="submit" name="Enter" value="決定">
</FORM>
_HERE_
&FOOTER;
}
#==================#
# ■ 主要機能　    #
#==================#
sub MAIN {
&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<FORM METHOD="POST">
管理員密碼
<INPUT TYPE="HIDDEN" NAME="Command" VALUE="MAIN">
<INPUT size="16" type="password" name="Pass" maxlength="16">
　<INPUT type="submit" name="Enter" value="決定">
</FORM>
_HERE_
&FOOTER;
}

#==================#
# ■ 主要機能      #
#==================#
sub MENU {
&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<FORM METHOD="POST">
<TABLE border="0">
<TR><TD>
<INPUT type="hidden" name="Password" value="$admpass">
<INPUT type="radio" name="Command" value="USERLIST">用戶一覽<BR>
<INPUT type="radio" name="Command" value="ITEMLIST">道具一覽<BR>
<INPUT type="radio" name="Command" value="Cokkie">User Lock<BR>
<INPUT type="radio" name="Command" value="ITEMCHG">ITEM Data Changer<BR>
</td><td width="10">　</td><td>
<FONT COLOR="RED" size="1">
<INPUT type="radio" name="Command" value="BSAVE">保存<BR>
<INPUT type="radio" name="Command" value="BREAD">讀入<BR>
<INPUT type="radio" name="Command" value="RESET">數據初始化
</FONT>
</TD></TR>
</TABLE>
<BR><INPUT type="submit" name="Enter" value="決定">
</FORM>
_HERE_

&FOOTER;
}
#==================#
# ■ 保存 　　　　 #
#==================#
sub BACKSAVE {

	open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
	open(DB,">$back_file"); seek(DB,0,0); print DB @userlist; close(DB);

&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
保存完成。<br>
<br><B><FONT color="#ff0000">>><a href="index.cgi">HOME</a> >><a href="admin.cgi">ADMIN</a></b></FONT>
_HERE_
&FOOTER;

}
#==================#
# ■ 讀入　　　　  #
#==================#
sub BACKREAD {

open(DB,"$back_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
讀入完成。<br>
<br><B><FONT color="#ff0000">>><a href="index.cgi">HOME</a> >><a href="admin.cgi">ADMIN</a></b></FONT>
_HERE_
&FOOTER;
}
#==================#
# ■ 數據初始化　  #
#==================#
sub DATARESET {
if ($RESET9 ne "1"){&ERROR("同意");}#き啦
if ($RESET0){#NPC 初始化
	open(DB,"$npc_file");seek(DB,0,0); @baselist=<DB>;close(DB);
	$LEN = @baselist;
	$basyo = 1;
	if ($LEN > 0) {
		for ($i=0; $i<$LEN; $i++) {
			($w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,) = split(/,/, $baselist[$i]);
			if ($w_cl eq "$BOSS"){  #政府方面NPC
				$w_wep = "水素粒子水鐵砲<>WG";$w_watt = "100";$w_wtai = "200";
				$w_bou = "特種部隊服裝<>DB";$w_bdef = "50";$w_btai = "100";
				$w_bou_h = "源氏的盔<>DH";$w_bdef_h = "50";$w_btai_h = "100";
				$w_bou_f = "Nike的Air Force1<>DF";$w_bdef_f = "50";$w_btai_f = "100";
				$w_bou_a = "米奇的手袋<>DA";$w_bdef_a = "50";$w_btai_a = "100";
				if ($w_l_name eq "金發") {$w_icon = "42";}elsif ($w_l_name eq "田原") {$w_icon = "43";}elsif ($w_l_name eq "近藤") {$w_icon = "44";}elsif ($w_l_name eq "野村") {$w_icon = "45";}elsif ($w_l_name eq "加藤") {$w_icon = "46";}
				$w_item[0] = "遊戲解除鑰匙<>Y";$w_eff[0] = "1";$w_itai[0] = "1";
				$w_item[1] = "無";$w_eff[1] = "0";$w_itai[1] = "0";
				$w_item[2] = "無";$w_eff[2] = "0";$w_itai[2] = "0";
				$w_item[3] = "無";$w_eff[3] = "0";$w_itai[3] = "0";
				$w_item[4] = "無";$w_eff[4] = "0";$w_itai[4] = "0";
				$w_item[5] = "教師證明書<>A";$w_eff[5] = "1";$w_itai[5] = "1";
				$w_dmes = "記著這個嘛，『人生是遊戲。』";$w_com = "如果惹怒老師就不行囉～";$w_msg = "呀？看見了啊～";
				$w_att = 200;$w_def = 400;$w_hit = 1000;
				$w_level = 40; $w_exp = int($w_level*$baseexp+(($w_level-1)*$baseexp)) - 17;
				$w_tactics = "無"; $w_death = "" ;
				$w_pls = 0;
				$w_wn=$w_wp=$w_wa=$w_wg=$w_we=$w_wc=$w_wd=$w_wb=$w_wf=$w_ws= 100;
				$w_mhit=$w_hit; $w_sta = $maxsta;
				$w_sts = "NPC";
			} elsif ($w_cl eq "$KANN"){  #政府方面NPC
				$w_wep = "狙擊鎗㊣<>WG";$w_watt = "75";$w_wtai = "200";
				$w_bou = "軍服㊣<>DB";$w_bdef = "40";$w_btai = "100";
				$w_bou_h = "軍帽㊣<>DH";$w_bdef_h = "40";$w_btai_h = "100";
				$w_bou_f = "軍靴㊣<>DF";$w_bdef_f = "40";$w_btai_f = "100";
				$w_bou_a = "軍服㊣<>DA";$w_bdef_a = "40";$w_btai_a = "100";
				if ($w_l_name eq "金發") {$w_icon = "42";}elsif ($w_l_name eq "田原") {$w_icon = "43";}elsif ($w_l_name eq "近藤") {$w_icon = "44";}elsif ($w_l_name eq "野村") {$w_icon = "45";}elsif ($w_l_name eq "加藤") {$w_icon = "46";}
				$w_item[0] = "無";$w_eff[0] = "0";$w_itai[0] = "0";
				$w_item[1] = "無";$w_eff[1] = "0";$w_itai[1] = "0";
				$w_item[2] = "無";$w_eff[2] = "0";$w_itai[2] = "0";
				$w_item[3] = "無";$w_eff[3] = "0";$w_itai[3] = "0";
				$w_item[4] = "無";$w_eff[4] = "0";$w_itai[4] = "0";
				$w_item[5] = "教師證明書<>A";$w_eff[5] = "1";$w_itai[5] = "1";
				$w_dmes = "";$w_com = "";$w_msg = "";
				$w_att = 175;$w_def = 300;$w_hit = 750;
				$w_level = 30; $w_exp = int($w_level*$baseexp+(($w_level-1)*$baseexp)) - 17;
				$w_tactics = "無"; $w_death = "" ;
				$w_pls = 0;
				$w_wn=$w_wp=$w_wa=$w_wg=$w_we=$w_wc=$w_wd=$w_wb=$w_wf=$w_ws= 100;
				$w_mhit=$w_hit; $w_sta = $maxsta;
				$w_sts = "NPC";
			} elsif ($w_cl eq "$ZAKO"){  #政府方面NPC
				$w_wep = "狙擊鎗β<>WG";$w_watt = "50";$w_wtai = "200";
				$w_bou = "軍服β<>DB";$w_bdef = "30";$w_btai = "100";
				$w_bou_h = "軍帽β<>DH";$w_bdef_h = "30";$w_btai_h = "100";
				$w_bou_f = "軍靴β<>DF";$w_bdef_f = "30";$w_btai_f = "100";
				$w_bou_a = "軍服β<>DA";$w_bdef_a = "30";$w_btai_a = "100";
				if ($w_l_name eq "金發") {$w_icon = "42";}elsif ($w_l_name eq "田原") {$w_icon = "43";}elsif ($w_l_name eq "近藤") {$w_icon = "44";}elsif ($w_l_name eq "野村") {$w_icon = "45";}elsif ($w_l_name eq "加藤") {$w_icon = "46";}
				$w_item[0] = "無";$w_eff[0] = "0";$w_itai[0] = "0";
				$w_item[1] = "無";$w_eff[1] = "0";$w_itai[1] = "0";
				$w_item[2] = "無";$w_eff[2] = "0";$w_itai[2] = "0";
				$w_item[3] = "無";$w_eff[3] = "0";$w_itai[3] = "0";
				$w_item[4] = "無";$w_eff[4] = "0";$w_itai[4] = "0";
				$w_item[5] = "兵士證明書<>A";$w_eff[5] = "1";$w_itai[5] = "1";
				$w_dmes = "";$w_com = "";$w_msg = "";
				$w_att = 0;$w_def = 200;$w_hit = 500;
				$w_level = 20; $w_exp = int($w_level*$baseexp+(($w_level-1)*$baseexp)) - 17;
				$w_tactics = "無"; $w_death = "" ;
				$w_pls = $basyo;$basyo++;if ($basyo >= 22){$basyo = 1;};
				$w_wn=$w_wp=$w_wa=$w_wg=$w_we=$w_wc=$w_wd=$w_wb=$w_wf=$w_ws= 100;
				$w_mhit=$w_hit; $w_sta = $maxsta;
				$w_sts = "NPC";
			} else{;}#其他的NPC
			$w_kill = 0 ;
			$w_id = ($a_id . "$i"); $w_password = $a_pass;
			$w_tactics = "";
			$w_club="";
			$w_log = "" ; $w_bid = "" ; $w_inf="";
				$w_seikaku = "無";	#性格未完成
				$w_sinri = "無";		#心理未完成
				$w_teamID = $a_group_id;	#隊伍ID未完成
				$w_teamPass = $a_group_pass;	#隊伍密碼
				$w_tactics = "通常";
				$w_ousen = "通常";
				$w_club = "NPC";
				$w_password = $a_pass_npc;
				$w_item_get = "無";
				$w_eff_get = "0";
				$w_itai_get = "0";
			$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
		}
	}
	open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
}if ($RESET1){#時間初始化
	#時間文件更新
	$endtime = $now + ($battle_limit*60*60*24);
	$timelist="$now,$endtime,\n" ;
	open(DB,">$time_file"); seek(DB,0,0); print DB $timelist; close(DB);
}if ($RESET2){#學生號碼初始化
	#學生號碼文件更新
	$memberlist="0,0,0,0,\n" ;
	open(DB,">$member_file"); seek(DB,0,0); print DB $memberlist; close(DB);
}if ($RESET3){#禁止區域初始化
	#禁止區域文件更新
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now+(60*60*8));
	$min = "0$min" if ($min < 10);$month++;$year += 1900;
		if (($hour >= 4)&&($hour < 12)){$hour = 8;}
		elsif (($hour >= 12)&&($hour < 20)){$hour = 16;}
		elsif (($hour >= 20)&&($hour < 4)){$hour = 0;}
		else {$hour = 0;}
	$areadata[0] = ("$year,$month,$mday,$hour,0\n") ;   #區域追加時刻
	$areadata[1] = "1,0,\n" ; #禁止區域數，hacking標誌

	@work = @place ;@work2 = @area ;@work3 = @arno ;

	$ar = splice(@work,0,1) ;$areadata[2] = "$ar," ;
	$ar2 = splice(@work2,0,1) ;$areadata[3] = "$ar2," ;
	$ar3 = splice(@work3,0,1) ;$areadata[4] = "$ar3," ;

	for ($i=1; $i<$#place+1; $i++) {
		$chk=$#work+1;$index = int(rand($chk));
		$ar  = splice(@work,$index,1)  ;$areadata[2] = ($areadata[2] . "$ar,");
		$ar2 = splice(@work2,$index,1) ;$areadata[3] = ($areadata[3] . "$ar2,");
		$ar3 = splice(@work3,$index,1) ;$areadata[4] = ($areadata[4] . "$ar3,");
	}
	#weather
	local($weth) = int(rand(11)) ;
	$areadata[2] = ($areadata[2] . "\n");
	$areadata[3] = ($areadata[3] . "\n");
	$areadata[4] = ($areadata[4] . "\n");
	$areadata[5] = "$weth\n";
	$BRNUM = $arealist[6];
	if ($RESET10){$BRNUM++;}
	$areadata[6] = $BRNUM;

	open(DB,">$area_file"); seek(DB,0,0); print DB @areadata; close(DB);
	}if ($RESET4){#初始化及遊戲開始追加狀態
	#Newgame Log
	$loglist = "$now,$weth,,,,,,,,,,NEWGAME,,\n" ;
	open(DB,">$log_file"); seek(DB,0,0); print DB $loglist; close(DB);
}if ($RESET5){#道具狀態初始化
	#Del Area Item
	for ($i=0; $i<$#area+1; $i++) {@areaitem = "" ;$filename = "$LOG_DIR/$i$item_file";open(DB,">$filename"); seek(DB,0,0); print DB @areaitem; close(DB);}
	#Put Area Item
	open(DB,"$DAT_DIR/itemfile.dat");seek(DB,0,0); @itemlist=<DB>;close(DB);

	for ($i=0;$i<$#itemlist+1;$i++) {
		($idx,$count,$w_i,$w_e,$w_t) = split(/,/, $itemlist[$i]);
		chomp $w_t;
		if ($idx eq 99) {
			for ($a=$count; $a>=0;$a--){
				$idx = int(rand($#place)+1);
				$filename = "$LOG_DIR/$idx$item_file";
				open(DB,"$filename");seek(DB,0,0); @areaitem=<DB>;close(DB);
				push(@areaitem,"$w_i,$w_e,$w_t,\n") ;
				open(DB,">$filename"); seek(DB,0,0); print DB @areaitem; close(DB);
			}
		}else{
			$filename = "$LOG_DIR/$idx$item_file";
			open(DB,"$filename");seek(DB,0,0); @areaitem=<DB>;close(DB);
			for ($a=$count; $a>=0;$a--){
				push(@areaitem,"$w_i,$w_e,$w_t,\n") ;
			}
			open(DB,">$filename"); seek(DB,0,0); print DB @areaitem; close(DB);
		}
	}
}if ($RESET6){#鎗聲狀態初始化
	#鎗聲狀態更新
	local($null_data) = "0,,,,";
	open(DB,">$gun_log_file");
	for ($i=0; $i<6; $i++){print DB "$null_data\n";}
	close(DB);
}if ($RESET7){#用戶保存數據文件夾刪掉
	#用戶保存數據刪掉
	opendir(DIR, "$u_save_dir");
	foreach $file (readdir(DIR)) {unless($file =~ /^\.{1,2}$/){if($file =~ /$u_save_file/){push (@f_list,"$u_save_dir$file");}}}
	closedir(DIR);unlink(@f_list);
}if ($RESET8){#Flag文件更新
	#FLAG文件更新
	open(FLAG,">$end_flag_file"); print FLAG ""; close(FLAG);
}if ($RESET9){#Messenger 更新
	open(mes_file,">$mes_file"); print mes_file ""; close(mes_file);open(memberfile,">$memberfile"); print memberfile ""; close(memberfile);
}
&HEADER ;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
初期化完成。<br>
<br><B><FONT color="#ff0000">>><a href="index.cgi">HOME</a> >><a href="admin.cgi">ADMIN</a></b></FONT>
_HERE_
&FOOTER;
}
#==================#
# ■ Decoding處理  #
#==================#
sub ADMDECODE {
$p_flag=0;
if ($ENV{'REQUEST_METHOD'} eq "POST") {if ($ENV{'CONTENT_LENGTH'} > 51200) { &ERROR("是異常的輸入"); }read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});$p_flag=1;}
else { $buffer = $ENV{'QUERY_STRING'}; }
@pairs = split(/&/, $buffer);
foreach (@pairs) {
	($name,$value) = split(/=/, $_);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	# EUC變換字符編碼
	if ($name eq "Del") { push(@DEL,$value);}
	#&jcode'convert(*value, "euc", "", "z");
	#&jcode::tr(\$value, '﹛', ' ');
	#$value =~ s/</&lt;/g;
	#$value =~ s/>/&gt;/g;
	#$value =~ s/&/&amp;/g;
	#$value =~ s/"/&quot;/g;
	#$value =~ s/ /&nbsp;/g;
	#$value =~ s/,/﹜/g; #數據破損對策
	$in{$name} = $value;
}

$id = $in{'Id'};
$admpass = $in{'Password'};
$admpas = $in{'Pass'};
$Command = $in{'Command'};
$Message = $in{'Message'};
if ($Command eq "RESETACC"){
$RESET0 = 0;$RESET1 = 0;$RESET2 = 0;$RESET3 = 0;$RESET4 = 0;$RESET5 = 0;$RESET6 = 0;$RESET7 = 0;$RESET8 = 0;$RESET9 = 0;$RESET10 = 0;
$RESET0 = $in{'RESET0'};$RESET1 = $in{'RESET1'};$RESET2 = $in{'RESET2'};$RESET3 = $in{'RESET3'};$RESET4 = $in{'RESET4'};$RESET5 = $in{'RESET5'};$RESET6 = $in{'RESET6'};$RESET7 = $in{'RESET7'};$RESET8 = $in{'RESET8'};$RESET9 = $in{'RESET9'};$RESET10 = $in{'RESET10'};
}
if ($Command eq "USERCHG3"){
$w_id = $in{'w_id'};$w_password = $in{'w_password'};$w_f_name = $in{'w_f_name'};$w_l_name = $in{'w_l_name'};$w_sex = $in{'w_sex'};$w_cl = $in{'w_cl'};$w_no = $in{'w_no'};$w_endtime = $in{'w_endtime'};$w_att = $in{'w_att'};$w_def = $in{'w_def'};$w_hit = $in{'w_hit'};$w_mhit = $in{'w_mhit'};$w_level = $in{'w_level'};$w_exp = $in{'w_exp'};$w_sta = $in{'w_sta'};$w_wep = $in{'w_wep'};$w_watt = $in{'w_watt'};$w_wtai = $in{'w_wtai'};$w_bou = $in{'w_bou'};$w_bdef = $in{'w_bdef'};$w_btai = $in{'w_btai'};$w_bou_h = $in{'w_bou_h'};$w_bdef_h = $in{'w_bdef_h'};$w_btai_h = $in{'w_btai_h'};$w_bou_f = $in{'w_bou_f'};$w_bdef_f = $in{'w_bdef_f'};$w_btai_f = $in{'w_btai_f'};$w_bou_a = $in{'w_bou_a'};$w_bdef_a = $in{'w_bdef_a'};$w_btai_a = $in{'w_btai_a'};$w_tactics = $in{'w_tactics'};$w_death = $in{'w_death'};$w_msg = $in{'w_msg'};$w_sts = $in{'w_sts'};$w_pls = $in{'w_pls'};$w_kill = $in{'w_kill'};$w_icon = $in{'w_icon'};$w_item0 = $in{'w_item0'};$w_eff0 = $in{'w_eff0'};
$w_itai0 = $in{'w_itai0'};$w_item1 = $in{'w_item1'};$w_eff1 = $in{'w_eff1'};$w_itai1 = $in{'w_itai1'};$w_item2 = $in{'w_item2'};$w_eff2 = $in{'w_eff2'};$w_itai2 = $in{'w_itai2'};$w_item3 = $in{'w_item3'};$w_eff3 = $in{'w_eff3'};$w_itai3 = $in{'w_itai3'};$w_item4 = $in{'w_item4'};$w_eff4 = $in{'w_eff4'};$w_itai4 = $in{'w_itai4'};$w_item5 = $in{'w_item5'};$w_eff5 = $in{'w_eff5'};$w_itai5 = $in{'w_itai5'};$w_log = $in{'w_log'};$w_dmes = $in{'w_dmes'};$w_bid = $in{'w_bid'};$w_club = $in{'w_club'};$w_wn = $in{'w_wn'};$w_wp = $in{'w_wp'};$w_wa = $in{'w_wa'};$w_wg = $in{'w_wg'};$w_we = $in{'w_we'};$w_wc = $in{'w_wc'};$w_wd = $in{'w_wd'};$w_wb = $in{'w_wb'};$w_wf = $in{'w_wf'};$w_ws = $in{'w_ws'};$w_com = $in{'w_com'};$w_inf = $in{'w_inf'};$w_ousen = $in{'w_ousen'};$w_seikaku = $in{'w_seikaku'};$w_sinri = $in{'w_sinri'};$w_item_get = $in{'w_item_get'};$w_eff_get = $in{'w_eff_get'};$w_itai_get = $in{'w_itai_get'};$w_teamID = $in{'w_teamID'};$w_teamPass = $in{'w_teamPass'};$w_IP = $in{'w_IP'};

$USERCGH = $in{'Del'};}
	if($buffer eq ""){$Command = "LOGON"; $p_flag=1;}
}
#==================#
# ■ 一覽表示處理  #
#==================#
sub USERLIST {

$col_s1 = "<font color=white>" ;
$col_s2 = "<font color=red>" ;
$col_s3 = "<font color=skyblue>" ;
$col_e = "</font>" ;

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

push(@log,"<center><font color=\"#FF0000\" face=\"Verdana\" size=\"6\"><span id=\"BR\" style=\"width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline\">生存者一覽</span></font></center>");
push(@log,"<form method=\"POST\">\n");
push(@log,"刪掉訊息：<INPUT size=\"64\" type=\"text\" name=\"Message\" maxlength=\"64\"><BR><BR>\n");
push(@log,"<TABLE border=\"1\" class=\"b3\" cellspacing=\"0\" cellpadding=\"0\">\n");
push(@log,"<tr align=\"center\" class=\"b1\"><td height=\"1\" class=\"b1\">殺</td><TD width=\"50\" class=\"b1\" rowspan=\"2\">頭像</TD><td width=\"100\" class=\"b1\">名字 [出席號碼]</td><td class=\"b1\">能量</td><td width=\50\" class=\"b1\">體力</td><td class=\"b1\">狀態</td><td class=\"b1\">基本行動</td><td class=\"b1\">場所</td><td class=\"b1\">IP</td><td class=\"b1\">T-NAME</td></tr>
			<tr class=\"b3\"><td class=\"b1\">變</td><td class=\"b1\">ID-PASS</td><td class=\"b1\">攻擊</td><td class=\"b1\">防御</td><TD class=\"b1\" colspan=\"3\">武器</TD><TD class=\"b1\">防具(體)</TD><td class=\"b1\">T-PASS</td></tr>");
foreach (0 .. $#userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$_]);
	$col_s = $col_s1;
	if ($w_f_name =~ /兵士|監查員|板持/){$col_s = $col_s3;$w_password = "N/A";$w_teamPass = "N/A";}
	if ($w_hit <= 0) { $col_s = $col_s2; $w_sts = "死亡";}
	push(@log,"<tr><td><input type=checkbox name=Del value=\"$_\" class=\"b2\"></td><TD rowspan=\"2\" class=\"b3\"><IMG src=\"$imgurl$icon_file[$w_icon]\" width=\"50\" height=\"50\" border=\"0\" align=\"middle\"></TD><td align=\"center\" class=\"b3\">$col_s$w_f_name $w_l_name \[$w_cl\]$col_e</td><td class=\"b3\">$col_s$w_sta$col_e</td><td class=\"b3\">$col_s$w_hit/$w_mhit$col_e</td><td class=\"b3\">$col_s$w_sts$col_e</td><td class=\"b3\">$col_s$w_tactics$col_e</td><td class=\"b3\">$col_s$place[$w_pls]$col_e</td><td class=\"b3\">$col_s$w_IP$col_e</td><td class=\"b3\">$col_s$w_teamID$col_e</td></tr>
			   <TR><td class=\"b3\">　</td><td class=\"b3\"><font color=\"444444\">$w_id - $w_password</font></td><TD class=\"b3\">$col_s$w_att$col_e</TD><TD class=\"b3\">$col_s$w_def$col_e</TD><TD class=\"b3\" colspan=\"3\">$col_s$w_wep / $w_watt / $w_wtai$col_e</TD><TD class=\"b3\">$col_s$w_bou / $w_bdef / $w_btai$col_e</TD><td class=\"b3\">$col_s$w_teamPass$col_e</td></tr>");
}
push(@log,"</table><BR>\n");
push(@log,"<table border=\"2\" class=\"b1\"><TR class=\"b2\"><TD class=\"b2\"><b><font size=\"+1\"><input type=radio name=Command value=\"USERDEL\" class=\"b2\"><font color=red>　殺　　</font><input type=radio name=Command value=\"USERCHG\" class=\"b2\"><font color=yellow>　變　　</font><input type=radio name=Command value=\"ENTER\" class=\"b2\"><font color=skyblue>　入</font></font><b></TD></TR></table><BR>") ;
push(@log,"<input type=hidden name=Password value=$admpass><input type=submit value=\"確定\"><input type=reset value=\"重寫\"></form><BR>") ;

&HEADER ;
print @log;
&FOOTER;

}
#========#
# ■ 變  #
#========#
sub USERCHG {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$USERCHG = $DEL[0];
foreach (0 .. $#DEL) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$DEL[$_]]);
	&USERCHG2;exit;
}
}
#=========#
# ■ 變2  #
#=========#
sub USERCHG2 {
#狀態情報修正部
$USERCHG1 = ":</TD><TD><INPUT size=\"58\" type=\"text\" name";
$USERCHG2 = "<INPUT size=\"96\" type=\"text\" name";
&HEADER;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<FORM METHOD="POST">
<INPUT type="hidden" name="Password" value="$admpass">
<INPUT type="hidden" name="Command" value="USERCHG3">
<INPUT type="hidden" name="Del" value="$USERCHG">
<TABLE border="1" class="b1">
<TR><TD>ID(id)$USERCHG1="w_id" value="$w_id"></TD></TR>
<TR><TD>密碼(password)$USERCHG1="w_password" value="$w_password"></TD></TR>
<TR><TD>姓(f_name)$USERCHG1="w_f_name" value="$w_f_name"></TD></TR>
<TR><TD>名(l_name)$USERCHG1="w_l_name" value="$w_l_name"></TD></TR>
<TR><TD>性別(sex)$USERCHG1="w_sex" value="$w_sex"></TD></TR>
<TR><TD>班級(cl)$USERCHG1="w_cl" value="$w_cl"></TD></TR>
<TR><TD>出席番號(no)$USERCHG1="w_no" value="$w_no"></TD></TR>
<TR><TD>最後行動的時間(endtime)$USERCHG1="w_endtime" value="$w_endtime"></TD></TR>
<TR><TD>攻擊力(att)$USERCHG1="w_att" value="$w_att"></TD></TR>
<TR><TD>防御力(def)$USERCHG1="w_def" value="$w_def"></TD></TR>
<TR><TD>體力(hit)$USERCHG1="w_hit" value="$w_hit"></TD></TR>
<TR><TD>最大體力(mhit)$USERCHG1="w_mhit" value="$w_mhit"></TD></TR>
<TR><TD>等級(level)$USERCHG1="w_level" value="$w_level"></TD></TR>
<TR><TD>經驗值(exp)$USERCHG1="w_exp" value="$w_exp"></TD></TR>
<TR><TD>能量(sta)$USERCHG1="w_sta" value="$w_sta"></TD></TR>
<TR><TD>裝備武器名<>種類(wep)$USERCHG1="w_wep" value="$w_wep"></TD></TR>
<TR><TD>裝備武器的攻擊力(watt)$USERCHG1="w_watt" value="$w_watt"></TD></TR>
<TR><TD>裝備武器的數量或使用回數(wtai)$USERCHG1="w_wtai" value="$w_wtai"></TD></TR>
<TR><TD>裝備防具名<>種類(bou)$USERCHG1="w_bou" value="$w_bou"></TD></TR>
<TR><TD>裝備防具的防御力(bdef)$USERCHG1="w_bdef" value="$w_bdef"></TD></TR>
<TR><TD>裝備防具的耐久度(btai)$USERCHG1="w_btai" value="$w_btai"></TD></TR>
<TR><TD>裝備頭防具名<>種類(bou_h)$USERCHG1="w_bou_h" value="$w_bou_h"></TD></TR>
<TR><TD>裝備頭防具的防御力(bdef_h)$USERCHG1="w_bdef_h" value="$w_bdef_h"></TD></TR>
<TR><TD>裝備頭防具的耐久度(btai_h)$USERCHG1="w_btai_h" value="$w_btai_h"></TD></TR>
<TR><TD>裝備足防具<>種類(bou_f)$USERCHG1="w_bou_f" value="$w_bou_f"></TD></TR>
<TR><TD>裝備足防具的防御力(bdef_f)$USERCHG1="w_bdef_f" value="$w_bdef_f"></TD></TR>
<TR><TD>裝備足防具的耐久度(btai_f)$USERCHG1="w_btai_f" value="$w_btai_f"></TD></TR>
<TR><TD>裝備腕防具名<>種類(bou_a)$USERCHG1="w_bou_a" value="$w_bou_a"></TD></TR>
<TR><TD>裝備腕防具的防御力(bdef_a)$USERCHG1="w_bdef_a" value="$w_bdef_a"></TD></TR>
<TR><TD>裝備腕防具的耐久度(btai_a)$USERCHG1="w_btai_a" value="$w_btai_a"></TD></TR>
<TR><TD>行動方針(tactics)$USERCHG1="w_tactics" value="$w_tactics"></TD></TR>
<TR><TD>自分之殺害者(death)$USERCHG1="w_death" value="$w_death"></TD></TR>
<TR><TD>殺害時的口頭語(msg)$USERCHG1="w_msg" value="$w_msg"></TD></TR>
<TR><TD>現在狀態（睡眠·治療·通常）(sts)$USERCHG1="w_sts" value="$w_sts"></TD></TR>
<TR><TD>現在位置(pls)$USERCHG1="w_pls" value="$w_pls"></TD></TR>
<TR><TD>殺害人數(kill)$USERCHG1="w_kill" value="$w_kill"></TD></TR>
<TR><TD>頭像號碼(icon)$USERCHG1="w_icon" value="$w_icon"></TD></TR>
<TR><TD>所持道具名<>種類(item0)$USERCHG1="w_item0" value="$w_item[0]"></TD></TR>
<TR><TD>所持道具的效力（子彈．箭的數）(eff0)$USERCHG1="w_eff0" value="$w_eff[0]"></TD></TR>
<TR><TD>所持道具的數量(itai0)$USERCHG1="w_itai0" value="$w_itai[0]"></TD></TR>
<TR><TD>所持道具名<>種類(item1)$USERCHG1="w_item1" value="$w_item[1]"></TD></TR>
<TR><TD>所持道具的效力（子彈．箭的數）(eff1)$USERCHG1="w_eff1" value="$w_eff[1]"></TD></TR>
<TR><TD>所持道具的數量(itai1)$USERCHG1="w_itai1" value="$w_itai[1]"></TD></TR>
<TR><TD>所持道具名<>種類(item2)$USERCHG1="w_item2" value="$w_item[2]"></TD></TR>
<TR><TD>所持道具名的效力（子彈．箭的數）(eff2)$USERCHG1="w_eff2" value="$w_eff[2]"></TD></TR>
<TR><TD>所持道具名的數量(itai2)$USERCHG1="w_itai2" value="$w_itai[2]"></TD></TR>
<TR><TD>所持道具名<>種類(item3)$USERCHG1="w_item3" value="$w_item[3]"></TD></TR>
<TR><TD>所持道具的效力（子彈．箭的數）(eff3)$USERCHG1="w_eff3" value="$w_eff[3]"></TD></TR>
<TR><TD>所持道具的數量(itai3)$USERCHG1="w_itai3" value="$w_itai[3]"></TD></TR>
<TR><TD>所持道具名<>種類(item4)$USERCHG1="w_item4" value="$w_item[4]"></TD></TR>
<TR><TD>所持道具的效力（子彈．箭的數）(eff4)$USERCHG1="w_eff4" value="$w_eff[4]"></TD></TR>
<TR><TD>所持道具的數量(itai4)$USERCHG1="w_itai4" value="$w_itai[4]"></TD></TR>
<TR><TD>附件名<>種類(item5)$USERCHG1="w_item5" value="$w_item[5]"></TD></TR>
<TR><TD>附件的防御力(eff5)$USERCHG1="w_eff5" value="$w_eff[5]"></TD></TR>
<TR><TD>附件的數量(itai5)$USERCHG1="w_itai5" value="$w_itai[5]"></TD></TR>
<TR><TD colspan="2" width="500">狀態　　<input type=radio name=Message value=\"add\" class=\"b2\" checked>追加<input type=radio name=Message value=\"change\" class=\"b2\">改變<BR><hr>$w_log</TD></TR>
<TR><TD colspan="2">$USERCHG2="w_log"></TD></TR>
<TR><TD>遺言(dmes)$USERCHG1="w_dmes" value="$w_dmes"></TD></TR>
<TR><TD>前戰鬥者的ID(bid)$USERCHG1="w_bid" value="$w_bid"></TD></TR>
<TR><TD>學部(club)$USERCHG1="w_club" value="$w_club"></TD></TR>
<TR><TD>斬熟練度(wn)$USERCHG1="w_wn" value="$w_wn"></TD></TR>
<TR><TD>毆熟練度(wp)$USERCHG1="w_wp" value="$w_wp"></TD></TR>
<TR><TD>射熟練度(wa)$USERCHG1="w_wa" value="$w_wa"></TD></TR>
<TR><TD>鎗熟練度(wg)$USERCHG1="w_wg" value="$w_wg"></TD></TR>
<TR><TD>未使用(we)$USERCHG1="w_we" value="$w_we"></TD></TR>
<TR><TD>投熟練度(wc)$USERCHG1="w_wc" value="$w_wc"></TD></TR>
<TR><TD>爆熟練度(wd)$USERCHG1="w_wd" value="$w_wd"></TD></TR>
<TR><TD>棍熟練度(wb)$USERCHG1="w_wb" value="$w_wb"></TD></TR>
<TR><TD>返回(wf)$USERCHG1="w_wf" value="$w_wf"></TD></TR>
<TR><TD>刺熟練度(ws)$USERCHG1="w_ws" value="$w_ws"></TD></TR>
<TR><TD>代表句(com)$USERCHG1="w_com" value="$w_com"></TD></TR>
<TR><TD>負傷狀態（優勝時『勝』輸入）(inf)$USERCHG1="w_inf" value="$w_inf"></TD></TR>
<TR><TD>應戰行動(ousen)$USERCHG1="w_ousen" value="$w_ousen"></TD></TR>
<TR><TD>性格(seikaku)$USERCHG1="w_seikaku" value="$w_seikaku"></TD></TR>
<TR><TD>心理(sinri)$USERCHG1="w_sinri" value="$w_sinri"></TD></TR>
<TR><TD>新道具名<>種類(item_get)$USERCHG1="w_item_get" value="$w_item_get"></TD></TR>
<TR><TD>新道具的效力（子彈．箭的數）(eff_get)$USERCHG1="w_eff_get" value="$w_eff_get"></TD></TR>
<TR><TD>新道具的數量(itai_get)$USERCHG1="w_itai_get" value="$w_itai_get"></TD></TR>
<TR><TD>小組ID(teamID)$USERCHG1="w_teamID" value="$w_teamID"></TD></TR>
<TR><TD>小組Pass(teamPass)$USERCHG1="w_teamPass" value="$w_teamPass"></TD></TR>
<TR><TD>IP Address(IP)$USERCHG1="w_IP" value="$w_IP"></TD></TR>
</TABLE>
<BR><INPUT type="submit" name="Enter" value="決定">
</FORM>
_HERE_
&FOOTER;
}
#========#
# ■ 變  #
#========#
sub USERCHG3 {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

foreach (0 .. $#DEL) {
	($c_id,$c_password,$c_f_name,$c_l_name,$c_sex,$c_cl,$c_no,$c_endtime,$c_att,$c_def,$c_hit,$c_mhit,$c_level,$c_exp,$c_sta,$c_wep,$c_watt,$c_wtai,$c_bou,$c_bdef,$c_btai,$c_bou_h,$c_bdef_h,$c_btai_h,$c_bou_f,$c_bdef_f,$c_btai_f,$c_bou_a,$c_bdef_a,$c_btai_a,$c_tactics,$c_death,$c_msg,$c_sts,$c_pls,$c_kill,$c_icon,$c_item[0],$c_eff[0],$c_itai[0],$c_item[1],$c_eff[1],$c_itai[1],$c_item[2],$c_eff[2],$c_itai[2],$c_item[3],$c_eff[3],$c_itai[3],$c_item[4],$c_eff[4],$c_itai[4],$c_item[5],$c_eff[5],$c_itai[5],$c_log,$c_dmes,$c_bid,$c_club,$c_wn,$c_wp,$c_wa,$c_wg,$c_we,$c_wc,$c_wd,$c_wb,$c_wf,$c_ws,$c_com,$c_inf,$c_ousen,$c_seikaku,$c_sinri,$c_item_get,$c_eff_get,$c_itai_get,$c_teamID,$c_teamPass,$c_IP,) = split(/,/, $userlist[$DEL[$_]]);
	if ($Message ne "change"){$w_log = "$c_log$w_log";}
	$userlist[$DEL[$_]] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item0,$w_eff0,$w_itai0,$w_item1,$w_eff1,$w_itai1,$w_item2,$w_eff2,$w_itai2,$w_item3,$w_eff3,$w_itai3,$w_item4,$w_eff4,$w_itai4,$w_item5,$w_eff5,$w_itai5,$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
}

open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

&USERLIST;
}
#========#
# ■ 入  #
#========#
sub ENTER {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
foreach (0 .. $#DEL) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$DEL[$_]]);
}
&HEADER;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">Administrative Mode</span></font></center>
<B><FONT color="#ff0000" size="+1">-轉送-</FONT></B><BR>
<FORM METHOD="POST" ACTION="battle.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="main">
<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$w_id">
<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$w_password">
<h2>$w_f_name $w_l_name ($w_cl $w_sex$w_no番)</h2>
<h5><font color="Yellow">沒有管理者權限的人是完全禁止進入。</font></h5>
<INPUT type="submit" name="Enter" value="開始">
</FORM>
_HERE_
&FOOTER;
exit;
}
#==================#
# ■ 刪除處理      #
#==================#
sub USERDEL {

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

foreach (0 .. $#DEL) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$DEL[$_]]);
	$w_msg = $Message;
	&LOGSAVE("DEATH4") ;
	$w_hit = 0 ; $w_sts = "死亡"; $w_death=$deth;
	$userlist[$DEL[$_]] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
}

open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

&USERLIST;

}
