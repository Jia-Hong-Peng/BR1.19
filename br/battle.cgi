#! /usr/bin/perl

#������������������������������������������
#�� 	-      BR MAIN SCRIPT      - 	 ��
#�� 									 ��
#�� 	�@�@	�l�{�Ǥ@��	�@�@		 ��
#�� 									 ��
#�� MAIN	-	�D�n�B�z				 ��
#�� COM		-	���O�B�z�@�@			 ��
#�� HEAL	-	�v���B�z				 ��
#�� INN		-	�ίv�B�z				 ��
#�� INNHEAL	-	�R�i�B�z				 ��
#�� BB_CK	-	�������s������@�@�@	 ��
#������������������������������������������

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
else {&ERROR("�������X��","No Command selected","BATTLE");}
&UNLOCK;
exit;
#==================#
# �� �D�n�B�z	   #
#==================#
sub MAIN {
	&HEADER;
	require"$LIB_DIR/disp_sts.cgi";
	require"$LIB_DIR/disp_cmd.cgi";
	&STS();
	&FOOTER;
}
#==================#
# �� ���O�B�z�@�@  #
#==================#
sub COM {
#�� ���ʡP�˯��P�ӧQ��
if (($Command eq "MOVE")&&($Command2 =~ /MV/))	{require "$LIB_DIR/lib2.cgi";&MOVE;}				#����
elsif($Command eq "SEARCH")						{require "$LIB_DIR/lib2.cgi";&SEARCH;}				#����
elsif($Command =~ /GET_/)						{require "$LIB_DIR/lib2.cgi";&WINGET;}				#�ԧQ�~
#�� ��_�B�z��
elsif($Command eq "kaifuku"){	if($Command5 eq "HEAL")		{&HEAL;}								#�v��
								if($Command5 eq "INN")		{&INN;}									#�ίv
								if($Command5 eq "INNHEAL")	{&INNHEAL;}}							#�R�i
elsif($Command eq "HEAL")	{&HEAL;}																#�v��
elsif($Command eq "INN")	{&INN;}																	#�ίv
elsif($Command eq "INNHEAL"){&INNHEAL;}																#�R�i
#�� ITEM1
elsif($Command =~ /ITEM_/)			{require "$LIB_DIR/item1.cgi";&ITEM;}							#�D��ϥ�
elsif($Command =~ /DEL_/)			{require "$LIB_DIR/item1.cgi";&ITEMDEL;}						#�D���m
elsif($Command eq "ITEMDELNEW")		{require "$LIB_DIR/item1.cgi";&ITEMDELNEW;}						#�D����
elsif($Command eq "ITEMGETNEW")		{require "$LIB_DIR/item1.cgi";&ITEMGETNEW;}						#�D��߬B
elsif($Command =~ /ITEMNEWXCG_/)	{require "$LIB_DIR/item1.cgi";&ITEMNEWXCG;}						#�D��洫
elsif($Command eq "ITMAIN"){if($Command3 eq "WEPDEL")	{require "$LIB_DIR/item1.cgi";&WEPDEL;}		#�Z�����U
							if($Command3 eq "WEPDEL2")	{require "$LIB_DIR/item1.cgi";&WEPDEL2;}	#�Z�����
							if($Command3 eq "BOUDELH")	{require "$LIB_DIR/item1.cgi";&BOUDELH;}	#�Y���㰣�U
							if($Command3 eq "BOUDELB")	{require "$LIB_DIR/item1.cgi";&BOUDELB;}	#�騾�㰣�U
							if($Command3 eq "BOUDELA")	{require "$LIB_DIR/item1.cgi";&BOUDELA;}	#�è��㰣�U
							if($Command3 eq "BOUDELF")	{require "$LIB_DIR/item1.cgi";&BOUDELF;}	#�����㰣�U
							if($Command3 eq "BOUDEL")	{require "$LIB_DIR/item1.cgi";&BOUDEL;}}	#�˹��~���U
#�� ATTACK
elsif($Command =~ /ATK/)		{require "$LIB_DIR/attack.cgi";require"$LIB_DIR/lib4.cgi";&ATTACK1;}#����
elsif($Command eq "RUNAWAY")	{require "$LIB_DIR/attack.cgi";&RUNAWAY;}							#�k�`
#�� LIB3
elsif($Command =~ /OUK_/)								{require"$LIB_DIR/lib3.cgi";&OUKYU;}		#����B�m
elsif(($msg2 ne "")||($dmes2 ne "")||($com2 ne ""))		{require"$LIB_DIR/lib3.cgi";&WINCHG;}		#�f�Y�y�ܧ�
elsif(($teamID2 ne "")||($teamPass2 ne ""))				{require"$LIB_DIR/lib3.cgi";&TEAM;}			#�p�վާ@
elsif($Command eq "SPECIAL"){if($Command4 eq "SPEAKER")	{require "$LIB_DIR/lib3.cgi";&SPEAKER;}		#��a���n���ϥ�
							 if($Command4 eq "HACK")	{require "$LIB_DIR/lib3.cgi";&HACKING;}}	#Hacking
elsif($Command =~ /KOU_/)		{require"$LIB_DIR/lib3.cgi";&KOUDOU;}								#�򥻤�w
elsif($Command =~ /OUS_/)		{require"$LIB_DIR/lib3.cgi";&OUSEN;}								#���Ԥ�w
elsif ($Command eq "SEVE")		{require"$LIB_DIR/lib3.cgi";&SEVE;}									#Messener
elsif($Command =~ /POI_/)		{require "$LIB_DIR/lib3.cgi";&POISON;}								#�r���V�J
elsif($Command =~ /PSC_/)		{require "$LIB_DIR/lib3.cgi";&PSCHECK;}								#�r��
#�� ITEM2
elsif(($Command =~ /SEIRI_/)&&($Command2 =~ /SEIRI2_/)){require "$LIB_DIR/item2.cgi";&ITEMSEIRI;}	#�D���z
elsif(($Command =~ /GOUSEI1_/)&&($Command2 =~ /GOUSEI2_/)&&($Command3 =~ /GOUSEI3_/))
														{require "$LIB_DIR/item2.cgi";&ITEMGOUSEI;}	#�D��X��
elsif(($Command =~ /SEITO_/)&&($Command2 =~ /JO_/)) {require "$LIB_DIR/item2.cgi";&ITEMJOUTO;}		#�D������
#�� ADMIN
elsif($Command eq "BSAVE")	{require "admin.cgi";&BACKSAVE;}										#�O�s
elsif($Command eq "BREAD")	{require "admin.cgi";&BACKREAD;}										#Ū�J
elsif($Command eq "RESET")	{require "admin.cgi";&DATARESET;}										#��l��
#�� ��ܳ�
if(($Command =~ /BATTLE/)||($Command =~ /ATK/))
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#�԰����G
elsif($Command eq "ITEMJOUTO")
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#�D������
elsif ($mflg ne "ON") {&MAIN;}
}
#===========================#
# �� �v���P�ίv�P�R�i�B�z�@	#
#===========================#
sub HEAL	{$sts = "�v��";$endtime = $now;&SAVE;}
sub INN		{$sts = "�ίv";$endtime = $now;&SAVE;}
sub INNHEAL	{$sts = "�R�i";$endtime = $now;&SAVE;}
#===========================#
# �� �������s������@�@�@�@ #
#===========================#
sub BB_CK{if($wf eq $w_id){$wf = "";}else{&ERROR("������X�ݡC","Used Browser Back Command","BATTLE-BB_CK");}}
1;
