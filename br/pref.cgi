#�X�ݸT��
$host1 = &GetHostName($ENV{'REMOTE_ADDR'});
$host2 = $ENV{'REMOTE_ADDR'};
if (($host1 eq $host2)||($host1 eq "")) {$host = "$host2";}else{$host = "$host1-$host2";}
local ($oklist) = 0;
foreach $oklist(@oklist){if($host2 eq $oklist){$okflg = 1;}}
#�X�ݸT��ֹ�
if ($okflg eq 0){foreach $kick(@kick){if (($host1 =~ /$kick/)||($host2 eq $kick)){&ERROR("���ʤ��Υۥ��Ȥϥ��������ػߤȤʤäƤ��뤫���ۥ��Ȥ�Ƚ�̽���ޤ���<BR>�����ͤˤ��䤤��碌����������<BR>HOST ID:$host, $host2");}}}
#�޲z���Ū�J
$areafile=$area_file;
open(DB,"$area_file");seek(DB,0,0); @arealist=<DB>;close(DB);
open(FLAG,$end_flag_file) || exit; $fl=<FLAG>; close(FLAG);

($y,$m,$d,$hh,$mm) = split(/,/, $arealist[0]);
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
$month++;$year += 1900;
#if (($year eq $y) &&($month eq $m)&&($mday > $d)&& ($fl !~ /�פF/)){&ERROR("Internal Server ERROR","Please contact with Administrator","�T��ϰ�l�[���~") ;}#�T��ϰ�ץ��@��
if	 (($year eq $y)&&($month eq $m)&&($mday eq $d)&&($hour >= $hh+24)&&($fl !~ /�פF/)){&ADDKINSHI2;&ADDKINSHI2;&ADDKINSHI2;&ADDKINSHI;}#�T��ϰ�ץ��@��
elsif(($year eq $y)&&($month eq $m)&&($mday eq $d)&&($hour >= $hh+16)&&($fl !~ /�פF/)){&ADDKINSHI2;&ADDKINSHI2;&ADDKINSHI;}#�T��ϰ�ץ�16�p��
elsif(($year eq $y)&&($month eq $m)&&($mday eq $d)&&($hour >= $hh+8)&&($fl !~ /�פF/)){&ADDKINSHI2;&ADDKINSHI;}#�T��ϰ�ץ�8�p��
elsif(($year eq $y)&&($month eq $m)&&($mday eq $d)&&($hour >= $hh)&&($fl !~ /�פF/)){&ADDKINSHI;}#�T��ϰ�l�[�H
else {($ar,$hackflg,$a) = split(/,/,$arealist[1]) ;}
#Re-get time
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
$month++;$year += 1900;
#�� Stamina Max
if ($ar >= 4){$maxsta = 500;}
else{$maxsta = 300;}

($secc,$minc,$hourc,$mdaycook,$monthc,$yearc,$wdayc,$ydayc,$isdstc) = localtime($now + $save_limit*86400);
$weekcook = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') [$wdayc];
$mdaycook = "0$mdaycook" if ($mdaycook < 10);
$monthcook = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec') [$monthc];
$yearcook = $yearc+1900;
$expires = "$weekcook, $mdaycook-$monthcook-$yearcook 00:00:00 GMT";
#==================#
# �� �T��ϰ�l�[  #
#==================#
sub ADDKINSHI {
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now+(1*60*60*8));
$month++;$year += 1900;
if (($hour >= 4)&&($hour < 12)){$hour = 8;}
elsif (($hour >= 12)&&($hour < 20)){$hour = 16;}
elsif (($hour >= 20)&&($hour < 4)){$hour = 0;}
else {$hour = 0;}
local($weth) = int(rand(10));
if (($weth < 0)&&($weth > 9)){$weth = "0";}
$newareadata[0] = "$year,$month,$mday,$hour,0\n";	#�ϰ�l�[�ɨ�
($ar,$hackflg,$a) = split(/,/,$arealist[1]) ;
$ar2 = $ar + 1;
$newareadata[1] = "$ar2,0,\n";#�T��ϰ��
$newareadata[2] = $arealist[2];
$newareadata[3] = $arealist[3];
$newareadata[4] = $arealist[4];
$newareadata[5] = "$weth\n";
$newareadata[6] = $arealist[6];
open(DB,">$areafile"); seek(DB,0,0); print DB @newareadata; close(DB);

($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);

#�T��ϰ�l�[���A
&LOGSAVE("AREAADD");

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
#TEMP�O�s
open(DB,">$back_file"); seek(DB,0,0); print DB @userlist1; close(DB);
#�T��ϰ�̦��`�B�z
for ($cnt=0; $cnt<$ar2; $cnt++) {
	for ($i=0; $i<$#userlist+1; $i++) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
		if (($place[$w_pls] eq $place[$ara[$cnt]]) && ($w_hit > 0) && ($fl !~ /�פF/)){#�ͦs&����&�T��ϰ�H
			if	 ($ar eq 4){$w_sta += 200;}#�̤j��qUP
			if	 (($w_sts eq "NPC")&&($ar2 < 21)&&($w_f_name eq "�L�h")) {$w_pls = $ara[$ar2 + int(rand(21 - $ar2)) + 1];}#�L�h�۰ʦ^��
			elsif(($w_sts eq "NPC")&&($w_f_name =~ /�O��|�ʬd��/)){;}#�O���A�ʬd�S���B�z
			elsif(($w_sts ne "NPC")&&($w_f_name ne "�L�h")&&($w_ousen eq "�k�`")){$w_pls = $ara[$ar2 + int(rand(21 - $ar2)) + 1];}#�k�`���Ԧ۰ʦ^��
			else{&LOGSAVE("DEATHAREA");$w_hit=0;$w_death=$deth;}#NPC�H�~���`
			if ($ar2 eq 19){$w_teamID=$w_teamPass="�L";}
			$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
		}elsif($ar2 eq 4){$w_sta += 200;}#�ͦs�̪��̤j��qUP
	}
}
open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
#Back Up
$back_file = "$LOG_DIR/BUF_$hour.log";
open(DB,">$back_file"); seek(DB,0,0); print DB @userlist; close(DB);
}
#========================#
# �� �T��ϰ�l�[(�ץ�)  #
#========================#
sub ADDKINSHI2 {
if ($hh eq 0){$hour = 8;}
elsif ($hh eq 8){$hour = 16;}
elsif ($hh eq 16){$hour = 0;}
else {$hour = 0;}
$newareadata[0] = "$year,$month,$mday,$hour,0";	#�ϰ�l�[�ɨ�
($ar,$hackflg,$a) = split(/,/,$arealist[1]) ;
$ar2 = $ar + 1;
$newareadata[1] = "$ar2,0,\n" ;#�T��ϰ��
$newareadata[2] = $arealist[2] ;
$newareadata[3] = $arealist[3] ;
$newareadata[4] = $arealist[4] ;
$newareadata[5] = $arealist[5] ;
$newareadata[6] = $arealist[6] ;

($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);
open(DB,">$area_file"); seek(DB,0,0); print DB @newareadata; close(DB);

#�T��ϰ�l�[���A
&LOGSAVE("AREAADD") ;

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
#�T��ϰ�l�[���(�O��)
for ($cnt=0; $cnt<$ar2; $cnt++) {
	for ($i=0; $i<$#userlist+1; $i++) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
		if (($place[$w_pls] eq $place[$ara[$cnt]]) && ($w_hit > 0) && ($fl !~ /�פF/)){#�ͦs&����&�T��ϰ�H
			if	 ($ar eq 4){$w_sta += 200;}#�̤j��qUP
			if	 (($w_sts eq "NPC")&&($ar2 < 21)&&($w_f_name eq "�L�h")) {$w_pls = $ara[$ar2 + int(rand(21 - $ar2)) + 1];}#�L�h�۰ʦ^��
			elsif(($w_sts eq "NPC")&&($w_f_name =~ /�O��|�ʬd��/)){;}#�O���A�ʬd�S���B�z
			elsif(($w_sts ne "NPC")&&($w_f_name ne "�L�h")&&($w_ousen eq "�k�`")){$w_pls = $ara[$ar2 + int(rand(21 - $ar2)) + 1];}#�k�`���Ԧ۰ʦ^��
			else{&LOGSAVE("DEATHAREA");$w_hit=0;$w_death=$deth;}#NPC�H�~���`
			if ($ar2 eq 19){$w_teamID=$w_teamPass="�L";}
			$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
		}
	}
}
if ($hh eq 0){$hh = 8;}
elsif ($hh eq 8){$hh = 16;}
elsif ($hh eq 16){$hh = 0;}
else {$hour = 0;}
open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
@arealist=@newareadata;
}
1;
