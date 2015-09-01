#==================#
# ■ 活動處理      #
#==================#
sub EVENT {

local($dice) = int(rand(5)) ;
local($dice2) = int(rand(5)+5) ;
$Command = "MAIN";
if ($dice < 2) {return ; }


if ($pls eq 0) {	#分校

} elsif ($pls eq 1) {   #北之岬

} elsif ($pls eq 2) {   #鎌石村住宅街
	$log = ($log . "突然，天空出現烏鴉群！<BR>") ;
	if ($dice eq 2) {$log = ($log . "被烏鴉襲擊，頭部受了傷！<BR>") ;$inf =~ s/頭//g ;$inf = ($inf . "頭") ;}
	elsif ($dice eq 3) {
		$log = ($log . "被烏鴉襲擊，受到 <font color=\"red\"><b>$dice2</b></font> 傷害！<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;

			#死亡狀態
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {
		$log = ($log . "呼，總算擊退了···。<BR>") ;
	}
	$chksts="OK";
} elsif ($pls eq 3) {	#鎌石村役場
} elsif ($pls eq 4) {	#郵便局
} elsif ($pls eq 5) {	#消防署
} elsif ($pls eq 6) {	#觀音堂
} elsif ($pls eq 7) {	#高原池
} elsif ($pls eq 8) {	#菅原神社
} elsif ($pls eq 9) {	#遺跡
} elsif ($pls eq 10) {	#山岳地帶
	$log = ($log . "哇！土砂崩壞倒塌！<BR>") ;
	if ($dice eq 2) {$log = ($log . "已經盡量閃避，不過，還是被石頭滑落打傷了腳！<BR>") ;$inf =~ s/足//g ;$inf = ($inf . "足") ;}
	elsif ($dice eq 3) {
		$log = ($log . "石頭滑落，受到 <font color=\"red\"><b>$dice2</b></font> 傷害！<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;

			#死亡狀態
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "呼...總算是避開了...。<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 11) {	#隧道
} elsif ($pls eq 12) {	#平瀨村住宅街
	$log = ($log . "突然，天空出現烏鴉群！<BR>") ;
	if ($dice eq 2) {$log = ($log . "被烏鴉襲擊，頭部受了傷！<BR>") ;$inf =~ s/頭//g ;$inf = ($inf . "頭") ;}
	elsif ($dice eq 3) {
		$log = ($log . "被烏鴉襲擊，受到 <font color=\"red\"><b>$dice2</b></font> 傷害！<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;

			#死亡狀態
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "呼，總算擊退了···。<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 13) {	#無學寺
} elsif ($pls eq 14) {	#分校跡
} elsif ($pls eq 15) {	#鷹野神社
} elsif ($pls eq 16) {	#森林地帶
	$log = ($log . "突然，野狗襲擊過來了！<BR>") ;
	if ($dice eq 2) {$log = ($log . "手臂被咬傷了！<BR>") ;$inf =~ s/腕//g ;$inf = ($inf . "腕") ;}
	elsif ($dice eq 3) {
		$log = ($log . "被野狗襲擊，受到 <font color=\"red\"><b>$dice2</b></font> 傷害！<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;

			#死亡狀態
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "呼...總算擊退了...。<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 17) {	#源五郎池
	$log = ($log . "糟糕，失足滑下去了！<BR>") ;
	if ($dice <= 3) {
		$dice2 += 10;
		if ($sta < $dice2){$dice2 = $sta;$dice2--;}
		$sta-=$dice2;
		$log = ($log . "掉下池中了，不過，已努力爬回上來！<BR>能量減去 <font color=\"red\"><b>$dice2</b></font> 點！<BR>") ;
	} else {$log = ($log . "呼...幸好沒掉下水池...。<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 18) {	#冰川村住宅街
	$log = ($log . "突然，天空出現烏鴉群！<BR>") ;
	if ($dice eq 2) {$log = ($log . "被烏鴉襲擊，頭部受了傷！<BR>") ;$inf =~ s/頭//g ;$inf = ($inf . "頭") ;}
	elsif ($dice eq 3) {
		$log = ($log . "被烏鴉襲擊，受到 <font color=\"red\"><b>$dice2</b></font> 傷害。<BR>") ;
		$hit-=$dice2;
		if ($hit <= 0) {
			$hit = $mhit = 0;
			$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no番) 死亡。</b></font><br>") ;

			#死亡狀態
			&LOGSAVE("DEATH") ;
			$Command = "EVENT";
		}
	} else {$log = ($log . "呼，總算擊退了···。<BR>") ;}
	$chksts="OK";
} elsif ($pls eq 19) {	#診療所
} elsif ($pls eq 20) {	#燈台
} elsif ($pls eq 21) {	#南之岬
}
}

1