#==================#
# ■ ID核對處理　　#
#==================#
sub IDCHK {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$jyulog = "" ;$jyulog2 = "" ;$jyulog3 = "" ;#槍聲
$mem=0;
$chksts = "NG";
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $id2) {	#ID一致？
		if ($w_password eq $password2) {	#密碼正常？
			if ($w_hit > 0) {	#生存？
				$chksts = "OK";$Index=$i;$mem++;$plsmem[$w_pls]++ ;
				($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,) = split(/,/, $userlist[$i]);
				&CSAVE;
				open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);#槍聲
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[0]) ;
				if (($now < ($guntime+(30)))&& ($wid ne $id) && ($wid2 ne $id)) {$jyulog = "<font color=\"yellow\"><b>在$gunpls，聽見了槍聲…。</b></font><br>";}#使用槍30秒以內？
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[1]) ;
				if (($now < ($guntime+(30)))&& ($wid ne $id) && ($wid2 ne $id) && ($place[$pls] eq $gunpls)) {$jyulog2 = "<font color=\"yellow\"><b>聽到慘叫聲？誰，誰被殺了…？</b></font><br>";}#殺害30秒以內？
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[2]) ;
				if (($now < ($guntime+(60)))) {$jyulog3 = "<font color=\"yellow\"><b>從$gunpls聽見$wid的聲音…</b></font><br><font color=\"lime\"><b>『$wid2』</b></font><br>";}#揚聲器使用1分以內？
			} else {if($c_id ne "2YBRU"){&CDELETE;}&ERROR("已經死亡。<BR><BR>死因：$w_death<BR><BR><font color=\"lime\"><b>$w_msg</b></font><br><br><EMBED src=\"$dead\" HEIGHT=70 width=140>") ;}
		} else {if ($w_password eq "2YBRU") {&ERROR("被管理員鎖上。請盡快聯絡管理者。") ;}else{&ERROR("密碼不相符。") ;}}
	} else {if ($w_hit > 0) {$plsmem[$w_pls]++ ;if ($w_sts ne "NPC"){ $mem ++ ; }}
	}
}
if ($chksts eq "NG") {&ERROR("ID找不到。") ;}
local($b_limit) = ($battle_limit * 3) + 1;
if ((($mem eq 1) && ($inf =~ /勝/) && ($ar > $b_limit))||(($mem eq 1) && ($ar > $b_limit))) {if($fl !~ /終了/){open(FLAG,">$end_flag_file"); print(FLAG "終了\n"); close(FLAG);&LOGSAVE("WINEND1");}require "$LIB_DIR/disp.cgi";&ENDING;}#優勝？
elsif ($inf =~ /解/){require "$LIB_DIR/disp.cgi";&ENDING;}
elsif ($fl =~ /解除/){require "$LIB_DIR/disp.cgi";&ENDING;}
else {if ($log ne '') {$wlog = $log ;$log="";&SAVE;$log=$wlog;}$bid = "" ;}
&SAVE;
}
#==================#
# ■ decoding處理  #
#==================#
sub DECODE {
$p_flag=0;
	if ($ENV{'REQUEST_METHOD'} eq "POST") {$p_flag=1;if ($ENV{'CONTENT_LENGTH'} > 51200) {&ERROR("輸入異常"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }@pairs = split(/&/, $buffer);foreach (@pairs) {
	($name,$value) = split(/=/, $_);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	#&jcode::convert(*value, "euc", "", "z");&jcode::tr(\$value, '　', ' ');

	$value =~ s/&amp;/&/g;$value =~ s/&lt;/</g;$value =~ s/&gt;/>/g;$value =~ s/&quot;/"/g;$value =~ s/&nbsp;/ /g;
	$value =~ s/&/&amp;/g;$value =~ s/</&lt;/g;$value =~ s/>/&gt;/g;$value =~ s/"/&quot;/g;$value =~ s/ /&nbsp;/g;$value =~ s/,/，/g; #數據破損對策
$in{$name} = $value;
}

$mode = $in{'mode'};$id2 = $in{'Id'};$password2 = $in{'Password'};

$Command = $in{'Command'};$Command2 = $in{'Command2'};$Command3 = $in{'Command3'};$Command4 = $in{'Command4'};$Command5 = $in{'Command5'};

$l_name2 = $in{'L_Name'};$f_name2 = $in{'F_Name'};$teamID2 = $in{'teamID2'};$teamPass2 = $in{'teamPass2'};$msg2 = $in{'Message'};$dmes2 = $in{'Message2'};$com2 = $in{'Comment'};$dengon = $in{'Dengon'};$sex2 = $in{'Sex'};$icon2 = $in{'Icon'};$itno2 = $in{'Itno'};$getid = $in{'WId'};$speech = $in{'speech'};$IP = $in{'IP'};$IPAdd = $in{'IPAdd'};

$Message = $in{'Mess'};$m_id = $in{'M_Id'};$full_name = $in{'full_name'};

srand;
}
#===================#
# ■ 體力完了　　	#
#===================#
sub DRAIN{
local($d_mode) = $_[0];
$log = ($log . "$l_name能量耗盡了…。最大HP減少。<BR>");
$sta = 100;
$mhit -= 100;
if ($mhit <= 0) {
	$hit = $mhit = 0;
	$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>");
		&LOGSAVE("DEATH") ; #死亡狀態
		$mem--;if ($mem == 1) {&LOGSAVE("WINEND1");}
	if($d_mode eq "mov"){&SAVE;return;}
	elsif($d_mode eq "eve"){$Command = "EVENT";}
} elsif($hit > $mhit){$hit = $mhit;}
}
#===================#
# ■ 用戶信息保存	#
#===================#
sub SAVE {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$IP =~ s/\n//;
$chksts = 0;
for ($i=0; $i<$#userlist+1; $i++) {($w_i,$w_p,$a) = split(/,/, $userlist[$i]);if (($id2 eq $w_i) && ($password2 eq $w_p)) {$chksts = 1;$Index=$i;last;}}#ID一致？

if ($chksts){
	if ($hit <= 0) {$sts = "死亡";$inf = $now;}
	$userlist[$Index] =			"$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n";
	open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
}
}
#===================#
# ■ 敵情報保存		#
#===================#
sub SAVE2 {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$w_IP =~ s/\n//;
if ($w_hit <= 0) {$w_sts = "死亡";$w_inf = $now;}
$userlist[$Index2] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;

open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
}
#===================#
# ■ 續還　　　　	#
#===================#
sub CREAD {
local($xx, $name, $value);
for $xx (split(/; */, $ENV{'HTTP_COOKIE'})) {
	if ($xx =~ /BR/){
		$cooks = $xx;
		$cooks =~ s/BR=//;
		$cooks =~ s/([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;
		($c_id,$c_password,$c_f_name,$c_l_name,$c_sex,$c_cl,$c_no,$c_endtime,$c_att,$c_def,$c_hit,$c_mhit,$c_level,$c_exp,$c_sta,$c_wep,$c_watt,$c_wtai,$c_bou,$c_bdef,$c_btai,$c_bou_h,$c_bdef_h,$c_btai_h,$c_bou_f,$c_bdef_f,$c_btai_f,$c_bou_a,$c_bdef_a,$c_btai_a,$c_tactics,$c_death,$c_msg,$c_sts,$c_pls,$c_kill,$c_icon,$c_item[0],$c_eff[0],$c_itai[0],$c_item[1],$c_eff[1],$c_itai[1],$c_item[2],$c_eff[2],$c_itai[2],$c_item[3],$c_eff[3],$c_itai[3],$c_item[4],$c_eff[4],$c_itai[4],$c_item[5],$c_eff[5],$c_itai[5],$c_log,$c_dmes,$c_bid,$c_club,$c_wn,$c_wp,$c_wa,$c_wg,$c_we,$c_wc,$c_wd,$c_wb,$c_wf,$c_ws,$c_com,$c_inf,$c_f_name_y,$c_l_name_y,$c_koma) = split(/,/, $cooks);
	}
}
}
#===================#
# ■ 保存　　　　	#
#===================#
sub CSAVE {
$cook = "$id,$password,$f_name,$l_name,$sex,$cl,$no,0,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,";
$cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
print "Set-Cookie: BR=$cook; expires=$expires\n";
}
#===================#
# ■ 刪除　　　　	#
#===================#
sub CDELETE {
$cook = "2YBRU,,,,,,,$now,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,";
$cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
print "Set-Cookie: BR=$cook; expires=$expires\n";
}
#===================#
# ■ 狀態保存		#
#===================#
sub LOGSAVE {local($work) = @_[0] ;require"$LIB_DIR/lib4.cgi";&LOGSAVE2($work);}
#===================#
# ■ 主人名取得ぜ	#
#===================#
sub GetHostName {my($ip_address) = @_;my(@addr) = split(/\./, $ip_address);my($packed_addr) = pack("C4", $addr[0], $addr[1], $addr[2], $addr[3]);my($name, $aliases, $addrtype, $length, @addrs);($name, $aliases, $addrtype, $length, @addrs) = gethostbyaddr($packed_addr, 2);return $name;}
#===================#
# ■ ？部　　		#
#===================#
sub HEADER {
print "Content-type: text/html\n\n";
print <<"_HERE_";
<HTML><HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=big5">
<TITLE>$game</TITLE>
<LINK REL="stylesheet" TYPE="text/css" HREF="BRU.CSS">
</HEAD>
<BODY rightmargin="0" topmargin="0" leftmargin="0" bgcolor="#000000" text="#ffffff" link="#ff0000" vlink="#ff0000" aLink="#ff0000" 
_HERE_
if ($HEADERINDEX){print "onload=\"typeMain('tw','color=#black','新世紀開始，一個的國家衰落。$$完全失業率人數佔全國十五%$$失業者突破一千萬人$$完全不上學學生八十萬人$$大人們害怕孩子失去自信，通過了一個法案。$$新世紀教育改革法【俗稱BR法】$$選拔全國50個初中3年的學班。$$班級將進行『最後的一人』戰鬥。$$據說最後生存的學生才可以返回家的『殺人遊戲』···。',9)\"onload=\"BRU.scrollIntoView(true)\"><CENTER><DIV ID=\"BRU\">";}
else{print "onload=\"BRU.scrollIntoView(true)\"><CENTER><DIV ID=\"BRU\"><SCRIPT language=JavaScript src=\"BRU.JS\"></SCRIPT>";}
}
#===================#
# ■ footer部		#
#===================#
sub FOOTER {
print <<"_HERE_";
</CENTER>
</DIV>
<div width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr><td colspan="2">
<HR>
</tr></td>
<tr><td>
<font color="yellow">注意:System的變更請參照詳細規則。<BR>最適合解析度800X600，按F11可改變為全屏幕顯示。</font>
</td><td>
<p style="text-align: right">
<b><font face="Viner Hand ITC" color="#ff0000" style="font-size: 9pt">
<a href="http://www.happy-ice.com/battle/">BATTLE ROYALE $ver</a><br>
<a href="http://withlove.no-ip.com">繁體化：Withlove -- 夢幻學園 (Youko)</a><br>
<a href="http://wlserver.net/">WLserver Network Services</a></font></b>
</p></tr></td>
</table>
</div>
</BODY>
</HTML>
_HERE_
}
#===================#
# ■ 錯誤處理		#
#===================#
sub ERROR{#■錯誤畫面
if ($lockflag) { &UNLOCK; }
$errmes0 = @_[0];
$errmes1 = @_[1];
$errmes2 = @_[2];
if ($errmes1 eq ""){$errmes1 = "N/A"}
if ($errmes2 eq ""){$errmes2 = "N/A"}
&HEADER;
print <<"_HERE_";
<B><FONT color="#ff0000" size="+3" face="Verdana">錯誤發生</FONT></B><BR><BR>
<FONT size="2">$errmes0<BR><BR>
Comment:$errmes1<BR><BR>
ERROR ID:$errmes2<BR><BR>
<BR><B><FONT color="#ff0000"><A href="index.cgi">HOME</A></B></Font>
_HERE_
&FOOTER;
exit;
}
#===================#
# ■ Auto Select	#
#===================#
sub AS {
$AS_MES = @_[0];
if ($ASN eq ""){$ASN = "0";}
if ($AS_MES){
	print "<A title=\"$AS_MES\" onclick=sl($ASN); href=\"javascript:void(0);\" onmouseover=\"status=\'$AS_MES\';return true;\">";
}else{
	print "<A onclick=sl($ASN); href=\"javascript:void(0);\" onmouseover=\"status=\' \';return true;\">";
}
$ASN++;
}
#===========#
# ■ LOCK	#
#===========#
sub LOCK {
local($retry,$mtime);
# 1分以上舊的鎖刪掉的-symlink函數式鎖-mkdir函數式鎖
if	 (-e $lockf) {$mtime = (stat($lockf))[9];if ($mtime < time - 60){ &UNLOCK;}}
elsif($lkey eq 1){$retry = 5;while (!symlink(".", $lockf)){if (--$retry <= 5){&ERROR("遊戲維護中。請耐心等候。");}sleep(1);}}
elsif($lkey eq 2){$retry = 5;while (!mkdir($lockf, 0755)){if (--$retry <= 5) {&ERROR("遊戲維護中。請耐心等候。");}sleep(1);}}
elsif($lkey eq 3){local($lk) = mkdir($lockf, 0755);if ($lk eq 0)			 {&ERROR("遊戲維護中。請耐心等候。");}}
$lockflag=1;
}
#===========#
# ■ UNLOCK	#
#===========#
sub UNLOCK {if($lkey eq 1){unlink($lockf);}elsif($lkey eq 2){rmdir($lockf);}elsif($lkey eq 3){ rmdir($lockf);}$lockflag=0;}
1;
