#! /usr/bin/perl

#□■□■□■□■□■□■□■□■□■□■□
#■ 	-      BR MAIN SCRIPT      - 	 ■
#□ 									 □
#■ 	　　	子程序一覽	　　		 ■
#□ 									 □
#■ MAIN	-	主要處理				 ■
#□ COM		-	指令處理　　			 □
#■ HEAL	-	治療處理				 ■
#□ INN		-	睡眠處理				 □
#■ INNHEAL	-	靜養處理				 ■
#□ BB_CK	-	不正當瀏覽防止　　　	 □
#■□■□■□■□■□■□■□■□■□■□■

#require"jcode.pl";
require"br.cgi";
require"$LIB_DIR/lib1.cgi";

&LOCK;
require"pref.cgi";
&DECODE;
&CREAD;
&IDCHK;
if ($mode eq "main"){&MAIN;}
elsif ($mode eq "command"){&COM;}
else {&ERROR("不正當的訪問","No Command selected","BATTLE");}
&UNLOCK;
exit;
#==================#
# ■ 主要處理	   #
#==================#
sub MAIN {
	&HEADER;
	require"$LIB_DIR/disp_sts.cgi";
	require"$LIB_DIR/disp_cmd.cgi";
	&STS();
	&FOOTER;
}
#==================#
# ■ 指令處理　　  #
#==================#
sub COM {
#★ 移動·檢索·勝利時
if (($Command eq "MOVE")&&($Command2 =~ /MV/))	{require "$LIB_DIR/lib2.cgi";&MOVE;}				#移動
elsif($Command eq "SEARCH")						{require "$LIB_DIR/lib2.cgi";&SEARCH;}				#探索
elsif($Command =~ /GET_/)						{require "$LIB_DIR/lib2.cgi";&WINGET;}				#戰利品
#★ 恢復處理部
elsif($Command eq "kaifuku"){	if($Command5 eq "HEAL")		{&HEAL;}								#治療
								if($Command5 eq "INN")		{&INN;}									#睡眠
								if($Command5 eq "INNHEAL")	{&INNHEAL;}}							#靜養
elsif($Command eq "HEAL")	{&HEAL;}																#治療
elsif($Command eq "INN")	{&INN;}																	#睡眠
elsif($Command eq "INNHEAL"){&INNHEAL;}																#靜養
#★ ITEM1
elsif($Command =~ /ITEM_/)			{require "$LIB_DIR/item1.cgi";&ITEM;}							#道具使用
elsif($Command =~ /DEL_/)			{require "$LIB_DIR/item1.cgi";&ITEMDEL;}						#道具棄置
elsif($Command eq "ITEMDELNEW")		{require "$LIB_DIR/item1.cgi";&ITEMDELNEW;}						#道具丟棄
elsif($Command eq "ITEMGETNEW")		{require "$LIB_DIR/item1.cgi";&ITEMGETNEW;}						#道具撿拾
elsif($Command =~ /ITEMNEWXCG_/)	{require "$LIB_DIR/item1.cgi";&ITEMNEWXCG;}						#道具交換
elsif($Command eq "ITMAIN"){if($Command3 eq "WEPDEL")	{require "$LIB_DIR/item1.cgi";&WEPDEL;}		#武器除下
							if($Command3 eq "WEPDEL2")	{require "$LIB_DIR/item1.cgi";&WEPDEL2;}	#武器丟棄
							if($Command3 eq "BOUDELH")	{require "$LIB_DIR/item1.cgi";&BOUDELH;}	#頭防具除下
							if($Command3 eq "BOUDELB")	{require "$LIB_DIR/item1.cgi";&BOUDELB;}	#體防具除下
							if($Command3 eq "BOUDELA")	{require "$LIB_DIR/item1.cgi";&BOUDELA;}	#腕防具除下
							if($Command3 eq "BOUDELF")	{require "$LIB_DIR/item1.cgi";&BOUDELF;}	#足防具除下
							if($Command3 eq "BOUDEL")	{require "$LIB_DIR/item1.cgi";&BOUDEL;}}	#裝飾品除下
#★ ATTACK
elsif($Command =~ /ATK/)		{require "$LIB_DIR/attack.cgi";require"$LIB_DIR/lib4.cgi";&ATTACK1;}#攻擊
elsif($Command eq "RUNAWAY")	{require "$LIB_DIR/attack.cgi";&RUNAWAY;}							#逃亡
#★ LIB3
elsif($Command =~ /OUK_/)								{require"$LIB_DIR/lib3.cgi";&OUKYU;}		#應急處置
elsif(($msg2 ne "")||($dmes2 ne "")||($com2 ne ""))		{require"$LIB_DIR/lib3.cgi";&WINCHG;}		#口頭語變更
elsif(($teamID2 ne "")||($teamPass2 ne ""))				{require"$LIB_DIR/lib3.cgi";&TEAM;}			#小組操作
elsif($Command eq "SPECIAL"){if($Command4 eq "SPEAKER")	{require "$LIB_DIR/lib3.cgi";&SPEAKER;}		#攜帶揚聲器使用
							 if($Command4 eq "HACK")	{require "$LIB_DIR/lib3.cgi";&HACKING;}}	#Hacking
elsif($Command =~ /KOU_/)		{require"$LIB_DIR/lib3.cgi";&KOUDOU;}								#基本方針
elsif($Command =~ /OUS_/)		{require"$LIB_DIR/lib3.cgi";&OUSEN;}								#應戰方針
elsif ($Command eq "SEVE")		{require"$LIB_DIR/lib3.cgi";&SEVE;}									#Messener
elsif($Command =~ /POI_/)		{require "$LIB_DIR/lib3.cgi";&POISON;}								#毒物混入
elsif($Command =~ /PSC_/)		{require "$LIB_DIR/lib3.cgi";&PSCHECK;}								#毒見
#★ ITEM2
elsif(($Command =~ /SEIRI_/)&&($Command2 =~ /SEIRI2_/)){require "$LIB_DIR/item2.cgi";&ITEMSEIRI;}	#道具整理
elsif(($Command =~ /GOUSEI1_/)&&($Command2 =~ /GOUSEI2_/)&&($Command3 =~ /GOUSEI3_/))
														{require "$LIB_DIR/item2.cgi";&ITEMGOUSEI;}	#道具合成
elsif(($Command =~ /SEITO_/)&&($Command2 =~ /JO_/)) {require "$LIB_DIR/item2.cgi";&ITEMJOUTO;}		#道具轉讓
#★ ADMIN
elsif($Command eq "BSAVE")	{require "admin.cgi";&BACKSAVE;}										#保存
elsif($Command eq "BREAD")	{require "admin.cgi";&BACKREAD;}										#讀入
elsif($Command eq "RESET")	{require "admin.cgi";&DATARESET;}										#初始化
#★ 表示部
if(($Command =~ /BATTLE/)||($Command =~ /ATK/))
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#戰鬥結果
elsif($Command eq "ITEMJOUTO")
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#道具轉讓
elsif ($mflg ne "ON") {&MAIN;}
}
#===========================#
# ■ 治療·睡眠·靜養處理　	#
#===========================#
sub HEAL	{$sts = "治療";$endtime = $now;&SAVE;}
sub INN		{$sts = "睡眠";$endtime = $now;&SAVE;}
sub INNHEAL	{$sts = "靜養";$endtime = $now;&SAVE;}
#===========================#
# ■ 不正當瀏覽防止　　　　 #
#===========================#
sub BB_CK{if($wf eq $w_id){$wf = "";}else{&ERROR("不正當訪問。","Used Browser Back Command","BATTLE-BB_CK");}}
1;
