## ----------------------------------------------------------------------------+
## BATTLE ROYALE CGI
##   (C) 2000 by Happy Ice.
##   E-MAIL: webmaster@happy-ice.com
##   HomePage: http://www.happy-ice.com/battle/
##
## Re-Edited By 2Y (Yuta Yamashita)
##	(C) 2003 by - 2Y -
##	E-MAIL:	2Y@mindspring.com
##	HP:		http://2Y.on.to
##�� �C���������ܧ��Y�T��
$ver = "V01.19";$ver2y = "1�]4";
## ---[�`�N�ƶ�]---------------------------------------------------------------+
## 1. ��γo�ӹC���{���O�w�˩ιC���̦����󪺷l���A�@�̤��Ӿ�@�����d���C
##											      
## 2. ��ܮɭԪ�TAB�O4�Ŷ��C�奻�Хνs�边�]�w�C
##				
## 3. �����]�m�����D�Χ�y�����D�Ш�ۤ��i�O�ЧU�C
##    ���l�󪺰��D������^���A���L�A�p��MSN�A���D���঳�Ī��^���C
##											
## 4. ����J���ʪ��C�����D�A�o�ӥD���]��²�檺�����C
##														 
## 5. �p�G�����~���i�A�έn�D���A�D�����޲z�����i�P�g�W�C
##														        		- 2Y -
## ----------------------------------------------------------------------------+
#�� �C�����D
$game = "�� BATTLE ROYALE �� ($ver) [BRU Ver. $ver2y] �C�����ѡGWithlove -- �ڤ۾Ƕ� (http://withlove.no-ip.com)";
#�� �U���C���l�}�w�w��(�������D�ʡD��í�w�H)
$start_mon = "3";$start_day = "4";$start_hour = "24";$start_min = "0";$start_sec = "0";
#------- �򥻳]�w ---------
#�� �޲z��??&�K�X
# �]���i��Ouser log�Y�쪺��]�A�u,�v(�p���I)�ЧO�ΡC
$a_id = "BR" ; # �ܦ�NPC�ϥήɪ�ID�C
$a_pass = "12341234" ;
$a_pass_npc = "ADMIN_NPC";#�L�h���K�X
$a_group_id = "ADMIN_GROUP";#�L�h���p�զW
$a_group_pass = "ADMIN_PASS";#�L�h���p�ձK�X
#�� �ؿ�(�̫�/�����W)
# ����ƾڿs�����w�ܧ�C
$LOG_DIR = "log9428" ;
$DAT_DIR = "dat2ksi9" ;
$LIB_DIR = "lib812add" ;
#�� �챵�B(��UCGI���챵�D�l�[�i��)
# �e���W���Q��ܪ��챵�C
@links = (
    '>><A href="index.htm">HOME</A>',
    '>><A href="rule.htm" target="_blank">RULE</A>',
    '>><A href="rank.cgi" target="_blank">RANKING</A>',
    '>><A href="map.cgi" target="_blank">MAP</A>',
    '>><A href="news.cgi" target="_blank">NEWS</A>',
    '>><A href="admin.cgi">ADMIN</A>'
    );
# �޲z�覡�Ϊ��챵�C
$home = "http://withlove.no-ip.com/br/"; #�]�w�ﭺ�����챵
#�� �ӧO�s��
$u_save_dir = "$LOG_DIR/users_save/"; #�Τ�s�ɥؿ�
$u_save_file = "_back.log"; #ID���[���r�Ŧ�
#�� �Τ���
# �]���ƾڿs������$LOG_DIR/�H�U�Х��w�ܧ�C
$user_file = "$LOG_DIR/userdatfile_1234.log" ;
$back_file = "$LOG_DIR/da23fd8s91k29kd91.log" ;
#�� log file
$log_file = "$LOG_DIR/newsfile1283dseie983.log" ;
#�� lockfile�W
$lockf = "lock/dummydjwow839.txt";
#�� �����Φ�
# �� 0=no 1=symlink��� 2=mkdir��� 3=Tripod��(�ȩw)
# �������ծɭԨ�A�Ⱦ�����mkdir��ƪ��A�ɭԭn�O�ϥΥi��
# �ϥ�symlink��ơC
$lkey = 2;
#�� �Τ�Ƥ��
$member_file = "$LOG_DIR/memberfile938s9d9k.log" ;
#�� �T��ϰ���
$area_file = "$LOG_DIR/areafiledis83929.log" ;
#�� ��I�Z�����
$wep_file = "$DAT_DIR/wepfile823829ksks.dat" ;
#�� �ӤH�p�����D����
$stitem_file = "$DAT_DIR/stitemfile3928skso9.dat" ;
#�� ���o�D����
$item_file = "itemfile.log" ;
#�� �ɶ��޲z���
$time_file = "$LOG_DIR/timefile.log" ;
#�� �j�nlog file
$gun_log_file = "$LOG_DIR/gunlog.log" ;
#�� ����
$end_flag_file = "$LOG_DIR/e_flag.txt" ;
#�� �Ѯ�
@weather = ("�ִ�","��","�ܳ�","�B","���B","�x��","�p�B","��","��","�@��");
#�� �Z�Ÿ��X
@clas = ("3�~A��","3�~B��","3�~C��","3�~D��","3�~E��","3�~F��","3�~G��","3�~H��","3�~I��","3�~J��");
$clmax = 10;#�Z�ż�
$manmax= 21;#�ʧO�̤j��
$maxmem=$clmax*$manmax*2; #�̤j�n����
#�� ����
@place = ("����","�_���a","�_����v��","�_���г�","�l�K��","�����p","������","�M����","�������","���","�s���a�a","�G�D","�����v��","�x","���","�n������","�˪L�a�a","���G����","�n����v��","�E����","�O�x","�n���a");
# SU=�o�{�W�[ SD:�o�{��� DU:���m�W�[ DD:���m��� AU:�����W�[ AD:�������
@arsts = ("SU","DD","DU","SU","SD","SU","AU","SU","SD","AD","SU","DD","DU","SD","AD","SD","SD","SD","AU","SU","DU","SU");
@area = ("D-6","A-2","B-4","C-3","C-4","C-5","C-6","D-3","E-2","E-4","E-5","E-7","F-2","F-9","G-3","G-6","H-4","H-6","I-6","I-7","I-10","J-6");
@arno = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21");
@arinfo = (
	"���աC�o�̤��[�|�����T��ϰ�C<BR>�p�G�����I���}�A����N�|�z���K�C",
	"��V���S����i�H�ݱo���C<BR>�ʵ�����k��ǥ̪ͭ��F����Ϊ̡K�C",
	"�H�e�]���H�b�o�̩~��a�C<BR>�p���w�ܦ��o�V�C",
	"�o�̬O�������߶ܡH<BR>�{�b�ܦ��ֳ����b�K�C",
	"�o����M�S������F��K�C",
	"�����o�̬O�������A���O�s�������]�S���C",
	"�j�p�U�ئU�˪��򹳳Q�ѩ^�ۡC<BR>�]�ߥO�H�򰩮��M�C",
	"�o�̪����ܲM���C",
	"�j���O�ǰݪ����Q���������s�ǡC",
	"�o�˪��a��|�����F�X�{�ܡH<BR>���F�������M���Ӭ۫H�A���L�K�C",
	"����@��o�Ӯq�����a�C<BR>��M�A�p�G�b�o�̯��ߵۡA<BR>�Q��L���٦��쪺�i��ʤ]�ܰ��C",
	"�u�·t�C<BR>�p�G�b�o�˪��a��Qŧ���A�۫H�|�O�۷�M�I�C",
	"�o�̻P��L����v��t���h�A<BR>�����P�o�V�L�áK�C",
	"������o�F���a��C",
	"�դѪ��ǮլݤW�h�Pı�]�S����A���O�A<BR>�]�ߪ��ǮմN���@�ˤF�A�ר�O�b�o�̡K�C",
	"�n�ε۪��P�{�A�Pı�]�ܲY�G���K�C",
	"�{�{���������h�ӭZ���C<BR>�Y�q���O��M�Qŧ�����Ƥ]�Ӥ��δN�K�C",
	"�o�̻P�仡�O���l���p���O�h�A�C<BR>�����O�H�򰩮��M���a��K�C",
	"�o�̡A���L��v�󪺰ө��S�O�h�C<BR>�O�ө����٬O����a�C",
	"�I�R�a�a�A<BR>�p�G�M���į�N�n���I��ʤF�K�C",
	"�p�G�@���n��ߥR���A�֭n������c������F�C<BR>�a�O�O���j�q���F���岪�C������H",
	"�L�h����M�K�u�Ӫ̭�������ܡH<BR>�ƿ���B�I�ۡC",
);
#�� �C���ƾڦ��Ĵ����C�H��Ƭ����C�q�{1�P���C
$save_limit = 7;
#�� ���Ŵ��ɰ򥻸g���
$baseexp = 9;
#�� �򥻼��m��
$BASE = 20 ;
#�� �C���̧C�}�ʤ��
# �ά��ʡD�������̫᪺�@�H�M�w�A�n�O�o�Ӥ�ƥH�U�C�����|�~�����C
# 0����1��C
$battle_limit = 3;
#�� �C�����ݦX�p���
$limit = 3;
#�� ��O�̤j��
$maxsta = 100;
#�� ���汹�I���O����q���O
$okyu_sta = 50;
#�� �r�����O����q���O
$dokumi_sta = 30;
#�� ��_�q���]�w
$kaifuku_time = 10; # ��q��_�ɶ�(��):60��1�I��_
$kaifuku_rate = 2;  # ��O��Ƥ�v�G��q���G�����@(���]�w�ɳ]��0)
#�� �ɨ� (���~�A�Ⱦ����ɭԡB$now=time+��(9*60*60);�Ҥl:9�ɶ��t)
$now=time;

#------- �ϥΪ̳]�w ---------
#�T���O�s�����W
$mes_file = "$LOG_DIR/mes.log";
#�O�s����������
$listmax = 100;
#�T����ܼ�
$mesmax = 5;
#�����ƫO�s���
$memberfile = "$LOG_DIR/member.log";
#�����I�ƫ���߱����ɶ�
$mem_time = 120;
#�T�����C��
$col_to = "red";
#�e�X�T�����C��
$col_from = "blue";
#�����o�e���T���C��
$col_all = "green";


#------- �w�������p�]�w ---------

#�� �X�ݸT��
@kick = ("218.188.104.92","TANATOS","TANATOS","TANATOS");
#�� �X�ݩӻ{
@oklist = ("TANATOS","TANATOS","TANATOS","TANATOS");
# ����X�ݸT��
# �W�r������o�����p�ư��C
# ���Q�ư������p�A�Ч�עަa�}��J�X�ݩӻ{�C
# �ҡG@oklist = ("127.0.0","TANATOS","TANATOS","TANATOS");
# �o�˰��A127.0.0.*** ��IP�a�}���Q�ڵ��C
# �p�G�Q�ΡApref.cgi��7-21��C

#�� method=POST ���w (0=no 1=yes) ���w���ʹﵦ
$Met_Post = 1;

#�� �q��L���I��Z�ư��ɫ��w
$base_url = 0; #�p�G�ϥαư�����г]�w��1

#�����]�w��J���a�}(�qhttp://�g)�D�i�ƼƳ]�w
@base_list = ("dummy","dummy");


#------- �w�������p�]�w�D��ܾ��� ---------

#�� �P�@�n�O�T��((0=no 1=yes)
# �p�G�γo�Ӿ��઺�ܡA�ܱo����Ӧ�CATV�����Ҫ��n�O
# �]�w�ɭԽЪ`�N�C
$IP_deny = 0;

#�� �ϥ�(0=no 1=yes)
# �]�w��0�����ܦ��b�עަa�}����ܡC
$IP_host = 0;

#�� ��\�ӦۦP�˥D�H���n�OorIP�a�}
# �ٲ����ܯ�a�}�M�D�H�W���d����w�C
# �Ҥl1) hogehoge.ne.�p�Gjp ����*�Dhogehoge.ne.jp ���D�H�Q��\�C
# �Ҥl2)192.168.0����192.168.0.*���a�}�Q��\�C
# �`�N�G�o�ӳ]�w�����Ū��ܥ������D�H(�a�})�����\�i��H�C
@IP_ok = ("dummy","dummy");

#�� �b�i�檬�p��(�W)��ܥD�H�H��(0=no 1=yes)
# �]��1���ܷs�W���n�O�ɢעަa�}�N�Q��ܡC
$host_view = 0;


#------- ��ܾ��� ---------

# NPC�]�m���L(0=no 1=yes)
# �p�G�]�m�Цbbase.dat�s�@NPC�ƾڡC
$npc_mode = 1;
$npc_num = 26;	# Number of NPC
$npc_file = "$DAT_DIR/base.dat"; #NPC DATA FILE
$BOSS = "���";$KANN = "�ʬd��";$ZAKO = "�L�h";
# �Y���覡(0=no 1=yes)
$icon_mode = 1;
# �Y���e�����u�ؿ��v
# �� �n�O�qhttp:// URL�Ъ`��
# �� �̫ᥲ�w�[�W /
$imgurl = "img/";
# map���e���u�ؿ��v
# �� �n�O�qhttp:// URL�Ъ`��
# �� �̫ᥲ�w�[�W /
$map = "map";#		
# Meter���Ϲ����
$blue = "img/blue.PNG";$gold = "img/gold.PNG";$green = "img/green.PNG";$pink = "img/pink.PNG";$red = "img/red.PNG";$yellow = "img/yellow.PNG";
# ���A���Ϲ����
$fine = "img/fine.swf";$caution = "img/caution.swf";$danger = "img/danger.swf";$dead = "img/dead.swf";$poison = "img/poison.swf";
# �w�q(�W�U�]�w���w�۹�C�W���k�͡A�U���k��)
# �k�;ǥ��Y��
@m_icon_file = ('i_akamatsu.jpg','i_keita.jpg','i_ooki.jpg','i_oda.jpg','i_kawada.jpg','i_kiriyama.jpg','i_kuninobu.jpg','i_kuramoto.jpg','i_kuronaga.jpg','i_sasagawa.jpg','i_sugimura.jpg','i_yutaka.jpg','i_takiguchi.jpg','i_duki.jpg','i_nanahara.jpg','i_niida.jpg','i_numai.jpg','i_hatagami.jpg','i_mimura.jpg','i_motobuchi.jpg','i_yamamoto.jpg');
@m_icon_name = ('1�f ���Q�q��','2�f ���q�q��','3�f �j��߹D','4�f ´�бӾ�','5�f �t�г��^','6�f ��s�M��','7�f ��H�y��','8�f �ܤ��v�G','9�f �ª���','10�f �@�t�s��','11�f ��������','12�f �u����','13�f �]�f�u�@��','14�f �멣��','15�f �C���]','16�f �s���ЩM��','17�f �h���R','18�f �X�W����','19�f �T���H�v','20�f �������@','21�f �s���M��');
# �k�;ǥ��Y��
@f_icon_file = ('i_inada.jpg','i_utsumi.jpg','i_eto.jpg','i_sakura.jpg','i_kanai.jpg','i_yukiko.jpg','i_yumiko.jpg','i_kotohiki.jpg','i_sakaki.jpg','i_hirono.jpg','i_souma.jpg','i_haruka.jpg','i_takako.jpg','i_tendo.jpg','i_noriko.jpg','i_yuka.jpg','i_noda.jpg','i_fujiyoshi.jpg','i_matsui.jpg','i_minami.jpg','i_yahagi.jpg');
@f_icon_name = ('1�f �_�з��J','2�f �������K','3�f ���ôf','4�f �p�t ��','5�f �����u','6�f �_�����l','7�f ��U�ͬ��l','8�f �^�u�[�N�l','9�f �����l','10�f �M����f�D','11�f �۰����l','12�f ���A�a','13�f �d��Q�l','14�f �Ѱ�u�}','15�f ���t��l','16�f ���t����','17�f �����o��','18�f �æN��@','19�f �Q������','20�f �n��´','21�f �ڧ@�n��');
# NPC���Y��
@n_icon_file = ('i_sakamochi.jpg','i_tahara.jpg','i_kondou.jpg','i_nomura.jpg','i_kato.jpg','i_hayashida.jpg','i_ocha.jpg','i_bus.jpg');
@n_icon_name = ('�O�����o ����','�L�h �Э�','�L�h ����','�L�h ����','�L�h �[��','�L�Щ��� ����','�q��','���ӤH');
# �S���Y��
@s_icon_file = ('GPO3.gif','i_ana.jpg','i_anna.jpg','i_anno.jpg','i_ikumi.jpg','i_junya.jpg','i_kazumi.jpg','i_keiko.jpg','i_uncle.jpg');
@s_icon_name = ('GPO3','�s����','�_�t�w�`','�w���}�l','�T������','�C�T����','�s���M��','�j�e�y�l','�T������');
@s_icon_pass = ('GPO3pass','','','','','','','','');
# �Y���w�q(�S���n�ЧO�ܧ�)
#-----------�q�o��-----------------
@icon_file = (@m_icon_file,@f_icon_file,@n_icon_file,@s_icon_file);
@icon_name = (@m_icon_name,@f_icon_name,@n_icon_name,@s_icon_name);
$icon_check1 = $#m_icon_file + 1;
$icon_check2 = $icon_check1 + $#f_icon_file + 1;
$icon_check3 = $icon_check2 + $#n_icon_file + 1;
$icon_check4 = $icon_check3 + $#s_icon_file + 1;
#-----------��o��-----------------
#========== �]�w��o�� ===============
1;
