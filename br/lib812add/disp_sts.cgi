#==================#
# ■ 人物狀態    　#
#==================#
sub STS {
local($watt_2) = 0 ;
if (($sts =~ /睡眠|治療|靜養/)&&($Command eq "MAIN")&&($mode ne "main")) {
	$up = int(($now - $endtime) / (1*$kaifuku_time));
	if ($inf =~ /腹/){ $up = int($up / 2) ; }if ($ousen eq "治療專念"){ $up = int($up * 2) ; }
	if ($sts eq "睡眠") {
		$maxp = $maxsta - $sta ;		#最大值
		if ($up > $maxp) { $up = $maxp ; }
		$sta += $up ;
		if ($sta > $maxsta) { $sta = $maxsta ; }
		$log = ($log . "睡眠的結果，能量 $up 恢復了。<BR>") ;
		$sts = "懇橘"; $endtime = 0 ;
		&SAVE ;
	} elsif ($sts eq "治療") {
		if ($kaifuku_rate eq 0){$kaifuku_rate = 1;}
		$up = int($up / $kaifuku_rate) ;
		$maxp = $mhit - $hit ;  #最大值
		if ($up > $maxp) { $up = $maxp ; }
		$hit += $up ;
		if ($hit > $mhit) { $hit = $mhit ; }
		$log = ($log . "治療的結果，體力 $up 恢復了。<BR>") ;
		$sts = "正常"; $endtime = 0 ;
		&SAVE ;
	} elsif ($sts eq "靜養") {
		if ($kaifuku_rate eq 0){$kaifuku_rate = 1;}
		$ups = $up;
		$up = int($up / $kaifuku_rate) ;
		$maxp = $mhit - $hit ;  #最大值
		if ($up > $maxp) { $up = $maxp ; }
		$hit += $up ;
		if ($hit > $mhit) { $hit = $mhit ; }
		$maxp = $maxsta - $sta ;	#最大值
		if ($ups > $maxp) { $ups = $maxp ; }
		$sta += $ups ;
		if ($sta > $maxsta) { $sta = $maxsta ; }
		$log = ($log . "靜養的結果，體力 $up ，能量 $ups 恢復。<BR>") ;
		$sts = "正常"; $endtime = 0 ;
		&SAVE ;
	}
}
#定義(LIB)
&definition;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">$place[$pls] ($area[$pls])</span></font></center>
<TABLE width="755" border="0" cellspacing="0" collspacing="0">
<TR><TD><B><FONT color="#ff0000">@links</FONT></B></TD></TR>
</TABLE>
<TABLE width="757">
  <TR>
	<TD valign="top" width="550">
	  <TABLE border="1" width="550" height="292" cellspacing="0" cellpadding="0">
		<TR><TD width="70" colspan="1" class="b1"><B>LV. $level</B></TD>
			<TD width="215" colspan="3" class="b1"><B>$month月 $mday日 $week曜日 $hour:$min分</B></TD>
			<TD colspan="1" class="b1" width="39"><B>天氣</B></TD>
			<TD colspan="1" class="b3" width="86">$weather[$arealist[5]]</TD>
			<TD colspan="1" class="b1" width="62"><B>受傷部位</B></TD>
			<TD colspan="1" class="b3" width="63">$kega</TD></TR>
		<TR><TD ROWSPAN="4" height="1" class="b3"><IMG src="$imgurl$icon_file[$icon]" height="70" border="0" align="middle"></TD>
			<TD class="b2"><B>姓　名</B></TD>
			<TD colspan="2" class="b3">$full_name</TD>
			<TD ROWSPAN="4" height="1" class="b2"><B>狀　態</B>$condi</TD>
			<TD ROWSPAN="4" colspan="4" class="b3" height="70">$kegaimg $CONDITION</TD></TR>
		<TR><TD ROWSPAN="1" class="b2"><B>出席番號</B></TD>
			<TD ROWSPAN="1" colspan="2" class="b3">$cln</TD></TR>
		<TR><TD class="b2"><B>小　組</B></TD>
			<TD colspan="2" class="b3">$teamID</TD></TR>
		<TR><TD class="b2"><B>經驗值</B></TD>
			<TD colspan="2" class="b3"><a onmouseover="status='距離下次升級經驗值：$levuprem';return true;" onmouseout="status='';return true;" href="javascript:void(0)" title="距離下次升級經驗值：$levuprem"><font color="white">$exp\ / $up</font></a> <BR>$bar_exp\</TD></TR>
		<TR><TD class="b2"><B>攻擊力</B></TD>
			<TD class="b3">$att+$watt_2</TD>
			<TD class="b2"><B>能　量</B></TD>
			<TD class="b3">$sta / $maxsta</TD>
			<TD colspan="4" class="b3">$bar_sta</TD></TR>
		<TR><TD class="b2"><B>防禦力</B></TD>
			<TD class="b3">$def+$ball</TD>
			<TD class="b2"><B>體　力</B></TD>
			<TD class="b3">$hit / $mhit</TD>
			<TD colspan="4" class="b3">$bar_hit</TD></TR>
		<TR><TD class="b2"><B>武　器</B></TD>
			<TD colspan="3" class="b3">$w_name</TD>
			<TD colspan="2" class="b3">$watt</TD>
			<TD colspan="2" class="b3">$wtai</TD></TR>
		<TR><TD class="b2"><B>防　具</B></TD>
			<TD colspan="3" class="b3">$b_name</TD>
			<TD colspan="2" class="b3">$bdef</TD>
			<TD colspan="2" class="b3">$btai</TD></TR>
		<TR><TD class="b2"><B>基本方針</B></TD>
			<TD class="b3">$tactics</TD>
			<TD class="b2"><B>學　部</B></TD>
			<TD class="b3">$club</TD>
			<TD class="b2"><B>熟練值</B></TD>
			<TD colspan="3" class="b3">毆：$wp 鎗：$wg 劍：$ws 投：$wc 爆：$wd</TD></TR>
		<TR><TD class="b2"><B>應戰方針</B></TD>
			<TD class="b3">$ousen</TD>
			<TD class="b2"><B>委員會</B></TD>
			<TD class="b3">準備中</TD>
			<TD class="b2"><B>　</B></TD>
			<TD colspan="3" class="b3">　</TD></TR>
		<TR><TD class="b3" colspan="8" height="1" align="center">
<TABLE border="0" cellspacing="0" cellpadding="0"><TR><TD>
<TABLE border="1" cellspacing="0" cellpadding="0">
  <TR><TD class="b1" colspan="4">裝備</TD></TR>
  <TR><TD class="b2">種</TD><TD class="b2">名</TD><TD class="b2">效</TD><TD class="b2">耐</TD></TR>
  <TR><TD class="b3">頭</TD><TD class="b3">$b_name_h</TD><TD class="b3">$bdef_h</TD><TD class="b3">$btai_h</font></TD></TR>
  <TR><TD class="b3">腕</TD><TD class="b3">$b_name_a</TD><TD class="b3">$bdef_a</TD><TD class="b3">$btai_a</font></TD></TR>
  <TR><TD class="b3">足</TD><TD class="b3">$b_name_f</TD><TD class="b3">$bdef_f</TD><TD class="b3">$btai_f</font></TD></TR>
  <TR><TD class="b3">飾</TD><TD class="b3">$b_name_i</TD><TD class="b3">$eff[5]</TD><TD class="b3">$itai[5]</font></TD></TR>
</TABLE>
  </TD><TD width="20"></TD><TD>
<TABLE border="1" cellspacing="0" cellpadding="0">
  <TR><TD class="b1" colspan="4">所持品</TD></TR>
  <TR><TD class="b2">名</TD><TD class="b2">效</TD><TD class="b2">數</TD><TD class="b2">種</TD></TR>
_HERE_
for ($i=0; $i<5; $i++) {$itemtype = "";
	($i_name,$i_kind) = split(/<>/, $item[$i]);
	if ($i_kind =~ /HH|HD/) {$itemtype = "【體力回復】";}
	elsif ($i_kind =~ /SH|SD/) {$itemtype = "【能量回復】";}
	elsif ($i_kind eq TN) {$itemtype = "【陷阱】";}
	elsif ($i_kind =~ /W/) {$itemtype = "【武器";
		if ($i_kind =~ /G/)  {$itemtype = ($itemtype . "(鎗");
			if ($i_kind =~ /S/){$itemtype = ($itemtype . "-消音");}
			$itemtype = ($itemtype . ")");}
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
	print "<TR><TD class=\"b3\">$i_name</TD><TD class=\"b3\">$eff[$i]</TD><TD class=\"b3\">$itai[$i]</TD><TD class=\"b3\"><font color=\"00ffff\">$itemtype</font></TD></TR>";
}
print <<"_HERE_";
</TABLE>
</TD></TR></TABLE>
			</TD>
		  </TR>
	  </TABLE>
	  </TD>
	  <TD valign="top" width="200">
	  <TABLE border="1" width="200" height="292" cellspacing="0" cellpadding="0">
		<TR height="1"><TD height="1" width="200" class="b1"><B>指令</B></TD></TR>
		<TR>
		<TD align="left" valign="top" width="200" class="b3">
		<FORM METHOD="POST" name="BR" style="MARGIN: 0px">
		<INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
		<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
		<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
		<p style="text-align: left">
_HERE_
			&COMMAND;
print <<"_HERE_";
		</p>
		</FORM>
		</TD>
		</TR>
	  </TABLE>
	  </TD>
	</TR><TR>
	  <TD colspan="1" valign="top" height="150">
		<TABLE border="1" height="150" cellspacing="0" cellpadding="0">
		  <TR height="1"><TD height="1" width="290" class="b1"><B>行動狀態</B></TD><TD height="1" width="260" class="b1"><B>對話記錄</B></TD></TR>
		  <TR>
			<TD width="290" valign="top" class="b3"><p style="text-align: left">$log</p></TD>
			<TD width="260" valign="top" class="b3"><p style="text-align: left">
_HERE_
$nomes =1;$mes_i = 0;
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
foreach (0 .. $#messagelist) {
	($from_id,$w_full_name,$to_id,$from_message,$mes_time) = split(/,/, $messagelist[$_]);
	if ($id eq $to_id) {#受信
		print "□$mes_time ($w_full_name) <BR>　<SPAN STYLE=\"background:$col_to\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($id eq $from_id) {#送信
		print "☆$mes_time (自己) <BR>　<SPAN STYLE=\"background:$col_from\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($to_id eq "ALL") {#All
		print "○$mes_time ($w_full_name) <BR>　<SPAN STYLE=\"background:$col_all\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	}
}
if ($nomes) {print "沒有訊息。<br>";}

@new_memberlist =();$mem = "";$chk =1;
open(IN,"$memberfile");seek(IN,0,0); @memberlist=<IN>;close(IN);
foreach (0 .. $#memberlist) {
	($get_time,$mem_id,$mem_name) = split(/,/, $memberlist[$_]);
	if ($mem_id eq $id) {$new_memberlist[$_]="$now,$mem_id,$full_name,\n";$mem++;$chk=0;}#自分？
	elsif ($now-$mem_time <= $get_time) {unshift (@new_memberlist,"$get_time,$mem_id,$mem_name,\n");$mem++;}#Player
}
if ($chk) {unshift (@new_memberlist,"$now,$id,$full_name,\n");$mem++;}#如果自己沒在Data追加
open(OUT,">$memberfile"); seek(OUT,0,0); print OUT @new_memberlist; close(OUT);
print <<"_HERE_";
			</p></TD>
		  </TR>
		</TABLE>
	  </TD><TD colspan="1" valign="top" height="150">
		<TABLE border="1" cellspacing="0" height="150" cellpadding="0">
		  <TR height="1"><TD height="1" width="200" class="b1"><B>使者</B></TD></TR>
		  <TR><TD valign="top" class="b3">
			<form method="POST"  name="MSG" style="MARGIN: 0px">
_HERE_
if ($MESSENGER ne 1){print "　";}else{
print <<"_HERE_";
			訊息：<br><INPUT size="36" type="text" name="Mess" maxlength="19" ><BR>
			<input type="hidden" name="M_Id" value="ALL">
			<input type="hidden" name="mode" value="command">
			<input type="hidden" name="Command" value="SEVE">
			<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
			<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
			<input type="hidden" name="full_name" value="$full_name">
			<input type="submit" value="確定"><input type="reset" value="重寫"><BR>
			在線者：$mem人<BR>
_HERE_
	if (($teamID ne "無")||($teamID ne "")){
#	print "	對象：<A onclick=sl_msg(0); href=\"javascript:void(0);\"><INPUT type=\"radio\" name=\"Command2\" value=\"MSG_ALL\" checked>全員</A>";
#	print "　　　 <A onclick=sl_msg(1); href=\"javascript:void(0);\"><INPUT type=\"radio\" name=\"Command2\" value=\"MSG_GROUP\">小組</A><BR>";
	}
}
print <<"_HERE_";
		  </TD></form>
		  </TR>
		</TABLE>
</TD></TR></TABLE>
_HERE_
}
1;
