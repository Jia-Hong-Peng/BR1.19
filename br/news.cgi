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
	$week = ('��','��','��','��','��','��','�g') [$wday];
	if (($getmonth != $month)||($getday != $mday)){
		if ($getmonth !=0){push (@log,"</LI></UL>");}
		$getmonth=$month;$getday = $mday;
		push (@log,"<P><font color=\"lime\"><B>$month�� $mday�� ($week�`��)</B></font><BR><UL>");
	}

	if (($host ne "")&&($getkind =~ /DEATH/)) { $host = "($host)"; }

	if	 ($getkind eq "DEATH")		{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> ���`�C<font color=\"red\"><b>$host</b></font><BR>") ;}#���` (�ۤ�����])
	elsif($getkind eq "DEATH1")		{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> ���`�C<font color=\"red\"><b>$host</b></font><BR>");}#���` (�r��)
	elsif($getkind eq "DEATH2")		{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �Q <font color=\"red\">$w_f_name2 $w_l_name2 ($w_cl2 $w_sex2$w_no2�f) </font> ���`�C<font color=\"red\"><b>$host</b></font><BR>");}#���` (�L��)
	elsif($getkind eq "DEATH3")		{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �Q <font color=\"red\">$w_f_name2 $w_l_name2 ($w_cl2 $w_sex2$w_no2�f) </font> ���`�C<font color=\"red\"><b>$host</b></font><BR>");}#���` (�L��)
	elsif($getkind eq "DEATH4")		{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �Q <font color=\"red\">�F��</font> �B�D���`�C<font color=\"red\"><b>$host</b></font><BR>");}#���`�]�F���^
	elsif($getkind eq "DEATHAREA")	{push (@log,"<LI>$hour��$min���A<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �]�B�� <font color=\"red\">�T��ϰ�</font> �Ӧ��`�C<font color=\"red\"><b>$host</b></font><BR>");}#���` (�T��ϰ�)
	elsif($getkind eq "G-DATT")		{push (@log,"<LI>$hour��$min���A<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �p�� <font color=\"skyblue\"><b>�i$host�j</b></font> �����C<BR>");}#�p�ղ���
	elsif($getkind eq "G-JOIN")		{push (@log,"<LI>$hour��$min���A<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �p�� <font color=\"skyblue\"><b>�i$host�j</b></font> �����C<BR>");}#�p�յ���
	elsif($getkind eq "G-KANYU")	{push (@log,"<LI>$hour��$min���A<font color=\"skyblue\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> �p�� <font color=\"skyblue\"><b>�i$host�j</b></font> �[�J�C<BR>");}#�p�ե[�J
	elsif($getkind eq "HACK")		{push (@log,"<LI>$hour��$min���A<font color=\"orange\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font><font color=\"red\">Hacking\��\�\\�F</font><font color=\"red\">�C<b>$host</b></font><BR>");}#HACK���\
	elsif($getkind eq "WINEND")		{#�u�Ӫ̨M�w
		$log_num = pop @log;
		if ($log_num =~ /�C������/){push (@log,$log_num);}
		else{push (@log,$log_num);push (@log,"<LI>$hour��$min���A<font color=\"lime\"><b>�C�������D�H�W���C����I�������T�{</B></font> <BR>") ;}
	} elsif ($getkind eq "EX_END")	{#�C������
		$log_num = pop @log;
		if ($log_num =~ /�C������/){push (@log,$log_num);}
		else{
			push (@log,$log_num);
			push (@log,"<LI>$hour��$min���A<font color=\"lime\"><b>�C�������D�C���������</B></font> <BR>") ;
		}
	} elsif ($getkind eq "AREA")	{#�T��ϰ�l�[
		$log_num = pop @log;
		if ($w_cl ne ""){$wethe = "<font color=\"#CA9DE1\">�i�Ѯ�G$weather[$w_cl]�j</font>";}
		if (($log_num !~ /�C������/)||($log_num !~ /<UL>/)){
			push (@log,$log_num);
			if    ($w_sex eq "0")	{push (@log,"<LI>00��00���A<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> �T��ϰ�Q���w�C�U���T��ϰ� <font color=\"lime\">08�� <b>$place[$ar[$w_f_name]]�A</b>16�� <b>$place[$ar[$w_f_name+1]]�A</b>00�� <b>$place[$ar[$w_f_name+2]]</b></font>�C$wethe<BR>") ;}
			elsif ($w_sex eq "8")	{push (@log,"<LI>08��00���A<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> �T��ϰ�Q���w�C�U���T��ϰ� <font color=\"lime\">16�� <b>$place[$ar[$w_f_name]]�A</b>00�� <b>$place[$ar[$w_f_name+1]]�A</b>08�� <b>$place[$ar[$w_f_name+2]]</b></font>�C$wethe<BR>") ;}
			elsif ($w_sex eq "16")	{push (@log,"<LI>16��00���A<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> �T��ϰ�Q���w�C�U���T��ϰ� <font color=\"lime\">00�� <b>$place[$ar[$w_f_name]]�A</b>08�� <b>$place[$ar[$w_f_name+1]]�A</b>16�� <b>$place[$ar[$w_f_name+2]]</b></font>�C$wethe<BR>") ;}
			else {push (@log,"<LI>--��--���A<font color=\"lime\"><b>$place[$ar[$w_l_name]]</b></font> �T��ϰ�Q���w�C�U���T��ϰ� <font color=\"lime\">--��:<b>$place[$ar[$w_f_name]]�A--��:$place[$ar[$w_f_name+1]]�A--��:$place[$ar[$w_f_name+2]]</b></font>�C$wethe<BR>") ;}
			if ($kinshiarea eq 0){$kinshiarea = $w_sex;}
		}else{push (@log,$log_num);}
	} elsif ($getkind eq "ENTRY")	{#�s�W�n��
		if ($Command ne "2Y") {$host = "";}
		push (@log,"<LI>$hour��$min���A<font color=\"yellow\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) </b></font> ��աC<font color=\"black\">$host</font><BR>") ;
	} elsif ($getkind eq "NEWGAME") {push (@log,"<LI>$hour��$min���A�s�W���A�C���}�l<font color=\"#CA9DE1\">�i�Ѯ�G$weather[$w_f_name]�j</font><BR>") ;}#�޲z�����ƾڪ�l��
	$cnt++;
}

for ($i=0; $i<$arealist[1]  ; $i++) {$ars = ($ars . " $place[$ar[$i]]") ;}

if	 ($hh eq "0")	{$ars = "<BR><font color=\"lime\"><B>�{�b���T��ϰ�</B></FONT> $ars<BR><font color=\"lime\"><B>�U�����T��ϰ�</B></FONT> 00��: $place[$ar[$i]] 08��: $place[$ar[$i+1]] 16��: $place[$ar[$i+2]]";}
elsif($hh eq "8")	{$ars = "<BR><font color=\"lime\"><B>�{�b���T��ϰ�</B></FONT> $ars<BR><font color=\"lime\"><B>�U�����T��ϰ�</B></FONT> 08��: $place[$ar[$i]] 16��: $place[$ar[$i+1]] 00��: $place[$ar[$i+2]]";}
elsif($hh eq "16")	{$ars = "<BR><font color=\"lime\"><B>�{�b���T��ϰ�</B></FONT> $ars<BR><font color=\"lime\"><B>�U�����T��ϰ�</B></FONT> 16��: $place[$ar[$i]] 00��: $place[$ar[$i+1]] 08��: $place[$ar[$i+2]]";}

&HEADER ;
print "</center><font color=\"#FF0000\" face=\"Verdana\" size=\"6\"><span id=\"BR\" style=\"width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline\">�i�檬�p</span></font></center>";
print "<TABLE border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><TR><TD><img border=\"0\" src=\"img/i_sakamochi.jpg\" width=\"70\" height=\"70\"></TD><TD>�y���鴣�_�믫�C<BR>�H�{�b������p�C<BR>���ѭn�n�n�F��I�z</TD></TR></TABLE>";
print "$ars";
print @log;
print "</UL><center><B><a href=\"index.htm\">HOME</A></B><BR>";

&FOOTER;
&UNLOCK;

exit;
