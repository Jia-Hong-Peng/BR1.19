#==================#
# ■ 移動		   #
#==================#
sub MOVE {

local($mv) = $Command2;
$mv =~ s/MV//g ;

#移動前處理
$Command = "MAIN";
$Command2 = "";

$ok = 1;if (($inf =~ /足/)&&($sta > 18)) {$ok = 0;} elsif (($club eq "田徑部")&&($sta > 10)) {$ok = 0;} elsif ($sta > 13) {$ok = 0;}
if ($ok){$log = ($log . "能量不足不能移動…"); return ;}

if ($inf =~ /足/) {$sta -= int(rand(5) + 13) ;}
elsif ($club eq "田徑部") {$sta -= int(rand(5))+6 ;}
else {$sta -= int(rand(5))+8 ;}

($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21]) = split(/,/, $arealist[2]);
($war,$a) = split(/,/, $arealist[1]);
if($ar[$war] eq $place[$mv]) {
	$log = ($log . "$place[$mv]移動了。<br>這裡成為了禁止區域。<br>$arinfo[$mv]<br>") ;
} elsif(($ar[$war+1] eq $place[$mv])||($ar[$war+2] eq $place[$mv])) {
	$log = ($log . "$place[$mv]移動了。<br>這裡成為了禁止區域。<br>$arinfo[$mv]<br>") ;
} else {
	for ($i=0; $i<$war; $i++){if (($ar[$i] eq $place[$mv])&&($hackflg eq 0)&&($sts !~ /NPC/)){$log = ($log . "$place[$mv]是禁止區域。不能移動…。<BR>");return;}}#禁止移動？
	$log = ($log . "$place[$mv]移動了。<BR>$arinfo[$mv]<br>") ;
}

$pls = $mv;#移動

if($inf =~ /毒/){local($minus) = int(rand(8));$hit -= $minus;$log = ("毒發影響體力減少了 $minus。<BR>");require "$LIB_DIR/lib3.cgi";&POISONDEAD;}
if($sta <= 0){&DRAIN("mov");}#能量完了？
&SEARCH2;
&SAVE;
}
#==================#
# ■ 探索處理	   #
#==================#
sub SEARCH {

$ok = 1;if (($inf =~ /足/)&&($sta > 25)) {$ok = 0;} elsif (($club eq "田徑部")&&($sta > 15)) {$ok = 0;} elsif ($sta > 20) {$ok = 0;}
if ($ok){$log = ($log . "能量不足不能探索…") ; return ;}

$log = ($log . "$l_name，附近探索…。<br>") ;

if ($inf =~ /足/) {$sta -= int(rand(5) + 20) ;}
elsif ($club eq "田徑部") {$sta -= int(rand(5))+10;}
else {$sta -= int(rand(5))+15 ;}

if ($inf =~ /毒/) {
	local($minus) = int(rand(8));
	$hit -= $minus;
	$log = ("毒發影響體力減少了 $minus。<BR>");
	require "$LIB_DIR/lib3.cgi";
	&POISONDEAD;
}

if ($sta <= 0) {&DRAIN("mov");}#能量完了？

&SEARCH2;

if ($chksts ne "OK") {$log = ($log . "可是，沒找到什麼。<BR>") ;$Command = "MAIN" ;}

&SAVE;
}
#==================#
# ■ 探索處理2     #
#==================#
sub SEARCH2 {

local($i) = 0 ;
srand(time ^ $i) ;

srand($now);
local($a) = int(rand(1));		#敵人哪兒發現道具
local($dice1) = int(rand(10));	#敵人，道具發現

&TACTGET ;

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

$chksts="NG";$chksts2="NG";

if ($dice1 <= 5) {	#敵發見？
	for ($i=0; $i<$#userlist+1; $i++) {
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
		$w_bid2 = $w_bid;
		if($tactics eq "連鬥行動"){
			$w_bid2 = "";local($randam) = int(rand(100));
			$randam_set = 50;
			if($w_tactics ne "連鬥行動"){$randam_set = 75;}
			if($randam >= $randam_set){$w_bid2 = $w_bid;}
		}
		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid2 ne $id)){push @plist, $i;}
	}

#	for ($i=0;$i<@plist+5;$i++){push(@plist,splice(@plist,int(rand @plist+0),1));}
	#FIXED BY: (海蜇舖)
	@plist2 = ();
	for(@plist){
		my $r = rand @plist2+1;
		push(@plist2,$plist2[$r]);
		$plist2[$r] = $_;
	}

	foreach $i(@plist2){
		local($dice2) = int(rand(10)) ;	#敵人，道具發現
		local($dice3) = int(rand(10)) ;	#先制攻擊
		local($dice6) = int(rand(100)) ;	#視野
		($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);

#連鬥
		$w_bid2 = $w_bid;
		if ($tactics eq "連鬥行動") {$w_bid2 = "";}
#		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid ne $id)) {	#地方一致？
		if (($w_pls eq $pls) && ($w_id ne $id) && ($w_bid2 ne $id)) {	#地方一致？

			&TACTGET2;local($chk) = int($dice2 * $sen);

			if ($chk < $chkpnt) {
				if ($w_hit > 0) {#生存？
					require "$LIB_DIR/attack.cgi";$wf = $w_id;	#瀏覽器背部對應　↓隊伍
					if(($teamID ne "無")&&($teamID ne "")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){#轉讓
						&ATTJYO ;$chksts="OK";$chksts2="NG";last;
					}elsif($dice3 <= $chkpnt2){					#先制攻擊
						&ATTACK ;$chksts="OK";$chksts2="NG";last;
					}else{										#後攻攻擊 (奇襲)
						$Index2 = $i;$w_bid = $id ;$bid = $w_id ;
						&ATTACK2 ;$chksts="OK";$chksts2="NG";last;
					}
				} else {#屍體發現
					local($chkflg) = 0 ;
					local($dice4) = int(rand(10));
					if ($dice4 > 6){
						for ($j=0; $j<6; $j++) {if ($w_item[$j] ne "無" && $w_item[$j] ne "") {$chkflg=1;last;}}
						if ($chkflg){
							if ($w_wep !~ /空手/ || $w_bou !~ /內衣/ || $w_bou_h ne "無" || $w_bou_f ne "無" ||$w_bou_a ne "無"){
								$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,-1,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
								open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
								$wf = $w_id; #瀏覽器背部對應
								&DEATHGET;last;
							}
						}
					}
				}
			}else{ $chksts2="OK";}
		}
	}
	if ($chksts2 eq "OK") {#道具發現．空
		local($dice5) = int(rand(10));#道具發現
		if (($dice5 <= 5)&&($Command eq "SEARCH")) {require "$LIB_DIR/item1.cgi";&ITEMGET;}
		elsif ($chksts2 eq "OK") {$log = ($log . "什麼人潛藏著…。兵士嗎？<BR>") ;}
	}
} else {	#活動．道具發現
	$dice2 = int(rand(8)) ;
	if (($dice2 < $chkpnt)&&($Command eq "SEARCH")) {require "$LIB_DIR/item1.cgi";&ITEMGET;}#道具發現
	else{require "$LIB_DIR/event.cgi";&EVENT ;}
}

}
#===================#
# ■ 戰利品取得 	#
#===================#
sub WINGET {
if ($item[$itno2] ne "無" or $itno2>4 or $itno2<0) {$log = ($log . "所持品超過上限。<br>") ;$Command = "MAIN";return;}
if ($getid eq $id){$log = ($log . "自己奪取自己的攜帶品。<br>...。<br>") ;$Command = "MAIN";return;}

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
		&BB_CK;#瀏覽器背部對應
		if ($w_hit>0){$log = ($log . "想要$w_f_name的所持物品意欲非常強烈。<br>...。<br>") ;$Command = "MAIN";return;}
		if		($wk eq 6)	{($witem,$weff,$witai) = ($w_wep,$w_watt,$w_wtai);$w_wep = "空手<>WP"; $w_watt = 0; $w_wtai = "∞";}
		elsif	($wk eq 7)	{($witem,$weff,$witai) = ($w_bou,$w_bdef,$w_btai);$w_bou = "內衣<>DN"; $w_bdef = 0; $w_btai = "∞";}
		elsif	($wk eq 8)	{($witem,$weff,$witai) = ($w_bou_h,$w_bdef_h,$w_btai_h);$w_bou_h = "無"; $w_bdef_h = $w_btai_h = 0;}
		elsif	($wk eq 9)	{($witem,$weff,$witai) = ($w_bou_f,$w_bdef_f,$w_btai_f);$w_bou_f = "無"; $w_bdef_f = $w_btai_f = 0;}
		elsif	($wk eq 10)	{($witem,$weff,$witai) = ($w_bou_a,$w_bdef_a,$w_btai_a);$w_bou_a = "無"; $w_bdef_a = $w_btai_a = 0;}
		else				{($witem,$weff,$witai) = ($w_item[$wk],$w_eff[$wk],$w_itai[$wk]);$w_item[$wk] = "無"; $w_eff[$wk]=$w_itai[$wk] = 0;}
		$userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$id,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,\n" ;
		open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
		$wingetck=0;
		last;
	}
}
if($wingetck){&ERROR("內部錯誤，請向管理員報告。","WINGET INTERNAL ERROR","BATTLE-WINGET");}
if ($witem!~/^(無|空手|內衣)$/ && $i!=$#userlist+1){
	$item[$itno2] = $witem ;
	$eff[$itno2] = $weff; $itai[$itno2] = $witai ;
	($witem)=split(/<>/,$witem,2);
	$log = ($log . "$l_name 得到了 $witem。<BR>") ;
}else{$log = ($log . "放棄撿拾。<BR>") ;}

&SAVE;&SAVE2;

$Command = "MAIN";
}
#==================#
# ■ 屍體發現處理  #
#==================#
sub DEATHGET {

$log = ($log . "$w_f_name $w_l_name的屍體發現。<br>") ;

if ($w_death =~ /劍殺/) {
	if ($w_com eq 0)	{$log = ($log . "屍體的頭部和軀幹分離…。好像被什麼兵刃砍斷。<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "腹部像被銳利刀刃破開，內臟不斷流出來…。<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "從肩膀到胸口漂亮地被切開。傷口非常齊口…。<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "頭．軀幹．雙臂．兩腳都被分割。這樣的事是神志清醒的人能做嗎…。<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "臉部被集中地切碎。完全難以分辨生前的時的面貌…。<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "腹部被切開，不過，仔細看的話手腕多處地方也有刀傷…。<BR>是殺了對手之後而自殺的嗎？<br>") ;}
#	elsif ($w_com eq 0) {$log = ($log . "全身被什麼銳利武器造成大量的刺傷…。屍體的周圍，血流成河…。<br>") ;}
#	elsif ($w_com eq 1) {$log = ($log . "屍體被刺了好多次好多次的痕跡…。<br>") ;}
#	elsif ($w_com eq 2) {$log = ($log . "一擊刺中心臟。至今還從傷血湧出…。好像剛剛才被殺一樣。<br>") ;}
#	elsif ($w_com eq 3) {$log = ($log . "把喉嚨割破的…。眼珠還在反白…。<br>") ;}
#	elsif ($w_com eq 4) {$log = ($log . "從後面被刺進腹部。是突然襲擊嗎…？<br>") ;}
#	elsif ($w_com eq 5) {$log = ($log . "左腹部有嚴重傷痕。刺了之後，像被挖了什麼一樣的傷…。<br>") ;}
#	else				{$log = ($log . "雙目被刺…。好像流著血淚一樣…。<br>") ;}
	else				{$log = ($log . "從頭到胸淒慘地被切開…。<br>") ;}
}elsif ($w_death =~ /鎗傷/) {
	if ($w_com eq 0)	{$log = ($log . "胸…中3發，額1發的彈痕…。額的一發鎗傷好像是真正致命的…。<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "腹部有數發彈痕，血流出了。可是，那些血已經乾了。<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "頭部不見了，但屍體狀似跑著的…。只能從姓名牌知道死者的名字。<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "胸數發。並且，流著腦髓。大概殺了之後，塞進槍在口部射擊。做著戲弄的事…。<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "腹部處有孔，可以看見。這個絕對遭到鎗擊的傷口…。<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "臉有好幾發彈痕…。是誰這麼大怨恨？<br>") ;}
	else				{$log = ($log . "右頭部受到嚴重轟擊，腦袋也流了出來…。<br>") ;}
}elsif ($w_death =~ /爆殺/) {
	if ($w_com eq 0)	{$log = ($log . "在這一帶地方，身體的支離破碎的場面。就好像一塊鮮紅艷麗的畫布…。<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "雙腳被炸斷。但是看屍體的手臂作爬行狀想是打算逃跑的…。<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "是被炸彈攻擊了嗎？頭和右腕以外沒殘留其他的部份…。<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "是被炸彈攻擊了嗎？頭部的一半部份沒有了…。<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "由於爆炸氣流令被炸斷的一隻手，在5m滾動著…。<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "與其說是屍體不如說是肉塊…。<br>") ;}
	else				{$log = ($log . "頭和手找不到…。由於爆炸氣流被吹飛了嗎…。<br>") ;}
}elsif ($w_death =~ /撲殺/) {
	if ($w_com eq 0)	{$log = ($log . "好像不知被什麼壓倒腹部，蹲著…，就那樣斷絕呼吸了的…。<br>") ;}
	elsif ($w_com eq 1) {$log = ($log . "被狂打著頭部致死的…。臉紫色腫起來的…。<br>") ;}
	elsif ($w_com eq 2) {$log = ($log . "頭骨被折斷，骨頭扎了出來…。<br>") ;}
	elsif ($w_com eq 3) {$log = ($log . "好像被毆打了後頭部，把臉埋在地面裡，倒吊下流出大量的血…。<br>") ;}
	elsif ($w_com eq 4) {$log = ($log . "被從後面來的鈍器一樣的東西打了嗎？抱了頭倒著的…。<br>") ;}
	elsif ($w_com eq 5) {$log = ($log . "額破打碎，血和腦漿流動著。好像從正前方激烈地被打了…。<br>") ;}
	else				{$log = ($log . "頭被狠狠地打的向橫。怎樣看，頭的骨折也…。<br>") ;}
}elsif ($w_death =~ /毒/) {
	if ($w_com eq 0)	{$log = ($log . "在口上還流著一些毒物…？也有嘔吐的跡象…。<br>\n") ;}
	elsif ($w_com eq 1) {$log = ($log . "從口部流著血。看樣子，還像在睡著一樣…。<br>\n") ;}
	elsif ($w_com eq 2) {$log = ($log . "向屍體挨近臉部的話會嗅出杏仁氣味。是被毒死的…。<br>\n") ;}
	elsif ($w_com eq 3) {$log = ($log . "是被毒死的嗎？從口部噴出著大量攙雜的血泡…。<br>\n") ;}
	elsif ($w_com eq 4) {$log = ($log . "喝毒感到痛苦嗎？自己激烈地用指甲揪掉著喉嚨…。<br>\n") ;}
	elsif ($w_com eq 5) {$log = ($log . "是被什麼人毒害嗎？皮膚顏色變得又紫又黑…。<br>\n") ;}
	else				{$log = ($log . "皮膚顏色變得非常烏黑，從口中吐出大量的血…。<br>\n") ;}
} else					{$log = ($log . "淒慘仰起滾轉著的樣子…。<br>") ;}
$log =							($log . "請選擇物品欄的內容…。<br>") ;
$Command = "DEATHGET";

$chksts="OK";

}
#===================#
# ■ 戰略計算		#
#===================#
sub TACTGET {

$chkpnt = 5;	#敵，道具發見率
$chkpnt2 = 5;	#先制攻擊率
$atp = 1.00;
$dfp = 1.00;#					攻擊			防御	  �秘o見率	 先制攻擊率
if   ($tactics eq "攻擊重視"){$atp+=0.4;	$dfp-=0.4;}
elsif($tactics eq "防御重視"){$atp-=0.4;	$dfp+=0.4;				$chkpnt2-=2;}
elsif($tactics eq "隱密行動"){$atp-=0.4;	$dfp-=0.4;	$chkpnt-=2;	$chkpnt2+=4;}
elsif($tactics eq "探索行動"){$atp-=0.2;	$dfp-=0.2;	$chkpnt+=4;	$chkpnt2+=4;}
elsif($tactics eq "連鬥行動"){				$dfp-=0.4;}
if ($arealist[5] eq "0")	 {$atp+=0.2;	$dfp+=0.3;	$chkpnt+=2;	$chkpnt2+=2;}	#快晴
elsif ($arealist[5] eq "1")  {$atp+=0.2;	$dfp+=0.1;	$chkpnt+=1;	$chkpnt2+=1;}	#晴
elsif ($arealist[5] eq "2")  {;}													#變陰
elsif ($arealist[5] eq "3")  {$atp-=0.02;	$dfp-=0.03;	$chkpnt-=0.2;$chkpnt2-=0.3;}#雨
elsif ($arealist[5] eq "4")  {$atp-=0.05;	$dfp-=0.03;	$chkpnt-=0.3;$chkpnt2-=0.5;}#豪雨
elsif ($arealist[5] eq "5")  {$atp-=0.07;	$dfp-=0.05;	$chkpnt-=0.7;$chkpnt2-=0.5;}#台風
elsif ($arealist[5] eq "6")  {$atp-=0.07;	$dfp-=0.1;	$chkpnt-=1;	$chkpnt2-=0.7;}	#雷雨
elsif ($arealist[5] eq "7")  {$atp-=0.1;	$dfp-=0.15;	$chkpnt-=0.5;$chkpnt2+=1;}	#雪
elsif ($arealist[5] eq "8")  {				$dfp-=0.2;	$chkpnt+=1;	$chkpnt2-=1;}	#霧
elsif ($arealist[5] eq "9")  {$atp+=0.5;	$dfp-=0.3;				$chkpnt2-=1;}	#濃霧
if ($arsts[$pls] eq "WU")	 {$atp+=0.1;}	#攻擊增
elsif ($arsts[$pls] eq "WD") {$atp-=0.1;}	#攻擊減
elsif ($arsts[$pls] eq "DU") {$dfp+=0.1;}	#防御增
elsif ($arsts[$pls] eq "DD") {$dfp-=0.1;}	#防御減
elsif ($arsts[$pls] eq "SU") {$chkpnt+=1;}	#發見增
elsif ($arsts[$pls] eq "SD") {$chkpnt-=1;}	#發見減

if ($inf =~ /腕/) {$atp -= 0.2;}

local($kind) = $w_kind ;
local($wmei) = 0;
local($wweps) = "";

if(($kind =~ /G/)&&($w_wtai eq 0)){$wweps = "S";$wmei = 80;$wmei += int($wb/$BASE);}#棍棒/子彈槍
elsif($kind =~ /C/){$wweps = "M" ;$wmei = 70 ;$wmei += int($wc/$BASE);}#投
elsif($kind =~ /D/){$wweps = "L" ;$wmei = 50 ;$wmei += int($wd/$BASE);}#爆
elsif($kind =~ /G/){$wweps = "M" ;$wmei = 50 ;$wmei += int($wg/$BASE);}#鎗
elsif($kind =~ /S/){$wweps = "S" ;$wmei = 80 ;$wmei += int($ws/$BASE);}#劍
else 			   {$wweps = "S" ;$wmei = 70 ;$wmei += int($wp/$BASE);}#手

$weps = $wweps;
$mei = $wmei;

if ($inf =~ /頭/) {$mei -= 20;}
}
#===================#
# ■ 戰略計算		#
#===================#
sub TACTGET2 {

$atn = 1.00;
$dfn = 1.00;
$sen = 1.0;#					攻擊		  防御		  �秘o見率		奇襲(對手的先發制人攻擊率)
if	 ($w_ousen eq "攻擊重視"){$atn+=0.4;	$dfn-=0.4;				} 
elsif($w_ousen eq "防御重視"){$atn-=0.4;	$dfn+=0.4;	$sen-=0.2;	}
elsif($w_ousen eq "隱密行動"){$atn-=0.4;	$dfn-=0.6;	$sen+=0.4;	}
#elsif($w_ousen eq "探索行動"){$atn-=0.4;	$dfn-=0.4;	$sen-=0.4;	}
#elsif($w_ousen eq "連鬥行動"){				$dfn-=0.6;	$sen-=0.3;	}
elsif($w_ousen eq "治療專念"){				$dfn-=0.4;}
elsif($w_ousen eq "逃跑姿態"){				$dfn-=0.2;}
if ($arealist[5] eq "0")	 {$atn+=0.2;	$dfn+=0.3;}	#快晴
elsif ($arealist[5] eq "1")  {$atn+=0.2;	$dfn+=0.1;}	#晴
elsif ($arealist[5] eq "2")  {;}						#變陰
elsif ($arealist[5] eq "3")  {$atn-=0.02;	$dfn-=0.03;}#雨
elsif ($arealist[5] eq "4")  {$atn-=0.05;	$dfn-=0.03;}#豪雨
elsif ($arealist[5] eq "5")  {$atn-=0.07;	$dfn-=0.05;}#台風
elsif ($arealist[5] eq "6")  {$atn-=0.07;	$dfn-=0.1;}	#雷雨
elsif ($arealist[5] eq "7")  {$atn-=0.1;	$dfn-=0.15;}#雪
elsif ($arealist[5] eq "8")  {				$dfn-=0.2;}	#霧
elsif ($arealist[5] eq "9")  {$atn+=0.5;	$dfn-=0.3;}	#濃霧
if ($arsts[$w_pls] eq "WU")   {$atn+=0.2;}#攻擊增
elsif ($arsts[$w_pls] eq "WD"){$atn-=0.2;}#攻擊減
elsif ($arsts[$w_pls] eq "DU"){$dfn+=0.2;}#防御增
elsif ($arsts[$w_pls] eq "DD"){$dfn-=0.2;}#防御減

if($w_inf =~ /腕/){$atn -= 0.1;}

local($kind) = $w_kind2 ;
local($wmei) = 0;
local($wweps) = "" ;

if (($kind = "G")&&($w_wtai eq 0)){$wweps = "S" ;$wmei = 80 ;$wmei += int($wb/$BASE);}#子彈槍
elsif($kind =~ /C/){$wweps = "M" ;$wmei = 70 ;$wmei += int($wc/$BASE);}#投
elsif($kind =~ /D/){$wweps = "L" ;$wmei = 50 ;$wmei += int($wd/$BASE);}#爆
elsif($kind =~ /G/){$wweps = "M" ;$wmei = 50 ;$wmei += int($wg/$BASE);}#鎗
elsif($kind =~ /S/){$wweps = "S" ;$wmei = 80 ;$wmei += int($ws/$BASE);}#劍
else			   {$wweps = "S" ;$wmei = 70 ;$wmei += int($wp/$BASE);}#手

$weps2 = $wweps ;
$mei2 = $wmei ;

if ($w_inf =~ /頭/) { $mei2 -= 20; }
}

1;
