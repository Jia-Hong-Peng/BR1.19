#! /usr/bin/perl
$oldwinner = 0;		#過去優勝者表示 ON=1 OFF=0
$oldwinnerfile = "";#過去優勝者保存CGI檔案
#require"jcode.pl";
require"br.cgi";
require"$LIB_DIR/lib1.cgi";
&LOCK;
require"pref.cgi";
&DECODE;
&HEADER;
if ($mode eq "TOP"){&TOP;}
elsif ($mode eq "history"){&DISP;}
else {&TOP;}
&FOOTER;
&UNLOCK;
exit;
#==================#
# 表示部份		   #
#==================#
sub DISP{
if (($Command eq "WINNER")&&($oldwinner)){require"winner_old.cgi";}
else {

	require"$LIB_DIR/disp_sts.cgi";
	require"$LIB_DIR/disp_cmd.cgi";

	open(DB,"$win_file");seek(DB,0,0); @userlist=<DB>;close(DB);
	($WINNUM,$ver,$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,) = split(/,/, $userlist[$Command]);
	$Command = "閱覽";
	$sts = "優勝";
	&STS();
}
}
#==================#
# 處理      	   #
#==================#
sub TOP{
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">優勝者履歷</span></font></center>
<FORM METHOD="POST" name="BR">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="history">
<TABLE border="1" cellspacing="0" cellpadding="0">
<TR height="20"><TD class=\"b1\">&nbsp;</TD><TD class=\"b1\">回</TD><TD class=\"b1\">優勝者名</TD><TD class=\"b1\">Version</A></TD></TR>
_HERE_
&list;
print "</TABLE><BR><INPUT type=\"submit\" name=\"Enter\" value=\"觀看\"></FORM>";
}
#==================#
# ??處理    	   #
#==================#
sub list{
open(DB,"$win_file");seek(DB,0,0); @userlist=<DB>;close(DB);
for ($i=0; $i< ($#userlist + 1); $i++) {($WINNUM,$ver,$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/,$userlist[$i]);
	if($w_id ne "NOWINNER"){print "<TR height=\"20\">";&AS;print "<TD class=\"b2\"><INPUT type=\"radio\" name=\"Command\" value=\"$i\"></TD><TD class=\"b2\">第$WINNUM回</TD><TD class=\"b2\">-$w_f_name $w_l_name-</TD><TD class=\"b2\">$ver</TD></TR></A>";}
	else{print "<TR height=\"20\"><TD class=\"b3\">&nbsp;</TD><TD class=\"b3\">第$WINNUM回</TD><TD class=\"b3\">無記錄</TD><TD class=\"b3\">$ver</A></TD></TR>";}
}
print "<TR><TD colspan=\"4\" class=\"b3\"></TD></TR>";
if ($oldwinner) {print "<TR height=\"20\">";&AS;print "<TD class=\"b2\"><INPUT type=\"radio\" name=\"Command\" value=\"WINNER\"></TD><TD colspan=\"3\" class=\"b2\">&nbsp;☆★☆★☆★過去優勝者★☆★☆★☆</TD></TR></A>";}
}
