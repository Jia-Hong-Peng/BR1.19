#■□■□■□■□■□■□
#□　　　　　　　　　　■
#■　 ATTACK PROGRAM　 □
#□　　　　　　　　　　■
#■□■□■□■□■□■□
#		SUB 一覽
#================#
# ■ 戰鬥結果處理#
#================#
sub BATTLE {

#定義(LIB)
&definition;
#敵之定義
$w_phit = $w_hit / $w_mhit;
$att_filter="";
if	 ($w_phit <= 0){$w_phit = "<font color=\"red\">死亡</font>";$att_filter="style=\"filter:Xray()\""}
elsif($w_phit < 0.1){$w_phit = "<font color=\"red\">危險</font>";}
elsif($w_phit < 0.5){$w_phit = "<font color=\"yellow\">注意</font>";}
else {$w_phit = "<font color=\"#00FFFF\">通常</font>";}
($w_w_name,$w_w_kind) = split(/<>/, $w_wep);
if ($w_w_name =~ /☆/){$w_w_name = "<font color=\"yellow\">強化型武器</font>";}
elsif ($w_w_name =~ /★|β|㊣/){$w_w_name = "<font color=\"lime\">超級型武器</font>";}
elsif ($w_w_name =~ /■/){$w_w_name = "<font color=\"red\">終極型武器</font>";}
else {$w_w_name = "<font color=\"#00FFFF\">通常武器</font>";}
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
if (($teamID ne "無")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){print "轉讓</FONT></B></TD>";} else {print "戰鬥發生</FONT></B></TD>";}
print <<"_HERE_";
				<TR align="center"><TD width="100"><IMG src="$imgurl$icon_file[$icon]" width="70" height="70" border="0" align="middle"></TD><TD></TD><TD width="100"><IMG src="$imgurl$icon_file[$w_icon]" width="70" height="70" border="0" align="middle" $att_filter></TD></TR>
				<TR align="center">
				  <TD>$cl ($sex$no番) </TD><TD width="50" align="center">
_HERE_
if (($teamID eq "無")||($teamID eq "出席番號")){print "VS";}
print <<"_HERE_";
				  </TD><TD>$w_cl ($w_sex$w_no番) </TD>
				</TR>
				<TR align="center"><TD>$f_name $l_name</TD><TD><B>氏名</B></TD><TD>$w_f_name $w_l_name</TD></TR>
				<TR align="center"><TD>$bar_hit</TD><TD><B>體力</B></TD><TD>$w_phit</TD></TR>
				<TR align="center"><TD>$w_name</TD><TD><B>武器</B></TD><TD>$w_w_name</TD></TR>
			</TABLE>
			</TD>
		  </TR>
	  </TABLE>
	  </TD>
	  <TD valign="top" width="200">
	  <TABLE border="1" width="200" height="292" cellspacing="0" cellpadding="0">
		<TR height="1"><TD height="1" width="200" class="b1"><B>指令</B></TD></TR>
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
		  <TR height="1"><TD height="1" width="290" class="b1"><B>行動狀態</B></TD><TD height="1" width="260" class="b1"><B>對話記錄</B></TD></TR>
		  <TR>
			<TD valign="top" class="b3" width="290"><p style="text-align: left">$log</p></TD>
			<TD valign="top" class="b3" width="260"><p style="text-align: left">
_HERE_
$nomes =1;$mes_i = 0;
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
foreach (0 .. $#messagelist) {
	($from_id,$w_full_name,$to_id,$from_message,$mes_time) = split(/,/, $messagelist[$_]);
	if ($id eq $to_id) {#接收
		print "□$mes_time ($w_full_name) <BR>　<SPAN STYLE=\"background:$col_to\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($id eq $from_id) {#發送
		print "☆$mes_time (自己) <BR>　<SPAN STYLE=\"background:$col_from\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	} elsif ($to_id eq "ALL") {#All
		print "○$mes_time ($w_full_name) <BR>　<SPAN STYLE=\"background:$col_all\">『$from_message』</SPAN><BR>";
		$nomes =0;$mes_i ++;if ($mesmax <= $mes_i) {last;}
	}
}
if ($nomes) {print "沒有訊息。<br>";}

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
		  <TR height="1"><TD height="1" width="200" class="b1"><B>使者</B></TD></TR>
		  <TR><TD valign="top" class="b3"><form method="POST" formborder="0" framborder="0">　</TD></form>
		  </TR>
		</TABLE>
</TD></TR></TABLE>
_HERE_

$mflg="ON"; #表示
}
1;
