#==================#
# �� �H�����A    �@#
#==================#
sub STS {
local($watt_2) = 0 ;
if (($sts =~ /�ίv|�v��|�R�i/)&&($Command eq "MAIN")&&($mode ne "main")) {
	$up = int(($now - $endtime) / (1*$kaifuku_time));
	if ($inf =~ /��/){ $up = int($up / 2) ; }if ($ousen eq "�v���M��"){ $up = int($up * 2) ; }
	if ($sts eq "�ίv") {
		$maxp = $maxsta - $sta ;		#�̤j��
		if ($up > $maxp) { $up = $maxp ; }
		$sta += $up ;
		if ($sta > $maxsta) { $sta = $maxsta ; }
		$log = ($log . "�ίv�����G�A��q $up ��_�F�C<BR>") ;
		$sts = "����"; $endtime = 0 ;
		&SAVE ;
	} elsif ($sts eq "�v��") {
		if ($kaifuku_rate eq 0){$kaifuku_rate = 1;}
		$up = int($up / $kaifuku_rate) ;
		$maxp = $mhit - $hit ;  #�̤j��
		if ($up > $maxp) { $up = $maxp ; }
		$hit += $up ;
		if ($hit > $mhit) { $hit = $mhit ; }
		$log = ($log . "�v�������G�A��O $up ��_�F�C<BR>") ;
		$sts = "���`"; $endtime = 0 ;
		&SAVE ;
	} elsif ($sts eq "�R�i") {
		if ($kaifuku_rate eq 0){$kaifuku_rate = 1;}
		$ups = $up;
		$up = int($up / $kaifuku_rate) ;
		$maxp = $mhit - $hit ;  #�̤j��
		if ($up > $maxp) { $up = $maxp ; }
		$hit += $up ;
		if ($hit > $mhit) { $hit = $mhit ; }
		$maxp = $maxsta - $sta ;	#�̤j��
		if ($ups > $maxp) { $ups = $maxp ; }
		$sta += $ups ;
		if ($sta > $maxsta) { $sta = $maxsta ; }
		$log = ($log . "�R�i�����G�A��O $up �A��q $ups ��_�C<BR>") ;
		$sts = "���`"; $endtime = 0 ;
		&SAVE ;
	}
}
#�w�q(LIB)
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
			<TD width="215" colspan="3" class="b1"><B>$month�� $mday�� $week�`�� $hour:$min��</B></TD>
			<TD colspan="1" class="b1" width="39"><B>�Ѯ�</B></TD>
			<TD colspan="1" class="b3" width="86">$weather[$arealist[5]]</TD>
			<TD colspan="1" class="b1" width="62"><B>���˳���</B></TD>
			<TD colspan="1" class="b3" width="63">$kega</TD></TR>
		<TR><TD ROWSPAN="4" height="1" class="b3"><IMG src="$imgurl$icon_file[$icon]" height="70" border="0" align="middle"></TD>
			<TD class="b2"><B>�m�@�W</B></TD>
			<TD colspan="2" class="b3">$full_name</TD>
			<TD ROWSPAN="4" height="1" class="b2"><B>���@�A</B>$condi</TD>
			<TD ROWSPAN="4" colspan="4" class="b3" height="70">$kegaimg $CONDITION</TD></TR>
		<TR><TD ROWSPAN="1" class="b2"><B>�X�u�f��</B></TD>
			<TD ROWSPAN="1" colspan="2" class="b3">$cln</TD></TR>
		<TR><TD class="b2"><B>�p�@��</B></TD>
			<TD colspan="2" class="b3">$teamID</TD></TR>
		<TR><TD class="b2"><B>�g���</B></TD>
			<TD colspan="2" class="b3"><a onmouseover="status='�Z���U���ɯŸg��ȡG$levuprem';return true;" onmouseout="status='';return true;" href="javascript:void(0)" title="�Z���U���ɯŸg��ȡG$levuprem"><font color="white">$exp\ / $up</font></a> <BR>$bar_exp\</TD></TR>
		<TR><TD class="b2"><B>�����O</B></TD>
			<TD class="b3">$att+$watt_2</TD>
			<TD class="b2"><B>��@�q</B></TD>
			<TD class="b3">$sta / $maxsta</TD>
			<TD colspan="4" class="b3">$bar_sta</TD></TR>
		<TR><TD class="b2"><B>���m�O</B></TD>
			<TD class="b3">$def+$ball</TD>
			<TD class="b2"><B>��@�O</B></TD>
			<TD class="b3">$hit / $mhit</TD>
			<TD colspan="4" class="b3">$bar_hit</TD></TR>
		<TR><TD class="b2"><B>�Z�@��</B></TD>
			<TD colspan="3" class="b3">$w_name</TD>
			<TD colspan="2" class="b3">$watt</TD>
			<TD colspan="2" class="b3">$wtai</TD></TR>
		<TR><TD class="b2"><B>���@��</B></TD>
			<TD colspan="3" class="b3">$b_name</TD>
			<TD colspan="2" class="b3">$bdef</TD>
			<TD colspan="2" class="b3">$btai</TD></TR>
		<TR><TD class="b2"><B>�򥻤�w</B></TD>
			<TD class="b3">$tactics</TD>
			<TD class="b2"><B>�ǡ@��</B></TD>
			<TD class="b3">$club</TD>
			<TD class="b2"><B>���m��</B></TD>
			<TD colspan="3" class="b3">�ޡG$wp ��G$wg �C�G$ws ��G$wc �z�G$wd</TD></TR>
		<TR><TD class="b2"><B>���Ԥ�w</B></TD>
			<TD class="b3">$ousen</TD>
			<TD class="b2"><B>�e���|</B></TD>
			<TD class="b3">�ǳƤ�</TD>
			<TD class="b2"><B>�@</B></TD>
			<TD colspan="3" class="b3">�@</TD></TR>
		<TR><TD class="b3" colspan="8" height="1" align="center">
<TABLE border="0" cellspacing="0" cellpadding="0"><TR><TD>
<TABLE border="1" cellspacing="0" cellpadding="0">
  <TR><TD class="b1" colspan="4">�˳�</TD></TR>
  <TR><TD class="b2">��</TD><TD class="b2">�W</TD><TD class="b2">��</TD><TD class="b2">�@</TD></TR>
  <TR><TD class="b3">�Y</TD><TD class="b3">$b_name_h</TD><TD class="b3">$bdef_h</TD><TD class="b3">$btai_h</font></TD></TR>
  <TR><TD class="b3">��</TD><TD class="b3">$b_name_a</TD><TD class="b3">$bdef_a</TD><TD class="b3">$btai_a</font></TD></TR>
  <TR><TD class="b3">��</TD><TD class="b3">$b_name_f</TD><TD class="b3">$bdef_f</TD><TD class="b3">$btai_f</font></TD></TR>
  <TR><TD class="b3">��</TD><TD class="b3">$b_name_i</TD><TD class="b3">$eff[5]</TD><TD class="b3">$itai[5]</font></TD></TR>
</TABLE>
  </TD><TD width="20"></TD><TD>
<TABLE border="1" cellspacing="0" cellpadding="0">
  <TR><TD class="b1" colspan="4">�ҫ��~</TD></TR>
  <TR><TD class="b2">�W</TD><TD class="b2">��</TD><TD class="b2">��</TD><TD class="b2">��</TD></TR>
_HERE_
for ($i=0; $i<5; $i++) {$itemtype = "";
	($i_name,$i_kind) = split(/<>/, $item[$i]);
	if ($i_kind =~ /HH|HD/) {$itemtype = "�i��O�^�_�j";}
	elsif ($i_kind =~ /SH|SD/) {$itemtype = "�i��q�^�_�j";}
	elsif ($i_kind eq TN) {$itemtype = "�i�����j";}
	elsif ($i_kind =~ /W/) {$itemtype = "�i�Z��";
		if ($i_kind =~ /G/)  {$itemtype = ($itemtype . "(��");
			if ($i_kind =~ /S/){$itemtype = ($itemtype . "-����");}
			$itemtype = ($itemtype . ")");}
		if ($i_kind =~ /K/)  {$itemtype = ($itemtype . "(�C)");}
		if ($i_kind =~ /C/)  {$itemtype = ($itemtype . "(��)");}
		if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(��)");}
		if ($i_kind =~ /D/)  {$itemtype = ($itemtype . "(�z)");}
		$itemtype = ($itemtype . "�j");}
	elsif ($i_kind =~ /D/)  {$itemtype = "�i����";
		if ($i_kind =~ /B/)  {$itemtype = ($itemtype . "(��)");}
		if ($i_kind =~ /H/)  {$itemtype = ($itemtype . "(�Y)");}
		if ($i_kind =~ /F/)  {$itemtype = ($itemtype . "(��)");}
		if ($i_kind =~ /A/)  {$itemtype = ($itemtype . "(��)");}
		$itemtype = ($itemtype . "�j");}
	elsif (($i_kind eq R1)||($i_kind eq R2)) {$itemtype = "�i�p�F�j";}
	elsif ($i_kind eq Y) {
		if (($i_name eq "���C���Ѱ��_��")||($i_name eq "�C���Ѱ��_��")) {$itemtype = "�i�Ѱ��_�͡j";}
		elsif ($i_name eq "�i�l�u�j") {$itemtype = "�i�u�j";}
		else {$itemtype = "�i�D��j";}}
	elsif ($i_kind eq A) {$itemtype = "�i�˹��~�j";}
	elsif ($item[$i] eq "�L") {$itemtype = "�i�L�j";}
	else {$itemtype = "�i�����j";}
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
		<TR height="1"><TD height="1" width="200" class="b1"><B>���O</B></TD></TR>
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
		  <TR height="1"><TD height="1" width="290" class="b1"><B>��ʪ��A</B></TD><TD height="1" width="260" class="b1"><B>��ܰO��</B></TD></TR>
		  <TR>
			<TD width="290" valign="top" class="b3"><p style="text-align: left">$log</p></TD>
			<TD width="260" valign="top" class="b3"><p style="text-align: left">
_HERE_
$nomes =1;$mes_i = 0;
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
foreach (0 .. $#messagelist) {
	($from_id,$w_full_name,$to_id,$from_message,$mes_time) = split(/,/, $messagelist[$_]);
	if ($id eq $to_id) {#���H
		print "��$mes_time ($w_full_name) <BR>�@<SPAN STYLE=\"background:$col_to\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($id eq $from_id) {#�e�H
		print "��$mes_time (�ۤv) <BR>�@<SPAN STYLE=\"background:$col_from\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($to_id eq "ALL") {#All
		print "��$mes_time ($w_full_name) <BR>�@<SPAN STYLE=\"background:$col_all\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	}
}
if ($nomes) {print "�S���T���C<br>";}

@new_memberlist =();$mem = "";$chk =1;
open(IN,"$memberfile");seek(IN,0,0); @memberlist=<IN>;close(IN);
foreach (0 .. $#memberlist) {
	($get_time,$mem_id,$mem_name) = split(/,/, $memberlist[$_]);
	if ($mem_id eq $id) {$new_memberlist[$_]="$now,$mem_id,$full_name,\n";$mem++;$chk=0;}#�ۤ��H
	elsif ($now-$mem_time <= $get_time) {unshift (@new_memberlist,"$get_time,$mem_id,$mem_name,\n");$mem++;}#Player
}
if ($chk) {unshift (@new_memberlist,"$now,$id,$full_name,\n");$mem++;}#�p�G�ۤv�S�bData�l�[
open(OUT,">$memberfile"); seek(OUT,0,0); print OUT @new_memberlist; close(OUT);
print <<"_HERE_";
			</p></TD>
		  </TR>
		</TABLE>
	  </TD><TD colspan="1" valign="top" height="150">
		<TABLE border="1" cellspacing="0" height="150" cellpadding="0">
		  <TR height="1"><TD height="1" width="200" class="b1"><B>�Ϫ�</B></TD></TR>
		  <TR><TD valign="top" class="b3">
			<form method="POST"  name="MSG" style="MARGIN: 0px">
_HERE_
if ($MESSENGER ne 1){print "�@";}else{
print <<"_HERE_";
			�T���G<br><INPUT size="36" type="text" name="Mess" maxlength="19" ><BR>
			<input type="hidden" name="M_Id" value="ALL">
			<input type="hidden" name="mode" value="command">
			<input type="hidden" name="Command" value="SEVE">
			<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
			<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
			<input type="hidden" name="full_name" value="$full_name">
			<input type="submit" value="�T�w"><input type="reset" value="���g"><BR>
			�b�u�̡G$mem�H<BR>
_HERE_
	if (($teamID ne "�L")||($teamID ne "")){
#	print "	��H�G<A onclick=sl_msg(0); href=\"javascript:void(0);\"><INPUT type=\"radio\" name=\"Command2\" value=\"MSG_ALL\" checked>����</A>";
#	print "�@�@�@ <A onclick=sl_msg(1); href=\"javascript:void(0);\"><INPUT type=\"radio\" name=\"Command2\" value=\"MSG_GROUP\">�p��</A><BR>";
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
