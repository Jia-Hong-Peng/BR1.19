#������������������������������������������
#�� 	-    BR COMMAND DISPLAY    - 	 ��
#�� 									 ��
#�� 		�@�@�l�{�Ǥ@���@			 ��
#�� 									 ��
#�� COMMAND		-	���O���@			 ��
#�� definition	-	�w�q��				 ��
#������������������������������������������

#===================#
# �� ���O���@		#
#===================#
sub COMMAND {
local($i) = 0;
if ($sts =~ /�ίv|�v��|�R�i|�u��/) {
	$MESSENGER = "1";
	if ($sts eq "�v��"){
		if($Command eq "HEAL"){$log = ($log . "�v���˱w<BR>");}else{$log = ($log . "�v�����K<BR>");}
		$sts = "�v��";print "�v�����K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"HEAL2\" checked>�v��</A><BR><BR>";
	} elsif ($sts eq "�ίv"){
		if($Command eq "INN"){$log = ($log . "�y�L�Τ@�U<BR>");}else{$log = ($log . "�ίv���K<BR>");}
		$sts = "�ίv";print "�ίv���K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INN2\" checked>�ίv</A><BR><BR>";
	} elsif ($sts eq "�R�i"){
		if($Command eq "INNHEAL"){$log = ($log . "�R�i��<BR>");}else{$log = ($log . "�R�i���K<BR>");}
		$sts = "�R�i";print "�R�i���K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INNHEAL2\" checked>�R�i</A><BR><BR>";
	} elsif ($sts eq "�u��"){
		print "<center><BR>��$WINNUM�^�u�Ӫ�<BR>���`��-$kill<BR><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"��^\"></center>";
		$MESSENGER = "0";return;
	}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\">��^</A><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
	return;
}

if ((($Command eq '')||($Command eq "MAIN"))||(($Command eq "MOVE")&&($Command2 eq "MAIN"))||(($Command eq "ITMAIN")&&($Command3 eq "MAIN"))||(($Command eq "SPECIAL")&&($Command4 eq "MAIN"))) {   #MAIN
	$MESSENGER = "1";
	$log = ($log . "$jyulog$jyulog2$jyulog3�{�b�A�n��˰��K�C<br>") ;
	print "�i�椰��H<BR><BR>";
	if ((($inf =~ /��/)&&($sta > 18))||(($inf !~ /��/)&&($club eq "���W��")&&($sta > 10))||(($inf !~ /��/)&&($sta > 13))){
		print "<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\">";&AS;
		print "<select name=\"Command2\"><option value=\"MAIN\">�� ���� ��<BR>";
			local(@kin_ar) = split(/,/, $arealist[2]);#��T��ϰ쪺�W��@���ƦC�C
			if(($hackflg)||($sts eq "NPC")){$kinlist = "";} #���T��ϰ�@���C
			else{for($k=0;$k<$ar;$k++){ $kinlist = ($kinlist . $kin_ar[$k]);}}#�{�b���T��ϰ�l�[�C
			for ($j=0; $j<$#place+1; $j++) {
				if (($place[$j] ne $place[$pls])&&($kinlist !~ /$place[$j]/)) {print "<option value=\"MV$j\">$place[$j]($area[$j])<BR>";}
				elsif ($place[$j] eq $place[$pls]) {print "<option value=\"MAIN\"><--�{�b��m--><BR>";}
			}#�T��ϰ�B�z����&�{�b��m
		print "</select></A><BR>";
	}
	if ($place[$pls] eq "����") {if (($hackflg eq 1)||($sts eq "NPC")) {$ok = 1;}}
	else {$ok = 0;if (($inf =~ /��/)&&($sta > 25)) {$ok = 1;} elsif (($club eq "�Ю|��")&&($sta > 15)) {$ok = 1;} elsif ($sta > 20) {$ok = 1;}}
	if ($ok){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SEARCH\"> �� ���� ��&nbsp;</A><BR>";}
	print "<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">";&AS;
	print "<select name=\"Command3\"><option value=\"MAIN\">�� �D�� ��<BR><option value=\"ITEM\">�D��ϥΡP�˳�<BR><option value=\"DEL\">�D���m<BR><option value=\"SEIRI\">�D���z<BR><option value=\"GOUSEI\">�D��X��<BR>";
	if ($wep ne "�Ť�<>WP")	{print "<option value=\"WEPDEL\">���U�˳ƪZ��<BR>";
							 print "<option value=\"WEPDEL2\">�˳ƪZ����m<BR>";}
	if ($bou_h ne "�L")	{print "<option value=\"BOUDELH\">���U�Y������<BR>";}
	if ($bou ne "����<>DN")	{print "<option value=\"BOUDELB\">���U�@�騾��<BR>";}
	if ($bou_a ne "�L")	{print "<option value=\"BOUDELA\">���U�ó�����<BR>";}
	if ($bou_f ne "�L")	{print "<option value=\"BOUDELF\">���U��������<BR>";}
	if ($item[5] ne "�L")	{print "<option value=\"BOUDEL\">���U�˹��~<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"kaifuku\">";&AS;
	print "<select name=\"Command5\"><option value=\"MAIN\">�� �^�_ ��<BR><option value=\"HEAL\">�@�v��<BR><option value=\"INN\">�@�ίv<BR>";
	if ($place[$pls] eq "�E����") {print "<option value=\"INNHEAL\">�@�R�i<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">";&AS;
	print "<select name=\"Command4\"><option value=\"MAIN\" selected>�� �S�� ��<BR>";
	print "<option value=\"KOUDOU\">�@�򥻤�w<BR>";
	print "<option value=\"OUSEN\">�@���Ԥ�w<BR>";
	#print "<option value=\"WINCHG\">�@�f�Y�y�ܧ�<BR>";
	if ($sta > 50){print "<option value=\"OUKYU\">�@���汹�I<BR>";}
	print "<option value=\"TEAM\">�@�p��<BR>";
	if (($club eq "�Ʋz��" )&&($sta > 30)) { print "<option value=\"PSCHECK\">�@�r��<BR>"; }
	for ($poi=0; $poi<5; $poi++){if ($item[$poi] eq "�r��<>Y") {print "<option value=\"POISON\">�@�r���V�J<BR>";last;}}
	for ($spi=0; $spi<5; $spi++){if ($item[$spi] eq "��a���n��<>Y") {print "<option value=\"SPIICH\">�@���n���ϥ�<BR>";last;}}
	for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "����PC<>Y")&&($itai[$paso] >= 1)) {print "<option value=\"HACK\">��Hacking��<BR>";last;}}
	print "</select></A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GET")){	#�D��
	local($chkflg) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "�L") {$chkflg = $i;last;}}#�ŹD��H
	if ($chkflg eq "-1"){
		$log = ($log . "�o�ӹD��w�񤣤U�C<br>�ᱼ���ӡH<BR>");
		print "�ᱼ���ӡH<BR><BR>";
		($in, $ik) = split(/<>/, $item_get);&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>$in/$eff_get/$itai_get</A><BR><BR>";
		for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMNEWXCG_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	}else{
		print "�n�p��B�z�o�ӹD��H<BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>�˱�</A><BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMGETNEW\">��</A><BR>";
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "ITEM")){	#�D��
	$log = ($log . "�n��J����K�C<BR>") ;
	print "�Τ���H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEM_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "DEL")){	#�D���m
	$log = ($log . "��z�D�㤤�K�C<BR>");
	print "�ᱼ����H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"DEL_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "SEIRI")){	#�D���z
	$log = ($log . "��z�D�㤤�K�C<BR>");
	print "�n��X����H<BR><BR>";
	print "<select name=\"Command\">";
	print "<option value=\"MAIN\" selected>�פ�</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"SEIRI_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"MAIN\" selected>�פ�</option>";
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "�L") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"SEIRI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GOUSEI")){	#�D��X��
	$log = ($log . "�{�b�������F��A�n�X���s�@�Ǥ���ܡH<BR>") ;
	print "�n�X������H<BR><BR>";
	print "<select name=\"Command\"><option value=\"GOUSEI1_N\" selected>�X��1</option>" ;
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"GOUSEI1_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"GOUSEI2_N\" selected>�X��2</option>" ;
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "�L") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"GOUSEI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><select name=\"Command3\"><option value=\"GOUSEI3_N\" selected>�X��3</option>";
	for ($i3=0; $i3<5; $i3++) {if ($item[$i3] ne "�L") {($in3, $ik3) = split(/<>/, $item[$i3]);print "<option value=\"GOUSEI3_$i3\">$in3/$eff[$i3]/$itai[$i3]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "OUKYU")){	#����B�z
	$log = ($log . "�v���˱w�K�C<BR>") ;
	print "�v����B�H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	if ($inf =~ /�Y/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_0\">�Y</A><BR>"; }
	if ($inf =~ /��/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_1\">��</A><BR>"; }
	if ($inf =~ /��/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_2\">��</A><BR>"; }
	if ($inf =~ /��/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_3\">��</A><BR>"; }
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "KOUDOU")){	#�򥻤�w
	$log = ($log . "�Ҽ{�򥻤�w�K�C<BR>") ;
	print "�ШM�w�򥻤�w�C<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_0\">�q�`</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_1\">��������</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_2\">���s����</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_3\">���K���</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_4\">�į����</A><BR>";
	if($ar >= 7){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_5\">�s�����</A><BR>";}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "OUSEN")){	#���Ԥ�w
	$log = ($log . "�Ҽ{���Ԥ�w�K�C<BR>") ;
	print "�ШM�w���Ԥ�w�C<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_0\">�q�`</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_1\">��������</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_2\">���s����</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_3\">���K���</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_4\">�������</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_5\">�s�����</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_6\">�v���M��</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_7\">�k�]���A</A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command =~ /BATTLE0/){	#�԰����O
	local($a,$wid) = split(/_/, $Command);
	$log = ($log . "����A�n��˰��K�C");$chk = "checked" ;
	print "������H<BR><BR>�V���P�ɵo�X�T���G<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	($w_name,$w_kind) = split(/<>/, $wep);
	if(($w_kind =~ /G/)&&($wtai > 0)){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WG_$wid\" $chk>�g��($wg)</A><BR>"; $chk="";}
	if($w_kind =~ /K/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WK_$wid\" $chk>��(�C)($ws)</A><BR>"; $chk="";}
	if($w_kind =~ /C/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WC_$wid\" $chk>���Y(��)($wc)</A><BR>"; $chk="";}
	if($w_kind =~ /D/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WD_$wid\" $chk>���Y(�z)($wd)</A><BR>"; $chk="";}
	if($w_kind =~ /P|B/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>�ޥ�(��)($wp)</A><BR>"; $chk="";}
	if(($w_kind !~ /G|K|C|D|P|B/)&&(($w_kind =~ /G|A/)&&($wtai eq 0))){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>�ޥ�($wp)</A><BR>"; $chk="";}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"RUNAWAY\">�k�`</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "ITEMJOUTO"){	#�D������
	$log = ($log . "�D���������O�C<BR>");
	print "$w_cl$w_no�f $w_f_name $w_l_name<br>�@�@�@�@�������ӹD��H<INPUT type=\"hidden\" name=\"Command\" value=\"SEITO_$w_id\"><BR><BR>";
	print "<select name=\"Command2\"><option value=\"JO_MAIN\" selected>�פ�</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"JO_$i\">$in/$eff[$i]/$itai[$i]<BR></option>";}}
	print "</select><BR><BR>����<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "BATTLE2"){	#�D�㱰��
	local($itno) = -1;
	for($i=0; $i<5; $i++){if($item[$i] eq "�L"){$itno = $i;}}
	print "�ܨ�����H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#�Z���ҫ��H
	if($w_wep !~ /�Ť�/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#����ҫ��H
	if($w_bou !~ /����/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#����ҫ��H
	if($w_bou_h !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#����ҫ��H
	if($w_bou_f !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#����ҫ��H
	if($w_bou_a !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#�D��ҫ��H
	for($i=0; $i<6; $i++){if ($w_item[$i] ne "�L"){local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i]\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "DEATHGET") {  #����D�㱰��
	local($itno) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "�L") {$itno = $i;}}
	print "�n�ܨ�����H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#�Z���ҫ��H
	if($w_wep !~ /�Ť�/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#����ҫ��H
	if($w_bou !~ /����/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#����ҫ��H
	if($w_bou_h !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#����ҫ��H
	if($w_bou_f !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#����ҫ��H
	if($w_bou_a !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#�D��ҫ��H
	for ($i=0; $i<6; $i++) {if ($w_item[$i] ne "�L") {local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "POISON")) {	#�r���V�J
	$log = ($log . "�p�G�V�M�o�Ӭr�ġK�K�K�K�C<BR>") ;
&AS;print "�V�J����r���H<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"POI_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "PSCHECK")) {	#�r��
	$log = ($log . "�յ۽լd���S������Q�V�J�K�C<BR>") ;
&AS;print "��������նܡH<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"PSC_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "SPIICH")) { #��a���n���ϥ�
	$log = ($log . "�p�G�ϥγo�ӡA�j�a����ť���K<BR><BR>") ;
	print "�ϥ���a���n���A�V����H���ǹF�f�H�C";
	print "(�̦h20�ӥ����r)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"speech\"maxlength=\"50\"><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SPEAKER\">�ǹF</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�פ�</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">\n";
#} elsif (($Command eq SPECIAL)&&($Command4 eq "WINCHG")) {	#�f�Y�y�ܧ�
#	$log = ($log . "���`�ɡA�ܧ󦺤`�ɪ��f�Y�y�C<BR>") ;
#	print "�п�J�f�Y�y<BR>(�̦h32�ӥ����r)<BR><BR>";
#	print "���`�ɡG<BR><INPUT size=\"30\" type=\"text\" name=\"Message\" maxlength=\"64\" value=\"$msg\"><BR><BR>";
#	print "�򨥡G<BR><INPUT size=\"30\" type=\"text\" name=\"Message2\" maxlength=\"64\" value=\"$dmes\"><BR><BR>";
#	print "�N��y�G<BR><INPUT size=\"30\" type=\"text\" name=\"Comment\" maxlength=\"64\" value=\"$com\"><BR><BR>";
#	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "TEAM")) {	#����
	$log = ($log . "�p�ժ��զ��P�[�J�P����<BR>") ;
	print "�п�J�p�զW<BR>�@�@ �A�̡A�p�G����<br>�@�@�@�@ ����N�A�S�����Y�C<BR>";
	print "(�̦h12�ӥ����r)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"teamID2\" maxlength=\"24\" value=\"$teamID\"><BR><BR><BR>";
	print "�п�J�K�X�G<BR>(8�ӥ����r�H��)<BR><BR>";
	if (($teamID ne "")||($teamID ne "�L")){$teamPass2 = "���ܧ󪺱��p"}else{$teamPass2 = "";}
	print "<INPUT size=\"30\" type=\"text\" name=\"teamPass2\" maxlength=\"16\" value=\"$teamPass2\"><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq USRSAVE) {							#�Τ�ƾګO�s
	local($u_dat) = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n" ;
	open(DB,">$u_save_dir$id$u_save_file"); seek(DB,0,0); print DB $u_dat; close(DB);
	$log = ($log . "���`�O�������C<BR>") ;
&AS;print "<br><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} else {
	print "�i�椰��H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>��^</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
}

}
#===========#
# �� �w�q��	#
#===========#
sub definition {
$up = int(($level*$baseexp)+(($level-1)*$baseexp)) ;
$levuprem = $up-$exp;
#Name Def & class
$full_name ="$f_name $l_name";$cln = "$cl $sex$no�f" ;
#�t�˦a��
$kega ="";$kegaimg ="";$condi = "<BR><BR>���`";$kegaa=0;
if (($sta <= "50")||($hit <= "50")){$condition="C";$condi = "<BR><BR>�`�N"}
if ($inf =~ /�Y/) {$kegaimg = ($kegaimg . "H");$kega = ($kega . "�Y ");$kegaa=1;}
if ($inf =~ /��/) {$kegaimg = ($kegaimg . "A");$kega = ($kega . "�� ");$kegaa=1;}
if ($inf =~ /��/) {$kegaimg = ($kegaimg . "B");$kega = ($kega . "�� ");$kegaa=1;}
if ($inf =~ /��/) {$kegaimg = ($kegaimg . "F");$kega = ($kega . "�� ");$kegaa=1;}
if ($kegaa){$condi = "<BR><BR>�t��";$condition="C";}
if ($inf =~ /�r/) {$condi = "<BR><BR>�r";$condition="P";}
if ($kega eq "")  {$kega = "�L" ;}
if (($sta <= "25")&&($hit <= "50")){$condition="D";$condi = "<BR><BR>ĵ�i"}
if ($kegaimg eq ""){$kegaimg = ($kegaimg . "OK");}
$kegaimg = ($kegaimg . ".jpg");
$kegaimg = "<IMG src=\"img/$kegaimg\" align=\"top\" border=\"0\" align=\"middle\">";
#Condition
if	 ($condition eq "C") {$CONDITION = "<EMBED src=\"$caution\" HEIGHT=70 width=140>";}
elsif($condition eq "D") {$CONDITION = "<EMBED src=\"$danger\" HEIGHT=70 width=140>";}
elsif($condition eq "P") {$CONDITION = "<EMBED src=\"$poison\" HEIGHT=70 width=140>";}
else {$CONDITION = "<EMBED src=\"$fine\" HEIGHT=70 width=140>";}
#get time
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);  $month++;$year += 1900;$week = ('��','��','��','��','��','��','�g') [$wday];
#�˳� Def
($w_name,$w_kind) = split(/<>/, $wep);($b_name,$b_kind) = split(/<>/, $bou);($b_name_h,$b_kind_h) = split(/<>/, $bou_h);($b_name_f,$b_kind_f) = split(/<>/, $bou_f);($b_name_a,$b_kind_a) = split(/<>/, $bou_a);($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
if (($w_kind =~ /G|A/) && ($wtai == 0)) {$watt_2 = int($watt/10) ;}else {$watt_2 = $watt ;}#�Ҵ� or �l�u�� or �b�}
$ball = $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #�˹����@��H
#Bar Def
$exp_bar1 = int($exp / $up * 100);$sta_bar1 = int($sta / $maxsta* 100);$hit_bar1 = int($hit / $mhit* 100);

if ($exp_bar1 > 100){$exp_bar1 = 100;}if ($sta_bar1 > 100){$sta_bar1 = 100;}if ($hit_bar1 > 100){$hit_bar1 = 100;}
$exp_bar2 = 100 - $exp_bar1;$sta_bar2 = 100 - $sta_bar1;$hit_bar2 = 100 - $hit_bar1;
$bar_exp1 = "<IMG src=\"$yellow\" width=\"$exp_bar2%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta1 = "<IMG src=\"$red\" width=\"$sta_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit1 = "<IMG src=\"$pink\" width=\"$hit_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_exp2 = "<IMG src=\"$gold\" width=\"$exp_bar1%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta2 = "<IMG src=\"$blue\" width=\"$sta_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit2 = "<IMG src=\"$green\" width=\"$hit_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";
if ($exp_bar2 eq 0){$bar_exp1 = "";}if ($sta_bar2 eq 0){$bar_sta1 = "";}if ($hit_bar2 eq 0){$bar_hit1 = "";}if ($exp_bar1 eq 0){$bar_exp2 = "";}if ($sta_bar1 eq 0){$bar_sta2 = "";}if ($hit_bar1 eq 0){$bar_hit2 = "";}
$bar_exp = "$bar_exp2$bar_exp1";$bar_sta = "$bar_sta2$bar_sta1";$bar_hit = "$bar_hit2$bar_hit1";
}

1;
