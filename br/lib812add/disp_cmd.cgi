#□■□■□■□■□■□■□■□■□■□■□
#■ 	-    BR COMMAND DISPLAY    - 	 ■
#□ 									 □
#■ 		　　子程序一覽　			 ■
#□ 									 □
#■ COMMAND		-	指令部　			 ■
#□ definition	-	定義部				 □
#■□■□■□■□■□■□■□■□■□■□■

#===================#
# ■ 指令部　		#
#===================#
sub COMMAND {
local($i) = 0;
if ($sts =~ /睡眠|治療|靜養|優勝/) {
	$MESSENGER = "1";
	if ($sts eq "治療"){
		if($Command eq "HEAL"){$log = ($log . "治療傷患<BR>");}else{$log = ($log . "治療中…<BR>");}
		$sts = "治療";print "治療中…<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"HEAL2\" checked>治療</A><BR><BR>";
	} elsif ($sts eq "睡眠"){
		if($Command eq "INN"){$log = ($log . "稍微睡一下<BR>");}else{$log = ($log . "睡眠中…<BR>");}
		$sts = "睡眠";print "睡眠中…<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INN2\" checked>睡眠</A><BR><BR>";
	} elsif ($sts eq "靜養"){
		if($Command eq "INNHEAL"){$log = ($log . "靜養休息<BR>");}else{$log = ($log . "靜養中…<BR>");}
		$sts = "靜養";print "靜養中…<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INNHEAL2\" checked>靜養</A><BR><BR>";
	} elsif ($sts eq "優勝"){
		print "<center><BR>第$WINNUM回優勝者<BR>殺害數-$kill<BR><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"返回\"></center>";
		$MESSENGER = "0";return;
	}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\">返回</A><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
	return;
}

if ((($Command eq '')||($Command eq "MAIN"))||(($Command eq "MOVE")&&($Command2 eq "MAIN"))||(($Command eq "ITMAIN")&&($Command3 eq "MAIN"))||(($Command eq "SPECIAL")&&($Command4 eq "MAIN"))) {   #MAIN
	$MESSENGER = "1";
	$log = ($log . "$jyulog$jyulog2$jyulog3現在，要怎樣做…。<br>") ;
	print "進行什麼？<BR><BR>";
	if ((($inf =~ /足/)&&($sta > 18))||(($inf !~ /足/)&&($club eq "陸上部")&&($sta > 10))||(($inf !~ /足/)&&($sta > 13))){
		print "<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\">";&AS;
		print "<select name=\"Command2\"><option value=\"MAIN\">■ 移動 ■<BR>";
			local(@kin_ar) = split(/,/, $arealist[2]);#把禁止區域的名單作為排列。
			if(($hackflg)||($sts eq "NPC")){$kinlist = "";} #實行禁止區域一覽。
			else{for($k=0;$k<$ar;$k++){ $kinlist = ($kinlist . $kin_ar[$k]);}}#現在的禁止區域追加。
			for ($j=0; $j<$#place+1; $j++) {
				if (($place[$j] ne $place[$pls])&&($kinlist !~ /$place[$j]/)) {print "<option value=\"MV$j\">$place[$j]($area[$j])<BR>";}
				elsif ($place[$j] eq $place[$pls]) {print "<option value=\"MAIN\"><--現在位置--><BR>";}
			}#禁止區域處理部分&現在位置
		print "</select></A><BR>";
	}
	if ($place[$pls] eq "分校") {if (($hackflg eq 1)||($sts eq "NPC")) {$ok = 1;}}
	else {$ok = 0;if (($inf =~ /足/)&&($sta > 25)) {$ok = 1;} elsif (($club eq "田徑部")&&($sta > 15)) {$ok = 1;} elsif ($sta > 20) {$ok = 1;}}
	if ($ok){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SEARCH\"> ■ 探索 ■&nbsp;</A><BR>";}
	print "<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">";&AS;
	print "<select name=\"Command3\"><option value=\"MAIN\">■ 道具 ■<BR><option value=\"ITEM\">道具使用·裝備<BR><option value=\"DEL\">道具棄置<BR><option value=\"SEIRI\">道具整理<BR><option value=\"GOUSEI\">道具合成<BR>";
	if ($wep ne "空手<>WP")	{print "<option value=\"WEPDEL\">除下裝備武器<BR>";
							 print "<option value=\"WEPDEL2\">裝備武器棄置<BR>";}
	if ($bou_h ne "無")	{print "<option value=\"BOUDELH\">除下頭部防具<BR>";}
	if ($bou ne "內衣<>DN")	{print "<option value=\"BOUDELB\">除下護體防具<BR>";}
	if ($bou_a ne "無")	{print "<option value=\"BOUDELA\">除下腕部防具<BR>";}
	if ($bou_f ne "無")	{print "<option value=\"BOUDELF\">除下足部防具<BR>";}
	if ($item[5] ne "無")	{print "<option value=\"BOUDEL\">除下裝飾品<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"kaifuku\">";&AS;
	print "<select name=\"Command5\"><option value=\"MAIN\">■ 回復 ■<BR><option value=\"HEAL\">　治療<BR><option value=\"INN\">　睡眠<BR>";
	if ($place[$pls] eq "診療所") {print "<option value=\"INNHEAL\">　靜養<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">";&AS;
	print "<select name=\"Command4\"><option value=\"MAIN\" selected>■ 特殊 ■<BR>";
	print "<option value=\"KOUDOU\">　基本方針<BR>";
	print "<option value=\"OUSEN\">　應戰方針<BR>";
	#print "<option value=\"WINCHG\">　口頭語變更<BR>";
	if ($sta > 50){print "<option value=\"OUKYU\">　應急措施<BR>";}
	print "<option value=\"TEAM\">　小組<BR>";
	if (($club eq "料理部" )&&($sta > 30)) { print "<option value=\"PSCHECK\">　毒見<BR>"; }
	for ($poi=0; $poi<5; $poi++){if ($item[$poi] eq "毒藥<>Y") {print "<option value=\"POISON\">　毒物混入<BR>";last;}}
	for ($spi=0; $spi<5; $spi++){if ($item[$spi] eq "攜帶揚聲器<>Y") {print "<option value=\"SPIICH\">　揚聲器使用<BR>";last;}}
	for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "移動PC<>Y")&&($itai[$paso] >= 1)) {print "<option value=\"HACK\">※Hacking※<BR>";last;}}
	print "</select></A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GET")){	#道具
	local($chkflg) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "無") {$chkflg = $i;last;}}#空道具？
	if ($chkflg eq "-1"){
		$log = ($log . "這個道具已放不下。<br>丟掉哪個？<BR>");
		print "丟掉哪個？<BR><BR>";
		($in, $ik) = split(/<>/, $item_get);&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>$in/$eff_get/$itai_get</A><BR><BR>";
		for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMNEWXCG_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	}else{
		print "要如何處理這個道具？<BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>捨棄</A><BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMGETNEW\">撿</A><BR>";
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "ITEM")){	#道具
	$log = ($log . "要放入什麼…。<BR>") ;
	print "用什麼？<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEM_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "DEL")){	#道具棄置
	$log = ($log . "整理道具中…。<BR>");
	print "丟掉什麼？<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"DEL_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "SEIRI")){	#道具整理
	$log = ($log . "整理道具中…。<BR>");
	print "要整合什麼？<BR><BR>";
	print "<select name=\"Command\">";
	print "<option value=\"MAIN\" selected>終止</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"SEIRI_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"MAIN\" selected>終止</option>";
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "無") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"SEIRI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GOUSEI")){	#道具合成
	$log = ($log . "現在持有的東西，要合成製作些什麼嗎？<BR>") ;
	print "要合成什麼？<BR><BR>";
	print "<select name=\"Command\"><option value=\"GOUSEI1_N\" selected>合成1</option>" ;
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"GOUSEI1_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"GOUSEI2_N\" selected>合成2</option>" ;
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "無") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"GOUSEI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><select name=\"Command3\"><option value=\"GOUSEI3_N\" selected>合成3</option>";
	for ($i3=0; $i3<5; $i3++) {if ($item[$i3] ne "無") {($in3, $ik3) = split(/<>/, $item[$i3]);print "<option value=\"GOUSEI3_$i3\">$in3/$eff[$i3]/$itai[$i3]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "OUKYU")){	#應急處理
	$log = ($log . "治療傷患…。<BR>") ;
	print "治療何處？<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	if ($inf =~ /頭/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_0\">頭</A><BR>"; }
	if ($inf =~ /腕/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_1\">腕</A><BR>"; }
	if ($inf =~ /腹/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_2\">腹</A><BR>"; }
	if ($inf =~ /足/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_3\">足</A><BR>"; }
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "KOUDOU")){	#基本方針
	$log = ($log . "考慮基本方針…。<BR>") ;
	print "請決定基本方針。<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_0\">通常</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_1\">攻擊重視</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_2\">防御重視</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_3\">隱密行動</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_4\">採索行動</A><BR>";
	if($ar >= 7){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_5\">連鬥行動</A><BR>";}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "OUSEN")){	#應戰方針
	$log = ($log . "考慮應戰方針…。<BR>") ;
	print "請決定應戰方針。<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_0\">通常</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_1\">攻擊重視</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_2\">防御重視</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_3\">隱密行動</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_4\">探索行動</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_5\">連鬥行動</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_6\">治療專念</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_7\">逃跑姿態</A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif ($Command =~ /BATTLE0/){	#戰鬥指令
	local($a,$wid) = split(/_/, $Command);
	$log = ($log . "那麼，要怎樣做…。");$chk = "checked" ;
	print "做什麼？<BR><BR>向對手同時發出訊息：<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	($w_name,$w_kind) = split(/<>/, $wep);
	if(($w_kind =~ /G/)&&($wtai > 0)){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WG_$wid\" $chk>射擊($wg)</A><BR>"; $chk="";}
	if($w_kind =~ /K/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WK_$wid\" $chk>斬(劍)($ws)</A><BR>"; $chk="";}
	if($w_kind =~ /C/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WC_$wid\" $chk>投擲(投)($wc)</A><BR>"; $chk="";}
	if($w_kind =~ /D/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WD_$wid\" $chk>投擲(爆)($wd)</A><BR>"; $chk="";}
	if($w_kind =~ /P|B/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>毆打(毆)($wp)</A><BR>"; $chk="";}
	if(($w_kind !~ /G|K|C|D|P|B/)&&(($w_kind =~ /G|A/)&&($wtai eq 0))){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>毆打($wp)</A><BR>"; $chk="";}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"RUNAWAY\">逃亡</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif ($Command eq "ITEMJOUTO"){	#道具轉讓
	$log = ($log . "道具轉讓指令。<BR>");
	print "$w_cl$w_no番 $w_f_name $w_l_name<br>　　　　轉讓哪個道具？<INPUT type=\"hidden\" name=\"Command\" value=\"SEITO_$w_id\"><BR><BR>";
	print "<select name=\"Command2\"><option value=\"JO_MAIN\" selected>終止</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "無") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"JO_$i\">$in/$eff[$i]/$itai[$i]<BR></option>";}}
	print "</select><BR><BR>消息<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif ($Command eq "BATTLE2"){	#道具掠奪
	local($itno) = -1;
	for($i=0; $i<5; $i++){if($item[$i] eq "無"){$itno = $i;}}
	print "奪走什麼？<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#武器所持？
	if($w_wep !~ /空手/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#防具所持？
	if($w_bou !~ /內衣/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#防具所持？
	if($w_bou_h !~ /無/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#防具所持？
	if($w_bou_f !~ /無/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#防具所持？
	if($w_bou_a !~ /無/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#道具所持？
	for($i=0; $i<6; $i++){if ($w_item[$i] ne "無"){local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i]\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif ($Command eq "DEATHGET") {  #屍體道具掠奪
	local($itno) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "無") {$itno = $i;}}
	print "要奪走什麼？<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#武器所持？
	if($w_wep !~ /空手/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#防具所持？
	if($w_bou !~ /內衣/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#防具所持？
	if($w_bou_h !~ /無/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#防具所持？
	if($w_bou_f !~ /無/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#防具所持？
	if($w_bou_a !~ /無/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#道具所持？
	for ($i=0; $i<6; $i++) {if ($w_item[$i] ne "無") {local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "POISON")) {	#毒物混入
	$log = ($log . "如果混和這個毒藥…嘿嘿嘿。<BR>") ;
&AS;print "混入什麼毒物？<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"POI_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "PSCHECK")) {	#毒見
	$log = ($log . "試著調查有沒有什麼被混入…。<BR>") ;
&AS;print "做什麼測試嗎？<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"PSC_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "SPIICH")) { #攜帶揚聲器使用
	$log = ($log . "如果使用這個，大家應該聽見…<BR><BR>") ;
	print "使用攜帶揚聲器，向全體人員傳達口信。";
	print "(最多20個全角字)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"speech\"maxlength=\"50\"><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SPEAKER\">傳達</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>終止</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">\n";
#} elsif (($Command eq SPECIAL)&&($Command4 eq "WINCHG")) {	#口頭語變更
#	$log = ($log . "殺害時，變更死亡時的口頭語。<BR>") ;
#	print "請輸入口頭語<BR>(最多32個全角字)<BR><BR>";
#	print "殺害時：<BR><INPUT size=\"30\" type=\"text\" name=\"Message\" maxlength=\"64\" value=\"$msg\"><BR><BR>";
#	print "遺言：<BR><INPUT size=\"30\" type=\"text\" name=\"Message2\" maxlength=\"64\" value=\"$dmes\"><BR><BR>";
#	print "代表句：<BR><INPUT size=\"30\" type=\"text\" name=\"Comment\" maxlength=\"64\" value=\"$com\"><BR><BR>";
#	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "TEAM")) {	#隊伍
	$log = ($log . "小組的組成·加入·脫離<BR>") ;
	print "請輸入小組名<BR>　　 再者，如果脫離<br>　　　　 雙方將再沒有關係。<BR>";
	print "(最多12個全角字)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"teamID2\" maxlength=\"24\" value=\"$teamID\"><BR><BR><BR>";
	print "請輸入密碼：<BR>(8個全角字以內)<BR><BR>";
	if (($teamID ne "")||($teamID ne "無")){$teamPass2 = "不變更的情況"}else{$teamPass2 = "";}
	print "<INPUT size=\"30\" type=\"text\" name=\"teamPass2\" maxlength=\"16\" value=\"$teamPass2\"><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} elsif ($Command eq USRSAVE) {							#用戶數據保存
	local($u_dat) = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n" ;
	open(DB,">$u_save_dir$id$u_save_file"); seek(DB,0,0); print DB $u_dat; close(DB);
	$log = ($log . "正常記錄結束。<BR>") ;
&AS;print "<br><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
} else {
	print "進行什麼？<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>返回</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"決定\">";
}

}
#===========#
# ■ 定義部	#
#===========#
sub definition {
$up = int(($level*$baseexp)+(($level-1)*$baseexp)) ;
$levuprem = $up-$exp;
#Name Def & class
$full_name ="$f_name $l_name";$cln = "$cl $sex$no番" ;
#負傷地方
$kega ="";$kegaimg ="";$condi = "<BR><BR>正常";$kegaa=0;
if (($sta <= "50")||($hit <= "50")){$condition="C";$condi = "<BR><BR>注意"}
if ($inf =~ /頭/) {$kegaimg = ($kegaimg . "H");$kega = ($kega . "頭 ");$kegaa=1;}
if ($inf =~ /腕/) {$kegaimg = ($kegaimg . "A");$kega = ($kega . "腕 ");$kegaa=1;}
if ($inf =~ /腹/) {$kegaimg = ($kegaimg . "B");$kega = ($kega . "腹 ");$kegaa=1;}
if ($inf =~ /足/) {$kegaimg = ($kegaimg . "F");$kega = ($kega . "足 ");$kegaa=1;}
if ($kegaa){$condi = "<BR><BR>負傷";$condition="C";}
if ($inf =~ /毒/) {$condi = "<BR><BR>毒";$condition="P";}
if ($kega eq "")  {$kega = "無" ;}
if (($sta <= "25")&&($hit <= "50")){$condition="D";$condi = "<BR><BR>警告"}
if ($kegaimg eq ""){$kegaimg = ($kegaimg . "OK");}
$kegaimg = ($kegaimg . ".jpg");
$kegaimg = "<IMG src=\"img/$kegaimg\" align=\"top\" border=\"0\" align=\"middle\">";
#Condition
if	 ($condition eq "C") {$CONDITION = "<EMBED src=\"$caution\" HEIGHT=70 width=140>";}
elsif($condition eq "D") {$CONDITION = "<EMBED src=\"$danger\" HEIGHT=70 width=140>";}
elsif($condition eq "P") {$CONDITION = "<EMBED src=\"$poison\" HEIGHT=70 width=140>";}
else {$CONDITION = "<EMBED src=\"$fine\" HEIGHT=70 width=140>";}
#get time
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);  $month++;$year += 1900;$week = ('日','月','火','水','木','金','土') [$wday];
#裝備 Def
($w_name,$w_kind) = split(/<>/, $wep);($b_name,$b_kind) = split(/<>/, $bou);($b_name_h,$b_kind_h) = split(/<>/, $bou_h);($b_name_f,$b_kind_f) = split(/<>/, $bou_f);($b_name_a,$b_kind_a) = split(/<>/, $bou_a);($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
if (($w_kind =~ /G|A/) && ($wtai == 0)) {$watt_2 = int($watt/10) ;}else {$watt_2 = $watt ;}#棍棒 or 子彈鎗 or 箭弓
$ball = $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #裝飾防護具？
#Bar Def
$exp_bar1 = int($exp / $up * 100);$sta_bar1 = int($sta / $maxsta* 100);$hit_bar1 = int($hit / $mhit* 100);

if ($exp_bar1 > 100){$exp_bar1 = 100;}if ($sta_bar1 > 100){$sta_bar1 = 100;}if ($hit_bar1 > 100){$hit_bar1 = 100;}
$exp_bar2 = 100 - $exp_bar1;$sta_bar2 = 100 - $sta_bar1;$hit_bar2 = 100 - $hit_bar1;
$bar_exp1 = "<IMG src=\"$yellow\" width=\"$exp_bar2%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta1 = "<IMG src=\"$red\" width=\"$sta_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit1 = "<IMG src=\"$pink\" width=\"$hit_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_exp2 = "<IMG src=\"$gold\" width=\"$exp_bar1%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta2 = "<IMG src=\"$blue\" width=\"$sta_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit2 = "<IMG src=\"$green\" width=\"$hit_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";
if ($exp_bar2 eq 0){$bar_exp1 = "";}if ($sta_bar2 eq 0){$bar_sta1 = "";}if ($hit_bar2 eq 0){$bar_hit1 = "";}if ($exp_bar1 eq 0){$bar_exp2 = "";}if ($sta_bar1 eq 0){$bar_sta2 = "";}if ($hit_bar1 eq 0){$bar_hit2 = "";}
$bar_exp = "$bar_exp2$bar_exp1";$bar_sta = "$bar_sta2$bar_sta1";$bar_hit = "$bar_hit2$bar_hit1";
}

1;
