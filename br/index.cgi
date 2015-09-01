#! /usr/bin/perl
#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
open(DB,"$area_file");seek(DB,0,0); @arealist=<DB>;close(DB);
require "pref.cgi";
#Kick Out
if ($base_url) {$ref_url = $ENV{'HTTP_REFERER'};$ref_url =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;if ($ref_url !~ /$base_url/i) {require"$LIB_DIR/lib4.cgi";&KICKOUT;}}
#移動者&生存者
$ok = 0;$idou = 0;$no = 0;
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
foreach $userlist(@userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
	if (($w_hit > 0) && ($w_sts!~/NPC/)) {$ok++;}
	if (($w_sts eq "正常")&&($w_hit > 0)){$idou++;}
	if ($w_hit <= 0){$no++;}
}
$HEADERINDEX="2";
&HEADER ;
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);  $month++;$year += 1900;$week = ('日','月','火','水','木','金','土') [$wday];
$start_mon_rem = $start_mon - $month;
$start_day_rem = $start_day - $mday;
$start_hour_rem = $start_hour - $hour;
$start_min_rem = $start_min - $min;
$start_sec_rem = $start_sec - $sec;

print <<"_HERE_";
<font color="#FF0000" face="Verdana" size="6">
<span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">■ BATTLE ROYALE ULTIMATE ■</span></font><br>
<table border="0" align="center">
<tr><td><font color="yellow"><B>遊戲討論</B></font></td><td>：</td><td><a href="http://withlove.no-ip.com" target="_blank"><font color="#FFFFFF">Withlove -- 夢幻學園</font></a> <font color="#FFFFFF">-</font> <a href="http://withlove.no-ip.com/new-vbb/forumdisplay.php?s=&forumid=58" target="_blank"><font color="#FFFFFF">專題討論版</font></a>　　<font color="ffffff">GM</font> - Youko</td></tr>
<tr><td><font color="yellow"><B>現在時間</B></font></td><td>：</td><td>$month月 $mday日 $week曜日 $hour:$min分</td></tr>
<tr><td><font color="yellow"><B>開催回數</B></font></td><td>：</td><td><font size="+1" color="red"><B><U>第$arealist[6]回開催中</U></B></font><br></td></tr>
<tr><td><font color="yellow"><B>遊戲情報</B></font></td><td>：</td><td>遊戲於2003-09-27正式開放　|　遊戲討論教師：allyouget</td></tr>
</table>
<FORM NAME="time" style="MARGIN: 0px">遊戲現時狀態：<INPUT NAME="str" SIZE=30></FORM>
<SCRIPT language=JavaScript>
<!--
massage='$game';scrolltime=0;start=0;scrollspead=20;
function FSCROLL(){scrolltime=scrolltime+1;
if(scrolltime==scrollspead){scrolltime=0;msgscroll='';start=start+1;
	mmassage='【BRU】 ';
	if(start>massage.length){start=0}
	for(i=start;i<massage.length;i++){msgscroll=msgscroll+massage.charAt(i)}
	top.window.document.title=mmassage+msgscroll+massage+massage;setTimeout('FSCROLL()');}
else{setTimeout('FSCROLL()');}}
setTimeout('FSCROLL()')

var timerId;var x = 0;
function secCountDown() {
timerId = setTimeout("secCountDown()", 1000)
t = $start_mon_rem;d = $start_day_rem;h = $start_hour_rem;m = $start_min_rem;s = $start_sec_rem;x++;s -= x
if (s < 0) { t = s / 60;u = Math.floor(t);m += u; u = u * 60; s -= u ;}
if (m < 0) { t = m / 60;u = Math.floor(t);h += u; u = u * 60; m -= u ;}
if (h < 0) { t = h / 24;u = Math.floor(t);d += u; u = u * 60; h -= u ;}
if ((d <= 0)&&(h <= 0)&&(m <= 0)&&(s <= 0)||(d < 0)) {document.forms['time'].elements['str'].value = "開放中";clearTimeout( setTimeout );}
else {if (h < 10) { h = "0" + h; }if (m < 10) { m = "0" + m; }if (s < 10) { s = "0" + s; }document.forms['time'].elements['str'].value = d + "日" + h + "時間" + m + "分" + s + "秒";}
}

secCountDown();


var aryTMP=new Array();var chkRun=0;var chkKill=0;var msgBak="";var objBak="";var classBak="";var msgClm="";var maxRow=0;var msgDsp="";var msgScr="";
function typeMain(obj,cls,msg,max){
msgBak=msg;objBak=obj;classBak=cls;maxRow=0;maxRow=max-1;
if(chkRun==1){chkKill=1;return}
var cntMsgX=0;var cntMsgY=0;var cntLen=0;
 msgDsp="";msgScr="";msgClm="";
funcNum=aryTMP.length;
for(i=0;i<funcNum;i++){aryTMP[i]=""}
prtLay(obj,"");
while(msg.indexOf('%20')>=0){msg=msg.replace(/%20/," ")}
aryTMP=msg.split("$$");
typeWrite(obj,cls,cntMsgX,cntMsgY,cntLen)
}
function typeWrite(obj,cls,cntMsgX,cntMsgY,cntLen){
chkRun=1;msgDsp=aryTMP[cntMsgY];
if(chkKill==1){chkKill=0;chkRun=0;clearTimeout(writeID);typeMain(objBak,classBak,msgBak,maxRow+1)}
else{
 if(cntMsgX>msgDsp.length){cntMsgX=0;cntMsgY++;msgClm="";if(cntMsgY<=maxRow){for(i=0;i<cntMsgY;i++){msgClm+=aryTMP[i]+"<BR>"}}else{for(i=(cntMsgY-maxRow);i<cntMsgY;i++){msgClm+=aryTMP[i]+"<BR>"}}while(msgClm.indexOf(' ')>=0){msgClm=msgClm.replace(/ /,"&nbsp;")}msgScr="";if(cntMsgY<aryTMP.length){msgDsp=aryTMP[cntMsgY];writeID=setTimeout("typeWrite('"+obj+"','"+cls+"','"+cntMsgX+"','"+cntMsgY+"','"+cntLen+"')",50)}else{chkRun=0;chkKill=0;clearTimeout(writeID)}
 }else{if(cntLen&1){msgScr=msgDsp.substring(0,cntMsgX)+"<B style='"+cls+"'>_</B>"}else{msgScr=msgDsp.substring(0,cntMsgX)}while(msgScr.indexOf(' ')>=0){msgScr=msgScr.replace(/ /,"&nbsp;")}if(cntMsgX==msgDsp.length){csr=""}prtLay(obj,("<DIV style='"+cls+"'>"+msgClm+" "+msgScr+"</DIV>"));cntLen++;if(cntLen&1){cntMsgX++}writeID=setTimeout("typeWrite('"+obj+"','"+cls+"','"+cntMsgX+"','"+cntMsgY+"','"+cntLen+"')",50)}
}
}
function prtLay(obj,html){obj=getLay(obj);if(document.getElementById||document.all){obj.innerHTML=html}else if(document.layers){obj.document.open();obj.document.write(html);obj.document.close()}else if(document.all){obj.innerHTML=html}}
function getLay(obj){if(document.getElementById){return document.getElementById(obj)}else if(document.layers){return document.layers[obj]}else if(document.all){return document.all(obj)}}
// -->
</SCRIPT>
<table border="0" height="144"><tr><td align="center"><div id='tw'>&nbsp;</div></td></tr></table>
<font size="+1" color="lime">【生存者數：$ok人】　【現在移動者數：$idou人】　【死者數：$no人】</font>
<CENTER>
<FORM METHOD="POST" ACTION="battle.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="main">
<INPUT TYPE="HIDDEN" NAME="IPAdd" VALUE="$host">
<CENTER><FONT color="#ff0000" size="4" face="Verdana"><B>繼續遊戲</B></FONT></CENTER>
  <font size="2" face="Verdana">ID:</font>
  <font face="Verdana"><INPUT size="10" type="text" name="Id" maxlength="10" style="font-family: Chiller">&nbsp;&nbsp;&nbsp; </font>
  <font size="2" face="Verdana">Password:</font><font face="Verdana"><INPUT size="10" type="password" name="Password" maxlength="10"></font>&nbsp;&nbsp;&nbsp; <font face="Verdana"><INPUT type="submit" name="Enter" value="送出"></font></FORM>
</CENTER>
<P align="center">
<A href="rule.htm"><FONT color="#ff0000" size="4"><B>說明書</B></FONT></A><BR>
<BR>
<A href="regist.cgi"><FONT color="#ff0000" size="4"><B>新規登錄</B></FONT></A><BR>
<BR>
<A href="rank.cgi"><FONT color="#ff0000" size="4"><B>生存者一覽</B></FONT></A><BR>
<BR>
<A href="news.cgi"><FONT color="#ff0000" size="4"><B>進行狀況</B></FONT></A><BR>
<BR>
<A href="map.cgi"><FONT color="#ff0000" size="4"><B>會場地圖</B></FONT></A><BR>
<BR>
<A href="http://withlove.no-ip.com/new-vbb/showthread.php?s=&threadid=1649" target="_blank"><FONT color="#ff0000" size="4"><B>優勝者履歷</B></FONT></A><BR>
<BR>
<A href="admin.cgi"><FONT color="#ff0000" size="4"><B>管理介面</B></FONT></A><BR>
<BR>
<A href="http://withlove.no-ip.com/new-vbb/forumdisplay.php?s=&forumid=58" target="_blank"><FONT color="#ff0000" size="3"><B>Withlove 遊戲討論區</B></FONT></A><BR>
<BR>
<A href="http://on.to/2Y"><FONT color="#ff0000" size="3"><B>Battle Royale Ultimate 本家</B></FONT></A><BR>
<BR>
<A href="http://www.happy-ice.com/battle"><FONT color="#ff0000" size="3"><B>Battle Royale 本家</B></FONT></A><BR>
</P>
_HERE_
&FOOTER;
