#===================#
# ■ 狀態保存		#
#===================#
sub LOGSAVE2 {

local($work) = @_[0] ;
local($newlog) = "";

if ($work eq "NEWENT") {		#新規登錄
	$newlog = "$now,$f_name2,$l_name2,$sex2,$cl,$no,,,,,$host2,ENTRY,$IP,\n";
} elsif ($work eq "G-DATT"){	#小組脫離
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-DATT,$teamold,\n";
} elsif ($work eq "G-JOIN"){	#小組組成
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-JOIN,$teamID2,\n";
} elsif ($work eq "G-KANYU"){	#小組加入
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,G-KANYU,$teamID2,\n";
} elsif ($work eq "DEATH"){	#死亡(主要原因:陷阱·體力完了)
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH,$dmes,\n";
	$death = "衰弱死";$msg=$dmes;
} elsif ($work eq "DEATH1"){	#死亡(主要原因:毒死)
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH1,$dmes,\n";
	$death = "毒物攝取";$msg=$dmes;
} elsif ($work eq "DEATH2"){	#死亡(主要原因:敗死)
	local($w_name,$w_kind) = split(/<>/, $w_wep);
	if ($w_kind =~ /K/){$d2 = "斬殺";}#斬系
	elsif (($w_kind =~ /G/)&&($w_wtai > 0)){$d2 = "鎗殺";}#鎗系
	elsif ($w_kind =~ /C/){$d2 = "殺害";}#投系
	elsif ($w_kind =~ /D/){$d2 = "爆殺";}#爆系↓棍棒 or 子彈槍 or 箭弓
	elsif (($w_kind =~ /B/)||(($w_kind =~ /G|A/)&&($w_wtai == 0))){$d2 = "撲殺";}
	else {$d2 = "殺害";}
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,DEATH2,$dmes,\n";
	if ($w_no eq "政府"){$deth = "$w_f_name $w_l_name 被 $d2";}
	else {$deth = "$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 被 $d2";}
	if ($w_msg ne ""){$msg = "$w_f_name $w_l_name『$w_msg』";}
	else {$msg = "";}
} elsif ($work eq "DEATH3"){#敵人死亡(主要原因:敗死)
	local($w_name,$w_kind) = split(/<>/, $wep);
	if ($w_kind =~ /K/){$d2 = "劍殺";}#斬系
	elsif (($w_kind =~ /G/)&&($wtai > 0)){$d2 = "鎗殺";}#鎗系
	elsif ($w_kind =~ /C/){$d2 = "殺害";}#投系
	elsif ($w_kind =~ /D/){$d2 = "爆殺";}#爆系↓棍棒 or 子彈槍 or 箭弓
	elsif (($w_kind =~ /B/)||(($w_kind =~ /G|A/)&&($wtai == 0))){$d2 = "撲殺";}
	else {$d2 = "殺害" ;}
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$f_name,$l_name,$sex,$cl,$no,DEATH3,$w_dmes,\n";
	$deth = "$f_name $l_name ($cl $sex$no番) 被 $d2";
	if ($msg ne "") {$w_msg = "$f_name $l_name『$msg』";}
	else {$w_msg = "" ;}
	$w_log = "";
} elsif ($work eq "DEATH4" ){	#政府的殺害
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATH4,$w_dmes,\n";
	$deth = "政府的處刑";
	$log ="";
	if ($w_msg ne "") {$msg = "政府『$w_msg』";}
	else {$msg = "" ;}
} elsif ($work eq "DEATH5" ){	#政府的殺害2
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH4,$dmes,\n";
	$deth = "政府的處刑";
	$log ="";
	$msg = "政府『如果想取下可是不行啊，可疑的行動項圈都會爆破令你灰飛煙滅』";
} elsif ($work eq "DEATHAREA" ){	#死亡(主要原因:禁止區域)
	$newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATHAREA,$w_dmes,\n";
	$deth = "禁止停留的區域";
	$msg = "" ;$log ="";
} elsif ($work eq "WINEND1"){	#優勝決定
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,WINEND,$dmes,\n";
#	open(DB,"$win_file") || exit; seek(DB,0,0); @win_list=<DB>; close(DB);
#	unshift(@win_list,$newwinner);
#	open(DB,">$win_file"); seek(DB,0,0); print DB @win_list; close(DB);
	open(FLAG,">$end_flag_file"); print(FLAG "終了\n"); close(FLAG);
} elsif ($work eq "HACK"){	#Hacking成功
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,HACK,$dmes,\n";
} elsif ($work eq "EX_END"){	#Hacking停止程序
	$newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,EX_END,$dmes,\n";
} elsif ($work eq "AREAADD"){	#禁止區域追加
	$ar = $ar2 - 1 ;
	$newlog = "$now,$ar2,$ar,$hh,$weth,,,,,,,AREA,,\n";
}

open(DB,"$log_file") || exit; seek(DB,0,0); @loglist=<DB>; close(DB);
unshift(@loglist,$newlog);
open(DB,">$log_file"); seek(DB,0,0); print DB @loglist; close(DB);
}
#===================#
# ■ 彈出   		#
#===================#
sub KICKOUT{#■錯誤畫面
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
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">非法侵入者發現</span></font></center><BR><BR>
<FONT size="3">～請從正確的入口進入～<BR><BR>
</FONT><FONT size="2">表示3秒後自動轉向。<br>
如果沒有自動轉向，<a href="http://on.to/2Y">單擊這裡<a><br>CODE : $ref_ur<BR>
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
<a href="http://withlove.no-ip.com">繁體化：Withlove -- 夢幻學園 (Youko)</a></font></b>
</p></tr></td>
</table>
</div>
</BODY>
</HTML>
_HERE_
exit;
}

1;
