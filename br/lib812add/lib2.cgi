#==================#
# �� ����		   #
#==================#
sub MOVE {

local($mv) = $Command2;
$mv =~ s/MV//g ;

#���ʫe�B�z
$Command = "MAIN";
$Command2 = "";

$ok = 1;if (($inf =~ /��/)&&($sta > 18)) {$ok = 0;} elsif (($club eq "�Ю|��")&&($sta > 10)) {$ok = 0;} elsif ($sta > 13) {$ok = 0;}
if ($ok){$log = ($log . "��q�������ಾ�ʡK"); return ;}

if ($inf =~ /��/) {$sta -= int(rand(5) + 13) ;}
elsif ($club eq "�Ю|��") {$sta -= int(rand(5))+6 ;}
else {$sta -= int(rand(5))+8 ;}

($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21]) = split(/,/, $arealist[2]);
($war,$a) = split(/,/, $arealist[1]);
if($ar[$war] eq $place[$mv]) {
	$log = ($log . "$place[$mv]���ʤF�C<br>�o�̦����F�T��ϰ�C<br>$arinfo[$mv]<br>") ;
} elsif(($ar[$war+1] eq $place[$mv])||($ar[$war+2] eq $place[$mv])) {
	$log = ($log . "$place[$mv]���ʤF�C<br>�o�̦����F�T��ϰ�C<br>$arinfo[$mv]<br>") ;
} else {
	for ($i=0; $i<$war; $i++){if (($ar[$i] eq $place[$mv])&&($hackflg eq 0)&&($sts !~ /NPC/)){$log = ($log . "$place[$mv]�O�T��ϰ�C���ಾ�ʡK�C<BR>");return;}}#�T��ʡH
	$log = ($log . "$place[$mv]���ʤF�C<BR>$arinfo[$mv]<br>") ;
}

$pls = $mv;#����

if($inf =~ /�r/){local($minus) = int(rand(8));$hit -= $minus;$log = ("�r�o�v�T��O��֤F $minus�C<BR>");require "$LIB_DIR/lib3.cgi";&POISONDEAD;}
if($sta <= 0){&DRAIN("mov");}#��q���F�H
&SEARCH2;
&SAVE;
}
#==================#
# �� �����B�z	   #
#==================#
sub SEARCH {

$ok = 1;if (($inf =~ /��/)&&($sta > 25)) {$ok = 0;} elsif (($club eq "�Ю|��")&&($sta > 15)) {$ok = 0;} elsif ($sta > 20) {$ok = 0;}
if ($ok){$log = ($log . "��q�������౴���K") ; return ;}

$log = ($log . "$l_name�A���񱴯��K�C<br>") ;

if ($inf =~ /��/) {$sta -= int(rand(5) + 20) ;}
elsif ($club eq "�Ю|��") {$sta -= int(rand(5))+10;}
else {$sta -= int(rand(5))+15 ;}

if ($inf =~ /�r/) {
	local($minus) = int(rand(8));
	$hit -= $minus;
	$log = ("�r�o�v�T��O��֤F $minus�C<BR>");
	require "$LIB_DIR/lib3.cgi";
	&POISONDEAD;
}

if ($sta <= 0) {&DRAIN("mov");}#��q���F�H

&SEARCH2;

if ($chksts ne "OK") {$log = ($log . "�i�O�A�S��줰��C<BR>") ;$Command = "MAIN" ;}

&SAVE;
}
#==================#
# �� �����B�z2     #
#==================#
sub SEARCH2 {

local($i) = 0 ;
srand(time ^ $i) ;

srand($now);
local($a) = int(rand(1));		#�ĤH����o�{�D��
local($dice1) = int(rand(10));	#�ĤH�A�D��o�{

&TACTGET ;

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

$chksts="NG";$chksts2="NG";

if ($dice1 <= 5) {	#�ĵo���H
	for ($i=0; $i<$#userlist+1; $i++) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
		$w_bid2 = $w_bid;
		if($tactics eq "�s�����"){
			$w_bid2 = "";local($randam) = int(rand(100));
			$randam_set = 50;
			if($w_tactics ne "�s�����"){$randam_set = 75;}
			if($randam >= $randam_set){$w_bid2 = $w_bid;}
		}
		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid2 ne $id)){push @plist, $i;}
	}

#	for ($i=0;$i<@plist+5;$i++){push(@plist,splice(@plist,int(rand @plist+0),1));}
	#FIXED BY: (�����E)
	@plist2 = ();
	for(@plist){
		my $r = rand @plist2+1;
		push(@plist2,$plist2[$r]);
		$plist2[$r] = $_;
	}

	foreach $i(@plist2){
		local($dice2) = int(rand(10)) ;	#�ĤH�A�D��o�{
		local($dice3) = int(rand(10)) ;	#�������
		local($dice6) = int(rand(100)) ;	#����
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);

#�s��
		$w_bid2 = $w_bid;
		if ($tactics eq "�s�����") {$w_bid2 = "";}
#		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid ne $id)) {	#�a��@�P�H
		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid2 ne $id)) {	#�a��@�P�H

			&TACTGET2;local($chk) = int($dice2 * $sen);

			if ($chk < $chkpnt) {
				if ($w_hit > 0) {#�ͦs�H
					require "$LIB_DIR/attack.cgi";$wf = $w_id;	#�s�����I�������@������
					if(($teamID ne "�L")&&($teamID ne "")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){#����
						&ATTJYO ;$chksts="OK";$chksts2="NG";last;
					}elsif($dice3 <= $chkpnt2){					#�������
						&ATTACK ;$chksts="OK";$chksts2="NG";last;
					}else{										#������ (�_ŧ)
						$Index2 = $i;$w_bid = $id ;$bid = $w_id ;
						&ATTACK2 ;$chksts="OK";$chksts2="NG";last;
					}
				} else {#����o�{
					local($chkflg) = 0 ;
					local($dice4) = int(rand(10));
					if ($dice4 > 6){
						for ($j=0; $j<6; $j++) {if ($w_item[$j] ne "�L" && $w_item[$j] ne "") {$chkflg=1;last;}}
						if ($chkflg){
							if ($w_wep !~ /�Ť�/ || $w_bou !~ /����/ || $w_bou_h ne "�L" || $w_bou_f ne "�L" ||$w_bou_a ne "�L"){
								$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,-1,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
								open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
								$wf = $w_id; #�s�����I������
								&DEATHGET;last;
							}
						}
					}
				}
			}else{ $chksts2="OK";}
		}
	}
	if ($chksts2 eq "OK") {#�D��o�{�D��
		local($dice5) = int(rand(10));#�D��o�{
		if (($dice5 <= 5)&&($Command eq "SEARCH")) {require "$LIB_DIR/item1.cgi";&ITEMGET;}
		elsif ($chksts2 eq "OK") {$log = ($log . "����H���õۡK�C�L�h�ܡH<BR>") ;}
	}
} else {	#���ʡD�D��o�{
	$dice2 = int(rand(8)) ;
	if (($dice2 < $chkpnt)&&($Command eq "SEARCH")) {require "$LIB_DIR/item1.cgi";&ITEMGET;}#�D��o�{
	else{require "$LIB_DIR/event.cgi";&EVENT ;}
}

}
#===================#
# �� �ԧQ�~���o 	#
#===================#
sub WINGET {
if ($item[$itno2] ne "�L" or $itno2>4 or $itno2<0) {$log = ($log . "�ҫ��~�W�L�W���C<br>") ;$Command = "MAIN";return;}
if ($getid eq $id){$log = ($log . "�ۤv�ܨ��ۤv����a�~�C<br>...�C<br>") ;$Command = "MAIN";return;}

local($wk) = $Command;
$wk =~ s/GET_//g;
$wk+=0;
$wk=int($wk);
local($witem,$weff,$witai);

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$wingetck=1;
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $getid) {
		$Index2 = $i;
		&BB_CK;#�s�����I������
		if ($w_hit>0){$log = ($log . "�Q�n$w_f_name���ҫ����~�N���D�`�j�P�C<br>...�C<br>") ;$Command = "MAIN";return;}
		if		($wk eq 6)	{($witem,$weff,$witai) = ($w_wep,$w_watt,$w_wtai);$w_wep = "�Ť�<>WP"; $w_watt = 0; $w_wtai = "��";}
		elsif	($wk eq 7)	{($witem,$weff,$witai) = ($w_bou,$w_bdef,$w_btai);$w_bou = "����<>DN"; $w_bdef = 0; $w_btai = "��";}
		elsif	($wk eq 8)	{($witem,$weff,$witai) = ($w_bou_h,$w_bdef_h,$w_btai_h);$w_bou_h = "�L"; $w_bdef_h = $w_btai_h = 0;}
		elsif	($wk eq 9)	{($witem,$weff,$witai) = ($w_bou_f,$w_bdef_f,$w_btai_f);$w_bou_f = "�L"; $w_bdef_f = $w_btai_f = 0;}
		elsif	($wk eq 10)	{($witem,$weff,$witai) = ($w_bou_a,$w_bdef_a,$w_btai_a);$w_bou_a = "�L"; $w_bdef_a = $w_btai_a = 0;}
		else				{($witem,$weff,$witai) = ($w_item[$wk],$w_eff[$wk],$w_itai[$wk]);$w_item[$wk] = "�L"; $w_eff[$wk]=$w_itai[$wk] = 0;}
		$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
		open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
		$wingetck=0;
		last;
	}
}
if($wingetck){&ERROR("�������~�A�ЦV�޲z�����i�C","WINGET INTERNAL ERROR","BATTLE-WINGET");}
if ($witem!~/^(�L|�Ť�|����)$/ && $i!=$#userlist+1){
	$item[$itno2] = $witem ;
	$eff[$itno2] = $weff; $itai[$itno2] = $witai ;
	($witem)=split(/<>/,$witem,2);
	$log = ($log . "$l_name �o��F $witem�C<BR>") ;
}else{$log = ($log . "���߬B�C<BR>") ;}

&SAVE;&SAVE2;

$Command = "MAIN";
}
#==================#
# �� ����o�{�B�z  #
#==================#
sub DEATHGET {

$log = ($log . "$w_f_name $w_l_name������o�{�C<br>") ;

if ($w_death =~ /�C��/) {
	if ($w_com eq 0)	{$log = ($log . "���骺�Y���M�߷F�����K�C�n���Q����L�b���_�C<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "�������Q�U�Q�M�b�}�}�A��Ŧ���_�y�X�ӡK�C<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "�q�ӻH��ݤf�}�G�a�Q���}�C�ˤf�D�`���f�K�C<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "�Y�D�߷F�D���u�D��}���Q���ΡC�o�˪��ƬO���ӲM�����H�వ�ܡK�C<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "�y���Q�����a���H�C�������H����ͫe���ɪ������K�C<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "�����Q���}�A���L�A�J�Ӭݪ��ܤ�æh�B�a��]���M�ˡK�C<BR>�O���F��⤧��Ӧ۱����ܡH<br>") ;}
#	elsif ($w_com eq 0) {$log = ($log . "�����Q����U�Q�Z���y���j�q����ˡK�C���骺�P��A��y���e�K�C<br>") ;}
#	elsif ($w_com eq 1) {$log = ($log . "����Q��F�n�h���n�h��������K�C<br>") ;}
#	elsif ($w_com eq 2) {$log = ($log . "�@���뤤��Ŧ�C�ܤ��ٱq�˦��X�K�C�n�����~�Q���@�ˡC<br>") ;}
#	elsif ($w_com eq 3) {$log = ($log . "����V�ί}���K�C���]�٦b�ϥաK�C<br>") ;}
#	elsif ($w_com eq 4) {$log = ($log . "�q�᭱�Q��i�����C�O��Mŧ���ܡK�H<br>") ;}
#	elsif ($w_com eq 5) {$log = ($log . "���������Y���˲��C��F����A���Q���F����@�˪��ˡK�C<br>") ;}
#	else				{$log = ($log . "���سQ��K�C�n���y�ۦ�\�@�ˡK�C<br>") ;}
	else				{$log = ($log . "�q�Y��ݲY�G�a�Q���}�K�C<br>") ;}
}elsif ($w_death =~ /���/) {
	if ($w_com eq 0)	{$log = ($log . "�ݡK��3�o�A�B1�o���u���K�C�B���@�o��˦n���O�u���P�R���K�C<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "�������Ƶo�u���A��y�X�F�C�i�O�A���Ǧ�w�g���F�C<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "�Y�������F�A�����骬���]�۪��K�C�u��q�m�W�P���D���̪��W�r�C<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "�ݼƵo�C�åB�A�y�۸���C�j�����F����A��i�j�b�f���g���C�������˪��ơK�C<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "�����B���աA�i�H�ݨ��C�o�ӵ���D���������ˤf�K�C<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "�y���n�X�o�u���K�C�O�ֳo��j���H<br>") ;}
	else				{$log = ($log . "�k�Y�������Y���F���A���U�]�y�F�X�ӡK�C<br>") ;}
}elsif ($w_death =~ /�z��/) {
	if ($w_com eq 0)	{$log = ($log . "�b�o�@�a�a��A���骺�����}�H�������C�N�n���@���A���A�R���e���K�C<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "���}�Q���_�C���O�ݫ��骺���u�@���檬�Q�O����k�]���K�C<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "�O�Q���u�����F�ܡH�Y�M�k�åH�~�S�ݯd��L�������K�C<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "�O�Q���u�����F�ܡH�Y�����@�b�����S���F�K�C<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "�ѩ��z����y�O�Q���_���@����A�b5m�u�ʵۡK�C<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "�P�仡�O���餣�p���O�׶��K�C<br>") ;}
	else				{$log = ($log . "�Y�M��䤣��K�C�ѩ��z����y�Q�j���F�ܡK�C<br>") ;}
}elsif ($w_death =~ /����/) {
	if ($w_com eq 0)	{$log = ($log . "�n�������Q�������˸����A�۵ۡK�A�N�����_���I�l�F���K�C<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "�Q�g�����Y���P�����K�C�y����~�_�Ӫ��K�C<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "�Y���Q���_�A���Y��F�X�ӡK�C<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "�n���Q�ޥ��F���Y���A���y�I�b�a���̡A�˦Q�U�y�X�j�q����K�C<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "�Q�q�᭱�Ӫ��w���@�˪��F�襴�F�ܡH��F�Y�˵۪��K�C<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "�B�}���H�A��M���߬y�ʵۡC�n���q���e��E�P�a�Q���F�K�C<br>") ;}
	else				{$log = ($log . "�Y�Q�����a�����V��C��ˬݡA�Y������]�K�C<br>") ;}
}elsif ($w_death =~ /�r/) {
	if ($w_com eq 0)	{$log = ($log . "�b�f�W�٬y�ۤ@�Ǭr���K�H�]���æR����H�K�C<br>\n") ;}
	elsif ($w_com eq 1) {$log = ($log . "�q�f���y�ۦ�C�ݼˤl�A�ٹ��b�εۤ@�ˡK�C<br>\n") ;}
	elsif ($w_com eq 2) {$log = ($log . "�V��������y�����ܷ|��X��������C�O�Q�r�����K�C<br>\n") ;}
	elsif ($w_com eq 3) {$log = ($log . "�O�Q�r�����ܡH�q�f���Q�X�ۤj�q�e������w�K�C<br>\n") ;}
	elsif ($w_com eq 4) {$log = ($log . "�ܬr�P��h�W�ܡH�ۤv�E�P�a�Ϋ��Ҵ����۳��V�K�C<br>\n") ;}
	elsif ($w_com eq 5) {$log = ($log . "�O�Q����H�r�`�ܡH�ֽ��C���ܱo�S���S�¡K�C<br>\n") ;}
	else				{$log = ($log . "�ֽ��C���ܱo�D�`�Q�¡A�q�f���R�X�j�q����K�C<br>\n") ;}
} else					{$log = ($log . "�Y�G���_�u��۪��ˤl�K�C<br>") ;}
$log =							($log . "�п�ܪ��~�檺���e�K�C<br>") ;
$Command = "DEATHGET";

$chksts="OK";

}
#===================#
# �� �Բ��p��		#
#===================#
sub TACTGET {

$chkpnt = 5;	#�ġA�D��o���v
$chkpnt2 = 5;	#��������v
$atp = 1.00;
$dfp = 1.00;#					����			���s	  ȯ�o���v	 ��������v
if   ($tactics eq "��������"){$atp+=0.4;	$dfp-=0.4;}
elsif($tactics eq "���s����"){$atp-=0.4;	$dfp+=0.4;				$chkpnt2-=2;}
elsif($tactics eq "���K���"){$atp-=0.4;	$dfp-=0.4;	$chkpnt-=2;	$chkpnt2+=4;}
elsif($tactics eq "�������"){$atp-=0.2;	$dfp-=0.2;	$chkpnt+=4;	$chkpnt2+=4;}
elsif($tactics eq "�s�����"){				$dfp-=0.4;}
if ($arealist[5] eq "0")	 {$atp+=0.2;	$dfp+=0.3;	$chkpnt+=2;	$chkpnt2+=2;}	#�ִ�
elsif ($arealist[5] eq "1")  {$atp+=0.2;	$dfp+=0.1;	$chkpnt+=1;	$chkpnt2+=1;}	#��
elsif ($arealist[5] eq "2")  {;}													#�ܳ�
elsif ($arealist[5] eq "3")  {$atp-=0.02;	$dfp-=0.03;	$chkpnt-=0.2;$chkpnt2-=0.3;}#�B
elsif ($arealist[5] eq "4")  {$atp-=0.05;	$dfp-=0.03;	$chkpnt-=0.3;$chkpnt2-=0.5;}#���B
elsif ($arealist[5] eq "5")  {$atp-=0.07;	$dfp-=0.05;	$chkpnt-=0.7;$chkpnt2-=0.5;}#�x��
elsif ($arealist[5] eq "6")  {$atp-=0.07;	$dfp-=0.1;	$chkpnt-=1;	$chkpnt2-=0.7;}	#�p�B
elsif ($arealist[5] eq "7")  {$atp-=0.1;	$dfp-=0.15;	$chkpnt-=0.5;$chkpnt2+=1;}	#��
elsif ($arealist[5] eq "8")  {				$dfp-=0.2;	$chkpnt+=1;	$chkpnt2-=1;}	#��
elsif ($arealist[5] eq "9")  {$atp+=0.5;	$dfp-=0.3;				$chkpnt2-=1;}	#�@��
if ($arsts[$pls] eq "WU")	 {$atp+=0.1;}	#�����W
elsif ($arsts[$pls] eq "WD") {$atp-=0.1;}	#������
elsif ($arsts[$pls] eq "DU") {$dfp+=0.1;}	#���s�W
elsif ($arsts[$pls] eq "DD") {$dfp-=0.1;}	#���s��
elsif ($arsts[$pls] eq "SU") {$chkpnt+=1;}	#�o���W
elsif ($arsts[$pls] eq "SD") {$chkpnt-=1;}	#�o����

if ($inf =~ /��/) {$atp -= 0.2;}

local($kind) = $w_kind ;
local($wmei) = 0;
local($wweps) = "";

if(($kind =~ /G/)&&($w_wtai eq 0)){$wweps = "S";$wmei = 80;$wmei += int($wb/$BASE);}#�Ҵ�/�l�u�j
elsif($kind =~ /C/){$wweps = "M" ;$wmei = 70 ;$wmei += int($wc/$BASE);}#��
elsif($kind =~ /D/){$wweps = "L" ;$wmei = 50 ;$wmei += int($wd/$BASE);}#�z
elsif($kind =~ /G/){$wweps = "M" ;$wmei = 50 ;$wmei += int($wg/$BASE);}#��
elsif($kind =~ /S/){$wweps = "S" ;$wmei = 80 ;$wmei += int($ws/$BASE);}#�C
else 			   {$wweps = "S" ;$wmei = 70 ;$wmei += int($wp/$BASE);}#��

$weps = $wweps;
$mei = $wmei;

if ($inf =~ /�Y/) {$mei -= 20;}
}
#===================#
# �� �Բ��p��		#
#===================#
sub TACTGET2 {

$atn = 1.00;
$dfn = 1.00;
$sen = 1.0;#					����		  ���s		  ȯ�o���v		�_ŧ(��⪺���o��H�����v)
if	 ($w_ousen eq "��������"){$atn+=0.4;	$dfn-=0.4;				} 
elsif($w_ousen eq "���s����"){$atn-=0.4;	$dfn+=0.4;	$sen-=0.2;	}
elsif($w_ousen eq "���K���"){$atn-=0.4;	$dfn-=0.6;	$sen+=0.4;	}
#elsif($w_ousen eq "�������"){$atn-=0.4;	$dfn-=0.4;	$sen-=0.4;	}
#elsif($w_ousen eq "�s�����"){				$dfn-=0.6;	$sen-=0.3;	}
elsif($w_ousen eq "�v���M��"){				$dfn-=0.4;}
elsif($w_ousen eq "�k�]���A"){				$dfn-=0.2;}
if ($arealist[5] eq "0")	 {$atn+=0.2;	$dfn+=0.3;}	#�ִ�
elsif ($arealist[5] eq "1")  {$atn+=0.2;	$dfn+=0.1;}	#��
elsif ($arealist[5] eq "2")  {;}						#�ܳ�
elsif ($arealist[5] eq "3")  {$atn-=0.02;	$dfn-=0.03;}#�B
elsif ($arealist[5] eq "4")  {$atn-=0.05;	$dfn-=0.03;}#���B
elsif ($arealist[5] eq "5")  {$atn-=0.07;	$dfn-=0.05;}#�x��
elsif ($arealist[5] eq "6")  {$atn-=0.07;	$dfn-=0.1;}	#�p�B
elsif ($arealist[5] eq "7")  {$atn-=0.1;	$dfn-=0.15;}#��
elsif ($arealist[5] eq "8")  {				$dfn-=0.2;}	#��
elsif ($arealist[5] eq "9")  {$atn+=0.5;	$dfn-=0.3;}	#�@��
if ($arsts[$w_pls] eq "WU")   {$atn+=0.2;}#�����W
elsif ($arsts[$w_pls] eq "WD"){$atn-=0.2;}#������
elsif ($arsts[$w_pls] eq "DU"){$dfn+=0.2;}#���s�W
elsif ($arsts[$w_pls] eq "DD"){$dfn-=0.2;}#���s��

if($w_inf =~ /��/){$atn -= 0.1;}

local($kind) = $w_kind2 ;
local($wmei) = 0;
local($wweps) = "" ;

if (($kind = "G")&&($w_wtai eq 0)){$wweps = "S" ;$wmei = 80 ;$wmei += int($wb/$BASE);}#�l�u�j
elsif($kind =~ /C/){$wweps = "M" ;$wmei = 70 ;$wmei += int($wc/$BASE);}#��
elsif($kind =~ /D/){$wweps = "L" ;$wmei = 50 ;$wmei += int($wd/$BASE);}#�z
elsif($kind =~ /G/){$wweps = "M" ;$wmei = 50 ;$wmei += int($wg/$BASE);}#��
elsif($kind =~ /S/){$wweps = "S" ;$wmei = 80 ;$wmei += int($ws/$BASE);}#�C
else			   {$wweps = "S" ;$wmei = 70 ;$wmei += int($wp/$BASE);}#��

$weps2 = $wweps ;
$mei2 = $wmei ;

if ($w_inf =~ /�Y/) { $mei2 -= 20; }
}

1;
