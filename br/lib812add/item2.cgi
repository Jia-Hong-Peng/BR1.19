#==================#
# �� �D������      #
#==================#
sub ITEMJOUTO {
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
$sitei = $Command;
$sitei =~ s/SEITO_//g;
$wk2 = $Command2;
$wk2 =~ s/JO_//g;
$chk = "1" ;
for ($i=0; $i<$#userlist+1; $i++){($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $sitei){$chk = "0" ;last;}
}
if ($chk){&ERROR("�������X��","No such item exist","BATTLE-ITEMJOUTO");}
$Index2 = $i;
&BB_CK;
if ($wk2 =~ /MAIN/){#�Ǩ�
	if (length($dengon) > 0) {
		$log = ($log . "<font color=\"lime\"><b>$f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
		$w_log = ($w_log . "<font color=\"lime\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
	}
	$log = ($log . "$w_cl $w_sex$w_no�f $w_f_name $w_l_name��������C<br>\n") ;
}else{
	($in2, $ik2) = split(/<>/, $item[$wk2]);
	if ($item[$wk2] eq "�L") {&ERROR("�������X��","Item does not exist","BATTLE-ITEMJOUTO");}
	for ($j=0; $j<5; $j++) {if ($w_item[$j] eq "�L") {$chk = "OK" ; last;}}
	if ($chk eq "0") {$log = ($log . "���D����w���C<br>\n");}
	if ($chk eq "OK") {$w_item[$j] = $item[$wk2];$w_eff[$j] = $eff[$wk2];$w_itai[$j] = $itai[$wk2];
		$item[$wk2] = "�L";$eff[$wk2] = 0;$itai[$wk2] = 0;
		$log = ($log . "$w_cl $w_sex$w_no�f $w_f_name $w_l_name�N$in2�����C<br>\n") ;
		$w_log = ($w_log . "<font color=\"lime\"><b>$cl $sex$no�f $f_name $l_name�o��F$in2�C</b></font><br>") ;
		if (length($dengon) > 0) {
			$log = ($log . "<font color=\"lime\"><b>$f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
			$w_log = ($w_log . "<font color=\"lime\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
		}
		$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n";
		open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
	}
	else{ &ERROR("�������~�C�ЦV�޲z�����i�C","Internal Server Error","BATTLE-ITEMJOUTO") ; }
}
$Command = "MAIN";$Command2 = "";

$w_bid = $id ;$bid = $w_id ;

&SAVE;&SAVE2;
}
#==================#
# �� �D���z�@�@  #
#==================#
sub ITEMSEIRI {

local($wk) = $Command;
$wk =~ s/SEIRI_//g;
local($in, $ik) = split(/<>/, $item[$wk]);

local($wk2) = $Command2;
$wk2 =~ s/SEIRI2_//g;
local($in2, $ik2) = split(/<>/, $item[$wk2]);

if (($item[$wk] eq "�L")||($item[$wk2] eq "�L")) {
&ERROR("�������X�ݡC");
}

$log = ($log . "��z�D��C<br>") ;

if ($wk == $wk2) { #�P�D���ܡH
	$log = ($log . "$in���s��z�C<br>") ;
}elsif (($in eq $in2)&&($eff[$wk] eq $eff[$wk2])&&($ik =~ /HH|HD/)&&($ik2 =~ /HH|HD/)) { #��O�^�_�D��B�z
	$itai[$wk] = $itai[$wk] + $itai[$wk2];
	if (($ik eq "HD")||($ik2 eq "HD")) {
		$item[$wk] = "$in<>HD";
	}
	if(($ik eq "HD2")||($ik2 eq "HD2")) {
		$item[$wk] = "$in<>HD2";
	}
	$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
	$log = ($log . "$in�k���F�C<br>") ;
}elsif (($in eq $in2)&&($eff[$wk] eq $eff[$wk2])&&($ik =~ /SH|SD/)&&($ik2 =~ /SH|SD/)) { #��O�^�_�D��B�z
		$itai[$wk] = $itai[$wk] + $itai[$wk2];
	if (($ik eq "SD")||($ik2 eq "SD")) {
		$item[$wk] = "$in<>SD";
	}
	if(($ik eq "SD2")||($ik2 eq "SD2")) {
		$item[$wk] = "$in<>SD2";
	}
	$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
	$log = ($log . "$in�k���F�C<br>") ;
}elsif (($in eq $in2)&&($ik eq $ik2)&&(($ik =~ /WC|WD/)||($in =~ /�r��/))) { #�z���P�L�˪Z���P�r�ĳB�z
	$itai[$wk] = $itai[$wk] + $itai[$wk2];
	$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
	$log = ($log . "$in�k���F�C<br>") ;
}elsif ((($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y"))&&($in =~ /��|��/)) { #�l�u�P�b
	$eff[$wk] = $eff[$wk] + $eff[$wk2];
	$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
	$log = ($log . "$in�k���F�C<br>") ;
}else { #���P���D�㤣�Q�k��
$log = ($log . "$in�M$in2�����k���C<br>") ;
}

$Command = "MAIN";
$Command2 = "";

&SAVE;

}
#==================#
# �� �D��X���@�@  #
#==================#
sub ITEMGOUSEI {
$gousei=1;
$wk1 = $Command ;if ($wk1 eq "GOUSEI1_N"){$wk1 = "�L";$gousei--;}else{$wk1 =~ s/GOUSEI1_//g;($in1, $ik1) = split(/<>/, $item[$wk1]);}
$wk2 = $Command2;if ($wk2 eq "GOUSEI2_N"){$wk2 = "�L";$gousei--;}else{$wk2 =~ s/GOUSEI2_//g;($in2, $ik2) = split(/<>/, $item[$wk2]);}
$wk3 = $Command3;if ($wk3 eq "GOUSEI3_N"){$wk3 = "�L";$gousei--;}else{$wk3 =~ s/GOUSEI3_//g;($in3, $ik3) = split(/<>/, $item[$wk3]);}
if($gousei eq 0){if($wk1 eq "�L"){$wk1 = $wk3;$wk3 = "�L";$in1 = $in3;$in3 = "";$ik1 = $ik3;$ik3 = "";}elsif($wk2 eq "�L"){$wk2 = $wk3;$wk3 = "�L";$in2 = $in3;$in3 = "";$ik2 = $ik3;$ik3 = "";}if($wk3 ne "�L"){&ERROR("Internal Server ERROR");}}

if ($gousei < 0) {$log = ($log . "�S����ܹD��C<br>") ;}
else{$chk = "NG" ;

	if	 (($itai[$wk1] eq 1)||($itai[$wk1] eq "��")){$chk = "ON"; $itai[$wk1] eq 1;$j=$wk1;}
	elsif($ik1 =~ /DB|DH|DF|DA/){$chk = "ON";$j=$wk1;}
	elsif(($itai[$wk2] eq 1)||($itai[$wk2] eq "��")){$chk = "ON"; $itai[$wk2] eq 1;$j=$wk2;}
	elsif($ik2 =~ /DB|DH|DF|DA/){$chk = "ON";$j=$wk2;}
	elsif(($gousei eq 1)&&(($itai[$wk3] eq 1)||($itai[$wk3] eq "��"))){$chk = "ON"; $itai[$wk3] eq 1;$j=$wk3;}
	elsif(($gousei eq 1)&&($ik3 =~ /DB|DH|DF|DA/)){$chk = "ON";$j=$wk3;}
	else{for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}}

	if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;}
	else {#�D��X�����t2�ӡP3�ӡPERROR
		if($gousei eq 0){&ITEMGOUTWO;}
		elsif($gousei eq 1){&ITEMGOUTHREE;}
		else{&ERROR("Internal Server ERROR");}
	}
}
$Command = "MAIN";
$Command2 = "";

&SAVE;

}
#==================#
# �� �X��2		   #
#==================#
sub ITEMGOUTWO{
$log = ($log . "�X���D��C<br>") ;
if (($wk1 == $wk2)||($in1 eq $in2)) {$log = ($log . "�˵�$in1�C<br>");}#�P�D���ܡH
else{
	&ITEMTABLE;
	#�@��
	local($k) = 0;
	local($l) = $#g_item1+1;
	for ($k=0; $k<$l; $k++) {
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"name"} = "$g_name[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"kind"} = "$g_kind[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"eff"}  = "$g_eff[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"itai"} = "$g_itai[$k]";
	}
	if($gousei{$in1}{$in2}{name}){ #�ϥΦX��
		$log = ($log . "$in1�M$in2 $gousei{$in1}{$in2}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in1}{$in2}{name}<>$gousei{$in1}{$in2}{kind}";
		$eff[$j] = $gousei{$in1}{$in2}{eff} ;
		$itai[$j] = $gousei{$in1}{$in2}{itai} ;
		&ITEMCOUNT;
	}elsif($gousei{$in2}{$in1}{name}){ #�ϥΦX��(�f)
		$log = ($log . "$in1�M$in2 $gousei{$in2}{$in1}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in2}{$in1}{name}<>$gousei{$in2}{$in1}{kind}";
		$eff[$j] = $gousei{$in2}{$in1}{eff} ;
		$itai[$j] = $gousei{$in2}{$in1}{itai} ;
		&ITEMCOUNT;
	}else {$log = ($log . "$in1�M$in2����զX�C<br>") ;}#����X��
}
}
#==================#
# �� �X��3		   #
#==================#
sub ITEMGOUTHREE{
$log = ($log . "�X���D��C<br>") ;
if((($wk1 == $wk2)||($in1 eq $in2))||(($wk1 == $wk3)||($in1 eq $in3))) {$log = ($log . "�˵�$in1�C<br>");}#�P�D���ܡH
elsif(($wk2 == $wk3)||($in2 eq $in3)) {$log = ($log . "�˵�$in2�C<br>");}
else{
	&ITEMTABLE;
	#�@��
	local($k) = 0;
	local($l) = $#g_item1+1;
	for ($k=0; $k<$l; $k++){
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"$g_item3[$k]"}{"name"} = "$g_name[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"$g_item3[$k]"}{"kind"} = "$g_kind[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"$g_item3[$k]"}{"eff"}  = "$g_eff[$k]";
		$gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"$g_item3[$k]"}{"itai"} = "$g_itai[$k]";
	}
	if($gousei{$in1}{$in2}{$in3}{name}){ #�ϥΦX��1
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in1}{$in2}{$in3}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in1}{$in2}{$in3}{name}<>$gousei{$in1}{$in2}{$in3}{kind}";
		$eff[$j] = $gousei{$in1}{$in2}{$in3}{eff};
		$itai[$j] = $gousei{$in1}{$in2}{$in3}{itai};
		&ITEMCOUNT;
	}elsif($gousei{$in1}{$in3}{$in2}{name}){#�ϥΦX��2
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in1}{$in3}{$in2}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in1}{$in3}{$in2}{name}<>$gousei{$in1}{$in3}{$in2}{kind}";
		$eff[$j] = $gousei{$in1}{$in3}{$in2}{eff};
		$itai[$j] = $gousei{$in1}{$in3}{$in2}{itai};
		&ITEMCOUNT;
	}elsif($gousei{$in2}{$in1}{$in3}{name}){#�ϥΦX��3
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in2}{$in1}{$in3}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in2}{$in1}{$in3}{name}<>$gousei{$in2}{$in1}{$in3}{kind}";
		$eff[$j] = $gousei{$in2}{$in1}{$in3}{eff};
		$itai[$j] = $gousei{$in2}{$in1}{$in3}{itai};
		&ITEMCOUNT;
	}elsif($gousei{$in2}{$in3}{$in1}{name}){#�ϥΦX��4
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in2}{$in3}{$in1}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in2}{$in3}{$in1}{name}<>$gousei{$in2}{$in3}{$in1}{kind}";
		$eff[$j] = $gousei{$in2}{$in3}{$in1}{eff};
		$itai[$j] = $gousei{$in2}{$in3}{$in1}{itai};
		&ITEMCOUNT;
	}elsif($gousei{$in3}{$in2}{$in1}{name}){#�ϥΦX��5
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in3}{$in2}{$in1}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in2}{$in3}{$in1}{name}<>$gousei{$in3}{$in2}{$in1}{kind}";
		$eff[$j] = $gousei{$in3}{$in2}{$in1}{eff};
		$itai[$j] = $gousei{$in3}{$in2}{$in1}{itai};
		&ITEMCOUNT;
	}elsif($gousei{$in3}{$in1}{$in2}{name}){#�ϥΦX��6
		$log = ($log . "$in1�M$in2�M$in3 $gousei{$in3}{$in1}{$in2}{name}�����F�I<BR>");
		$item[$j] = "$gousei{$in3}{$in1}{$in2}{name}<>$gousei{$in3}{$in1}{$in2}{kind}";
		$eff[$j] = $gousei{$in3}{$in1}{$in2}{eff};
		$itai[$j] = $gousei{$in3}{$in1}{$in2}{itai};
		&ITEMCOUNT;
	}else {$log = ($log . "$in1�M$in2�M$in3����զX�C<br>") ;}#����X��
}
}
#==================#
# �� Item Count    #
#==================#
sub ITEMCOUNT{
if($wk1 eq $j){
	if($ik2 =~ /DB|DH|DF|DA/){$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}
	else{$itai[$wk2] -= 1;if ($itai[$wk2] <= 0) {$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}}
	if($gousei eq 1){
		if($ik3 =~ /DB|DH|DF|DA/){$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}
		else{$itai[$wk3] -= 1;if ($itai[$wk3] <= 0) {$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}}
	}
}elsif($wk2 eq $j){
	if($ik1 =~ /DB|DH|DF|DA/){$item[$wk1] = "�L"; $eff[$wk1] = 0; $itai[$wk1] = 0 ;}
	else{$itai[$wk1] -= 1;if ($itai[$wk1] <= 0) {$item[$wk1] = "�L"; $eff[$wk1] = 0; $itai[$wk1] = 0 ;}}
	if($gousei eq 1){
		if($ik3 =~ /DB|DH|DF|DA/){$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}
		else{$itai[$wk3] -= 1;if ($itai[$wk3] <= 0) {$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}}
	}
}elsif(($gousei eq 1)&&($wk3 eq $j)){
	if($ik1 =~ /DB|DH|DF|DA/){$item[$wk1] = "�L"; $eff[$wk1] = 0; $itai[$wk1] = 0 ;}
	else{$itai[$wk1] -= 1;if ($itai[$wk1] <= 0) {$item[$wk1] = "�L"; $eff[$wk1] = 0; $itai[$wk1] = 0 ;}}
	if($ik2 =~ /DB|DH|DF|DA/){$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}
	else{$itai[$wk2] -= 1;if ($itai[$wk2] <= 0) {$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}}
}else{
	if($ik =~ /DB|DH|DF|DA/){$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
	else{$itai[$wk] -= 1;if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}}
	if($ik2 =~ /DB|DH|DF|DA/){$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}
	else{$itai[$wk2] -= 1;if ($itai[$wk2] <= 0) {$item[$wk2] = "�L"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}}
	if($gousei eq 1){
		if($ik3 =~ /DB|DH|DF|DA/){$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}
		else{$itai[$wk3] -= 1;if ($itai[$wk3] <= 0) {$item[$wk3] = "�L"; $eff[$wk3] = 0; $itai[$wk3] = 0 ;}}
	}
}
}
#==================#
# �� Item Tablt    #
#==================#
sub ITEMTABLE{
#�D��X���μƾ�
#�X������1
@g_item1 = ("���o",	"�T�o",		"�H��",		"����",				"�N���l",			"�ⴣ�q��",		"�浰",		"�ѥ]");
#�X������2
@g_item2 = ("�ή�",	"�Ų~�l",		"����",		"�ɤ��u",			"������",				"�O��",	"�QĨ",		"�@��");
#�X������3
@g_item3 = ("�L",	"�L",			"�L",		"�L",				"�L",					"�L",			"�L",		"�L");
#�X���D��W��
@g_name = ("����",	"�����K�~��",	"�����u��",	"�����ġ�",	"��²�����K��g����",	"����PC",	"�QĨ��",	"�@���ѥ]");
#�X���D�����
@g_kind = ("Y",		"WD",			"WD",		"WD",				"WG",					"Y",			"SH",		"HH");
#�X���D��ĪG��
@g_eff = ("1",		"40",			"50",		"75",				"80",					"1",			"100",		"100");
#�X���D��@�[��
@g_itai = ("1",		"1",			"1",		"6",				"8",					"0",			"2",		"2");
}
1;
