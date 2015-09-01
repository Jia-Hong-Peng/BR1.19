#■□■□■□■□■□■□■□■□
#□      　　　　　　　　　　　■
#■　DISP. ENDING & READER　　 □
#□　　　　　　　　　　　　　　■
#■□■□■□■□■□■□■□■□
#===================#
# ■ 優勝處理		#
#===================#
sub ENDING {
open(FLAG,$end_flag_file) || exit; $fl=<FLAG>; close(FLAG);

if ($inf =~ /勝/){&ENDING2;}
elsif ($inf =~ /解/){&EX_ENDING2;}
elsif ($fl =~ /解除/){&EX_ENDING;}
elsif(($mem == 1)&&($fl =~ /終了/)){&ENDING2;}
else{ &ERROR("不正當訪問。"); }

}

#======================#
#　　　　Footer　　　　#
#======================#
sub END_FOOT{

print <<"_HERE_";

<CENTER>
製作總指揮<BR><BR>
tanatos<BR><BR>
Special Thanks<BR><BR>
神谷榮和氏(<a href="http://www.geocities.co.jp/Bookend/5696/index.html">再讀</A>)<BR><BR>
箕輪氏(<a href="http://www01.u-page.so-net.ne.jp/zb3/t-c/TC.html">心之扉</A>)<BR><BR>
海蜇氏(<a href="http://homepage1.nifty.com/kurage-ya/">海蜇舖</A>)<BR><BR>
<BR>
<A href="index.htm"><B><FONT color="#ff0000" size="+2">返回</FONT></B></A><BR></P>
</CENTER>

_HERE_

&FOOTER;
&UNLOCK;
exit ;
}

#==================#
# 　 通常Ending 　 #
#==================#
sub ENDING2{

	&HEADER;

print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">優勝者決定</FONT></B><BR><BR>

<CENTER>
突然廣播器響起了，然後大地東亞共和國的國歌傳出了。<BR>
然後，聽見了一把熟悉的聲音。<BR>
<BR>
「恭喜恭喜。終於產生優勝者。老師真的為你獲得冠軍而高興喲。<BR>
迎接你的勝利吧！辛苦你了。」<BR>
<BR>
現在，能夠呼吸的人我是最後的一人嗎？<BR>
在發呆的聽著新擔當者的廣播。<BR>
真的是那樣嗎？<BR>
大概，這個計劃好像令我成為政府的人買足球彩票的耍樂對象。<BR>
可是，聽到這個廣播後，緊張的意識開始消失了。<BR>
意識開始朦朧。。。<BR>
大概，因為數日完全沒睡。。。<BR>
．<BR>
．<BR>
．<BR>
眼前有個同班好友。<BR>
「你是想殺死我還是想做被殺的人？」<BR>
回頭向後看，發覺堆滿了同班同學的屍體。<BR>
「看見了吧！大家都被殺了，現在只剩下你和我！」<BR>
說罷好友拿著刀子向著我衝過來。<BR>
「受死吧！」<BR>
<BR>
可是...不知為什麼，我的刀子刺穿了他的身體，好友發出痛苦的聲音。<BR>
然後，四周回復了平靜，地上滿是鮮血...<BR>
「我不想這樣做的，大家都是朋友！　我只想活...只想活下去...」<BR>
．<BR>
．<BR>
．<BR>
身體的振盪，令我醒來。<BR>
一名軍人在我身旁。而我好像身處在一輛囚車之中。<BR>
軍人膝上面放置著彩色的紙。<BR>
上面寫著『優勝，恭喜恭喜！-- 共和國總統 --』。<BR>
<BR>
忽然，囚車的門打開了。<BR>
報導員以及閃光燈的閃光重重的包圍著我。<BR>
他們拿著麥克風向我跑過來。<BR>
「..你好..我是xx電視台的...新聞報導員...。<BR>
成為勝利者，有何感想呢？」<BR>
<BR>
我沒有理會那些向我訪問的人。<BR>
漫無目的地走著，腦中一片空白，直至坐上了另一輛車。<BR><BR>
這一刻，我無法確定所發生的事。<BR>
這是一個遊戲？我的同班好友真的永遠消失了？<BR>
或者這只是一個夢...我希望早點醒來。<BR><BR>
「$sex$no番 $f_name$l_name」<BR>
「下一次你還要參加嗎？這個國家計劃還會不斷進行...呵..呵」<BR>
抬頭看，才發現這個冷血的軍官也在身旁。<BR>
而且露出猙獰的笑容。<BR>
這個時候車子已關上門，開動了。<BR>
「我現在要去那裡？」<BR>
或者，這個夢不會完結，一直發著這個惡夢...<BR>
<BR>
<BR>
<BR>
<BR>
<DIV align="right">
Now,"1 student remaining"．<BR>
Surely 1 is lonly.<BR>
But there is hope there.<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;

}

#==========================#
#　　　程序解除Ending　　　#
#==========================#
sub EX_ENDING {
	&HEADER;

print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">遊戲緊急停止</FONT></B><BR><BR>

<CENTER>
突然如雷貫耳的汽笛聲響起。<br>
冠軍是決定了的…？哦，確實還生存的同學應該在…。<br>
那樣想的話，很好地耳熟的同學的聲音附近響遍。<br>
「程序結束了！已經不作戰也可以!!」<br>
<br>
無法相信。<br>
從這個惡魔的遊戲能逃出。但是，我們從現在起應該怎樣做才好？<br>
一起回去國家政府？<br>
還是嘩啦嘩啦逃跑，各自鳥獸散？<br>
不管怎樣完全不考慮返回家？<br>
沒有考慮的空暇。禁止區域的解除會在今夜的0:00回復到原來。<br>
而且，如果按照遊戲的正常進行程序，兵士會來處刑我們吧。<br>
「………」<br>
先取下戴在頸上的項圈。<br>
想到這裡，深深地呼吸著……<br>
<br>
不管如何先從這裡逃出。<br>
以後的事再慢慢考慮也不遲。<br>
我們還有『希望』。面向這個惡魔的遊戲，世紀的惡法的『希望』<br>
說不定從絕望中產生的希望，可以克服困難！<br>
不斷向前跑……！直至倒下！<br>
<br>
<br>
「遊戲緊急停止後，從會場逃出的少年們依然……」<br>
……一名少年眺望著在街頭螢光幕裡的臨時新聞。<br>
咬住嘴唇，握拳頭，認真的表情。<br>
「跑吧…！到了這個地步！」<br>
<br>
<br>
<BR>
<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;
}

#==============================#
#　解除鑰匙使用者專用Ending　　#
#==============================#
sub EX_ENDING2 {
&HEADER;
print <<"_HERE_";

<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"Verdana\">遊戲緊急停止</FONT></B><BR><BR>

<CENTER>
<br>
「嗄…嗄……」<br>
屍體由斜坡下滾到眼前。<br>
查探衣服後，發現一樣像電子鑰匙的東西。<br>
如果使用這個…自己和大家就能繼續生存，遊戲也被解開…。<br>
「………」<br>
但是，(迷惑)<br>
是這樣的話真的是好事嗎？能從國家政府之下逃脫嗎？<br>
哦…那樣的事還是以後才考慮。<br>
不管怎樣，如果仍然像笨蛋般跟同學互相廝殺下去…。<br>
<br>
遊戲結束的電子聲音響起，項圈發出(卡嚓)的聲音掉下到地板。<br>
並且，手上拿著不知曾宣告著多少人及同學死亡報告的麥克風，深深呼吸。<br>
「程序結束了！已經不作戰也可以!!」<br>
<br>
自己能做的事做了。<br>
以後大家各自考慮如何生存的事就行了。<br>
在這樣的地方跟本做什麼事也沒有用。<br>
從現在起自己才能決定自己以後的事…。<br>
<br>
「遊戲緊急停止後，嫌疑犯的學生依然……」<br>
……一名少年眺望著在街頭螢光幕裡的臨時新聞。<br>
嘴角浮出笑容，手插著口袋。<br>
「努力吧…誰都幫助不了你…」<br>
<BR>
<BR>
<BR><HR>
<BR>
_HERE_

&END_FOOT;
}
#===================#
# ■ 雷達表示部 	#
#===================#
sub READER {

if ($item[$wk] !~ /R/) {&ERROR("不正當的訪問。") ;}

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
open(DB,"$area_file");seek(DB,0,0); @arealist=<DB>;close(DB);

($ar,$hackflg,$a) = split(/,/, $arealist[1]);
@ara = split(/,/, $arealist[4]);

for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	for ($j=0; $j<$#area+1; $j++) {
		if (($w_pls eq $j)&&($w_hit > 0)) {$mem[$j] += 1;last;}
	}
}

if ($item[$wk] =~ /<>R2/) {
	for ($j=0; $j<$#area+1; $j++) {
		if ($j eq $pls) {$wk = $mem[$j];$mem[$j] = "<FONT color=\"#ff0000\"><b>$wk<b></FONT>";}
		elsif ($mem[$j] <= 0) {$mem[$j] = "　" ;}
	}
} else {
	for ($j=0; $j<$#area+1; $j++) {
		if ($j eq $pls) {$wk = $mem[$j];$mem[$j] = "<FONT color=\"#ff0000\"><b>$wk<b></FONT>";}
		else {$mem[$j] = "　" ;}
	}
}

if ($hackflg eq 0) {for ($j=0; $j<$ar; $j++) {$mem[$ara[$j]] = "<FONT color=\"#ff0000\"><b>×<b></FONT>";}}


print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="Verdana">$place[$pls]﹋$area[$pls]﹌</FONT></B><BR></P>
<TABLE width="568">
<TR><TD><B><FONT color="#ff0000">@links</FONT></B></TD></TR>
</TABLE>
<TABLE width="568">
  <TBODY>
	<TR>
	  <TD valign="top" width="279" height="311">
	<TABLE border="1" width="389" height="300">
		<TBODY align="center" valign="middle">
		  <TR>
			<TD>　</TD>
			<TD>01</TD>
			<TD>02</TD>
			<TD>03</TD>
			<TD>04</TD>
			<TD>05</TD>
			<TD>06</TD>
			<TD>07</TD>
			<TD>08</TD>
			<TD>09</TD>
			<TD>10</TD>
		  </TR>
		  <TR>
			<TD>A</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>$mem[1]</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>B</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>$mem[2]</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>C</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>$mem[3]</TD>
			<TD>$mem[4]</TD>
			<TD>$mem[5]</TD>
			<TD>$mem[6]</TD>
			<TD>　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>D</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>$mem[7]</TD>
			<TD>　</TD>
			<TD>$mem[0]</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>E</TD>
			<TD>　</TD>
			<TD>$mem[8]</TD>
			<TD>　</TD>
			<TD>$mem[9]</TD>
			<TD>$mem[10]</TD>
			<TD>　</TD>
			<TD>$mem[11]</TD>
			<TD>　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>F</TD>
			<TD>　</TD>
			<TD>$mem[12]</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>$mem[13]</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>G</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>$mem[14]</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>$mem[15]</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>H</TD>
			<TD bgcolor="#00ffff">　</TD>
				<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>$mem[16]</TD>
			<TD>　</TD>
			<TD>$mem[17]</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		  <TR>
			<TD>I</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>　</TD>
			<TD>$mem[18]</TD>
			<TD>$mem[19]</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>　</TD>
			<TD>$mem[20]</TD>
		  </TR>
		  <TR>
			<TD>J</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD>$mem[21]</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
			<TD bgcolor="#00ffff">　</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	  <TD valign="top" width="200" height="311">
	  <TABLE border="1" cellspacing="0">
		<TBODY>
		  <TR><TD align="center" width="250"><B>指令</B></TD>
		  <TR>
			<TD align="left" valign="top" width="190" height="280">
			<FORM METHOD="POST" name="BR" style="MARGIN: 0px">
			<INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
			<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
			<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_
require"$LIB_DIR/disp_cmd.cgi";
			&COMMAND;

print <<"_HERE_";
			</FORM>
			</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	</TR>
	<TR>
	  <TD colspan="2" valign="top" height="101">
	  <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
		<TBODY>
		  <TR>
			<TD height="20" valign="top" width="600">使用雷達。<BR><BR>數字：區域人數<BR>紅數字：自分區域的人數</TD>
		  </TR>
		</TBODY>
	  </TABLE>
	  </TD>
	</TR>
  </TBODY>
</TABLE>
_HERE_

$mflg="ON"; #表示


}

1;
