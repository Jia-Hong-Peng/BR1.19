#==================#
# �� �D����o  ��  #
#==================#
sub ITEMGET {

local($i) = 0 ;
local($chkflg) = -1;
local($sub) = "";

local($filename) = "$LOG_DIR/$pls$item_file";

open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);

if ($#itemlist < 0) {$log = ($log . "�o�Ӱϰ�w�g�����S���ܡK�H<BR>") ;$chksts="OK";return ;}
else {
	local($work) = int(rand($#itemlist)) ;#�H�����o�D��
	local($getitem,$geteff,$gettai) = split(/,/, $itemlist[$work]) ;#�D����o����
	local($itname,$itkind) = split(/<>/, $getitem);#�D����Ψ��o
	local($delitem) = splice(@itemlist,$work,1) ;#���o���D��R��
	if ($getitem =~ /<>TO/) { #����
		open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
		$result = int(rand($geteff/2)+($geteff/2));
		$log = ($log . "�O�����I���F $itname�A���� <font color=\"red\"><b>$result</b></font> �ˮ`�C<BR>") ;
		$hit-=$result;
		if ($hit <= 0) {$hit = 0;$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;&LOGSAVE("DEATH") ;$mem--;if ($mem == 1) {&LOGSAVE("WINEND1") ;}}#���`���A
		return ;
	}
#�D����o���yLog
	if	 ($getitem =~ /<>HH|<>HD/)	{$sub = "�Y�U�i�H�^�_��O�C";}
	elsif($getitem =~ /<>SH|<>SD/)	{$sub = "�Y�U�i�H�^�_��q�C";}
	elsif($getitem =~ /<>W/)		{$sub = "�o�ӪF��i�H�@���Z���C";}#�Z���H
	elsif($getitem =~ /<>D/)		{$sub = "�o�ӪF��i�H�@������C";}#����
	elsif($getitem =~ /<>A/)		{$sub = "�o�ӪF��i�H�˳ơC";}#�˹�
	elsif($getitem =~ /<>TN/)		{$sub = "�o�ӪF���G�m�����C"; }#����
	else {$sub = "�@�w�i�H�b����̯�ϥΧa�C";}

	($itname,$kind) = split(/<>/, $getitem) ;
		if ($kind =~ /HH|HD/) {$itemtype = "�i��O�^�_�j";}
		elsif ($kind =~ /SH|SD/){$itemtype = "�i��q�^�_�j";}
		elsif ($kind eq TN)		{$itemtype = "�i�����j";}
		elsif ($kind =~ /W/)	{$itemtype = "�i�Z��";
			if ($kind =~ /G/)	{$itemtype = ($itemtype . "(��)");}
			if ($kind =~ /K/)	{$itemtype = ($itemtype . "(�C)");}
			if ($kind =~ /C/)	{$itemtype = ($itemtype . "(��)");}
			if ($kind =~ /B/)	{$itemtype = ($itemtype . "(��)");}
			if ($kind =~ /D/)	{$itemtype = ($itemtype . "(�z)");}
			$itemtype = ($itemtype . "�j");}
		elsif ($kind =~ /D/)	{$itemtype = "�i����";
			if ($kind =~ /B/)	{$itemtype = ($itemtype . "(��)");}
			if ($kind =~ /H/)	{$itemtype = ($itemtype . "(�Y)");}
			if ($kind =~ /F/)	{$itemtype = ($itemtype . "(��)");}
			if ($kind =~ /A/)	{$itemtype = ($itemtype . "(��)");}
			$itemtype = ($itemtype . "�j");}
		elsif (($kind eq R1)||($kind eq R2)) {$itemtype = "�i�p�F�j";}
		elsif ($kind eq Y) {
			if (($itname eq "���C���Ѱ��_��")||($itname eq "�C���Ѱ��_��")) {$itemtype = "�i�Ѱ��_�͡j";}
			elsif ($itname eq "�l�u") {$itemtype = "�i�u�j";}
			else {$itemtype = "�i�D��j";}}
		elsif ($kind eq A) {$itemtype = "�i�˹��~�j";}
		else {$itemtype = "�i�����j";}

	$log = ($log . "$itname (�ġG$geteff �ơG$gettai) <font color=\"00ffff\">$itemtype</font> �o�{�C<br>$sub<BR>") ;

	$sameitem = 0;
	for ($i=0; $i<5; $i++){#�P�@�D��P�_
		if (($item[$i] eq $getitem)&&($getitem =~ /<>WC|<>TN|<>NR|�l�u|��ñ|�i�M��|�Ѭr��|�_���u��|�q��/)){$chkflg = $i;$sameitem = 1;last;}
		if (($item[$i] eq $getitem)&&($getitem =~ /��|�ѥ]/)){$chkflg = $i;$sameitem = 2;last;}
	}

	if ($sameitem eq "1") {#�o�{�P�˪��D���
		open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
		if ($item[$chkflg] =~ /�l�u/) {$eff[$chkflg] += $geteff;}
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
# �� �D��洫�@�@  #
#==================#
sub ITEMNEWXCG {
local($wk) = $Command;$wk =~ s/ITEMNEWXCG_//g;
if (($item[$wk] eq "�L")||($item_get eq "�L")) {&ERROR("�������X�ݡC");}
local($in, $ik) = split(/<>/, $item_get);
local($in2, $ik2) = split(/<>/, $item[$wk]);

$log = ($log . "$in �߬B�A$in2 ��m�C<br>") ;

local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
$item[$wk] = $item_get;
$eff[$wk] = $eff_get;
$itai[$wk] = $itai_get;

$item_get = "�L"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;
}
#=====================#
# �� �D���m�@�@�@�@ #
#=====================#
sub ITEMDELNEW {
if (($item_get eq "�L")||(($item_get eq ""))){$log = ($log . "�߰_�C<br>");}
else{
	local($in, $ik) = split(/<>/, $item_get);
	$log = ($log . "$in �߬B�C<br>");
	local($filename) = "$LOG_DIR/$pls$item_file";
	open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
	push(@itemlist,"$item_get,$eff_get,$itai_get,\n") ;
	open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
}
$item_get = "�L"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;
}
#==================#
# �� �D��߬B�@�@�@#
#==================#
sub ITEMGETNEW {
if ($item_get eq "�L") {&ERROR("�������X�ݡC"."NO NEW TITEM"."ITEM-ITEMGETNEW");}
local($chkflg) = -1;
for ($i=0; $i<5; $i++) {if ($item[$i] eq "�L") {$chkflg = $i;last;}}#�D�����H
if ($chkflg eq -1) {$log = ($log . "�D����w���C<BR>$itname ����߬B�C<BR>");}#�ҫ��~��
else{
	if ($item[$chkflg] eq "�L") {$item[$chkflg] = $item_get; $eff[$chkflg] = $eff_get; $itai[$chkflg] = $itai_get;}
	($itname,$kind) = split(/<>/, $item_get) ;
	$log = ($log . "��o�F $itname�C$sub<BR>") ;
}

$item_get = "�L"; $eff_get = 0; $itai_get = 0 ;
$Command = "MAIN";

&SAVE;

}
#==================#
# �� �D����@�@  #
#==================#
sub ITEMDEL {

local($wk) = $Command;
$wk =~ s/DEL_//g;

if ($item[$wk] eq "�L") {&ERROR("�������X�ݡC");}

local($in, $ik) = split(/<>/, $item[$wk]);

$log = ($log . "$in ��m�C<br>") ;

local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;
$Command = "MAIN";

&SAVE;

}
#==================#
# �� �D��ϥΡ@�@  #
#==================#
sub ITEM {

local($result) = 0;local($wep2) = "" ;local($watt2) = 0;local($wtai2) = 0 ;local($up) = 0 ;

local($wk) = $Command;$wk =~ s/ITEM_//g;

if ($item[$wk] eq "�L") {&ERROR("�������X�ݡC");}

local($in, $ik) = split(/<>/, $item[$wk]);local($w_name,$w_kind) = split(/<>/, $wep);local($d_name,$d_kind) = split(/<>/, $bou);

if ($item[$wk] =~ /<>SH/) { #��q�^�_
	$log = ($log . "$in �ϥΡC<BR>��q�^�_�C<BR>");
	$sta += $eff[$wk] ;
	if ($sta > $maxsta) {$sta = $maxsta;}
	$itai[$wk] --;
	if ($itai[$wk] == 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
} elsif($item[$wk] =~ /<>HH/) { #��O�^�_
	$log = ($log . "$in �ϥΡC<BR>��O�^�_�C<BR>");
	$hit += $eff[$wk] ;
	if ($hit > $mhit) {$hit = $mhit;}
	$itai[$wk] --;
	if ($itai[$wk] == 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
} elsif($in eq "�Ѭr��") { #�Ѭr
	if ($inf =~ /�r/){$log = ($log . "$in �ϥΡC<BR>�r���A�Ѱ��C<BR>");$inf =~ s/�r//g;$itai[$wk] --;if ($itai[$wk] == 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ; }}
	else {$log = ($log . "$in �ϥΤ]�S���N�q�C<BR>");}
} elsif($item[$wk] =~ /<>SD|<>HD/) {	#�r�J
	if	 ($item[$wk] =~ /<>SD2|<>HD2/){$result = int($eff[$wk]*2);}#�Ʋz���S�s�H
	elsif($item[$wk] =~ /<>SD1|<>HD1/){$result = int($eff[$wk]*1.5);}#��O��
	else { $result = $eff[$wk] ; }
	$inf =~ s/�r//g ;$inf = ($inf . "�r");
	$hit -= $result ;
	$log = ($log . "��K�V�|�I<BR>�n���Q�r���V�J�F�I����<BR><font color=\"red\"><b>$result</b></font>�I<BR>\n") ;
	$itai[$wk] --;
	local($tp, $poisonid) = split(/-/, $item[$wk]);
	$wb = $poisonid;
	$poisoni = $item[$wk];
	if ($itai[$wk] == 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
	$poisondeadchk = 1;
	if ($hit <= 0){require "$LIB_DIR/lib3.cgi";&POISONDEAD;}
} elsif(($item[$wk] =~ /<>W/) && ($item[$wk] !~ /<>WF/)) {  #�Z���˳�
	$log = ($log . "$in �˳ơC<BR>") ;
	$wep2 = $wep; $watt2 = $watt; $wtai2 = $wtai ;
	$wep = $item[$wk]; $watt = $eff[$wk]; $wtai = $itai[$wk] ;
	if ($wep2 !~ /�Ť�/) {$item[$wk] = $wep2; $eff[$wk] = $watt2; $itai[$wk] = $wtai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DB/) { #����˳� (��)
	$log = ($log . "$in �@�騾��˳ơC<BR>");
	$bou2 = $bou; $bdef2 = $bdef; $btai2 = $btai ;
	$bou = $item[$wk]; $bdef = $eff[$wk]; $btai = $itai[$wk] ;
	if ($bou2 !~ /����/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DH/) { #����˳� (�Y)
	$log = ($log . "$in �Y������˳ơC<BR>");
	$bou2 = $bou_h; $bdef2 = $bdef_h; $btai2 = $btai_h ;
	$bou_h = $item[$wk]; $bdef_h = $eff[$wk]; $btai_h = $itai[$wk] ;
	if ($bou2 !~ /�L/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DF/) { #����˳� (��)
	$log = ($log . "$in ��������˳ơC<BR>");
	$bou2 = $bou_f; $bdef2 = $bdef_f; $btai2 = $btai_f ;
	$bou_f = $item[$wk]; $bdef_f = $eff[$wk]; $btai_f = $itai[$wk] ;
	if ($bou2 !~ /�L/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>DA/) { #����˳� (��)
	$log = ($log . "$in �ó�����˳ơC<BR>");
	$bou2 = $bou_a; $bdef2 = $bdef_a; $btai2 = $btai_a ;
	$bou_a = $item[$wk]; $bdef_a = $eff[$wk]; $btai_a = $itai[$wk] ;
	if ($bou2 !~ /�L/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>A/) {  #����˳�
	$log = ($log . "$in ����˳ơC<BR>");
	$bou2 = $item[5]; $bdef2 = $eff[5]; $btai2 = $itai[5] ;
	$item[5] = $item[$wk]; $eff[5] = $eff[$wk]; $itai[5] = $itai[$wk] ;
	if ($bou2 !~ /�L/) {$item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;}
	else {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif($item[$wk] =~ /<>R/) {  #�p�F
	&HEADER;require"$LIB_DIR/disp.cgi";&READER;&FOOTER;
} elsif($item[$wk] =~ /<>TN/) { #����
	$log = ($log . "$in �����˳]�F�C<BR>�ۤv�]���H�o�{�K�C<BR>");
	$item[$wk] =~ s/TN/TO/g ;
	$filename = "$LOG_DIR/$pls$item_file";
	open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
	push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
	open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
	$itai[$wk] -- ;$item[$wk] =~ s/TO/TN/g ;
	if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in eq "�i�M��") && ($wep =~ /<>WK/)) { #�i�M�ۨϥ�&�p�M�t�˳ơH
	$watt += (int(rand(2)) + $eff[$wk]);
	$log = ($log . "$in �ϥΡC<BR>$w_name �����O�ܦ� $watt�C<BR>");
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in eq "�_���u��") && ($d_kind eq "DB") && ($d_name ne "����")) { #�_���u��&��A�t�˳ơH
	$btai += (int(rand(2)) + $eff[$wk]);
	$log = ($log . "$in �ϥΡC<BR>$d_name �@�[�O�ܦ� $btai�C<BR>");
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} elsif(($in =~ /�l�u/) && ($wep =~ /<>WG/)) {  #�l�u�ϥ�&�j�t�˳ơH

	$up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; } else { $up = $eff[$wk]; }
	$wtai += $up ; $eff[$wk] -= $up ;

	if ($eff[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
	if ($wep =~ /<>WGB/) { $wep =~ s/<>WGB/<>WG/g;}
	$log = ($log . "$in�A$w_name �˼u�q�ɥR�C<BR>$w_name ���ϥΦ^�� $up �����C<BR>");
} elsif(($in =~ /�b/) && ($wep =~ /<>WA/)) {	#�b�ϥ�&�}�t�˳ơH
	$up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; }else { $up = $eff[$wk]; }
	$wtai += $up ; $eff[$wk] -= $up;
	if ($eff[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
	if ($wep =~ /<>WAB/) { $wep =~ s/<>WAB/<>WA/g ;}
	$log = ($log . "$in �ϥΡA$w_name ���}�b�ƶq�ɥR�C<BR>$w_name ���ϥΦ^�� $up �����C<BR>");
} elsif($in =~ /�q��/){
	my($pc_ck) = 0;
	for ($paso=0; $paso<5; $paso++){
		if (($item[$paso] eq "����PC<>Y")&&($itai[$paso] < 5)){
			$itai[$paso] += $eff[$wk];
			if($itai[$paso] > 5){ $itai[$paso] = 5; }
			$itai[$wk] -- ;
			if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
			$log = ($log . "$in ����PC�R�q�C<BR>����PC���ϥΦ^�� $itai[$paso] �W�[�C<BR>");
			$pc_ck = 1;
			last;
		}
	}
	if ($pc_ck == 0){$log = ($log . "�o�ӪF��n�p��ϥΡK�C<BR>");$Command="MAIN";}
} elsif($in eq "����PC") {$Command4="HACK";require "$LIB_DIR/lib3.cgi";&HACKING;
} elsif($in eq "�C���Ѱ��_��") {
	if ($pls eq 0){
		$inf = ($inf . "��");
		open(FLAG,">$end_flag_file"); print(FLAG "�Ѱ��פF\n"); close(FLAG);
		&LOGSAVE("EX_END");
		$log = ($log . "�ϥθѰ��_�Ͱ���F�C���C<br>����渨�F�I<BR>");$Command="MAIN";
		&SAVE;
	}else{
		$log = ($log . "�b�o�̨ϥΨS������N�q�K�C<BR>");$Command="MAIN";
	}
} elsif ($in eq "��ñ") { #��ñ�ϥ�
	$log = ($log . "��ñ�ܡH�յۥ��}�C<BR>\n");
	local($omi) = int(rand(100)) ;
	if	  ($omi < 20) {$omi="2";&omikuji1;$log = ($log . "�O�j�N�I�֭n������n�Ƶo�ͤF�I<BR><font color=\"00FFFF\">�i��j+$lvuphit �i��j+$lvupatt �i���j+$lvupdef</font><BR>") ;}
	elsif ($omi < 40) {$omi="1";&omikuji1;$log = ($log . "���N�ܡH�Pı�u�n�I<BR><font color=\"00FFFF\">�i��j+$lvuphit �i��j+$lvupatt �i���j+$lvupdef</font><BR>") ;}
	elsif ($omi < 60) {$omi="0";&omikuji1;$log = ($log . "�p�N�ܡH����L�]�S��������O...�H<BR><font color=\"00FFFF\">�i��j+$lvuphit �i��j+$lvupatt �i���j+$lvupdef</font><BR>") ;}
	elsif ($omi < 80) {$omi="0";&omikuji2;$log = ($log . "���Ϊ̡K�C�����A���N�Q�K�C<BR><font color=\"00FFFF\">�i��j-$lvuphit �i��j-$lvupatt �i���j-$lvupdef</font><BR>") ;}
	else {$omi="1";&omikuji2; $log = ($log . "�j��??�`ı�o������i�Ȫ��Ƨ֭n���{�K�C<BR><font color=\"00FFFF\">�i��j-$lvuphit �i��j-$lvupatt �i���j-$lvupdef</font><BR>") ; }
	$itai[$wk] -- ;
	if ($itai[$wk] <= 0) {$item[$wk] = "�L"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
} else {
	$log = ($log . "������ϥγo�ӪF��K�C<BR>");$Command="MAIN";
}

$Command = "MAIN";

&SAVE;

}
#==================#
# �� ��ñrandom�@�@#
#==================#
sub omikuji1 {$lvuphit = int(rand(2) + $omi);$lvupatt = int(rand(2) + $omi);$lvupdef = int(rand(2) + $omi);
$hit += $lvuphit ;$mhit += $lvuphit ; $att += $lvupatt; $def += $lvupdef;
}
sub omikuji2 {$lvuphit = int(rand(2) + $omi);$lvupatt = int(rand(2) + $omi);$lvupdef = int(rand(2) + $omi);
$hit -= $lvuphit ;$mhit -= $lvuphit ; $att -= $lvupatt; $def -= $lvupdef;
}
#========================#
# �� ���U�˳ƪZ�����B�z  #
#========================#
sub WEPDEL {
local($j) = 0 ;
if ($wep =~ /�Ť�/) {$log = ($log . "$l_name �S���˳ƪZ���C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $wep);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $wep; $eff[$j] = $watt; $itai[$j] = $wtai ;
	$wep = "�Ť�<>WP"; $watt = 0; $wtai = "��" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#==================#
# �� �˳ƪZ���߸m  #
#==================#
sub WEPDEL2 {
if ($wep =~ /�Ť�/) {$log = ($log . "$l_name�S���˳ƪZ���C<br>") ;$Command = "MAIN" ;return ;}
local($in, $ik) = split(/<>/, $wep);
$log = ($log . "$in �ᱼ�C<br>") ;
#�Z�����
local($filename) = "$LOG_DIR/$pls$item_file";
open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
push(@itemlist,"$wep,$watt,$wtai,\n") ;
open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
$wep = "�Ť�<>WP"; $watt = 0; $wtai = "��" ;
$Command = "MAIN";
&SAVE;
}
#======================#
# �� ���U�Y���㪺�B�z  #
#======================#
sub BOUDELH {
local($j) = 0 ;
if ($bou_h =~ /�L/) {$log = ($log . "$l_name�S���˳��Y������C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_h);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $bou_h; $eff[$j] = $bdef_h; $itai[$j] = $btai_h ;
	$bou_h = "�L"; $bdef_h = 0; $btai_h = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#========================#
# �� ���U���騾�㪺�B�z  #
#========================#
sub BOUDELB {
local($j) = 0 ;
if ($bou =~ /����/) {$log = ($log . "$l_name�S���˳��@�騾��C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $bou; $eff[$j] = $bdef; $itai[$j] = $btai ;
	$bou = "����<>DN"; $bdef = 0; $btai = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#========================#
# �� ���U���u���㪺�B�z  #
#========================#
sub BOUDELA {
local($j) = 0 ;
if ($bou_a =~ /�L/) {$log = ($log . "$l_name�S���˳Ƶó�����C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_a);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $bou_a; $eff[$j] = $bdef_a; $itai[$j] = $btai_a ;
	$bou_a = "�L"; $bdef_a = 0; $btai_a = 0 ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#==================#
# �� �����㪺�B�z  #
#==================#
sub BOUDELF {
local($j) = 0 ;
if ($bou_f =~ /�L/) {$log = ($log . "$l_name�S���˳ƨ�������C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $bou_f);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $bou_f; $eff[$j] = $bdef_f; $itai[$j] = $btai_f ;
	$bou_f = "�L"; $bdef_f = 0; $btai_f = "��" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
#======================#
# �� ���U�˹��~���B�z  #
#======================#
sub BOUDEL {
local($j) = 0 ;
if ($item[5] =~ /�L/) {$log = ($log . "$l_name�S���˳Ƹ˹��~�C<br>") ;$Command = "MAIN" ;return ;}
($w_name,$w_kind) = split(/<>/, $item[5]);
#��a�����~�Ŷ��T�{
local($chk) = "NG" ;
for ($j=0; $j<5; $j++) {if ($item[$j] eq "�L") {$chk = "ON" ; last;}}
if ($chk eq "NG") {$log = ($log . "���~�񤣤U�A�D����w���C<br>") ;
} else {
	$log = ($log . "$w_name�w���J�D����C<br>") ;
	$item[$j] = $item[5]; $eff[$j] = $eff[5]; $itai[$j] = $itai[5] ;
	$item[5] = "�L"; $eff[5] = 0; $itai[5] = "0" ;
	&SAVE ;
}
$Command = "MAIN" ;
}
1;