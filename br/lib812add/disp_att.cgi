#������������������������
#���@�@�@�@�@�@�@�@�@�@��
#���@ ATTACK PROGRAM�@ ��
#���@�@�@�@�@�@�@�@�@�@��
#������������������������
#		SUB �@��
#================#
# �� �԰����G�B�z#
#================#
sub BATTLE {

#�w�q(LIB)
&definition;
#�Ĥ��w�q
$w_phit = $w_hit / $w_mhit;
$att_filter="";
if	 ($w_phit <= 0){$w_phit = "<font color=\"red\">���`</font>";$att_filter="style=\"filter:Xray()\""}
elsif($w_phit < 0.1){$w_phit = "<font color=\"red\">�M�I</font>";}
elsif($w_phit < 0.5){$w_phit = "<font color=\"yellow\">�`�N</font>";}
else {$w_phit = "<font color=\"#00FFFF\">�q�`</font>";}
($w_w_name,$w_w_kind) = split(/<>/, $w_wep);
if ($w_w_name =~ /��/){$w_w_name = "<font color=\"yellow\">�j�ƫ��Z��</font>";}
elsif ($w_w_name =~ /��|�]|��/){$w_w_name = "<font color=\"lime\">�W�ū��Z��</font>";}
elsif ($w_w_name =~ /��/){$w_w_name = "<font color=\"red\">�׷����Z��</font>";}
else {$w_w_name = "<font color=\"#00FFFF\">�q�`�Z��</font>";}
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">$place[$pls] ($area[$pls])</span></font></center>
<TABLE width="755" border="0" cellspacing="0" collspacing="0">
<TR><TD><B><FONT color="#ff0000">@links</FONT></B></TD></TR>
</TABLE>
<TABLE width="757">
	<TR>
	<TD valign="top" width="550">
	  <TABLE border="1" width="550" height="292" cellspacing="0">
		  <TR align="center">
			<TD valign="top" class="b3">
			<TABLE border="0">
				<TR align="center">
				  <TD colspan="3"><B><FONT color="#ff0000" size="5" face="Verdana">
_HERE_
if (($teamID ne "�L")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){print "����</FONT></B></TD>";} else {print "�԰��o��</FONT></B></TD>";}
print <<"_HERE_";
				<TR align="center"><TD width="100"><IMG src="$imgurl$icon_file[$icon]" width="70" height="70" border="0" align="middle"></TD><TD></TD><TD width="100"><IMG src="$imgurl$icon_file[$w_icon]" width="70" height="70" border="0" align="middle" $att_filter></TD></TR>
				<TR align="center">
				  <TD>$cl ($sex$no�f) </TD><TD width="50" align="center">
_HERE_
if (($teamID eq "�L")||($teamID eq "�X�u�f��")){print "VS";}
print <<"_HERE_";
				  </TD><TD>$w_cl ($w_sex$w_no�f) </TD>
				</TR>
				<TR align="center"><TD>$f_name $l_name</TD><TD><B>��W</B></TD><TD>$w_f_name $w_l_name</TD></TR>
				<TR align="center"><TD>$bar_hit</TD><TD><B>��O</B></TD><TD>$w_phit</TD></TR>
				<TR align="center"><TD>$w_name</TD><TD><B>�Z��</B></TD><TD>$w_w_name</TD></TR>
			</TABLE>
			</TD>
		  </TR>
	  </TABLE>
	  </TD>
	  <TD valign="top" width="200">
	  <TABLE border="1" width="200" height="292" cellspacing="0" cellpadding="0">
		<TR height="1"><TD height="1" width="200" class="b1"><B>���O</B></TD></TR>
		<TR>
		<TD align="left" valign="top" height="260" width="200" class="b3">
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
			<TD valign="top" class="b3" width="290"><p style="text-align: left">$log</p></TD>
			<TD valign="top" class="b3" width="260"><p style="text-align: left">
_HERE_
$nomes =1;$mes_i = 0;
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
foreach (0 .. $#messagelist) {
	($from_id,$w_full_name,$to_id,$from_message,$mes_time) = split(/,/, $messagelist[$_]);
	if ($id eq $to_id) {#����
		print "��$mes_time ($w_full_name) <BR>�@<SPAN STYLE=\"background:$col_to\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($id eq $from_id) {#�o�e
		print "��$mes_time (�ۤv) <BR>�@<SPAN STYLE=\"background:$col_from\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($to_id eq "ALL") {#All
		print "��$mes_time ($w_full_name) <BR>�@<SPAN STYLE=\"background:$col_all\">�y$from_message�z</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	}
}
if ($nomes) {print "�S���T���C<br>";}

@new_memberlist =();$mem ="";$chk =1;
open(IN,"$memberfile");seek(IN,0,0); @memberlist=<IN>;close(IN);
foreach (0 .. $#memberlist) {
	($get_time,$mem_id,$mem_name) = split(/,/, $memberlist[$_]);
	if ($mem_id eq $id) {$new_memberlist[$_]="$now,$mem_id,$full_name,\n";$chk=0;}
	elsif ($now-$mem_time <= $get_time) {unshift (@new_memberlist,"$get_time,$mem_id,$mem_name,\n");$mem ="$mem_name-$mem";}
}
if ($chk) {unshift (@new_memberlist,"$now,$id,$full_name,\n");$mem ="-$mem";}
open(OUT,">$memberfile"); seek(OUT,0,0); print OUT @new_memberlist; close(OUT);
$mem ="-$mem";
print <<"_HERE_";
			</p></TD>
		  </TR>
		</TABLE>
	  </TD><TD colspan="1" valign="top" height="150">
		<TABLE border="1" cellspacing="0" height="150" cellpadding="0">
		  <TR height="1"><TD height="1" width="200" class="b1"><B>�Ϫ�</B></TD></TR>
		  <TR><TD valign="top" class="b3"><form method="POST" formborder="0" framborder="0">�@</TD></form>
		  </TR>
		</TABLE>
</TD></TR></TABLE>
_HERE_

$mflg="ON"; #���
}
1;
