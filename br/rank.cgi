#! /usr/bin/perl
#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
require "pref.cgi";

	$ok = "0";
	$idou = "0";
	open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
	@tmp = map {(split /,/)[13]} @userlist;
	@kill = @userlist[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	@temp = map {(split /,/)[35]} @kill;
	@kil = @kill[sort {$temp[$b] <=> $temp[$a]} 0 .. $#temp];
	push(@log,"<center><font color=\"#FF0000\" face=\"Verdana\" size=\"6\"><span id=\"BR\" style=\"width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline\">�ͦs�̤@��</span></font></center>");
	push(@log,"<TABLE border=\"1\"><tr align=\"center\" class=\"b1\"><td width=\"100\" class=\"b1\">�W�r<br>�Z�ŵf��</td><td width=\"70\" class=\"b1\">�Y��</td><td class=\"b1\">����</td><td class=\"b1\">���`�̼�</td><td class=\"b1\">�p�զW</td><td width=\"300\" class=\"b1\">�N��y</td></tr>\n");
	foreach (@kil) {($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/,);
		if ($hackflg eq 0) {if (($w_hit > 0) && ($w_sts!~/NPC/)) {&DISPLAY;$rnk2++;$ok++;} else { $ng++; }}
		else {if ($w_hit > 0) {&DISPLAY;$rnk2++;$ok++;} else { $ng++; }}
		if (($w_sts eq "���`")&&($w_hit > 0)){$idou++;}
	}
	push(@log,"</table><BR>\n");
	push(@log,"�i�ͦs�̼ơG$ok�H�j�@�i�{�b���ʪ̼ơG$idou�H�j</table><BR><BR>\n");
	push(@log,"<B><a href=\"index.htm\">HOME</A></B><BR>\n");

	&HEADER ;
	print @log;
	&FOOTER;
&UNLOCK;
exit;

#=============#
# �� ��ܳ�   #
#=============#
sub DISPLAY {
push(@log,"<tr class=\"b3\"><td align=\"center\" class=\"b3\">$w_f_name $w_l_name<br>$w_cl $w_sex$w_no�f</td><td align=\"center\" class=\"b3\"><IMG src=\"$imgurl$icon_file[$w_icon]\" width=\"70\" height=\"70\" border=\"0\" align=\"absmiddle\"></td><td class=\"b3\">$w_level</td><td class=\"b3\">$w_kill</td><td class=\"b3\">$w_teamID</td><td class=\"b3\">$w_com</td></tr>\n");
}
