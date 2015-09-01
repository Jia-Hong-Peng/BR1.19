#===========================#
# ■ �秘o訊消息登記處理	#
#===========================#
sub SEVE {
$Command="MAIN";$mode = "main";
#MESSENGER
#Saved Mess File			|	Num of Mess Saved|1 Mess Length|Maximum Mess Disp
$mes_file = "$LOG_DIR/mes.log";	$listmax = 100;	  $mes = 100;	$mesmax = 5;
# 輸入訊息核對
if ($Message eq "") {$log = ($log . "沒有任何訊息。<br>");return;}
elsif ($m_id eq "def_select") {$log = ($log . "沒有輸入訊息。<br>");return;}
elsif (length($m_id) > 38) { &ERROR("訊息的文字數超出上限。(最多19個全角字)") ; }
#@word = ("on9","西","狗","屌","撚","柒","76","仆","老母","老豆","幹","鳩","臭","含","蕭","家產","做愛","蕉","fuck","ｆｕｃｋ","fxck","fuxk");
#for ($i = 0;$i < 24;$i++)
#{
#if ($message =~ /@word[$i]/) {
#print &ERROR("訊息禁止輸入不雅字眼。");
#exit();
#}
#}
# 傳訊情報保存
open(DB,"$mes_file");seek(DB,0,0); @messagelist=<DB>;close(DB);
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);
$mes_time ="$hour時$min分";
unshift (@messagelist,"$id,$full_name,$m_id,$Message,$mes_time,\n");
if ($#messagelist >= $listmax) {pop (@messagelist);}
open(DB,">$mes_file"); seek(DB,0,0); print DB @messagelist; close(DB);
}
#===================#
# ■ 毒物混入處理	#
#===================#
sub POISON {
for ($i=0; $i<5; $i++) {if ($item[$i] =~ /毒藥/) {last ;}}
local($wk) = $Command;
$wk =~ s/POI_//g;
if (($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/) || ($item[$i] !~ /毒藥/)) {&ERROR("不正當的訪問。");}
$itai[$i]--;
if ($itai[$i] <= 0) {$item[$i] = "無"; $eff[$i] = $itai[$i] = 0 ;}
local($in, $ik) = split(/<>/, $item[$wk]);
$log = ($log . "$in混入了毒物。非常小心的樣子···。<br>") ;
if	  ($club eq "料理部") {
	if($item[$wk] =~ /<>H.*/){$item[$wk] =~ s/<>H.*/<>HD2-$id/g;}
	else{ $item[$wk] =~ s/<>S.*/<>SD2-$id/g; }
}elsif($item[5] eq "毒物制作書") {
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
# ■ 毒見處理		#
#===================#
sub PSCHECK {
local($wk) = $Command;
$wk =~ s/PSC_//g;
if(($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/)||($club ne "料理部")){&ERROR("不正當的訪問。");}
local($in, $ik) = split(/<>/, $item[$wk]);
if ($ik =~ /SH|HH/) {$log = ($log . "唔？ $in 看起來很安全···。<br>") ;}
else {$log = ($log . "唔？ $in 毒物快被混入了···。<br>") ;}
$sta -= $dokumi_sta ;
if ($sta <= 0) {&DRAIN("com");}#能量完了？
&SAVE ;
$Command = "MAIN" ;
}
#===================#
# ■ 毒物混入處理	#
#===================#
sub POISONDEAD {
if ($hit <= 0) {

$hit = 0;
$mem--;

$com = int(rand(6));
$poisonid="2Y0";

if ($poisondeadchk){local($tp, $poisonid) = split(/-/, $poisoni);}
else{$poisonid = $wb;}
#用戶文件取得
open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

#核對
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($poisonid eq $w_id) {#同一ID
		#經驗地-敵
		$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
		$Index2 = $i;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no番) 毒發身亡。【殘餘$mem人】</b></font><br>") ;
		$w_kill++;$w_bid = $id;&SAVE2;last;
	}
}

$log = ($log . "<font color=\"lime\"><b>$w_f_name $w_l_name『$w_msg』</b></font><br>") ;

local($b_limit) = ($battle_limit * 3) + 1;

if (($mem eq 1) && ($w_sts ne "NPC") && ($ar > $b_limit)){$w_inf = ($w_inf . "勝") ;}

#死亡狀態
&LOGSAVE("DEATH1") ;
$death = $deth ;

$bid = $w_id ;

&SAVE;


}
}
#==================#
# ■ 口頭語變更處理#
#==================#
#sub WINCHG {$msg = $msg2;$dmes = $dmes2 ;$com = $com2 ;$log = ($log . "口頭語變更完成。<br>");&SAVE;$Command = "MAIN";}
#==================#
# ■ 隊伍變更處理  #
#==================#
sub TEAM {
$teamold = $teamID;
if (length($teamID) > 24){&ERROR("口頭語的文字數超過上限。(最多12個全角字)","over length","BATTLE-TEAM");}
if (length($teamPass) > 18){&ERROR("口頭語的文字數超過上限。(最多8個全角字)","over length","BATTLE-TEAM");}
if ($teamID =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./){&ERROR("小組ID禁止使用文字進入。","taboo word","BATTLE-TEAM");}
if ($teamPass =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./){&ERROR("小組禁止使用文字密碼進入。","taboo word","BATTLE-TEAM");}

if ((($teamID2 eq $teamID))&&(($teamPass2 eq "")||($teamPass2 eq "就這樣不變更情況"))){;}
elsif ((($teamID2 eq "無")&&($teamPass2 eq "無"))||(($teamID2 eq "『無』")&&($teamPass2 eq "『無』"))){$teamID = "無";$teamPass = "無";&LOGSAVE("G-DATT");$log = ($log . "脫離小組。<br>") ;}
elsif (($teamID2 eq "")||($teamPass2 eq "")||($teamID2 eq "無")||($teamPass2 eq "無")||($teamID2 eq "『無』")||($teamPass2 eq "『無』")){&ERROR("要脫離小組。請把<BR>小組名．密碼雙方設為『無』。<br>","No Grop Name Entered","BATTLE-TEAM");}
elsif ($teamID ne $teamID2){
	if ($teamID ne "無"){&ERROR("要組成．加入新小組，應先脫離現在的小組。<br>","Need to get out before get in","BATTLE-TEAM");}
	elsif (($teamPass2 eq "就這樣不變更情況")||($teamPass2 eq "")){&ERROR("請輸入密碼。<br>","No Password has been entered","BATTLE-TEAM");}
	elsif ($teamPass2 eq $teamID2){&ERROR("小組名和密碼請不要相同。<br>","Group Name is same as Pass","BATTLE-TEAM");}
	elsif (($teamPass2 =~ /$teamID2/)||($$teamID2 =~ /teamPass2/)){&ERROR("小組名和密碼相似。<br>","Group Name and Pass is similar","BATTLE-TEAM");}
	#get User file
	open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
	#Same Name and ID check
	$ng = 0;
	foreach $userlist(@userlist) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist);
		if (($teamID2 eq $w_teamID)&&(($teamPass2 ne $w_teamPass)&&($w_sts ne "死亡"))) {&ERROR("同樣小組名存在，密碼不同。","Same Group Exists or Pass miss-match","BATTLE-TEAM");}
		elsif (($teamID2 eq $w_teamID)&&($teamPass2 eq $w_teamPass)) {$ng++;}
	}
	if ($ng eq 0){&LOGSAVE("G-JOIN");$teamID = $teamID2;$teamPass = $teamPass2;$log = ($log . "組成了小組 $teamID。");}
	elsif ($ng > 5){&ERROR("小組最大人數5人。<br>","Max Group Number","BATTLE-TEAM");}
	else {&LOGSAVE("G-KANYU");$teamID = $teamID2;$teamPass = $teamPass2;$log = ($log . "加入小組 $teamID 了。");}
}
&SAVE ;

$Command = "MAIN" ;
}
#==================#
# ■ 應急措施處理  #
#==================#
sub OUKYU {

local($wk) = $Command;
$wk =~ s/OUK_//g;

if	  ($wk eq 0) {$inf =~ s/頭//g ;}#頭
elsif ($wk eq 1) {$inf =~ s/腕//g ;}#腕
elsif ($wk eq 2) {$inf =~ s/腹//g ;}#腹
elsif ($wk eq 3) {$inf =~ s/足//g ;}#足

$log = ($log . "做了應急措施。<BR>") ;

$sta -= $okyu_sta ;

if ($sta <= 0) {&DRAIN("com");}#能量完了？

&SAVE ;

$Command = "MAIN" ;
}
#==================#
# ■ 基本方針變更  #
#==================#
sub KOUDOU {

local($wk) = $Command;
$wk =~ s/KOU_//g;
$old_tactics = $tactics;

if	 ($wk eq 1)	{$tactics = "攻擊重視";}
elsif($wk eq 2)	{$tactics = "防御重視";}
elsif($wk eq 3)	{$tactics = "隱密行動";}
elsif($wk eq 4)	{$tactics = "探索行動";}
elsif($wk eq 5)	{$tactics = "連鬥行動";}
else			{$tactics = "通常";}

$log = ($log . "基本方針由 $old_tactics 變更為 $tactics。<BR>\n") ;

&SAVE ;

$Command = "MAIN" ;
}
#==================#
# ■ 應戰方針變更  #
#==================#
sub OUSEN {

local($wk) = $Command;
$wk =~ s/OUS_//g;
$old_ousen = $ousen;

if		($wk eq 1)	{$ousen = "攻擊姿態";}
elsif	($wk eq 2)	{$ousen = "防御姿態";}
elsif	($wk eq 3)	{$ousen = "隱密行動";}
#elsif	($wk eq 4)	{$ousen = "探索行動";}
#elsif	($wk eq 5)	{$ousen = "連鬥行動";}
elsif	($wk eq 6)	{$ousen = "治療專念";}
elsif	($wk eq 7)	{$ousen = "逃跑姿態";}
else				{$ousen = "通常";}

$log = ($log . "應戰方針由 $old_ousen 變更為 $ousen。<BR>\n") ;

&SAVE ;

$Command = "MAIN" ;
}
#=====================#
# ■ 攜帶揚聲器使用   #
#=====================#
sub SPEAKER {
for ($i=0; $i<5; $i++){if ($item[$i] =~ /攜帶揚聲器/) {last;}}
if ($item[$i] !~ /攜帶揚聲器/) {&ERROR("不正當的訪問。");}

$log = ($log . " $speech<BR>");
$log = ($log . " 完整地傳達了嗎？<BR>");
open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$namae = "$f_name $l_name" ;
$gunlog[2] = "$now,$place[$pls],$namae,$speech,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

$Command = "MAIN" ;

}
#=====================#
# ■ hacking處理   #
#=====================#
sub HACKING{
for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "移動PC<>Y")&&($itai[$paso] >= 1)) {$junbi = 0;last;}}

if (($Command ne "SPECIAL")||($Command4 ne "HACK")) {&ERROR("不正當的訪問。");}

local($bonus) = 10;local($dice1) = int(rand(99)) ;local($dice2) = int(rand(10)) ;

if ($club =~ /電腦部/){$bonus = 15;} #個人電腦部的基本成功率

local($kekka) = $bonus;
$log = ($log . "嘗試了Hacking…");
if ($dice1 <= $kekka){	 #Hacking成敗判斷
	open(DB,"$area_file");seek(DB,0,0); my(@wk_arealist)=<DB>;close(DB);
	my($wk_ar,$wk_hack,$wk_a) = split(/,/, $wk_arealist[1]);  #Hacking標誌取得
	$wk_hack = 1;
	$wk_arealist[1] = "$wk_ar,$wk_hack,\n";
	open(DB,">$area_file"); seek(DB,0,0); print DB @wk_arealist; close(DB);
	$log = ($log . "Hacking\成\功\！全部的禁止區域被解除了!!<BR>") ;
	&LOGSAVE("HACK") ;
}else{$log = ($log . "可是，Hacking失敗了…<BR>") ;}

for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "移動PC<>Y")&&($itai[$paso] >= 1)){ last; }}

if ($dice1 >= 95){   #電池消耗&漏接時機材破壞
	$item[$paso] = "無"; $eff[$paso] = $itai[$paso] = 0 ;
	$log = ($log . "什麼啦！機械材料壞了。<BR>") ;
	if ($dice2 >= 9){  #政府項圈爆破！
		$hit = 0 ; $sts = "死亡"; $death = $deth = "政府的處刑";$mem--;
		if ($mem == 1) {open(FLAG,">$end_flag_file"); print(FLAG "終了\n"); close(FLAG);}
		&LOGSAVE("DEATH5") ;
		open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
		$gunlog[1] = "$now,$place[$pls],$id,,\n";
		open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
		$log = ($log . "什麼啦！機械材料壞了。<BR><br>是…什麼？從…項圈發出警告的聲響…!?<BR><BR><font color=\"red\">···!!···<br><br><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;
	}
}else{$itai[$paso] --;if ($itai[$paso] == 0) {$log = ($log . "用盡了移動PC電池的電力。<BR>") ;}}

&SAVE;
}
1;
