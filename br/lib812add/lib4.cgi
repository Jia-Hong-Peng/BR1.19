#===================#
# �� ���A�O�s		#
#===================#
sub LOGSAVE2 {

local($work) = @_[0] ;
local($newlog) = "";

if ($work eq "NEWENT") {		#�s�W�n��
	$newlog = "$now,$f_name2,$l_name2,$sex2,$cl,$no,,,,,$host2,ENTRY,$IP,\n";
} elsif ($work eq "G-DATT"){	#�p�ղ���
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-DATT,$teamold,\n";
} elsif ($work eq "G-JOIN"){	#�p�ղզ�
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-JOIN,$teamID2,\n";
} elsif ($work eq "G-KANYU"){	#�p�ե[�J
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-KANYU,$teamID2,\n";
} elsif ($work eq "DEATH"){	#���`(�D�n��]:�����P��O���F)
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH,$dmes,\n";
	$death = "�I�z��";$msg=$dmes;
} elsif ($work eq "DEATH1"){	#���`(�D�n��]:�r��)
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH1,$dmes,\n";
	$death = "�r�����";$msg=$dmes;
} elsif ($work eq "DEATH2"){	#���`(�D�n��]:�Ѧ�)
	local($w_name,$w_kind) = split(/<>/, $w_wep);
	if ($w_kind =~ /K/){$d2 = "�ٱ�";}#�٨t
	elsif (($w_kind =~ /G/)&&($w_wtai > 0)){$d2 = "���";}#��t
	elsif ($w_kind =~ /C/){$d2 = "���`";}#��t
	elsif ($w_kind =~ /D/){$d2 = "�z��";}#�z�t���Ҵ� or �l�u�j or �b�}
	elsif (($w_kind =~ /B/)||(($w_kind =~ /G|A/)&&($w_wtai == 0))){$d2 = "����";}
	else {$d2 = "���`";}
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,DEATH2,$dmes,\n";
	if ($w_no eq "�F��"){$deth = "$w_f_name $w_l_name �Q $d2";}
	else {$deth = "$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) �Q $d2";}
	if ($w_msg ne ""){$msg = "$w_f_name $w_l_name�y$w_msg�z";}
	else {$msg = "";}
} elsif ($work eq "DEATH3"){#�ĤH���`(�D�n��]:�Ѧ�)
	local($w_name,$w_kind) = split(/<>/, $wep);
	if ($w_kind =~ /K/){$d2 = "�C��";}#�٨t
	elsif (($w_kind =~ /G/)&&($wtai > 0)){$d2 = "���";}#��t
	elsif ($w_kind =~ /C/){$d2 = "���`";}#��t
	elsif ($w_kind =~ /D/){$d2 = "�z��";}#�z�t���Ҵ� or �l�u�j or �b�}
	elsif (($w_kind =~ /B/)||(($w_kind =~ /G|A/)&&($wtai == 0))){$d2 = "����";}
	else {$d2 = "���`" ;}
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$f_name,$l_name,$sex,$cl,$no,DEATH3,$w_dmes,\n";
	$deth = "$f_name $l_name ($cl $sex$no�f) �Q $d2";
	if ($msg ne "") {$w_msg = "$f_name $l_name�y$msg�z";}
	else {$w_msg = "" ;}
	$w_log = "";
} elsif ($work eq "DEATH4" ){	#�F�������`
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATH4,$w_dmes,\n";
	$deth = "�F�����B�D";
	$log ="";
	if ($w_msg ne "") {$msg = "�F���y$w_msg�z";}
	else {$msg = "" ;}
} elsif ($work eq "DEATH5" ){	#�F�������`2
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH4,$dmes,\n";
	$deth = "�F�����B�D";
	$log ="";
	$msg = "�F���y�p�G�Q���U�i�O����ڡA�i�ê���ʶ��鳣�|�z�}�O�A�ǭ��Ϸ��z";
} elsif ($work eq "DEATHAREA" ){	#���`(�D�n��]:�T��ϰ�)
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATHAREA,$w_dmes,\n";
	$deth = "�T��d���ϰ�";
	$msg = "" ;$log ="";
} elsif ($work eq "WINEND1"){	#�u�ӨM�w
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,WINEND,$dmes,\n";
#	open(DB,"$win_file") || exit; seek(DB,0,0); @win_list=<DB>; close(DB);
#	unshift(@win_list,$newwinner);
#	open(DB,">$win_file"); seek(DB,0,0); print DB @win_list; close(DB);
	open(FLAG,">$end_flag_file"); print(FLAG "�פF\n"); close(FLAG);
} elsif ($work eq "HACK"){	#Hacking���\
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,HACK,$dmes,\n";
} elsif ($work eq "EX_END"){	#Hacking����{��
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,EX_END,$dmes,\n";
} elsif ($work eq "AREAADD"){	#�T��ϰ�l�[
	$ar = $ar2 - 1 ;
	$newlog = "$now,$ar2,$ar,$hh,$weth,,,,,,,AREA,,\n";
}

open(DB,"$log_file") || exit; seek(DB,0,0); @loglist=<DB>; close(DB);
unshift(@loglist,$newlog);
open(DB,">$log_file"); seek(DB,0,0); print DB @loglist; close(DB);
}
#===================#
# �� �u�X   		#
#===================#
sub KICKOUT{#�����~�e��
if ($lockflag) { &UNLOCK; }
print "Content-type: text/html\n\n";
print <<"_HERE_";
<HTML><HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=big5">
<META http-equiv=refresh content=3;url=../../index.htm>
<TITLE>$game</TITLE>
<LINK REL="stylesheet" TYPE="text/css" HREF="BRU.CSS">
</HEAD>
<BODY contextmenu="false" bottommargin="0" rightmargin="0" topmargin="0" leftmargin="0" bgcolor="#000000" text="#ffffff" link="#ff0000" vlink="#ff0000" aLink="#ff0000" 
_HERE_
print "onload=\"BRU.scrollIntoView(true)\"><CENTER><DIV ID=\"BRU\">";
print "<SCRIPT language=JavaScript src=\"BRU.JS\"></SCRIPT>";
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">�D�k�I�J�̵o�{</span></font></center><BR><BR>
<FONT size="3">��бq���T���J�f�i�J��<BR><BR>
</FONT><FONT size="2">���3���۰���V�C<br>
�p�G�S���۰���V�A<a href="http://on.to/2Y">�����o��<a><br>CODE : $ref_ur<BR>
<BR><B><FONT color="#ff0000"><U>HOME</U></B></Font>
</CENTER>
</DIV>
<div width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr><td colspan="2">
<HR>
</tr></td>
<tr><td>
<p style="text-align: right">
<b><font face="Viner Hand ITC" color="#ff0000" style="font-size: 9pt">
<a href="http://www.happy-ice.com/battle/">BATTLE ROYALE $ver</a><br>
<a href="http://withlove.no-ip.com">�c��ơGWithlove -- �ڤ۾Ƕ� (Youko)</a></font></b>
</p></tr></td>
</table>
</div>
</BODY>
</HTML>
_HERE_
exit;
}

1;
