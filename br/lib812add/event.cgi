#==================#
# �� ���ʳB�z      #
#==================#
sub EVENT {

local($dice) = int(rand(5)) ;
local($dice2) = int(rand(5)+5) ;
$Command = "MAIN";
if ($dice < 2) {return ; }


if ($pls eq 0) {	#����

} elsif ($pls eq 1) {   #�_���a

} elsif ($pls eq 2) {   #�T�ۧ���v��
	$log = ($log . "��M�A�ѪťX�{�Q�~�s�I<BR>") ;
	if ($dice eq 2) {$log = ($log . "�Q�Q�~ŧ���A�Y�����F�ˡI<BR>") ;$inf =~ s/�Y//g ;$inf = ($inf . "�Y") ;}
	elsif ($dice eq 3) {
		$log = ($log . "�Q�Q�~ŧ���A���� <font color=\"red\"><b>$dice2</b></font> �ˮ`�I<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;

			#���`���A
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {
		$log = ($log . "�I�A�`�����h�F�P�P�P�C<BR>") ;
	}
	$chksts="OK";
} elsif ($pls eq 3) {	#�T�ۧ��г�
} elsif ($pls eq 4) {	#�l�K��
} elsif ($pls eq 5) {	#�����p
} elsif ($pls eq 6) {	#�[����
} elsif ($pls eq 7) {	#�����
} elsif ($pls eq 8) {	#�խ쯫��
} elsif ($pls eq 9) {	#���
} elsif ($pls eq 10) {	#�s���a�a
	$log = ($log . "�z�I�g��Y�a�˶�I<BR>") ;
	if ($dice eq 2) {$log = ($log . "�w�g�ɶq�{�סA���L�A�٬O�Q���Y�Ƹ����ˤF�}�I<BR>") ;$inf =~ s/��//g ;$inf = ($inf . "��") ;}
	elsif ($dice eq 3) {
		$log = ($log . "���Y�Ƹ��A���� <font color=\"red\"><b>$dice2</b></font> �ˮ`�I<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;

			#���`���A
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "�I...�`��O�׶}�F...�C<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 11) {	#�G�D
} elsif ($pls eq 12) {	#���u����v��
	$log = ($log . "��M�A�ѪťX�{�Q�~�s�I<BR>") ;
	if ($dice eq 2) {$log = ($log . "�Q�Q�~ŧ���A�Y�����F�ˡI<BR>") ;$inf =~ s/�Y//g ;$inf = ($inf . "�Y") ;}
	elsif ($dice eq 3) {
		$log = ($log . "�Q�Q�~ŧ���A���� <font color=\"red\"><b>$dice2</b></font> �ˮ`�I<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;

			#���`���A
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "�I�A�`�����h�F�P�P�P�C<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 13) {	#�L�Ǧx
} elsif ($pls eq 14) {	#���ո�
} elsif ($pls eq 15) {	#�N������
} elsif ($pls eq 16) {	#�˪L�a�a
	$log = ($log . "��M�A����ŧ���L�ӤF�I<BR>") ;
	if ($dice eq 2) {$log = ($log . "���u�Q�r�ˤF�I<BR>") ;$inf =~ s/��//g ;$inf = ($inf . "��") ;}
	elsif ($dice eq 3) {
		$log = ($log . "�Q����ŧ���A���� <font color=\"red\"><b>$dice2</b></font> �ˮ`�I<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;

			#���`���A
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "�I...�`�����h�F...�C<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 17) {	#��������
	$log = ($log . "�V�|�A�����ƤU�h�F�I<BR>") ;
	if ($dice <= 3) {
		$dice2 += 10;
		if ($sta < $dice2){$dice2 = $sta;$dice2--;}
		$sta-=$dice2;
		$log = ($log . "���U�����F�A���L�A�w�V�O���^�W�ӡI<BR>��q��h <font color=\"red\"><b>$dice2</b></font> �I�I<BR>") ;
	} else {$log = ($log . "�I...���n�S���U����...�C<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 18) {	#�B�t����v��
	$log = ($log . "��M�A�ѪťX�{�Q�~�s�I<BR>") ;
	if ($dice eq 2) {$log = ($log . "�Q�Q�~ŧ���A�Y�����F�ˡI<BR>") ;$inf =~ s/�Y//g ;$inf = ($inf . "�Y") ;}
	elsif ($dice eq 3) {
		$log = ($log . "�Q�Q�~ŧ���A���� <font color=\"red\"><b>$dice2</b></font> �ˮ`�C<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) ���`�C</b></font><br>") ;

			#���`���A
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "�I�A�`�����h�F�P�P�P�C<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 19) {	#�E����
} elsif ($pls eq 20) {	#�O�x
} elsif ($pls eq 21) {	#�n���a
}
}

1