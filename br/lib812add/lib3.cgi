#===========================#
# �� ȯ�o�T�����n�O�B�z	#
#===========================#
sub SEVE {
$Command="MAIN";$mode = "main";
#MESSENGER
#Saved Mess File			|	Num of Mess Saved|1 Mess Length|Maximum Mess Disp
$mes_file = "$LOG_DIR/mes.log";	$listmax = 100;	  $mes = 100;	$mesmax = 5;
# ��J�T���ֹ�
if ($Message eq "") {$log = ($log . "�S������T���C<br>");return;}
elsif ($m_id eq "def_select") {$log = ($log . "�S����J�T���C<br>");return;}
elsif (length($m_id) > 38) { &ERROR("�T������r�ƶW�X�W���C(�̦h19�ӥ����r)") ; }
#@word = ("on9","��","��","�x","��","�m","76","��","�ѥ�","�Ѩ�","�F","��","��","�t","��","�a��","���R","��","fuck","������","fxck","fuxk");
#for ($i = 0;$i < 24;$i++)
#{
#if ($message =~ /@word[$i]/) {
#print &ERROR("�T���T���J�����r���C");
#exit();
#}
#}
# �ǰT�����O�s
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);
$mes_time ="$hour��$min��";
unshift (@messagelist,"$id,$full_name,$m_id,$Message,$mes_time,\n");
if ($#messagelist >= $listmax) {pop (@messagelist);}
open(DB,">$mes_file"); seek(DB,0,0); print DB @messagelist; close(DB);
}
#===================#
# �� �r���V�J�B�z	#
#===================#
sub POISON {
for ($i=0; $i<5; $i++) {if ($item[$i] =~ /�r��/) {last ;}}
local($wk) = $Command;
$wk =~ s/POI_//g;
if (($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/) || ($item[$i] !~ /�r��/)) {&ERROR("�������X�ݡC");}
$itai[$i]--;
if ($itai[$i] <= 0) {$item[$i] = "�L"; $eff[$i] = $itai[$i] = 0 ;}
local($in, $ik) = split(/<>/, $item[$wk]);
$log = ($log . "$in�V�J�F�r���C�D�`�p�ߪ��ˤl�P�P�P�C<br>") ;
if	  ($club eq "�Ʋz��") {
	if($item[$wk] =~ /<>H.*/){$item[$wk] =~ s/<>H.*/<>HD2-$id/g;}
	else{ $item[$wk] =~ s/<>S.*/<>SD2-$id/g; }
}elsif($item[5] eq "�r����@��") {
	if($item[$wk] =~ /<>H.*/){$item[$wk] =~ s/<>H.*/<>HD1-$id/g;}
	else{ $item[$wk] =~ s/<>S.*/<>SD1-$id/g; }
} else {
	if($item[$wk] =~ /<>H.*/){$item[$wk] =~ s/<>H.*/<>HD-$id/g;}
	else{ $item[$wk] =~ s/<>S.*/<>SD-$id/g; }
}
&SAVE ;
$Command = "MAIN" ;
}
#===================#
# �� �r���B�z		#
#===================#
sub PSCHECK {
local($wk) = $Command;
$wk =~ s/PSC_//g;
if(($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/)||($club ne "�Ʋz��")){&ERROR("�������X�ݡC");}
local($in, $ik) = split(/<>/, $item[$wk]);
if ($ik =~ /SH|HH/) {$log = ($log . "���H $in �ݰ_�ӫܦw���P�P�P�C<br>") ;}
else {$log = ($log . "���H $in �r���ֳQ�V�J�F�P�P�P�C<br>") ;}
$sta -= $dokumi_sta ;
if ($sta <= 0) {&DRAIN("com");}#��q���F�H
&SAVE ;
$Command = "MAIN" ;
}
#===================#
# �� �r���V�J�B�z	#
#===================#
sub POISONDEAD {
if ($hit <= 0) {

$hit = 0;
$mem--;

$com = int(rand(6));
$poisonid="2Y0";

if ($poisondeadchk){local($tp, $poisonid) = split(/-/, $poisoni);}
else{$poisonid = $wb;}
#�Τ�����o
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

#�ֹ�
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($poisonid eq $w_id) {#�P�@ID
		#�g��a-��
		$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
		$Index2 = $i;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no�f) �r�o���`�C�i�ݾl$mem�H�j</b></font><br>") ;
		$w_kill++;$w_bid = $id;&SAVE2;last;
	}
}

$log = ($log . "<font color=\"lime\"><b>$w_f_name $w_l_name�y$w_msg�z</b></font><br>") ;

local($b_limit) = ($battle_limit * 3) + 1;

if (($mem eq 1) && ($w_sts ne "NPC") && ($ar > $b_limit)){$w_inf = ($w_inf . "��") ;}

#���`���A
&LOGSAVE("DEATH1") ;
$death = $deth ;

$bid = $w_id ;

&SAVE;


}
}
#==================#
# �� �f�Y�y�ܧ�B�z#
#==================#
#sub WINCHG {$msg = $msg2;$dmes = $dmes2 ;$com = $com2 ;$log = ($log . "�f�Y�y�ܧ󧹦��C<br>");&SAVE;$Command = "MAIN";}
#==================#
# �� �����ܧ�B�z  #
#==================#
sub TEAM {
$teamold = $teamID;
if (length($teamID) > 24){&ERROR("�f�Y�y����r�ƶW�L�W���C(�̦h12�ӥ����r)","over length","BATTLE-TEAM");}
if (length($teamPass) > 18){&ERROR("�f�Y�y����r�ƶW�L�W���C(�̦h8�ӥ����r)","over length","BATTLE-TEAM");}
if ($teamID =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./){&ERROR("�p��ID�T��ϥΤ�r�i�J�C","taboo word","BATTLE-TEAM");}
if ($teamPass =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./){&ERROR("�p�ոT��ϥΤ�r�K�X�i�J�C","taboo word","BATTLE-TEAM");}

if ((($teamID2 eq $teamID))&&(($teamPass2 eq "")||($teamPass2 eq "�N�o�ˤ��ܧ󱡪p"))){;}
elsif ((($teamID2 eq "�L")&&($teamPass2 eq "�L"))||(($teamID2 eq "�y�L�z")&&($teamPass2 eq "�y�L�z"))){$teamID = "�L";$teamPass = "�L";&LOGSAVE("G-DATT");$log = ($log . "�����p�աC<br>") ;}
elsif (($teamID2 eq "")||($teamPass2 eq "")||($teamID2 eq "�L")||($teamPass2 eq "�L")||($teamID2 eq "�y�L�z")||($teamPass2 eq "�y�L�z")){&ERROR("�n�����p�աC�Ч�<BR>�p�զW�D�K�X����]���y�L�z�C<br>","No Grop Name Entered","BATTLE-TEAM");}
elsif ($teamID ne $teamID2){
	if ($teamID ne "�L"){&ERROR("�n�զ��D�[�J�s�p�աA���������{�b���p�աC<br>","Need to get out before get in","BATTLE-TEAM");}
	elsif (($teamPass2 eq "�N�o�ˤ��ܧ󱡪p")||($teamPass2 eq "")){&ERROR("�п�J�K�X�C<br>","No Password has been entered","BATTLE-TEAM");}
	elsif ($teamPass2 eq $teamID2){&ERROR("�p�զW�M�K�X�Ф��n�ۦP�C<br>","Group Name is same as Pass","BATTLE-TEAM");}
	elsif (($teamPass2 =~ /$teamID2/)||($$teamID2 =~ /teamPass2/)){&ERROR("�p�զW�M�K�X�ۦ��C<br>","Group Name and Pass is similar","BATTLE-TEAM");}
	#get User file
	open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
	#Same Name and ID check
	$ng = 0;
	foreach $userlist(@userlist) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
		if (($teamID2 eq $w_teamID)&&(($teamPass2 ne $w_teamPass)&&($w_sts ne "���`"))) {&ERROR("�P�ˤp�զW�s�b�A�K�X���P�C","Same Group Exists or Pass miss-match","BATTLE-TEAM");}
		elsif (($teamID2 eq $w_teamID)&&($teamPass2 eq $w_teamPass)) {$ng++;}
	}
	if ($ng eq 0){&LOGSAVE("G-JOIN");$teamID = $teamID2;$teamPass = $teamPass2;$log = ($log . "�զ��F�p�� $teamID�C");}
	elsif ($ng > 5){&ERROR("�p�ճ̤j�H��5�H�C<br>","Max Group Number","BATTLE-TEAM");}
	else {&LOGSAVE("G-KANYU");$teamID = $teamID2;$teamPass = $teamPass2;$log = ($log . "�[�J�p�� $teamID �F�C");}
}
&SAVE ;

$Command = "MAIN" ;
}
#==================#
# �� ���汹�I�B�z  #
#==================#
sub OUKYU {

local($wk) = $Command;
$wk =~ s/OUK_//g;

if	  ($wk eq 0) {$inf =~ s/�Y//g ;}#�Y
elsif ($wk eq 1) {$inf =~ s/��//g ;}#��
elsif ($wk eq 2) {$inf =~ s/��//g ;}#��
elsif ($wk eq 3) {$inf =~ s/��//g ;}#��

$log = ($log . "���F���汹�I�C<BR>") ;

$sta -= $okyu_sta ;

if ($sta <= 0) {&DRAIN("com");}#��q���F�H

&SAVE ;

$Command = "MAIN" ;
}
#==================#
# �� �򥻤�w�ܧ�  #
#==================#
sub KOUDOU {

local($wk) = $Command;
$wk =~ s/KOU_//g;
$old_tactics = $tactics;

if	 ($wk eq 1)	{$tactics = "��������";}
elsif($wk eq 2)	{$tactics = "���s����";}
elsif($wk eq 3)	{$tactics = "���K���";}
elsif($wk eq 4)	{$tactics = "�������";}
elsif($wk eq 5)	{$tactics = "�s�����";}
else			{$tactics = "�q�`";}

$log = ($log . "�򥻤�w�� $old_tactics �ܧ� $tactics�C<BR>\n") ;

&SAVE ;

$Command = "MAIN" ;
}
#==================#
# �� ���Ԥ�w�ܧ�  #
#==================#
sub OUSEN {

local($wk) = $Command;
$wk =~ s/OUS_//g;
$old_ousen = $ousen;

if		($wk eq 1)	{$ousen = "�������A";}
elsif	($wk eq 2)	{$ousen = "���s���A";}
elsif	($wk eq 3)	{$ousen = "���K���";}
#elsif	($wk eq 4)	{$ousen = "�������";}
#elsif	($wk eq 5)	{$ousen = "�s�����";}
elsif	($wk eq 6)	{$ousen = "�v���M��";}
elsif	($wk eq 7)	{$ousen = "�k�]���A";}
else				{$ousen = "�q�`";}

$log = ($log . "���Ԥ�w�� $old_ousen �ܧ� $ousen�C<BR>\n") ;

&SAVE ;

$Command = "MAIN" ;
}
#=====================#
# �� ��a���n���ϥ�   #
#=====================#
sub SPEAKER {
for ($i=0; $i<5; $i++){if ($item[$i] =~ /��a���n��/) {last;}}
if ($item[$i] !~ /��a���n��/) {&ERROR("�������X�ݡC");}

$log = ($log . " $speech<BR>");
$log = ($log . " ����a�ǹF�F�ܡH<BR>");
open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$namae = "$f_name $l_name" ;
$gunlog[2] = "$now,$place[$pls],$namae,$speech,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

$Command = "MAIN" ;

}
#=====================#
# �� hacking�B�z   #
#=====================#
sub HACKING{
for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "����PC<>Y")&&($itai[$paso] >= 1)) {$junbi = 0;last;}}

if (($Command ne "SPECIAL")||($Command4 ne "HACK")) {&ERROR("�������X�ݡC");}

local($bonus) = 10;local($dice1) = int(rand(99)) ;local($dice2) = int(rand(10)) ;

if ($club =~ /�q����/){$bonus = 15;} #�ӤH�q�������򥻦��\�v

local($kekka) = $bonus;
$log = ($log . "���դFHacking�K");
if ($dice1 <= $kekka){	 #Hacking���ѧP�_
	open(DB,"$area_file");seek(DB,0,0); my(@wk_arealist)=<DB>;close(DB);
	my($wk_ar,$wk_hack,$wk_a) = split(/,/, $wk_arealist[1]);  #Hacking�лx���o
	$wk_hack = 1;
	$wk_arealist[1] = "$wk_ar,$wk_hack,\n";
	open(DB,">$area_file"); seek(DB,0,0); print DB @wk_arealist; close(DB);
	$log = ($log . "Hacking\��\�\\�I�������T��ϰ�Q�Ѱ��F!!<BR>") ;
	&LOGSAVE("HACK") ;
}else{$log = ($log . "�i�O�AHacking���ѤF�K<BR>") ;}

for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "����PC<>Y")&&($itai[$paso] >= 1)){ last; }}

if ($dice1 >= 95){   #�q������&�|���ɾ����}�a
	$item[$paso] = "�L"; $eff[$paso] = $itai[$paso] = 0 ;
	$log = ($log . "����աI��������a�F�C<BR>") ;
	if ($dice2 >= 9){  #�F�������z�}�I
		$hit = 0 ; $sts = "���`"; $death = $deth = "�F�����B�D";$mem--;
		if ($mem == 1) {open(FLAG,">$end_flag_file"); print(FLAG "�פF\n"); close(FLAG);}
		&LOGSAVE("DEATH5") ;
		open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
		$gunlog[1] = "$now,$place[$pls],$id,,\n";
		open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
		$log = ($log . "����աI��������a�F�C<BR><br>�O�K����H�q�K����o�Xĵ�i���n�T�K!?<BR><BR><font color=\"red\">�P�P�P!!�P�P�P<br><br><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;
	}
}else{$itai[$paso] --;if ($itai[$paso] == 0) {$log = ($log . "�κɤF����PC�q�����q�O�C<BR>") ;}}

&SAVE;
}
1;
