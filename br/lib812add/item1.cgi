#==================#
# ■ 道具取得  ぜ  #
#==================#
sub ITEMGET {

local($i) = 0 ;
local($chkflg) = -1;
local($sub) = "";

local($filename) = "$LOG_DIR/$pls$item_file";

open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);

if ($#itemlist < 0) {$log = ($log . "這個區域已經完全沒有嗎…？<BR>") ;$chksts="OK";return ;}
else {
	local($work) = int(rand($#itemlist)) ;#隨機取得道具
	local($getitem,$geteff,$gettai) = split(/,/, $itemlist[$work]) ;#道具取得情報
	local($itname,$itkind) = split(/<>/, $getitem);#道具分割取得
	local($delitem) = splice(@itemlist,$work,1) ;#取得之道具刪除
	if ($getitem =~ /<>TO/) { #陷阱
		open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
		$result = int(rand($geteff/2)+($geteff/2));
		$log = ($log . "是陷阱！中了 $itname，受到 <font color=\"red\"><b>$result</b></font> 傷害。<BR>") ;
		$hit-=$result;
		if ($hit <= 0) {$hit = 0;$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;&LOGSAVE("DEATH") ;$mem--;if ($mem == 1) {&LOGSAVE("WINEND1") ;}}#死亡狀態
		return ;
	}
#道具取得評語Log
	if	 ($getitem =~ /<>HH|<>HD/)	{$sub = "吃下可以回復體力。";}
	elsif($getitem =~ /<>SH|<>SD/)	{$sub = "吃下可以回復能量。";}
	elsif($getitem =~ /<>W/)		{$sub = "這個東西可以作為武器。";}#武器？
	elsif($getitem =~ /<>D/)		{$sub = "這個東西可以作為防具。";}#防具
	elsif($getitem =~ /<>A/)		{$sub = "這個東西可以裝備。";}#裝飾
	elsif($getitem =~ /<>TN/)		{$sub = "這個東西能佈置陷阱。"; }#陷阱
	else {$sub = "一定可以在什麼裡能使用吧。";}

	($itname,$kind) = split(/<>/, $getitem) ;
		if ($kind =~ /HH|HD/) {$itemtype = "【體力回復】";}
		elsif ($kind =~ /SH|SD/){$itemtype = "【能量回復】";}
		elsif ($kind eq TN)		{$itemtype = "【陷阱】";}
		elsif ($kind =~ /W/)	{$itemtype = "【武器";
			if ($kind =~ /G/)	{$itemtype = ($itemtype . "(鎗)");}
			if ($kind =~ /K/)	{$itemtype = ($itemtype . "(劍)");}
			if ($kind =~ /C/)	{$itemtype = ($itemtype . "(投)");}
			if ($kind =~ /B/)	{$itemtype = ($itemtype . "(毆)");}
			if ($kind =~ /D/)	{$itemtype = ($itemtype . "(爆)");}
			$itemtype = ($itemtype . "】");}
		elsif ($kind =~ /D/)	{$itemtype = "【防具";
			if ($kind =~ /B/)	{$itemtype = ($itemtype . "(體)");}
			if ($kind =~ /H/)	{$itemtype = ($itemtype . "(頭)");}
			if ($kind =~ /F/)	{$itemtype = ($itemtype . "(足)");}
			if ($kind =~ /A/)	{$itemtype = ($itemtype . "(腕)");}
			$itemtype = ($itemtype . "】");}
		elsif (($kind eq R1)||($kind eq R2)) {$itemtype = "【雷達】";}
		elsif ($kind eq Y) {
			if (($itname eq "假遊戲解除鑰匙")||($itname eq "遊戲解除鑰匙")) {$itemtype = "【解除鑰匙】";}
			elsif ($itname eq "子彈") {$itemtype = "【彈】";}
			else {$itemtype = "【道具】";}}
		elsif ($kind eq A) {$itemtype = "【裝飾品】";}
		else {$itemtype = "【不明】";}

	$log = ($log . "$itname (效：$geteff 數：$gettai) <font color=\"00ffff\">$itemtype</font> 發現。<br>$sub<BR>") ;

	$sameitem = 0;
	for ($i=0; $i<5; $i++){#同一道具判斷
		if (($item[$i] eq $getitem)&&($getitem =~ /<>WC|<>TN|<>NR|子彈|神簽|磨刀石|解毒劑|縫紉工具|電池/)){$chkflg = $i;$sameitem = 1;last;}
		if (($item[$i] eq $getitem)&&($getitem =~ /水|麵包/)){$chkflg = $i;$sameitem = 2;last;}
	}

	if ($sameitem eq "1") {#發現同樣的道具時
		open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
		if ($item[$chkflg] =~ /子彈/) {$eff[$chkflg] += $geteff;}
		else {$itai[$chkflg] += $gettai ;}
	} else {
		if ($sameitem eq "2") {$Command2 = "SAME_ITEM";}
		$Command = "ITMAIN";
		$Command3 = "GET";
		$item_get = $getitem; $eff_get = $geteff; $itai_get = $gettai;
	}
}
&SAVE;
$chksts="OK";
}
#==================#
# ■ 道具交換　　  #
#==================#
sub ITEMNEWXCG {
local($wk) = $Command;$wk =~ s/ITEMNEWXCG_//g;
if (($item[$wk] eq "無")||($item_get eq "無")) {&ERROR("不正當的訪問。");}
local($in, $ik) = split(/<>/, $item_get);
local($in2, $ik2) = split(/<>/, $item[$wk]);

$log = ($log . "$in 撿拾，$in2 棄置。<br>") ;

local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
$item[$wk] = $item_get;
$eff[$wk] = $eff_get;
$itai[$wk] = $itai_get;

$item_get = "無"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;
}
#=====================#
# ■ 道具棄置　　　　 #
#=====================#
sub ITEMDELNEW {
if (($item_get eq "無")||(($item_get eq ""))){$log = ($log . "撿起。<br>");}
else{
	local($in, $ik) = split(/<>/, $item_get);
	$log = ($log . "$in 撿拾。<br>");
	local($filename) = "$LOG_DIR/$pls$item_file";
	open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
	push(@itemlist,"$item_get,$eff_get,$itai_get,\n") ;
	open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
}
$item_get = "無"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;
}
#==================#
# ■ 道具撿拾　　　#
#==================#
sub ITEMGETNEW {
if ($item_get eq "無") {&ERROR("不正當的訪問。"."NO NEW TITEM"."ITEM-ITEMGETNEW");}
local($chkflg) = -1;
for ($i=0; $i<5; $i++) {if ($item[$i] eq "無") {$chkflg = $i;last;}}#道具欄位？
if ($chkflg eq -1) {$log = ($log . "道具欄已滿。<BR>$itname 不能撿拾。<BR>");}#所持品滿
else{
	if ($item[$chkflg] eq "無") {$item[$chkflg] = $item_get; $eff[$chkflg] = $eff_get; $itai[$chkflg] = $itai_get;}
	($itname,$kind) = split(/<>/, $item_get) ;
	$log = ($log . "獲得了 $itname。$sub<BR>") ;
}

$item_get = "無"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;

}
#==================#
# ■ 道具投棄　　  #
#==================#
sub ITEMDEL {

local($wk) = $Command;
$wk =~ s/DEL_//g;

if ($item[$wk] eq "無") {&ERROR("不正當的訪問。");}

local($in, $ik) = split(/<>/, $item[$wk]);

$log = ($log . "$in 棄置。<br>") ;

local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;
$Command = "MAIN";

&SAVE;

}
#==================#
# ■ 道具使用　　  #
#==================#
sub ITEM {

local($result) = 0;local($wep2) = "" ;local($watt2) = 0;local($wtai2) = 0 ;local($up) = 0 ;

local($wk) = $Command;$wk =~ s/ITEM_//g;

if ($item[$wk] eq "無") {&ERROR("不正當的訪問。");}

local($in, $ik) = split(/<>/, $item[$wk]);local($w_name,$w_kind) = split(/<>/, $wep);local($d_name,$d_kind) = split(/<>/, $bou);

if ($item[$wk] =~ /<>SH/) { #能量回復
	$log = ($log . "$in 使用。<BR>能量回復。<BR>");
	$sta += $eff[$wk] ;
	if ($sta > $maxsta) {$sta = $maxsta;}
	$itai[$wk] --;
	if ($itai[$wk] == 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
} elsif($item[$wk] =~ /<>HH/) { #體力回復
	$log = ($log . "$in 使用。<BR>體力回復。<BR>");
	$hit += $eff[$wk] ;
	if ($hit > $mhit) {$hit = $mhit;}
	$itai[$wk] --;
	if ($itai[$wk] == 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
} elsif($in eq "解毒劑") { #解毒
	if ($inf =~ /毒/){$log = ($log . "$in 使用。<BR>毒狀態解除。<BR>");$inf =~ s/毒//g;$itai[$wk] --;if ($itai[$wk] == 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ; }}
	else {$log = ($log . "$in 使用也沒有意義。<BR>");}
} elsif($item[$wk] =~ /<>SD|<>HD/) {	#毒入
	if	 ($item[$wk] =~ /<>SD2|<>HD2/){$result = int($eff[$wk]*2);}#料理部特製？
	elsif($item[$wk] =~ /<>SD1|<>HD1/){$result = int($eff[$wk]*1.5);}#能力者
	else { $result = $eff[$wk] ; }
	$inf =~ s/毒//g ;$inf = ($inf . "毒");
	$hit -= $result ;
	$log = ($log . "嗚…糟糕！<BR>好像被毒物混入了！受到<BR><font color=\"red\"><b>$result</b></font>！<BR>\n") ;
	$itai[$wk] --;
	local($tp, $poisonid) = split(/-/, $item[$wk]);
	$wb = $poisonid;
	$poisoni = $item[$wk];
	if ($itai[$wk] == 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
	$poisondeadchk = 1;
	if ($hit <= 0){require "$LIB_DIR/lib3.cgi";&POISONDEAD;}
} elsif(($item[$wk] =~ /<>W/) && ($item[$wk] !~ /<>WF/)) {  #武器裝備
	$log = ($log . "$in 裝備。<BR>") ;
	$wep2 = $wep; $watt2 = $watt; $wtai2 = $wtai ;
	$wep = $item[$wk]; $watt = $eff[$wk]; $wtai = $itai[$wk] ;
	if ($wep2 !~ /空手/) {$item[$wk] = $wep2; $eff[$wk] = $watt2; $itai[$wk] = $wtai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DB/) { #防具裝備 (體)
	$log = ($log . "$in 護體防具裝備。<BR>");
	$bou2 = $bou; $bdef2 = $bdef; $btai2 = $btai ;
	$bou = $item[$wk]; $bdef = $eff[$wk]; $btai = $itai[$wk] ;
	if ($bou2 !~ /內衣/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DH/) { #防具裝備 (頭)
	$log = ($log . "$in 頭部防具裝備。<BR>");
	$bou2 = $bou_h; $bdef2 = $bdef_h; $btai2 = $btai_h ;
	$bou_h = $item[$wk]; $bdef_h = $eff[$wk]; $btai_h = $itai[$wk] ;
	if ($bou2 !~ /無/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DF/) { #防具裝備 (足)
	$log = ($log . "$in 足部防具裝備。<BR>");
	$bou2 = $bou_f; $bdef2 = $bdef_f; $btai2 = $btai_f ;
	$bou_f = $item[$wk]; $bdef_f = $eff[$wk]; $btai_f = $itai[$wk] ;
	if ($bou2 !~ /無/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DA/) { #防具裝備 (腕)
	$log = ($log . "$in 腕部防具裝備。<BR>");
	$bou2 = $bou_a; $bdef2 = $bdef_a; $btai2 = $btai_a ;
	$bou_a = $item[$wk]; $bdef_a = $eff[$wk]; $btai_a = $itai[$wk] ;
	if ($bou2 !~ /無/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>A/) {  #附件裝備
	$log = ($log . "$in 附件裝備。<BR>");
	$bou2 = $item[5]; $bdef2 = $eff[5]; $btai2 = $itai[5] ;
	$item[5] = $item[$wk]; $eff[5] = $eff[$wk]; $itai[5] = $itai[$wk] ;
	if ($bou2 !~ /無/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>R/) {  #雷達
	&HEADER;require"$LIB_DIR/disp.cgi";&READER;&FOOTER;
} elsif($item[$wk] =~ /<>TN/) { #陷阱
	$log = ($log . "$in 陷阱裝設了。<BR>自己也難以發現…。<BR>");
	$item[$wk] =~ s/TN/TO/g ;
	$filename = "$LOG_DIR/$pls$item_file";
	open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
	push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
	open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
	$itai[$wk] -- ;$item[$wk] =~ s/TO/TN/g ;
	if ($itai[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in eq "磨刀石") && ($wep =~ /<>WK/)) { #磨刀石使用&小刀系裝備？
	$watt += (int(rand(2)) + $eff[$wk]);
	$log = ($log . "$in 使用。<BR>$w_name 攻擊力變成 $watt。<BR>");
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in eq "縫紉工具") && ($d_kind eq "DB") && ($d_name ne "內衣")) { #縫紉工具&衣服系裝備？
	$btai += (int(rand(2)) + $eff[$wk]);
	$log = ($log . "$in 使用。<BR>$d_name 耐久力變成 $btai。<BR>");
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in =~ /子彈/) && ($wep =~ /<>WG/)) {  #子彈使用&槍系裝備？

	$up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; } else { $up = $eff[$wk]; }
	$wtai += $up ; $eff[$wk] -= $up ;

	if ($eff[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
	if ($wep =~ /<>WGB/) { $wep =~ s/<>WGB/<>WG/g;}
	$log = ($log . "$in，$w_name 裝彈量補充。<BR>$w_name 的使用回數 $up 提高。<BR>");
} elsif(($in =~ /箭/) && ($wep =~ /<>WA/)) {	#箭使用&弓系裝備？
	$up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; }else { $up = $eff[$wk]; }
	$wtai += $up ; $eff[$wk] -= $up;
	if ($eff[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
	if ($wep =~ /<>WAB/) { $wep =~ s/<>WAB/<>WA/g ;}
	$log = ($log . "$in 使用，$w_name 的弓箭數量補充。<BR>$w_name 的使用回數 $up 提高。<BR>");
} elsif($in =~ /電池/){
	my($pc_ck) = 0;
	for ($paso=0; $paso<5; $paso++){
		if (($item[$paso] eq "移動PC<>Y")&&($itai[$paso] < 5)){
			$itai[$paso] += $eff[$wk];
			if($itai[$paso] > 5){ $itai[$paso] = 5; }
			$itai[$wk] -- ;
			if ($itai[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
			$log = ($log . "$in 移動PC充電。<BR>移動PC的使用回數 $itai[$paso] 增加。<BR>");
			$pc_ck = 1;
			last;
		}
	}
	if ($pc_ck == 0){$log = ($log . "這個東西要如何使用…。<BR>");$Command="MAIN";}
} elsif($in eq "移動PC") {$Command4="HACK";require "$LIB_DIR/lib3.cgi";&HACKING;
} elsif($in eq "遊戲解除鑰匙") {
	if ($pls eq 0){
		$inf = ($inf . "解");
		open(FLAG,">$end_flag_file"); print(FLAG "解除終了\n"); close(FLAG);
		&LOGSAVE("EX_END");
		$log = ($log . "使用解除鑰匙停止了遊戲。<br>項圈脫落了！<BR>");$Command="MAIN";
		&SAVE;
	}else{
		$log = ($log . "在這裡使用沒有什麼意義…。<BR>");$Command="MAIN";
	}
} elsif ($in eq "神簽") { #神簽使用
	$log = ($log . "神簽嗎？試著打開。<BR>\n");
	local($omi) = int(rand(100)) ;
	if	  ($omi < 20) {$omi="2";&omikuji1;$log = ($log . "是大吉！快要有什麼好事發生了！<BR><font color=\"00FFFF\">【體】+$lvuphit 【攻】+$lvupatt 【防】+$lvupdef</font><BR>") ;}
	elsif ($omi < 40) {$omi="1";&omikuji1;$log = ($log . "中吉嗎？感覺真好！<BR><font color=\"00FFFF\">【體】+$lvuphit 【攻】+$lvupatt 【防】+$lvupdef</font><BR>") ;}
	elsif ($omi < 60) {$omi="0";&omikuji1;$log = ($log . "小吉嗎？有跟無也沒有什麼分別...？<BR><font color=\"00FFFF\">【體】+$lvuphit 【攻】+$lvupatt 【防】+$lvupdef</font><BR>") ;}
	elsif ($omi < 80) {$omi="0";&omikuji2;$log = ($log . "凶或者…。完全，不吉利…。<BR><font color=\"00FFFF\">【體】-$lvuphit 【攻】-$lvupatt 【防】-$lvupdef</font><BR>") ;}
	else {$omi="1";&omikuji2; $log = ($log . "大凶??總覺得有什麼可怕的事快要降臨…。<BR><font color=\"00FFFF\">【體】-$lvuphit 【攻】-$lvupatt 【防】-$lvupdef</font><BR>") ; }
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "無"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} else {
	$log = ($log . "為什麼使用這個東西…。<BR>");$Command="MAIN";
}

$Command = "MAIN";

&SAVE;

}
#==================#
# ■ 神簽random　　#
#==================#
sub omikuji1 {$lvuphit = int(rand(2) + $omi);$lvupatt = int(rand(2) + $omi);$lvupdef = int(rand(2) + $omi);
$hit += $lvuphit ;$mhit += $lvuphit ; $att += $lvupatt; $def += $lvupdef;
}
sub omikuji2 {$lvuphit = int(rand(2) + $omi);$lvupatt = int(rand(2) + $omi);$lvupdef = int(rand(2) + $omi);
$hit -= $lvuphit ;$mhit -= $lvuphit ; $att -= $lvupatt; $def -= $lvupdef;
}
#========================#
# ■ 取下裝備武器的處理  #
#========================#
sub WEPDEL {
local($j) = 0 ;
if ($wep =~ /空手/) {$log = ($log . "$l_name 沒有裝備武器。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $wep);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $wep; $eff[$j] = $watt; $itai[$j] = $wtai ;
	$wep = "空手<>WP"; $watt = 0; $wtai = "∞" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#==================#
# ■ 裝備武器拋置  #
#==================#
sub WEPDEL2 {
if ($wep =~ /空手/) {$log = ($log . "$l_name沒有裝備武器。<br>") ;$Command = "MAIN" ;return ;}
local($in, $ik) = split(/<>/, $wep);
$log = ($log . "$in 丟掉。<br>") ;
#武器丟棄
local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$wep,$watt,$wtai,\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
$wep = "空手<>WP"; $watt = 0; $wtai = "∞" ;
$Command = "MAIN";
&SAVE;
}
#======================#
# ■ 取下頭防具的處理  #
#======================#
sub BOUDELH {
local($j) = 0 ;
if ($bou_h =~ /無/) {$log = ($log . "$l_name沒有裝備頭部防具。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_h);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $bou_h; $eff[$j] = $bdef_h; $itai[$j] = $btai_h ;
	$bou_h = "無"; $bdef_h = 0; $btai_h = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#========================#
# ■ 取下身體防具的處理  #
#========================#
sub BOUDELB {
local($j) = 0 ;
if ($bou =~ /內衣/) {$log = ($log . "$l_name沒有裝備護體防具。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $bou; $eff[$j] = $bdef; $itai[$j] = $btai ;
	$bou = "內衣<>DN"; $bdef = 0; $btai = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#========================#
# ■ 取下手臂防具的處理  #
#========================#
sub BOUDELA {
local($j) = 0 ;
if ($bou_a =~ /無/) {$log = ($log . "$l_name沒有裝備腕部防具。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_a);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $bou_a; $eff[$j] = $bdef_a; $itai[$j] = $btai_a ;
	$bou_a = "無"; $bdef_a = 0; $btai_a = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#==================#
# ■ 足防具的處理  #
#==================#
sub BOUDELF {
local($j) = 0 ;
if ($bou_f =~ /無/) {$log = ($log . "$l_name沒有裝備足部防具。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_f);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $bou_f; $eff[$j] = $bdef_f; $itai[$j] = $btai_f ;
	$bou_f = "無"; $bdef_f = 0; $btai_f = "∞" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#======================#
# ■ 取下裝飾品的處理  #
#======================#
sub BOUDEL {
local($j) = 0 ;
if ($item[5] =~ /無/) {$log = ($log . "$l_name沒有裝備裝飾品。<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $item[5]);
#攜帶的物品空間確認
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "無") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "物品放不下，道具欄已滿。<br>") ;
} else {
	$log = ($log . "$w_name已收入道具欄。<br>") ;
	$item[$j] = $item[5]; $eff[$j] = $eff[5]; $itai[$j] = $itai[5] ;
	$item[5] = "無"; $eff[5] = 0; $itai[5] = "0" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
1;