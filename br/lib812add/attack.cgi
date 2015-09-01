#□■□■□■□■□■□■□■□■□■□■□
#■ 	-    BR ATTACK PROGRAM    - 	 ■
#□ 									 □
#■ 		　　子程序一覽　			 ■
#□ 									 □
#■ ATTJYO		-	轉讓處理			 ■
#□ ATTACK		-	先制攻擊表示		 □
#■ ATTACK1		-	先制攻擊處理		 ■
#□ ATTACK2		-	後攻攻擊處理		 □
#■ WEPTREAT	-	武器攻擊處理		 ■
#□ DEATH		-	自分死亡處理		 ■
#■ DEATH2		-	敵死亡處理			 □
#□ RUNAWAY		-	逃亡處理			 ■
#■ DEFTREAT	-	防具種別處理		 □
#□ LVUPCHK		-	等級處理　　　　	 ■
#■ lvuprand	- 　等級隨機能力點處理　 □
#□ EN_KAIFUKU	-	敵回復處理			 ■
#■ BLOG_CK		-   敵戰鬥自動削除處理 　□
#□■□■□■□■□■□■□■□■□■□■□
#==================#
# ■ 轉讓處理	   #
#==================#
sub ATTJYO {
if (($teamID ne "無")&&($teamID ne "")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){
	$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 發現！<br>") ;
	$log = ($log . "$w_f_name $w_l_name 沒有任何發現...。<br>") ;
	$Command="ITEMJOUTO";
}else{&ERROR("不正當訪問","teamID and teamPass missmatch","ATTACK-ATTJYO");}
}
#==================#
# ■ 先制攻擊表示  #
#==================#
sub ATTACK {
$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 發現！<br>") ;
$log = ($log . "$w_f_name $w_l_name 這邊沒有任何發現...。<br>") ;
$Command=("BATTLE0" . "_" . $w_id);
}
#==================#
# ■ 先制攻擊處理  #
#==================#
sub ATTACK1 {
require "$LIB_DIR/lib2.cgi";
$kega2 = "" ; $kega3 = "" ;
$hakaiinf2 = ""; $hakaiinf3 = "";

local($i) = 0 ;
local($result) = 0 ;
local($result2) = 0 ;
local($dice1) = int(rand(100)) ;
local($dice2) = int(rand(100)) ;

local($a,$w_kind,$wid) = split(/_/, $Command);

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $wid) {$Index2=$i; last;}
}
#連鬥--->
if ((($tactics ne "連鬥行動")&&($w_bid eq $id))||($w_hit <= 0)) {&ERROR("不正當訪問","rento is not valid","Attack-ATTACK1") ;}
#<---連鬥
&BB_CK; #瀏覽器背部應對
$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 戰鬥開始！<br>") ;

($w_name,$a) = split(/<>/, $wep);
($w_name2,$w_kind2) = split(/<>/, $w_wep);
&TACTGET; &TACTGET2;	#基本行動

#播放機
if ((($wep =~ /G|A/) && ($wtai == 0)) || (($wep =~ /G|A/) && ($w_kind eq "WB"))) {$att_p = (($watt/10) + $att) * $atp ;}
else {$att_p = ($watt + $att) * $atp ;}
local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #裝飾防護具？
$def_p = $ball * $dfp ;

#敵
if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {$att_n = (($w_watt/10) + $w_att) * $atn ;}
else {$att_n = ($w_watt + $w_att) * $atn ;}
local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
if ($w_item[5] =~ /AD/) {$ball2 += $w_eff[5];} #裝飾防護具？
$def_n = $ball2 * $dfn ;

&BLOG_CK;
&EN_KAIFUKU;

$Command="BATTLE";

if ($w_pls ne $pls) {$log = ($log . "可是，$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 被逃跑了！<br>") ;&SAVE;return ;}#已經移動？

if (length($dengon) > 0) {
	$log = ($log . "<font color=\"lime\"><b>$f_name $l_name ($cl $sex$no番)「$dengon」</b></font><br>") ;
	$w_log = ($w_log . "<font color=\"lime\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no番)「$dengon」</b></font><br>") ;
}

&WEPTREAT($w_name, $w_kind, $wtai, $l_name, $w_l_name, "攻擊", "PC") ;
if ($dice1 < $mei) {	#攻擊成功

	$result = ($att_p*$wk) - $def_n;
	$result /= 2 ;
	$result += rand($result);

	&DEFTREAT($w_kind, "NPC") ;
	$result = int($result * $pnt) ;

	if ($result <= 0) {$result = 1} ;
	$log = ($log . "　　<font color=\"red\"><b>$result 受到 $hakaiinf3 $kega3 傷害</b></font>！<br>") ;

	$w_hit -= $result;
	$w_btai--;
	if ($w_btai <= 0) { $w_bou = "內衣<>DN"; $w_bdef=0; $w_btai="∞"; }

	$wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;
#經驗地-自己
	$expup = int(($w_level - $level)/5);if ($expup <1){$expup = 1;}if($w_hit < 1){$expup += 1;}$exp += $expup;

} else {$kega3="";$log = ($log . "可是，被避開了！<br>") ;}

if($w_hit <= 0){&DEATH2;}#敵死亡？
elsif((rand(10) < 5)&&($w_ousen !~ /治療專念|逃亡姿態/)){	#反擊

	if (($weps eq $weps2)||($weps2 eq "M")) {  #距離一緒？

		&WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "反擊", "NPC") ;

		if ($dice2 < $mei2) {   #攻擊成功
			$result2 = ($att_n*$wk) - $def_p;
			$result2 /= 2 ;
			$result2 += rand($result2);

			&DEFTREAT($w_kind2, "PC") ;
			$result2 = int($result2 * $pnt) ;

			if ($result2 <= 0) {$result2 = 1 ;}
			$log = ($log . "　　<font color=\"red\"><b>$result2 受到 $kega2 傷害</b></font>！<br>") ;

			$btai--;$hit -= $result2;

			if ($btai <= 0) { $bou = "內衣<>DN"; $bdef=0; $btai="∞"; }

			if ($hit <=0) {&DEATH;}#死亡？
			else {$log = ($log . "$w_l_name 逃跑了...。<br>") ;}#逃亡
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 攻：$result2 被：$result $hakaiinf2 $kega3 </b></font><br>") ;
			$w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
#經驗地-敵人
	$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
		} else {
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 被：$result $kega3 </b></font><br>") ;
			$log = ($log . "　　可是，千鈞一髮之際避開了！<br>") ;
		}
		#武器消耗
		if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) {$w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}}#鎗·射？
		elsif ($w_kind2 =~ /C|D/) {$w_wtai--; if ($w_wtai <= 0) { $w_wep ="空手<>WP"; $w_watt=0; $w_wtai="∞"; }}
		elsif (($w_kind2 =~ /N/) && (int(rand(5)) eq 0)) {$w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="空手<>WP"; $w_watt=0; $w_wtai="∞"; }}

	} else {
		$log = ($log . "$w_l_name 不能反擊！<br>﹛$w_l_name 逃跑了...。<br>") ;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 鬥戰：$f_name $l_name ($cl $sex$no番) 被：$result $hakaiinf2 $kega3 </b></font><br>") ;
	}
}else{	#逃跑
	$log = ($log . "$w_l_name 逃跑了...。<br>") ;
	$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 被：$result $hakaiinf2 $kega3 </b></font><br>");
	if($w_ousen eq "逃跑姿態"){#逃跑體態自動迴避
		($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);
		$w_pls = $ara[$ar + int(rand(21 - $ar)) + 1];
		$w_log = ($w_log . "<font color=\"lime\"><b>$place[$w_pls]已經離開了。</b></font><br>");
	}
}
#武器消耗
if (($w_kind =~ /G|A/) && ($wtai > 0)) {$wtai--; if ($wtai <= 0) { $wtai = 0 ; }}#鎗·射？
elsif ($w_kind =~ /C|D/) {$wtai--; if ($wtai <= 0) { $wep ="空手<>WP"; $watt=0; $wtai="∞"; }}
elsif (($w_kind =~ /N/) && (int(rand(5)) eq 0)) {$watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="空手<>WP"; $watt=0; $wtai="∞"; }}

&LVUPCHK();

$w_bid = $id ;
$bid = $w_id ;

&SAVE;
&SAVE2;
}
#==================#
# ■ 後攻攻擊處理  #
#==================#
sub ATTACK2 {
$kega2 = "" ; $kega3 = "" ;
$hakaiinf2 = ""; $hakaiinf3 = "";

if ($w_hit <= 0) {&ERROR("不正當訪問","no hit","attack-ATTACK2") ;}

local($result) = 0 ;
local($result2) = 0 ;
local($i) = 0 ;
local($dice1) = int(rand(100)) ;
local($dice2) = int(rand(100)) ;
($w_name,$w_kind) = split(/<>/, $wep);
($w_name2,$w_kind2) = split(/<>/, $w_wep);

&TACTGET; &TACTGET2;	#基本行動

#播放機
if (($wep =~ /G|A/) && ($wtai == 0)) {$att_p = (($watt/10) + $att) * $atp ;}
else {$att_p = ($watt + $att) * $atp ;}
local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #裝飾防護具？
$def_p = $ball * $dfp ;

#敵
if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {$att_n = (($w_watt/10) + $w_att) * $atn ;}
else {$att_n = ($w_watt + $w_att) * $atn ;}
local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
if ($w_item[5] =~ /AD/) {$ball += $w_eff[5];} #裝飾防護具？
$def_n = $ball2 * $dfn ;

&BLOG_CK;
&EN_KAIFUKU;

$Command="BATTLE";

$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no番) <BR>　　　　　　　　　　　　　　　突然襲擊過來！<br>") ;

&WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "攻擊", "NPC") ;
if ($dice2 < $me2) {	#攻擊成功

	$result = ($att_n*$wk) - $def_p;
	$result /= 2 ;
	$result += rand($result);
	$result = int($result) ;

	&DEFTREAT($w_kind2, "PC") ;
	$result = int($result * $pnt) ;

	if ($result <= 0) {$result = 1 ;}
	$log = ($log . "　　<font color=\"red\"><b>$result 受到 $kega2 傷害</b>！</font><br>") ;

	$hit -= $result;
	$btai--;

	if ($btai <= 0) { $bou = "內衣<>DN"; $bdef=0; $btai="∞"; }
	$w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
	($w_name2,$w_kind2) = split(/<>/, $w_wep);
#經驗地-敵
	$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
} else {$log = ($log . "　　可是，千鈞一髮之際避開了！<br>") ;}

if ($hit <= 0) {&DEATH;}#死亡？
elsif (rand(10) <5) { #反擊

	if ($weps eq $weps2) {

		&WEPTREAT($w_name, $w_kind,  $wtai, $l_name, $w_l_name, "反擊", "PC") ;
		if ($dice1 < $mei) {	#攻擊成功

			$result2 = ($att_p*$wk) - $def_n;
			$result2 /= 2 ;
			$result2 += rand($result2);
			$result2 = int($result2) ;

			&DEFTREAT($w_kind, "NPC") ;
			$result2 = int($result2 * $pnt) ;

			if ($result2 <= 0) {$result2 = 1 ;}
			$log = ($log . "　　<font color=\"red\"><b>$result2 受到 $hakaiinf3 $kega3 傷害</b>！</font><br>") ;

			$w_hit -= $result2;
			$w_btai--;

			if ($w_btai <= 0) { $w_bou = "內衣<>DN"; $w_bdef=0; $w_btai="∞"; }

			if ($w_hit <=0) {&DEATH2;}#死亡？
			else {$log = ($log . "　$l_name 逃跑了...。<br>") ;}#逃亡

			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 攻：$result 被：$result2 $hakaiinf2 $kega3 </b></font><br>") ;
			$wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;
			($w_name,$w_kind) = split(/<>/, $wep);
#經驗地-自分
	$expup = int(($w_level - $level)/5);if ($expup <1){$expup = 1;}if($w_hit < 1){$expup += 1;}$exp += $expup;
		} else {
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 攻：$result $hakaiinf2 </b></font><br>") ;
			$log = ($log . "　可是，被避開了！<br>") ;
		}
		#武器消耗
		if (($w_kind =~ /G|A/) && ($wtai > 0)) {$wtai--; if ($wtai <= 0) { $wtai = 0 ; }}#鎗·射？
		elsif ($w_kind =~ /C|D/) {$wtai--; if ($wtai <= 0) { $wep ="空手<>WP"; $watt=0; $wtai="∞"; }}
		elsif (($w_kind =~ /N/) && (int(rand(5)) eq 0)) {$watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="空手<>WP"; $watt=0; $wtai="∞"; }}
	} else {
		$log = ($log . "$l_name 不能反擊！<br> $l_name 逃跑了...。<br>") ;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 攻：$result $hakaiinf2 $kega3 </b></font><br>") ;
	}
}else{	#逃亡
	$log = ($log . "$w_l_name 逃走了...。<br>") ;
	$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥：$f_name $l_name ($cl $sex$no番) 被：$result $hakaiinf2 $kega3 </b></font><br>");
	if($w_ousen eq "逃跑姿態"){#逃跑體態自動迴避
		($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);
		$w_pls = $ara[$ar + int(rand(21 - $ar)) + 1];
		$w_log = ($w_log . "<font color=\"lime\"><b>$place[$w_pls]已經離開了。</b></font><br>");
	}
}
#武器消耗
if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) {$w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}}#鎗·射？
elsif ($w_kind2 =~ /C|D/) {$w_wtai--; if ($w_wtai <= 0) { $w_wep ="空手<>WP"; $w_watt=0; $w_wtai="∞"; }}
elsif (($w_kind2 =~ /N/) && (int(rand(5)) eq 0)) {$w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="空手<>WP"; $w_watt=0; $w_wtai="∞"; }}

&LVUPCHK();

&SAVE;
&SAVE2;
}
#==================#
# ■ 武器類別處理  #
#==================#
sub WEPTREAT {

local($wname)	= @_[0];#武器
local($wkind)	= @_[1];#武器
local($wwtai)	= @_[2];#數量
local($pn)		= @_[3];#攻擊者名
local($nn)		= @_[4];#防御者名
local($ind)		= @_[5];#攻擊類別 (攻擊/反擊)
local($attman)	= @_[6];#攻擊者 (PC/NPC)

local($dice3) = int(rand(100));	#傷1
local($dice4) = int(rand(4));	#傷2
local($dice5) = int(rand(100));	#破壞？

local($kega)	= 0;
local($kegainf)	= "";
local($k_work)	= "";
local($hakai)	= 0;

if ((($wkind =~ /B/)||(($wkind =~ /G|A/)&&($wwtai eq 0)))&&($wname ne "空手")){#棍棒，子彈鎗，箭弓
	$log = ($log . "$pn 的 $ind！<BR>　$wname 毆打 $nn！<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 15 ;$kegainf = "頭腕" ;			#受傷率，傷個體所
	$hakai = 2 ;		#破壞率
} elsif ($wkind =~ /C/) {			#投系
	$log = ($log . "$pn 的 $ind！<BR>　$wname 向著 $nn 投擲！<BR>");
	if ($attman eq "PC") {$wc++;$wk=$wc;} else {$w_wc++;$wk=$w_wc;}
	$kega = 15 ;$kegainf = "頭腕" ;			#受傷率，傷個體所
	$hakai = 0 ;		#破壞率
} elsif ($wkind =~ /D/) {			#爆系
	$log = ($log . "$pn 的 $ind！<BR>　$wname 向著 $nn 投擲！<BR>");
	if ($attman eq "PC") {$wd++;$wk=$wd;} else {$w_wd++;$wk=$w_wd;}
	$kega = 15 ;$kegainf = "頭腕腕足" ;		#受傷率，傷個體所
	$hakai = 0 ;		#破壞率
} elsif ($wkind =~ /G/) {			#鎗系
	$log = ($log . "$pn 的 $ind！<BR>　$wname 向著 $nn 發砲！<BR>");
	if ($attman eq "PC") {$wg++;$wk=$wg;$ps=$pls;} else {$w_wg++;$wk=$w_wg;$ps=$w_pls;}
	$kega = 25 ; $kegainf = "頭腕腹足" ;	#受傷率，傷個體所
	$hakai = 1 ;		#破壞率
	if ($wkind !~ /S/){#開鎗聲音注
		open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
		$gunlog[0] = "$now,$place[$ps],$id,$w_id,\n";
		open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
	}
} elsif ($wkind =~ /K/) {			#劍系
	$log = ($log . "$pn 的 $ind！<BR>　$wname 刺了 $nn！ <BR>");
	if ($attman eq "PC") {$ws++;$wk=$ws;} else {$w_ws++;$wk=$w_ws;}
	$kega = 25 ; $kegainf = "頭腕腹足" ;	#受傷率，傷個體所
	$hakai = 2 ;		#破壞率
} elsif ($wkind =~ /P/) {			#毆系
	$log = ($log . "$pn 的 $ind〞<BR>　$wname 毆打 $nn！<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 0 ; $kegainf = "" ;				#受傷率，傷個體所
	$hakai = 0 ;		#破壞率
} else {							#其它
	$log = ($log . "$pn 的 $ind！<BR>　$wname 攻擊 $nn！<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 0 ; $kegainf = "" ;				#受傷率，傷個體所
	$hakai = 0 ;		#破壞率
}

$wk = int($wk/$BASE) ;
if($wk == 0){$wk = 0.9;}elsif($wk == 1){$wk = 0.95;}elsif($wk == 2){$wk = 1.0;}elsif($wk == 3){$wk = 1.05;}elsif($wk == 4){$wk = 1.1;}else{$wk = 1.15;}
#對手？自己？
if ($attman eq "PC") {$wep_2 = $wep; $watt_2 = $watt; $wtai_2 = $wtai ;$w_inf_2 = $w_inf ;}
else {$w_wep_2 = $w_wep; $w_watt_2 = $w_watt; $w_wtai_2 = $w_wtai ;$inf_2 = $inf ;}

# 武器破壞
if ($dice5 < $hakai) {  #破壞？
	if ($attman eq "PC") {$wep_2 = "空手<>WP"; $watt_2 = 0 ; $wtai_2 = "∞" ;$hakaiinf3 = "武器損傷！" ;}#PC
	else {$w_wep_2 = "空手<>WP"; $w_watt_2 = 0 ; $w_wtai_2 = "∞" ;$hakaiinf2 = "武器損傷！" ;}
} else {$hakaiinf2 = "" ;$hakaiinf3 = "" ;}

# 受傷處理
if ($dice3 < $kega) {
	if	  (($dice4 eq 0) && ($kegainf =~ /頭/)) {$k_work = "頭" ;}#頭
	elsif (($dice4 eq 1) && ($kegainf =~ /腕/)) {$k_work = "腕" ;}#腕
	elsif (($dice4 eq 2) && ($kegainf =~ /腹/)) {$k_work = "腹" ;}#腹
	elsif (($dice4 eq 3) && ($kegainf =~ /足/)) {$k_work = "足" ;}#足
	else {return ;}

	if ($attman eq "PC") {  #PC
		if ((($w_item[5] =~ /AD/)||($w_bou =~ /<>DB/)) && ($k_work eq "腹")) {	#腹？
			if($w_item[5] =~ /AD/){$w_itai[5] --; if ($w_itai[5] <= 0) {$w_item[5]="無"; $w_eff[5]=$w_itai[5]=0;}}
			else{$w_btai --; if ($w_btai <= 0) { $w_bou = "內衣<>DN"; $w_bdef=0; $w_btai="∞"; }}
			return ;
		}
		elsif (($w_bou_h =~ /<>DH/) && ($k_work eq "頭")) {$w_btai_h --; if ($w_btai_h <= 0) {$w_bou_h="無"; $w_bdef_h=$w_btai_h=0;}return ;}#頭？
		elsif (($w_bou_f =~ /<>DF/) && ($k_work eq "足")) {$w_btai_f --; if ($w_btai_f <= 0) {$w_bou_f="無"; $w_bdef_f=$w_btai_f=0;}return ;}#足？
		elsif (($w_bou_a =~ /<>DA/) && ($k_work eq "腕")) {$w_btai_a --; if ($w_btai_a <= 0) {$w_bou_a="無"; $w_bdef_a=$w_btai_a=0;}return ;}#腕？
		else {$kega3 = ($k_work . "部分負傷");$w_inf_2 =~ s/$k_work//g ;$w_inf_2 = ($w_inf_2 . $k_work) ;}
	} else {
		if ((($item[5] =~ /AD/)||($bou =~ /<>DB/)) && ($k_work eq "腹")) {	#腹？
			if($item[5] =~ /AD/){$itai[5] --; if ($itai[5] <= 0) {$item[5]="無"; $eff[5]=$itai[5]=0;}}
			else{$btai --; if ($btai <= 0) { $bou = "內衣<>DN"; $bdef=0; $btai="∞"; }}
			return ;
		}
		elsif (($bou_h =~ /<>DH/) && ($k_work eq "頭")) {$btai_h --; if ($btai_h <= 0) {$bou_h="無"; $bdef_h=$btai_h=0;}return ;}#頭？
		elsif (($bou_f =~ /<>DF/) && ($k_work eq "足")) {$btai_f --; if ($btai_f <= 0) {$bou_f="無"; $bdef_f=$btai_f=0;}return ;}#足？
		elsif (($bou_a =~ /<>DA/) && ($k_work eq "腕")) {$btai_a --; if ($btai_a <= 0) {$bou_a="無"; $bdef_a=$btai_a=0;}return ;}#腕？
		else {$kega2 = ($k_work . "部分負傷");$inf_2 =~ s/$k_work//g ;$inf_2 = ($inf_2 . $k_work) ;}
	}
}
}
#==================#
# ■ 自分死亡處理  #
#==================#
sub DEATH {
$hit = 0;$w_kill++;
$mem--;

$com = int(rand(6)) ;

$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;
if ($w_msg ne "") {$log = ($log . "<font color=\"lime\"><b>$w_f_name $w_l_name『$w_msg』</b></font><br>") ;}
$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no番) 進行戰鬥，殺害了。【殘餘 $mem人】</b></font><br>") ;

local($b_limit) = ($battle_limit * 3) + 1;

if (($mem eq 1) && ($w_sts ne "NPC") && ($ar > $b_limit)){$w_inf = ($w_inf . "勝") ;}

open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

#死亡對數(記錄)
&LOGSAVE("DEATH2") ;
$death = $deth ;
}
#================#
# ■ 敵死亡處理  #
#================#
sub DEATH2 {

$w_hit = 0;$kill++;
$wf = $w_id; #瀏覽器背部應對
if (($w_cl ne "$BOSS")&&($w_cl ne "$ZAKO")){$mem--;}

$w_com = int(rand(6)) ;
$log = ($log . "<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no番) 殺害。【殘餘$mem人】</b></font><br>") ;

if (length($w_dmes) > 1) {$log = ($log . "<font color=\"yellow\"><b>$w_f_name $w_l_name『$w_dmes』</b></font><br>") ;}
if (length($msg) > 1) {$log = ($log . "<font color=\"lime\"><b>$f_name $l_name『$msg』</b></font><br>") ;}

local($b_limit) = ($battle_limit * 3) + 1;
if (($mem == 1)&& ($ar > $b_limit)) {$inf = ($inf . "勝") ;}

open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

#死亡對數(記錄)
&LOGSAVE("DEATH3") ;

$Command = "BATTLE2" ;
$w_death = $deth ;
$w_bid = "";

}
#==============#
# ■ 逃亡處理  #
#==============#
sub RUNAWAY {$log = ($log . "$l_name 全速逃走了。<BR>") ;$Command = "MAIN";}
#==================#
# ■ 防具種別處理  #
#==================#
sub DEFTREAT {

local($wkind)	= @_[0] ;#武器種別
local($defman)	= @_[1] ;#防御側(PC/NPC)

local($p_up) = 1.5 ;
local($p_down) = 0.5 ;

if ($defman eq "PC") {  #PC?
	local($b_name,$b_kind) = split(/<>/, $bou);
	local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
	local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
	local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
	local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
} else {
	local($b_name,$b_kind) = split(/<>/, $w_bou);
	local($b_name_h,$b_kind_h) = split(/<>/, $w_bou_h);
	local($b_name_f,$b_kind_f) = split(/<>/, $w_bou_f);
	local($b_name_a,$b_kind_a) = split(/<>/, $w_bou_a);
	local($b_name_i,$b_kind_i) = split(/<>/, $w_item[5]);
}

if (($wkind eq "WG") && ($b_kind_i eq "ADB")) {$pnt = $p_down ;}#鎗→防彈
elsif (($wkind eq "WG") && ($b_kind_h eq "DH")) {$pnt = $p_up ;}#鎗→頭
elsif (($wkind eq "WN") && ($b_kind eq "DBK")) {$pnt = $p_down ;}#斬→鎖
elsif (($wkind eq "WN") && ($b_kind_i eq "ADB")) {$pnt = $p_up ;}#斬→防彈
elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind_h eq "DH")) {$pnt = $p_down ;}#毆→頭
elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind =~ /DBA/)) {$pnt = $p_up ;}#毆→鎧甲
elsif (($wkind eq "WS") && ($b_kind =~ /DBA/)) {$pnt = $p_down ;}#刺→鎧甲
elsif (($wkind eq "WS") && ($b_kind =~ /DBK/)) {$pnt = $p_up ;}#刺→鎖
else {$pnt = 1.0 ;}
}
#======================#
# ■ 等級提升處理　　  #
#======================#
sub LVUPCHK {
if (($exp >= int($level*$baseexp+(($level-1)*$baseexp)))&&($hit > 0)) { #等級提升
	&lvuprand;$log = ($log . "等級提升了。<br><font color=\"00FFFF\">【體】+$lvuphit 【攻】+$lvupatt 【防】+$lvupdef</font>") ;
	$hit += $lvuphit ;$mhit += $lvuphit ; $att += $lvupatt; $def += $lvupdef; $level++;$sta += 50;if ($maxsta < $sta){$sta = $maxsta;};
}
if (($w_exp >= int($w_level*$baseexp+(($w_level-1)*$baseexp)))&&($w_hit > 0)) { #伊矛伙失永皿
	&lvuprand;$w_log = ($w_log . "等級提升了。<br><font color=\"00FFFF\">【體】+$lvuphit 【攻】+$lvupatt 【防】+$lvupdef</font>") ;
	$w_hit += $lvuphit ;$w_mhit += $lvuphit ; $w_att += $lvupdef; $w_def += $lvupatt; $w_level++;$w_sta += 50;if ($maxsta < $w_sta){$w_sta = $maxsta;};
}
}
#==============================#
# ■ 等級能力隨機提升處理　　  #
#==============================#
sub lvuprand {$lvuphit = int(rand(2) + 9);$lvupatt = int(rand(3) + 3);$lvupdef = int(rand(3) + 2);}
#======================#
# ■ 敵回復處理 	   #
#======================#
sub EN_KAIFUKU{ #敵回復處理
$up = int(($now - $w_endtime) / (1 * $kaifuku_time));
if (($w_inf =~ /呏/)&&($w_ousen ne "治療專念")) { $up = int($up / 2) ; }
if (($w_inf !~ /呏/)&&($w_ousen eq "治療專念")) { $up = int($up * 2) ; }
if ($w_sts eq "睡眠") {
	$w_sta += $up;
	if ($w_sta > $maxsta) { $w_sta = $maxsta; }
	$w_endtime = $now;
} elsif ($w_sts eq "治療") {
	if($kaifuku_rate == 0){$kaifuku_rate = 1;}
	$up = int($up / $kaifuku_rate);
	$w_hit += $up;
	if ($w_hit > $w_mhit) { $w_hit = $w_mhit; }
	$w_endtime = $now;
} elsif ($w_sts eq "靜養") {
	$w_sta += $up;
	if ($w_sta > $maxsta) { $w_sta = $maxsta; }
	if($kaifuku_rate == 0){$kaifuku_rate = 1;}
	$up = int($up / $kaifuku_rate);
	$w_hit += $up;
	if ($w_hit > $w_mhit) { $w_hit = $w_mhit; }
	$w_endtime = $now;
}
}
#=============================#
# ■ 敵人戰鬥記錄自動刪除處理 #
#=============================#
sub BLOG_CK{$log_len = length($w_log);if(($w_sts eq "NPC")&&($log_len > 500)){$w_log = "<font color=\"yellow\"><b>自動刪除</b></font><br>";}elsif($log_len > 2222) {$w_log = "<font color=\"yellow\"><b>$hour:$min:$sec 戰鬥回合記錄自動刪除。</b></font><br>";}}
1;
