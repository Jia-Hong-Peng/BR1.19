#��������������������������������
#��      �@�@�@�@�@�@�@�@�@�@�@��
#���@DISP. ENDING & READER�@�@ ��
#���@�@�@�@�@�@�@�@�@�@�@�@�@�@��
#��������������������������������
#===================#
# �� �u�ӳB�z		#
#===================#
sub ENDING {
open(FLAG,$end_flag_file) || exit; $fl=<FLAG>; close(FLAG);

if ($inf =~ /��/){&ENDING2;}
elsif ($inf =~ /��/){&EX_ENDING2;}
elsif ($fl =~ /�Ѱ�/){&EX_ENDING;}
elsif(($mem == 1)&&($fl =~ /�פF/)){&ENDING2;}
else{ &ERROR("������X�ݡC"); }

}

#======================#
#�@�@�@�@Footer�@�@�@�@#
#======================#
sub END_FOOT{

print <<"_HERE_";

<CENTER>
�s�@�`����<BR><BR>
tanatos<BR><BR>
Special Thanks<BR><BR>
�����a�M��(<a href="http://www.geocities.co.jp/Bookend/5696/index.html">�AŪ</A>)<BR><BR>
�߽���(<a href="http://www01.u-page.so-net.ne.jp/zb3/t-c/TC.html">�ߤ��v</A>)<BR><BR>
������(<a href="http://homepage1.nifty.com/kurage-ya/">�����E</A>)<BR><BR>
<BR>
<A href="index.htm"><B><FONT color="#ff0000" size="+2">��^</FONT></B></A><BR></P>
</CENTER>

_HERE_

&FOOTER;
&UNLOCK;
exit ;
}

#==================#
# �@ �q�`Ending �@ #
#==================#
sub ENDING2{

	&HEADER;

print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">�u�Ӫ̨M�w</FONT></B><BR><BR>

<CENTER>
��M�s�����T�_�F�A�M��j�a�F�Ȧ@�M�ꪺ��q�ǥX�F�C<BR>
�M��Ať���F�@����x���n���C<BR>
<BR>
�u���߮��ߡC�ש󲣥��u�Ӫ̡C�Ѯv�u�����A��o�a�x�Ӱ�����C<BR>
�ﱵ�A���ӧQ�a�I���W�A�F�C�v<BR>
<BR>
�{�b�A����I�l���H�ڬO�̫᪺�@�H�ܡH<BR>
�b�o�b��ť�۷s���̪��s���C<BR>
�u���O���˶ܡH<BR>
�j���A�o�ӭp���n���O�ڦ����F�����H�R���y�m�����A�ֹ�H�C<BR>
�i�O�Ať��o�Ӽs����A��i���N�Ѷ}�l�����F�C<BR>
�N�Ѷ}�l�a�g�C�C�C<BR>
�j���A�]���Ƥ駹���S�ΡC�C�C<BR>
�D<BR>
�D<BR>
�D<BR>
���e���ӦP�Z�n�͡C<BR>
�u�A�O�Q�������٬O�Q���Q�����H�H�v<BR>
�^�Y�V��ݡA�oı�ﺡ�F�P�Z�P�Ǫ�����C<BR>
�u�ݨ��F�a�I�j�a���Q���F�A�{�b�u�ѤU�A�M�ڡI�v<BR>
���}�n�ͮ��ۤM�l�V�ۧڽĹL�ӡC<BR>
�u�����a�I�v<BR>
<BR>
�i�O...����������A�ڪ��M�l���F�L������A�n�͵o�X�h�W���n���C<BR>
�M��A�|�P�^�_�F���R�A�a�W���O�A��...<BR>
�u�ڤ��Q�o�˰����A�j�a���O�B�͡I�@�ڥu�Q��...�u�Q���U�h...�v<BR>
�D<BR>
�D<BR>
�D<BR>
���骺�����A�O�ڿ��ӡC<BR>
�@�W�x�H�b�ڨ��ǡC�ӧڦn�����B�b�@���}�������C<BR>
�x�H���W����m�۱m�⪺�ȡC<BR>
�W���g�ۡy�u�ӡA���߮��ߡI-- �@�M���`�� --�z�C<BR>
<BR>
���M�A�}���������}�F�C<BR>
���ɭ��H�ΰ{���O���{���������]��ۧڡC<BR>
�L�̮��۳��J���V�ڶ]�L�ӡC<BR>
�u..�A�n..�ڬOxx�q���x��...�s�D���ɭ�...�C<BR>
�����ӧQ�̡A����P�Q�O�H�v<BR>
<BR>
�ڨS���z�|���ǦV�ڳX�ݪ��H�C<BR>
���L�ت��a���ۡA�����@���ťաA���ܧ��W�F�t�@�����C<BR><BR>
�o�@��A�ڵL�k�T�w�ҵo�ͪ��ơC<BR>
�o�O�@�ӹC���H�ڪ��P�Z�n�ͯu���û������F�H<BR>
�Ϊ̳o�u�O�@�ӹ�...�ڧƱ榭�I���ӡC<BR><BR>
�u$sex$no�f $f_name$l_name�v<BR>
�u�U�@���A�٭n�ѥ[�ܡH�o�Ӱ�a�p���ٷ|���_�i��...��..���v<BR>
���Y�ݡA�~�o�{�o�ӧN�媺�x�x�]�b���ǡC<BR>
�ӥB�S�X�u�񪺯��e�C<BR>
�o�ӮɭԨ��l�w���W���A�}�ʤF�C<BR>
�u�ڲ{�b�n�h���̡H�v<BR>
�Ϊ̡A�o�ӹڤ��|�����A�@���o�۳o�Ӵc��...<BR>
<BR>
<BR>
<BR>
<BR>
<DIV align="right">
Now,"1 student remaining"�D<BR>
Surely 1 is lonly.<BR>
But there is hope there.<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;

}

#==========================#
#�@�@�@�{�ǸѰ�Ending�@�@�@#
#==========================#
sub EX_ENDING {
	&HEADER;

print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">�C����氱��</FONT></B><BR><BR>

<CENTER>
��M�p�p�e�ժ��T���n�T�_�C<br>
�a�x�O�M�w�F���K�H�@�A�T���٥ͦs���P�����Ӧb�K�C<br>
���˷Q���ܡA�ܦn�a�ռ����P�Ǫ��n�������T�M�C<br>
�u�{�ǵ����F�I�w�g���@�Ԥ]�i�H!!�v<br>
<br>
�L�k�۫H�C<br>
�q�o�Ӵc�]���C����k�X�C���O�A�ڭ̱q�{�b�_���ӫ�˰��~�n�H<br>
�@�_�^�h��a�F���H<br>
�٬O�M�ռM�հk�]�A�U�۳��~���H<br>
���ޫ�˧������Ҽ{��^�a�H<br>
�S���Ҽ{���ŷv�C�T��ϰ쪺�Ѱ��|�b���]��0:00�^�_���ӡC<br>
�ӥB�A�p�G���ӹC�������`�i��{�ǡA�L�h�|�ӳB�D�ڭ̧a�C<br>
�u�K�K�K�v<br>
�����U���b�V�W������C<br>
�Q��o�̡A�`�`�a�I�l�ۡK�K<br>
<br>
���ަp����q�o�̰k�X�C<br>
�H�᪺�ƦA�C�C�Ҽ{�]����C<br>
�ڭ��٦��y�Ʊ�z�C���V�o�Ӵc�]���C���A�@�����c�k���y�Ʊ�z<br>
�����w�q���椤���ͪ��Ʊ�A�i�H�J�A�x���I<br>
���_�V�e�]�K�K�I���ܭˤU�I<br>
<br>
<br>
�u�C����氱���A�q�|���k�X���֦~�̵̨M�K�K�v<br>
�K�K�@�W�֦~����ۦb���Y�å����̪��{�ɷs�D�C<br>
�r��L�B�A�����Y�A�{�u�����C<br>
�u�]�a�K�I��F�o�Ӧa�B�I�v<br>
<br>
<br>
<BR>
<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;
}

#==============================#
#�@�Ѱ��_�ͨϥΪ̱M��Ending�@�@#
#==============================#
sub EX_ENDING2 {
&HEADER;
print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">�C����氱��</FONT></B><BR><BR>

<CENTER>
<br>
�u�ӡK�ӡK�K�v<br>
����ѱשY�U�u�체�e�C<br>
�d����A��A�o�{�@�˹��q�l�_�ͪ��F��C<br>
�p�G�ϥγo�ӡK�ۤv�M�j�a�N���~��ͦs�A�C���]�Q�Ѷ}�K�C<br>
�u�K�K�K�v<br>
���O�A(�g�b)<br>
�O�o�˪��ܯu���O�n�ƶܡH��q��a�F�����U�k��ܡH<br>
�@�K���˪����٬O�H��~�Ҽ{�C<br>
���ޫ�ˡA�p�G���M���³J���P�Ǥ��ۼr���U�h�K�C<br>
<br>
�C���������q�l�n���T�_�A����o�X(�d��)���n�����U��a�O�C<br>
�åB�A��W���ۤ������ŧi�ۦh�֤H�ΦP�Ǧ��`���i�����J���A�`�`�I�l�C<br>
�u�{�ǵ����F�I�w�g���@�Ԥ]�i�H!!�v<br>
<br>
�ۤv�వ���ư��F�C<br>
�H��j�a�U�ۦҼ{�p��ͦs���ƴN��F�C<br>
�b�o�˪��a��򥻰�����Ƥ]�S���ΡC<br>
�q�{�b�_�ۤv�~��M�w�ۤv�H�᪺�ơK�C<br>
<br>
�u�C����氱���A���åǪ��ǥ̵ͨM�K�K�v<br>
�K�K�@�W�֦~����ۦb���Y�å����̪��{�ɷs�D�C<br>
�L���B�X���e�A�ⴡ�ۤf�U�C<br>
�u�V�O�a�K�ֳ����U���F�A�K�v<br>
<BR>
<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;
}
#===================#
# �� �p�F��ܳ� 	#
#===================#
sub READER {

if ($item[$wk] !~ /R/) {&ERROR("�������X�ݡC") ;}

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$area_file");seek(DB,0,0); @arealist=<DB>;close(DB);

($ar,$hackflg,$a) = split(/,/, $arealist[1]);
@ara = split(/,/, $arealist[4]);

for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	for ($j=0; $j<$#area+1; $j++) {
		if (($w_pls eq $j)&&($w_hit > 0)) {$mem[$j] += 1;last;}
	}
}

if ($item[$wk] =~ /<>R2/) {
	for ($j=0; $j<$#area+1; $j++) {
		if ($j eq $pls) {$wk = $mem[$j];$mem[$j] = "<FONT color=\"#ff0000\"><b>$wk<b></FONT>";}
		elsif ($mem[$j] <= 0) {$mem[$j] = "�@" ;}
	}
} else {
	for ($j=0; $j<$#area+1; $j++) {
		if ($j eq $pls) {$wk = $mem[$j];$mem[$j] = "<FONT color=\"#ff0000\"><b>$wk<b></FONT>";}
		else {$mem[$j] = "�@" ;}
	}
}

if ($hackflg eq 0) {for ($j=0; $j<$ar; $j++) {$mem[$ara[$j]] = "<FONT color=\"#ff0000\"><b>��<b></FONT>";}}


print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="Verdana">$place[$pls]��$area[$pls]��</FONT></B><BR></P>
<TABLE width="568">
<TR><TD><B><FONT color="#ff0000">@links</FONT></B></TD></TR>
</TABLE>
<TABLE width="568">
  <TBODY>
	<TR>
	  <TD valign="top" width="279" height="311">
	<TABLE border="1" width="389" height="300">
		<TBODY align="center" valign="middle">
		  <TR>
			<TD>�@</TD>
			<TD>01</TD>
			<TD>02</TD>
			<TD>03</TD>
			<TD>04</TD>
			<TD>05</TD>
			<TD>06</TD>
			<TD>07</TD>
			<TD>08</TD>
			<TD>09</TD>
			<TD>10</TD>
		  </TR>
		  <TR>
			<TD>A</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>$mem[1]</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>B</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>$mem[2]</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>C</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>$mem[3]</TD>
			<TD>$mem[4]</TD>
			<TD>$mem[5]</TD>
			<TD>$mem[6]</TD>
			<TD>�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>D</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>$mem[7]</TD>
			<TD>�@</TD>
			<TD>$mem[0]</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>E</TD>
			<TD>�@</TD>
			<TD>$mem[8]</TD>
			<TD>�@</TD>
			<TD>$mem[9]</TD>
			<TD>$mem[10]</TD>
			<TD>�@</TD>
			<TD>$mem[11]</TD>
			<TD>�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>F</TD>
			<TD>�@</TD>
			<TD>$mem[12]</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>$mem[13]</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>G</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>$mem[14]</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>$mem[15]</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>H</TD>
			<TD bgcolor="#00ffff">�@</TD>
				<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>$mem[16]</TD>
			<TD>�@</TD>
			<TD>$mem[17]</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		  <TR>
			<TD>I</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>�@</TD>
			<TD>$mem[18]</TD>
			<TD>$mem[19]</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>�@</TD>
			<TD>$mem[20]</TD>
		  </TR>
		  <TR>
			<TD>J</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD>$mem[21]</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
			<TD bgcolor="#00ffff">�@</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	  <TD valign="top" width="200" height="311">
	  <TABLE border="1" cellspacing="0">
		<TBODY>
		  <TR><TD align="center" width="250"><B>���O</B></TD>
		  <TR>
			<TD align="left" valign="top" width="190" height="280">
			<FORM METHOD="POST" name="BR" style="MARGIN: 0px">
			<INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
			<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
			<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_
require"$LIB_DIR/disp_cmd.cgi";
			&COMMAND;

print <<"_HERE_";
			</FORM>
			</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	</TR>
	<TR>
	  <TD colspan="2" valign="top" height="101">
	  <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
		<TBODY>
		  <TR>
			<TD height="20" valign="top" width="600">�ϥιp�F�C<BR><BR>�Ʀr�G�ϰ�H��<BR>���Ʀr�G�ۤ��ϰ쪺�H��</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	</TR>
  </TBODY>
</TABLE>
_HERE_

$mflg="ON"; #���


}

1;
