#==================#
# �� ID�ֹ�B�z�@�@#
#==================#
sub IDCHK {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$jyulog = "" ;$jyulog2 = "" ;$jyulog3 = "" ;#�j�n
$mem=0;
$chksts = "NG";
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $id2) {	#ID�@�P�H
		if ($w_password eq $password2) {	#�K�X���`�H
			if ($w_hit > 0) {	#�ͦs�H
				$chksts = "OK";$Index=$i;$mem++;$plsmem[$w_pls]++ ;
				($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,) = split(/,/, $userlist[$i]);
				&CSAVE;
				open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);#�j�n
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[0]) ;
				if (($now < ($guntime+(30)))&& ($wid ne $id) && ($wid2 ne $id)) {$jyulog = "<font color=\"yellow\"><b>�b$gunpls�Ať���F�j�n�K�C</b></font><br>";}#�ϥκj30��H���H
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[1]) ;
				if (($now < ($guntime+(30)))&& ($wid ne $id) && ($wid2 ne $id) && ($place[$pls] eq $gunpls)) {$jyulog2 = "<font color=\"yellow\"><b>ť��G�s�n�H�֡A�ֳQ���F�K�H</b></font><br>";}#���`30��H���H
				local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[2]) ;
				if (($now < ($guntime+(60)))) {$jyulog3 = "<font color=\"yellow\"><b>�q$gunplsť��$wid���n���K</b></font><br><font color=\"lime\"><b>�y$wid2�z</b></font><br>";}#���n���ϥ�1���H���H
			} else {if($c_id ne "2YBRU"){&CDELETE;}&ERROR("�w�g���`�C<BR><BR>���]�G$w_death<BR><BR><font color=\"lime\"><b>$w_msg</b></font><br><br><EMBED src=\"$dead\" HEIGHT=70 width=140>") ;}
		} else {if ($w_password eq "2YBRU") {&ERROR("�Q�޲z����W�C�кɧ��p���޲z�̡C") ;}else{&ERROR("�K�X���۲šC") ;}}
	} else {if ($w_hit > 0) {$plsmem[$w_pls]++ ;if ($w_sts ne "NPC"){ $mem ++ ; }}
	}
}
if ($chksts eq "NG") {&ERROR("ID�䤣��C") ;}
local($b_limit) = ($battle_limit * 3) + 1;
if ((($mem eq 1) && ($inf =~ /��/) && ($ar > $b_limit))||(($mem eq 1) && ($ar > $b_limit))) {if($fl !~ /�פF/){open(FLAG,">$end_flag_file"); print(FLAG "�פF\n"); close(FLAG);&LOGSAVE("WINEND1");}require "$LIB_DIR/disp.cgi";&ENDING;}#�u�ӡH
elsif ($inf =~ /��/){require "$LIB_DIR/disp.cgi";&ENDING;}
elsif ($fl =~ /�Ѱ�/){require "$LIB_DIR/disp.cgi";&ENDING;}
else {if ($log ne '') {$wlog = $log ;$log="";&SAVE;$log=$wlog;}$bid = "" ;}
&SAVE;
}
#==================#
# �� decoding�B�z  #
#==================#
sub DECODE {
$p_flag=0;
	if ($ENV{'REQUEST_METHOD'} eq "POST") {$p_flag=1;if ($ENV{'CONTENT_LENGTH'} > 51200) {&ERROR("��J���`"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }@pairs = split(/&/, $buffer);foreach (@pairs) {
	($name,$value) = split(/=/, $_);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	#&jcode::convert(*value, "euc", "", "z");&jcode::tr(\$value, '�@', ' ');

	$value =~ s/&amp;/&/g;$value =~ s/&lt;/</g;$value =~ s/&gt;/>/g;$value =~ s/&quot;/"/g;$value =~ s/&nbsp;/ /g;
	$value =~ s/&/&amp;/g;$value =~ s/</&lt;/g;$value =~ s/>/&gt;/g;$value =~ s/"/&quot;/g;$value =~ s/ /&nbsp;/g;$value =~ s/,/�A/g; #�ƾگ}�l�ﵦ
$in{$name} = $value;
}

$mode = $in{'mode'};$id2 = $in{'Id'};$password2 = $in{'Password'};

$Command = $in{'Command'};$Command2 = $in{'Command2'};$Command3 = $in{'Command3'};$Command4 = $in{'Command4'};$Command5 = $in{'Command5'};

$l_name2 = $in{'L_Name'};$f_name2 = $in{'F_Name'};$teamID2 = $in{'teamID2'};$teamPass2 = $in{'teamPass2'};$msg2 = $in{'Message'};$dmes2 = $in{'Message2'};$com2 = $in{'Comment'};$dengon = $in{'Dengon'};$sex2 = $in{'Sex'};$icon2 = $in{'Icon'};$itno2 = $in{'Itno'};$getid = $in{'WId'};$speech = $in{'speech'};$IP = $in{'IP'};$IPAdd = $in{'IPAdd'};

$Message = $in{'Mess'};$m_id = $in{'M_Id'};$full_name = $in{'full_name'};

srand;
}
#===================#
# �� ��O���F�@�@	#
#===================#
sub DRAIN{
local($d_mode) = $_[0];
$log = ($log . "$l_name��q�ӺɤF�K�C�̤jHP��֡C<BR>");
$sta = 100;
$mhit -= 100;
if ($mhit <= 0) {
	$hit = $mhit = 0;
	$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>");
		&LOGSAVE("DEATH") ; #���`���A
		$mem--;if ($mem == 1) {&LOGSAVE("WINEND1");}
	if($d_mode eq "mov"){&SAVE;return;}
	elsif($d_mode eq "eve"){$Command = "EVENT";}
} elsif($hit > $mhit){$hit = $mhit;}
}
#===================#
# �� �Τ�H���O�s	#
#===================#
sub SAVE {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$IP =~ s/\n//;
$chksts = 0;
for ($i=0; $i<$#userlist+1; $i++) {($w_i,$w_p,$a) = split(/,/, $userlist[$i]);if (($id2 eq $w_i) && ($password2 eq $w_p)) {$chksts = 1;$Index=$i;last;}}#ID�@�P�H

if ($chksts){
	if ($hit <= 0) {$sts = "���`";$inf = $now;}
	$userlist[$Index] =			"$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n";
	open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
}
}
#===================#
# �� �ı����O�s		#
#===================#
sub SAVE2 {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$w_IP =~ s/\n//;
if ($w_hit <= 0) {$w_sts = "���`";$w_inf = $now;}
$userlist[$Index2] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;

open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
}
#===================#
# �� ���١@�@�@�@	#
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
# �� �O�s�@�@�@�@	#
#===================#
sub CSAVE {
$cook = "$id,$password,$f_name,$l_name,$sex,$cl,$no,0,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,";
$cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
print "Set-Cookie: BR=$cook; expires=$expires\n";
}
#===================#
# �� �R���@�@�@�@	#
#===================#
sub CDELETE {
$cook = "2YBRU,,,,,,,$now,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,";
$cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
print "Set-Cookie: BR=$cook; expires=$expires\n";
}
#===================#
# �� ���A�O�s		#
#===================#
sub LOGSAVE {local($work) = @_[0] ;require"$LIB_DIR/lib4.cgi";&LOGSAVE2($work);}
#===================#
# �� �D�H�W���o��	#
#===================#
sub GetHostName {my($ip_address) = @_;my(@addr) = split(/\./, $ip_address);my($packed_addr) = pack("C4", $addr[0], $addr[1], $addr[2], $addr[3]);my($name, $aliases, $addrtype, $length, @addrs);($name, $aliases, $addrtype, $length, @addrs) = gethostbyaddr($packed_addr, 2);return $name;}
#===================#
# �� �H���@�@		#
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
if ($HEADERINDEX){print "onload=\"typeMain('tw','color=#black','�s�@���}�l�A�@�Ӫ���a�I���C$$�������~�v�H�Ʀ�����Q��%$$���~�̬�}�@�d�U�H$$�������W�ǾǥͤK�Q�U�H$$�j�H�̮`�ȫĤl���h�۫H�A�q�L�F�@�Ӫk�סC$$�s�@���Ш|�ﭲ�k�i�U��BR�k�j$$��ޥ���50�Ӫ줤3�~���ǯZ�C$$�Z�űN�i��y�̫᪺�@�H�z�԰��C$$�ڻ��̫�ͦs���ǥͤ~�i�H��^�a���y���H�C���z�P�P�P�C',9)\"onload=\"BRU.scrollIntoView(true)\"><CENTER><DIV ID=\"BRU\">";}
else{print "onload=\"BRU.scrollIntoView(true)\"><CENTER><DIV ID=\"BRU\"><SCRIPT language=JavaScript src=\"BRU.JS\"></SCRIPT>";}
}
#===================#
# �� footer��		#
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
<font color="yellow">�`�N:System���ܧ�аѷӸԲӳW�h�C<BR>�̾A�X�ѪR��800X600�A��F11�i���ܬ����̹���ܡC</font>
</td><td>
<p style="text-align: right">
<b><font face="Viner Hand ITC" color="#ff0000" style="font-size: 9pt">
<a href="http://www.happy-ice.com/battle/">BATTLE ROYALE $ver</a><br>
<a href="http://withlove.no-ip.com">�c��ơGWithlove -- �ڤ۾Ƕ� (Youko)</a><br>
<a href="http://wlserver.net/">WLserver Network Services</a></font></b>
</p></tr></td>
</table>
</div>
</BODY>
</HTML>
_HERE_
}
#===================#
# �� ���~�B�z		#
#===================#
sub ERROR{#�����~�e��
if ($lockflag) { &UNLOCK; }
$errmes0 = @_[0];
$errmes1 = @_[1];
$errmes2 = @_[2];
if ($errmes1 eq ""){$errmes1 = "N/A"}
if ($errmes2 eq ""){$errmes2 = "N/A"}
&HEADER;
print <<"_HERE_";
<B><FONT color="#ff0000" size="+3" face="Verdana">���~�o��</FONT></B><BR><BR>
<FONT size="2">$errmes0<BR><BR>
Comment:$errmes1<BR><BR>
ERROR ID:$errmes2<BR><BR>
<BR><B><FONT color="#ff0000"><A href="index.cgi">HOME</A></B></Font>
_HERE_
&FOOTER;
exit;
}
#===================#
# �� Auto Select	#
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
# �� LOCK	#
#===========#
sub LOCK {
local($retry,$mtime);
# 1���H�W�ª���R����-symlink��Ʀ���-mkdir��Ʀ���
if	 (-e $lockf) {$mtime = (stat($lockf))[9];if ($mtime < time - 60){ &UNLOCK;}}
elsif($lkey eq 1){$retry = 5;while (!symlink(".", $lockf)){if (--$retry <= 5){&ERROR("�C�����@���C�Э@�ߵ��ԡC");}sleep(1);}}
elsif($lkey eq 2){$retry = 5;while (!mkdir($lockf, 0755)){if (--$retry <= 5) {&ERROR("�C�����@���C�Э@�ߵ��ԡC");}sleep(1);}}
elsif($lkey eq 3){local($lk) = mkdir($lockf, 0755);if ($lk eq 0)			 {&ERROR("�C�����@���C�Э@�ߵ��ԡC");}}
$lockflag=1;
}
#===========#
# �� UNLOCK	#
#===========#
sub UNLOCK {if($lkey eq 1){unlink($lockf);}elsif($lkey eq 2){rmdir($lockf);}elsif($lkey eq 3){ rmdir($lockf);}$lockflag=0;}
1;
