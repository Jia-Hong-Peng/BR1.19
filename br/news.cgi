#! /usr/bin/perl
#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
require "pref.cgi";
$kinshiarea = 0;
open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21],$ar[22]) = split(/,/, $arealist[4]);

$getmonth=$getday=0;
foreach $loglist(@loglist) {
	($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$host)= split(/,/, $loglist);
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($gettime);
	$hour = "0$hour" if ($hour < 10);
	$min = "0$min" if ($min < 10);  $month++;
	$year += 1900;
	$week = ('日','月','火','水','木','金','土') [$wday];
	if (($getmonth != $month)||($getday != $mday)){
		if ($getmonth !=0){push (@log,"</LI></UL>");}
		$getmonth=$month;$getday = $mday;
		push (@log,"<P><font color=\"lime\"><B>$month月 $mday日 ($week曜日)</B></font><BR><UL>");
	}

	if (($host ne "")&&($getkind =~ /DEATH/)) { $host = "($host)"; }

	if	 ($getkind eq "DEATH")		{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 死亡。<font color=\"red\"><b>$host</b></font><BR>") ;}#死亡 (自分之原因)
	elsif($getkind eq "DEATH1")		{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 死亡。<font color=\"red\"><b>$host</b></font><BR>");}#死亡 (毒死)
	elsif($getkind eq "DEATH2")		{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 被 <font color=\"red\">$w_f_name2 $w_l_name2 ($w_cl2 $w_sex2$w_no2番) </font> 殺害。<font color=\"red\"><b>$host</b></font><BR>");}#死亡 (他殺)
	elsif($getkind eq "DEATH3")		{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 被 <font color=\"red\">$w_f_name2 $w_l_name2 ($w_cl2 $w_sex2$w_no2番) </font> 殺害。<font color=\"red\"><b>$host</b></font><BR>");}#死亡 (他殺)
	elsif($getkind eq "DEATH4")		{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 被 <font color=\"red\">政府</font> 處刑殺害。<font color=\"red\"><b>$host</b></font><BR>");}#死亡（政府）
	elsif($getkind eq "DEATHAREA")	{push (@log,"<LI>$hour時$min分，<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 因處於 <font color=\"red\">禁止區域</font> 而死亡。<font color=\"red\"><b>$host</b></font><BR>");}#死亡 (禁止區域)
	elsif($getkind eq "G-DATT")		{push (@log,"<LI>$hour時$min分，<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 小組 <font color=\"skyblue\"><b>【$host】</b></font> 脫離。<BR>");}#小組脫離
	elsif($getkind eq "G-JOIN")		{push (@log,"<LI>$hour時$min分，<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 小組 <font color=\"skyblue\"><b>【$host】</b></font> 結成。<BR>");}#小組結成
	elsif($getkind eq "G-KANYU")	{push (@log,"<LI>$hour時$min分，<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 小組 <font color=\"skyblue\"><b>【$host】</b></font> 加入。<BR>");}#小組加入
	elsif($getkind eq "HACK")		{push (@log,"<LI>$hour時$min分，<font color=\"orange\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font><font color=\"red\">Hacking\成\功\了</font><font color=\"red\">。<b>$host</b></font><BR>");}#HACK成功
	elsif($getkind eq "WINEND")		{#優勝者決定
		$log_num = pop @log;
		if ($log_num =~ /遊戲結束/){push (@log,$log_num);}
		else{push (@log,$log_num);push (@log,"<LI>$hour時$min分，<font color=\"lime\"><b>遊戲結束．以上本遊戲實施本部選手確認</B></font> <BR>") ;}
	} elsif ($getkind eq "EX_END")	{#遊戲停止
		$log_num = pop @log;
		if ($log_num =~ /遊戲結束/){push (@log,$log_num);}
		else{
			push (@log,$log_num);
			push (@log,"<LI>$hour時$min分，<font color=\"lime\"><b>遊戲結束．遊戲緊急關停</B></font> <BR>") ;
		}
	} elsif ($getkind eq "AREA")	{#禁止區域追加
		$log_num = pop @log;
		if ($w_cl ne ""){$wethe = "<font color=\"#CA9DE1\">【天氣：$weather[$w_cl]】</font>";}
		if (($log_num !~ /遊戲結束/)||($log_num !~ /<UL>/)){
			push (@log,$log_num);
			if    ($w_sex eq "0")	{push (@log,"<LI>00時00分，<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> 禁止區域被指定。下次禁止區域 <font color=\"lime\">08時 <b>$place[$ar[$w_f_name]]，</b>16時 <b>$place[$ar[$w_f_name+1]]，</b>00時 <b>$place[$ar[$w_f_name+2]]</b></font>。$wethe<BR>") ;}
			elsif ($w_sex eq "8")	{push (@log,"<LI>08時00分，<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> 禁止區域被指定。下次禁止區域 <font color=\"lime\">16時 <b>$place[$ar[$w_f_name]]，</b>00時 <b>$place[$ar[$w_f_name+1]]，</b>08時 <b>$place[$ar[$w_f_name+2]]</b></font>。$wethe<BR>") ;}
			elsif ($w_sex eq "16")	{push (@log,"<LI>16時00分，<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> 禁止區域被指定。下次禁止區域 <font color=\"lime\">00時 <b>$place[$ar[$w_f_name]]，</b>08時 <b>$place[$ar[$w_f_name+1]]，</b>16時 <b>$place[$ar[$w_f_name+2]]</b></font>。$wethe<BR>") ;}
			else {push (@log,"<LI>--時--分，<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> 禁止區域被指定。下次禁止區域 <font color=\"lime\">--時:<b>$place[$ar[$w_f_name]]，--時:$place[$ar[$w_f_name+1]]，--時:$place[$ar[$w_f_name+2]]</b></font>。$wethe<BR>") ;}
			if ($kinshiarea eq 0){$kinshiarea = $w_sex;}
		}else{push (@log,$log_num);}
	} elsif ($getkind eq "ENTRY")	{#新規登錄
		if ($Command ne "2Y") {$host = "";}
		push (@log,"<LI>$hour時$min分，<font color=\"yellow\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) </b></font> 轉校。<font color=\"black\">$host</font><BR>") ;
	} elsif ($getkind eq "NEWGAME") {push (@log,"<LI>$hour時$min分，新規狀態遊戲開始<font color=\"#CA9DE1\">【天氣：$weather[$w_f_name]】</font><BR>") ;}#管理員的數據初始化
	$cnt++;
}

for ($i=0; $i<$arealist[1]  ; $i++) {$ars = ($ars . " $place[$ar[$i]]") ;}

if	 ($hh eq "0")	{$ars = "<BR><font color=\"lime\"><B>現在的禁止區域</B></FONT> $ars<BR><font color=\"lime\"><B>下次的禁止區域</B></FONT> 00時: $place[$ar[$i]] 08時: $place[$ar[$i+1]] 16時: $place[$ar[$i+2]]";}
elsif($hh eq "8")	{$ars = "<BR><font color=\"lime\"><B>現在的禁止區域</B></FONT> $ars<BR><font color=\"lime\"><B>下次的禁止區域</B></FONT> 08時: $place[$ar[$i]] 16時: $place[$ar[$i+1]] 00時: $place[$ar[$i+2]]";}
elsif($hh eq "16")	{$ars = "<BR><font color=\"lime\"><B>現在的禁止區域</B></FONT> $ars<BR><font color=\"lime\"><B>下次的禁止區域</B></FONT> 16時: $place[$ar[$i]] 00時: $place[$ar[$i+1]] 08時: $place[$ar[$i+2]]";}

&HEADER ;
print "</center><font color=\"#FF0000\" face=\"Verdana\" size=\"6\"><span id=\"BR\" style=\"width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline\">進行狀況</span></font></center>";
print "<TABLE border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><TR><TD><img border=\"0\" src=\"img/i_sakamochi.jpg\" width=\"70\" height=\"70\"></TD><TD>『全體提起精神。<BR>以現在為止的狀況。<BR>今天要好好幹喔！』</TD></TR></TABLE>";
print "$ars";
print @log;
print "</UL><center><B><a href=\"index.htm\">HOME</A></B><BR>";

&FOOTER;
&UNLOCK;

exit;
