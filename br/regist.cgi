#! /usr/bin/perl

#������������������������������������������
#�� 	-  BR REGISTRATION PROGRAM  - 	 ��
#�� 									 ��
#�� 		���֥롼�������			 ��
#�� 									 ��
#�� checker			-		Checker		 ��
#�� MAIN			-		�ᥤ��		 ��
#�� ��Ͽ����		-		REGIST		 ��
#�� INFO			-		��������	 ��
#�� CLUBMAKE		-		����ֺ���	 ��
#������������������������������������������

#require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib1.cgi";
&LOCK;
require "pref.cgi";

&DECODE;
&CREAD ;

if ($mode eq "regist"){&REGIST;}
elsif ($mode eq "info"){&INFO;}
elsif ($mode eq "info2"){&INFO2;}
else { &MAIN; }
&UNLOCK;
exit;

#==================#
# �� Checker       #
#==================#
sub checker {
if(($limit == "")||($limit == 0)){ $limit = 7;}local($t_limit) = ($limit * 3) + 1;

if (($fl =~ /�פF/)||($ar >= $t_limit)){&ERROR("�C���n���Ƥw���C<br><br>�@�е��ݤU���C���}�l�A��n���C") ;}

$chktim = $c_endtime + (1*60*60*2) ;	#���`�ɶ����o��
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($chktim);
$year+=1900; $month++;

if ($chktim > $now) {&ERROR("��ù���`�T�{��A2�p�ɤ���A�n�O�C<br><br>�@���^�n���i��ɶ��G$year/$month/$mday $hour:$min:$sec") ;}#�n�O�ɶ����~�H

#�Τ�����o
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$listnum = @userlist;
if (($userlist - $npc_num) >= $maxmem) {&ERROR("�ӽеn�����ѡA�C���̰����� ($maxmem��) �W���a�n���C") ;}#�̤j�H�ƶW�L�H

#���Ʈֹ�
foreach $userlist(@userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
	if (($c_id eq $w_id) && ($c_password eq $w_password) && ($w_sts ne "���`")) {&ERROR("�W�r��ID�T��Ƶn�O�C���ˬd�M���ΦV�޲z���߰ݡCHOST ID:$IPAdd-$w_f_name-$w_l_name") ;}#�P�@ID or �P�m�P�W�H
	if (($w_sts ne "���`")&&($host eq $w_IP)&&($host ne "209.137.141.2")) {&ERROR("�W�r��ID�T��Ƶn�O�C���ˬd�M���ΦV�޲z���߰ݡCCOMMENT:USED SAME PC HOST:$host") ;}#�P�@ID or �P�m�P�W�H
}
}
#==================#
# ��main		   #
#==================#
sub MAIN {
$hostchk = 0;
if (($SubServer)&&($host eq "209.137.141.2")){$hostchk=1;$host = $IPAdd;if ($IPAdd eq ""){&ERROR("�y���ͽбqTOP PAGE�X��")};}
if ($host eq "209.137.141.2"){$hostchk=1;}
&checker;&HEADER;
print <<"_HERE_";
<center><font color="#FF0000" face="Verdana" size="6"><span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">��դ���</span></font></center>
<BR><BR><img border="0" src="img/i_hayashida.jpg" width="70" height="70"><BR><BR>
�A�O��ե͡H�ڬO���̪L�СC<BR>�K�A�A�٫����D�Ǯ� (�S�X���c�����e)�A<BR>�L�צp��A����n�A����Ƨa�C<BR><BR>�����A�b�o�̼g�W�A���m�W�A�O�W�ʧO�I<BR>�A�V�ڴ���N�i�H�F�C
<FORM METHOD="POST"  ACTION="regist.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="regist">
<INPUT TYPE="HIDDEN" NAME="IP" VALUE="$host">
�m�G<INPUT size="16" type="text" name="F_Name" maxlength="6"><BR>
�W�G<INPUT size="16" type="text" name="L_Name" maxlength="6"><BR>
(�m,�W����6�Ӧr�H��)
<BR><BR>
�ʧO�G<SELECT name="Sex">
<OPTION value="NOSEX" selected>- �ʧO -</OPTION>
<OPTION value="�k��">�k��</OPTION>
<OPTION value="�k��">�k��</OPTION>
</SELECT>
_HERE_
print "�@�Y���G<SELECT name=\"Icon\">\n";
print "<OPTION value=\"NOICON\" selected>-�Y��-</OPTION><OPTION value=\"NOICON\">�k��</OPTION>\n";
	for ($i=0;$i<$icon_check1;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
print "<OPTION value=\"NOICON\">�k��</OPTION>";
	for ($i;$i<$icon_check2;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
#print "<OPTION value=\"NOICON\">�S��</OPTION>";
#for ($i;$i<$icon_check3;$i++){print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";}
print "</SELECT>\n";
print <<"_HERE_";
[<a href="view.htm" target="_blank">�Y���@��</a>]<BR><BR>
ID�G<INPUT size="8" type="text" name="Id" maxlength="8">�@�K�X�G<INPUT size="8" type="text" name="Password" maxlength="8"><BR>
(ID�A�K�X�b���^�Ʀr8�Ӧr�H��)<BR><BR>
<Table border="0" cellspacing="0" cellpadding="0">
<tr><td align="right">�f�Y�y�G</td><td><INPUT size="32" type="text" name="Message" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">���`���ɪ��x��</td></tr>
<tr><td align="right">��@���G</td><td><INPUT size="32" type="text" name="Message2" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">�������`�ɪ��x��</td>
<tr><td align="right">�N��y�G</td><td><INPUT size="32" type="text" name="Comment" maxlength="32"></td></tr>
<tr><td align="center" colspan="2">(�N��ʻy�y�C�O����ͦs�̤@����C)<BR>(32�Ӧr���w)</td></tr>
</table><BR>
<FONT color="yellow" size="2"><B>
�ۦPIP�ƼƵn�������T��F�䥦�����s�s�����C�������T��F<BR>
���a�W�r�ιC�����O�����T����r�����F�p�o�{�H�W�}�a�u�h���a�A<BR>
Withlove�޲z���N�|�j��R���C���H���θT��i�JWithlove Server�A<BR>
�N�|�����T��ɥ�Withlove���Ѫ��@���K�O�A�ȡA�п�u�o�p�p�C���u�h�A���¡C<BR>
_HERE_
if($hostchk){print "�y���ͤ����ίu��m�W�A�C���u�O���ݵ�c�C<BR>";}
print <<"_HERE_";
</U></B></FONT><BR>
<INPUT type="submit" name="Enter" value="�T�w">�@<INPUT type="reset" name="Reset" value="���g"><BR></FORM></CENTER>
<P align="center"><A href="index.cgi"><B><FONT color="#ff0000" size="4">��^</FONT></B></A></P>
_HERE_
&FOOTER;
}
#==================#
# ���n���B�z       #
#==================#
sub REGIST {
$host = $IP;
&checker;
#��J�H���ֹ�
if ($f_name2 eq '') { &ERROR("�m�󥼿�J�C") ; }
if (length($f_name2) > 12) { &ERROR("�m���J�r�ƶW�X���� (�̦h6�Ӥ���r)") ; }
if ($f_name2 =~ m/[>]/) { &ERROR("�̦h6�Ӥ���r") ; }
if ($l_name2 eq '') { &ERROR("�W�r����J�C") ; }
if (length($l_name2) > 12) { &ERROR("�W�r��J�r�ƶW�X���� (�̦h6�Ӥ���r)") ; }
if ($l_name2 =~ m/[>]/) { &ERROR("�̦h6�Ӥ���r") ; }
if ($sex2 eq "NOSEX") { &ERROR("�ʧO����ܡC") ; }
if (length($id2) > 8) { &ERROR("ID���r�ƶW�X����C(�̦h��J8�ӥb�Φr)") ; }
if ($id2 eq '') { &ERROR("ID����J�C") ; }
if ($id2 =~ m/[^0-9a-zA-Z]/) { &ERROR("ID�ХΥb�Φr��J�C(�̦h��J8�ӥb�Φr)") ; }
if ($password2 eq '') { &ERROR("�K�X����J�C") ; }
if (length($password2) > 8) { &ERROR("�K�X���r�ƶW�X����C(�̦h��J8�ӥb�Φr)") ; }
if ($password2 =~ m/[^0-9a-zA-Z]/) { &ERROR("�K�X�ХΥb�Φr��J�C(�̦h��J8�ӥb�Φr)") ; }
if ($icon2 eq "NOICON") { &ERROR("�Y������ܡC") ; }
if (($id2 =~ /$password2/)||($password2 =~ /$id2/)) { &ERROR("�K�X����PID�ۦP�C") ; }
if (length($msg2) > 64) { &ERROR("�f�Y�y����r�ƶW�X����C(�̦h��J32�ӥ����r)") ; }
if (length($dmes2) > 64) { &ERROR("�򨥪���r�ƶW�X����C(�̦h��J32�ӥ����r)") ; }
if (length($com2) > 64) { &ERROR("�N��y����r�ƶW�X����C(�̦h��J32�ӥ����r)") ; }
if ($msg2 eq "") { &ERROR("�п�J�f�Y�y�C(�̦h��J32�ӥ����r)") ; }
if ($dmes2 eq "") { &ERROR("�п�J�򨥡C(�̦h��J32�ӥ����r)") ; }
if ($com2 eq "") { &ERROR("�п�J�N��y�C(�̦h��J32�ӥ����r)") ; }
if(($sex2 =~ /�k��/)&&($icon2 >= $icon_check1 )) { &ERROR("�����ܻP�ʧO���P���Y���C") ; }
if(($sex2 =~ /�k��/)&&($icon2 < $icon_check1 )){ &ERROR("�����ܻP�ʧO���P���Y���C") ; }

@word = (" ","�@","on9","��","��","�x","��","�m","76","��","�ѥ�","�Ѩ�","�F","��","��","�t","��","�a��","���R","��","fuck","������","fxck","fuxk");
for ($i = 0;$i < 24;$i++)
{
if ($f_name2 =~ /@word[$i]/) {
print &ERROR("�`�N�m�����A�T���J�����r���ΪŦr�šC");
exit();
}
if ($l_name2 =~ /@word[$i]/) {
print &ERROR("�`�N�W�����A�T���J�����r���ΪŦr�šC");
exit();
}
if ($msg2 =~ /@word[$i]/) {
print &ERROR("�`�N�f�Y�y���A�T���J�����r���ΪŦr�šC");
exit();
}
if ($dmes2 =~ /@word[$i]/) {
print &ERROR("�`�N�����A�T���J�����r���ΪŦr�šC");
exit();
}
if ($com2 =~ /@word[$i]/) {
print &ERROR("�`�N�N��y���A�T���J�����r���ΪŦr�šC");
exit();
}
}

#get User file
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
#Same Name and ID check
foreach $userlist(@userlist) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
	if (($id2 eq $w_id) || (($f_name2 eq $w_f_name)&&($l_name2 eq $w_l_name))) {&ERROR("�P�˪�ID�ΦP�m�P�W���r�Ťw�g�s�b�C") ;}#�P�˪�ID�ΦP�m�P�W�H
}

#��I�Z�����
open(DB,"$wep_file") || exit; seek(DB,0,0); @weplist=<DB>; close(DB);

#�ӤH�p�������
open(DB,"$stitem_file") || exit; seek(DB,0,0); @stitemlist=<DB>; close(DB);

#�ǥ͸��X���
open(DB,"$member_file") || exit; seek(DB,0,0); $memberlist=<DB>; close(DB);
($m,$f,$mc,$fc) = split(/,/, $memberlist);

#�ʧO�H�Ʈֹ�
if ($sex2 eq "�k��") {
	if ($mc >= $clmax) { &ERROR("�k�ͼƥضW�X���w����n�O�C") ;}#�n������H
	$m+=1;$no=$m;$cl=$clas[$mc];
	if ($m >= $manmax) {$m=0;$mc+=1;}#(�Z)�ŧ�s�H
} else {
	if ($fc >= $clmax) {&ERROR("�k�ͼƥضW�X���w����n�O�C") ;}#�n������H
	$f+=1;$no=$f;$cl=$clas[$fc];
	if ($f >= $manmax) {$f=0;$fc+=1;}#(�Z)�ŧ�s�H
}

#�ǥ͸��X����s
$memberlist="$m,$f,$mc,$fc,\n" ;
open(DB,">$member_file"); seek(DB,0,0); print DB $memberlist; close(DB);

#������o�Z���W����o
$index = int(rand($#weplist));
($w_wep,$w_att,$w_tai) = split(/,/, $weplist[$index]);

#�ӤH�p�������ڦW����o
$index = int(rand($#stitemlist));
local($st_item,$st_eff,$st_tai) = split(/,/, $stitemlist[$index]);
$index = int(rand($#stitemlist));
local($st_item2,$st_eff2,$st_tai2) = split(/,/, $stitemlist[$index]);

#�ҫ��~�����
for ($i=0; $i<6; $i++) {$item[$i] = "�L"; $eff[$i]=$itai[$i]=0;}

#�����O
$rand = int(rand(25));
$att = $rand + 50;
$def = 100 - $rand;
$hit = 100;
$mhit = $hit ;$kill=0;$sta = $maxsta ;$level=1;
#�g���
$exp=0;
$reg_exp = $ar;
if ($reg_exp >= 4){$reg_exp-=4;$exp = ($ar * 10);}

$death = $msg = "";$sts = "���`"; $pls=0;$tactics = "�q�`" ;
$endtime = 0 ;$log = "";$dmes = "" ; $bid = "" ; $inf = "" ;

#����D��Ϊ�����o���Z��
$item[0] = "�ѥ]<>SH"; $eff[0] = 50; $itai[0] = 2;
$item[1] = "��<>HH"; $eff[1] = 50; $itai[1] = 2;
$item[2] = $w_wep; $eff[2] = $w_att; $itai[2] = $w_tai;

$wep = "�Ť�<>WP";
$watt = 0;
$wtai = "��" ;

if ($sex2 eq "�k��" ) {$bou = "�ժA<>DBN";}
else {$bou = "���L�A<>DBN";}
local($bou_reg,$bou_regi) = split(/<>,/, $bou);
$bdef = 5;
$btai = 30;

$bou_h = $bou_f = $bou_a = "�L" ;
$bdef_h = $bdef_f = $bdef_a = 0;
$btai_h = $btai_f = $btai_a = 0 ;

#�l�u�S�b��I
if ($w_wep =~ /<>WG/) {$item[3] = "�l�u<>Y"; $eff[3] = 10; $itai[3] = 1;$item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;}#�u
elsif ($w_wep =~ /<>WA/) {$item[3] = "�b<>Y"; $eff[3] = 12; $itai[3] = 1;$item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;}#�b
else {$item[3] = $st_item; $eff[3] = $st_eff; $itai[3] = $st_tai;$item[4] = $st_item2; $eff[4] = $st_eff2; $itai[4] = $st_tai2;}

&CLUBMAKE ; #�ǳ��@��

#User File
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$seikaku = "�L";#seikaku
$sinri = "�L";#sinri
$teamID = "�L";#TeamID
$teamPass = "�L";#TeamPass
$ousen = "�q�`";#Ousen
$item_get = "�L";
$eff_get = "0";
$itai_get = "0";
$newuser = "$id2,$password2,$f_name2,$l_name2,$sex2,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg2,$sts,$pls,$kill,$icon2,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes2,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com2,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n" ;

#New User Save
open(DB,">>$user_file"); seek(DB,0,0); print DB $newuser; close(DB);

#New User Log
&LOGSAVE("NEWENT") ;

$id=$id2; $password=$password2;

&CSAVE ;	#Cokie Save

($w_name,$w_kind) = split(/<>/, $w_wep);
($b_name,$b_kind) = split(/<>/, $bou_reg);

&HEADER;

print <<"_HERE_";
<center><B><FONT color="#ff0000" size="+3" face="Verdana">��դ��򧹦�</FONT></B><BR><BR></center>
<TABLE border="1" width="222" cellspacing="0">
  <TBODY>
	<TR><TD width="36" class="b1">(�Z)��</TD><TD colspan="3" class="b3">$cl</TD></TR>
	<TR><TD class="b1">�m�W</TD><TD colspan="3" class="b3">$f_name2 $l_name2</TD></TR>
	<TR><TD class="b1">�s��</TD><TD colspan="3" class="b3">$sex2$no��</TD></TR>
	<TR><TD class="b1">�ǳ�</TD><TD colspan="3" class="b3">$club</TD></TR>
	<TR><TD class="b1">��O</TD><TD class="b3">$hit/$mhit</TD><TD width="39" class="b1">��q</TD><TD class="b3">$sta</TD></TR>
	<TR><TD class="b1">�����O</TD><TD class="b3">$att</TD><TD class="b1">�Z��</TD><TD class="b3">$w_name</TD></TR>
	<TR><TD class="b1">���s�O</TD><TD class="b3">$def</TD><TD class="b1">����</TD><TD class="b3">$b_name</TD></TR>
  </TBODY>
</TABLE>
<P align="center">
_HERE_

if ($sex2 eq "�k��") {print "$f_name2 $l_name2�M�w�F�a�H<BR>\n" ;}
else {print "$f_name2 $l_name2�O�ܡH<BR>\n" ;}

print <<"_HERE_";

��ի�榣���A���L�A���ѬO�׾ǮȦ�C<BR><BR>
�A�]�u���B�A�d�U�O�ۤ��n���I<BR><BR>
<A href="regist.cgi?mode=info&Id=$id2&Password=$password2"><B><FONT color="#ff0000" size="+2">�׾ǮȦ�X�o</FONT></B></A><BR>
</P>
_HERE_
&FOOTER;
}

#===================#
# �������B�z		#
#===================#
sub INFO {

&HEADER;

print <<"_HERE_";
<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">�n������</FONT></B><BR><BR>
�i�}������A�o�{�ۤv�b�@�ӹ��ЫǪ��a��C�ڤ��O���ӥh�F�׾ǮȦ�ܡP�P�P�H<BR>
�u��F�A�b�h�׾ǮȦ檺�ڤh�����M�ηNŧ�ӡP�P�P�v<BR>
�a���|�P�A�ݨ���L���ǥͦn���]�b�C�Τߦa�ݪ��ܡA�o�{�F�j�a���V�W�M�W�F�Ȧⶵ��A<BR>
�Τ�I�ۤv���V�A�]�Pı��N�N������Ĳ�P�C<BR>
���b�ôb�j�a�����򳣮M�W�P�˪����ӻȦⶵ�骺�ɭ�...<BR><BR>
��M�A�q�e�������A�@�Өk�H���ƪZ�˸˳ƪ��x�H���F�i�ӡP�P�P�C<BR><BR>
<img border="0" src="img/i_sakamochi.jpg" width="70" height="70"><BR><BR>
�u�j�a�n�A�@�~�e���ɭԧڤ]�O�o���p�������̡C�ܺa����A��������p�������ȡC�ܦn�I<BR>
�H�ۮɶ���l�H���V�ӶV�w��{���A�L�۩��֤�l���ɭԡA�۫H�U��w�g�ѰO�F��a���h�V�O�h���W�~��ئ����Ѫ����|�a��A<BR>
�p����a�}�l�I�h�A�Q�A�����A���H�̤w�g�A�S���۫H�A�o�O�ܦM�I���C�]���A���j���H�̰Ӷq�s�w�F�o�ӭp���C<BR><BR>
<p align="center"><font color="#FF0000" face="Verdana" size="6">
<span id="BR" style="width:100%;filter:blur(add=1,direction=135,strength=9):glow(strength=5,color=gold); font-weight:700; text-decoration:underline">
�� BATTLE ROYALE ��</span></font></p><BR>
���Ѱ_�}�l�A�b�o�̽Ѧ�n�}�l���۱��`���C<BR>
�p�G�A�Q���U���Ӷ���A���ե���k�����ܡA�A�N�|�ߧY�Q���C<BR><BR>
����ѤU�@�H�ͦs����A�ĨĿ�u�O�ǳW�C<BR>
�u�r�A�Ѯv���ѰO�F���A�o�̬O�@�ӥ|����������q�C<BR><BR>
�ӳo�̬O�o�Ӯq�����աC<BR>
�Ѯv�|�@���b�o�̬ݵۦU��V�O�C<BR><BR>
����A�}�l���o�ӭp���p�����C�A�q�o�̥X�h��h���̤]�i�H�C<BR>
�C��8�p�� (0�I�M8�I�M6�I)�A�����q�s���C�@��T�^�C<BR><BR>
�b���̡A�j�a�|�ݨ�a�ϡA�o�Ӱϰ줰��ɭԦM�I�Ѯv�|�i���C<BR>
�n�n�a�F�Ѧa�ϡA���}���@�Ӱϰ�A<BR>
�n�ܧ֦a�q���Ӱϰ�X�ӳ�C<BR><BR>
����|�o�˻��O�A���k���s���M�I�ϰ쪺�d��A���Ӷ���O�|�z�����C<BR><BR>
�]���r�A���b�Ӱϰ줤���ؿv�����]�O����C<BR>
�N����}���õL�u�q�i�]�|���A���z��C<BR>
��F�A�ؿv�����`�O�i�H���A���N���ê��C<BR><BR>
���٬O�A�n���D�C�p�����ɶ�����C�A�u��<B><font color="yellow">�@�g</font></B>�ɶ��h�����C<BR><BR>
�ɶ����p�G�ٯd�U����@�H�A�ѤU�����ǤH������@�˷|�z���C�]���a�x�u����s��<u>�X�H</u>�C<BR><BR>
�J�M�ѥ[�F�����N�n���O�H�u�A�Ѯv�i���Q�ݨ�S�ӧQ�̩O�I<BR>
�A�̨C�ӤH�N�Q���o��@�Ӫ��~�]�A�̭��������M���A���n�w�A�H�Τ@��Z���C<BR><BR>
�U���}�l�A���ӾǸ��A���n�A�̪��F��A�@�ӭ����}�o�̡I<BR><BR>
<FORM METHOD="POST"  ACTION="battle.cgi" style="MARGIN: 0px">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="main">
<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
<center>
<INPUT type="submit" name="Enter" value="�q�ЫǥX�h">
</center>
</FORM>
_HERE_
&FOOTER;
}
#==================#
# ���ǳ��@��     #
#==================#
sub CLUBMAKE {
$wa=$wg=$wb=$wc=$wd=$ws=$wn=$wf=$wp=$we=0 ;
#    ��      ��  ��      ��      ��

local($dice) = int(rand(95)) ;

if		($dice < 10)	{$club = "�g����";$wg = 1 * $BASE;}
elsif	($dice < 20)	{$club = "�Ťⳡ";$wp = 1 * $BASE;}
elsif	($dice < 30)	{$club = "�βy��";$wc = 1 * $BASE;}
elsif	($dice < 40)	{$club = "��ǳ�";$wd = 1 * $BASE;}
elsif	($dice < 50)	{$club = "�C����";$ws = 1 * $BASE;}
elsif	($dice < 60)	{$club = "�C�D��";$ws = 1 * $BASE;}
elsif	($dice < 70)	{$club = "������";$wp = 1 * $BASE;}
elsif	($dice < 80)	{$club = "�q����";}
elsif	($dice < 90)	{$club = "�Ю|��";}
elsif	($dice < 100)	{$club = "�Ʋz��";}
}
