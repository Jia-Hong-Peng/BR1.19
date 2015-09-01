function sl_msg(x) {document.MSG.Command2[x].checked = true;}
function sl(x) {document.BR.Command[x].checked = true;}
function chk(x) {if (document.f1.Del[x].checked == true) {document.f1.Del[x].checked = false ;}else {document.f1.Del[x].checked = true ;}}
//ÉNÉçÉX
var cross_sprites = new Array();var cross_vertical = '#00FF00';var cross_horizon = '#00FF00';var cross_size = 2;
function cross_init(){
	if (document.layers) {captureEvents(Event.MOUSEMOVE);onMouseMove = cross_onMouseMove_NC;for (i = 0; i < 2; i ++){cross_sprites[i] = new Cross_NC(i);}}
	else if (document.all) {document.onmousemove = cross_onMouseMove_IE;for (i = 0; i < 2; i ++){cross_sprites[i] = new Cross_IE(i);}}
}
function Cross_NC(index){
	if (index == 0){document.write("<LAYER ID='CROSS" + index + "' VISIBILITY='hide' TOP=0 LEFT=0 HEIGHT=" + cross_size + " WIDTH=" + innerWidth + " Z-INDEX=10 BGCOLOR='" + cross_horizon + "'></LAYER>");}
	else{document.write("<LAYER ID='CROSS" + index + "' VISIBILITY='hide' TOP=0 LEFT=0 HEIGHT=" + innerHeight + " WIDTH=" + cross_size + " Z-INDEX=10 BGCOLOR='" + cross_vertical + "'></LAYER>");}
	this.obj = document.layers['CROSS' + index];
}
function cross_onMouseMove_NC(e){
	if(e.pageY <= 0 || e.pageY >= innerHeight + pageYOffset - cross_size || e.pageX <= 0 || e.pageX >= innerWidth + pageXOffset - cross_size) {for (i = 0; i < 2; i ++){cross_sprites[i].obj.visibility = 'hide';}}
	else{cross_sprites[0].obj.y = e.pageY - 1;cross_sprites[0].obj.x = pageXOffset;cross_sprites[0].obj.width = innerWidth;cross_sprites[1].obj.x = e.pageX - 1;cross_sprites[1].obj.y = pageYOffset;cross_sprites[1].obj.height = innerHeight;for (i = 0; i < 2; i ++){cross_sprites[i].obj.visibility = 'show';}}
}
function Cross_IE(index){
	if (index == 0){document.write("<DIV ID='CROSS" + index + "' STYLE='position:absolute;visibility:hidden;top:0px;left:0px;height:" + cross_size + "px;width:" + document.body.clientWidth + "px;font-size:1px;z-index:10;background:" + cross_horizon + ";'></DIV>");}
	else{document.write("<DIV ID='CROSS" + index + "' STYLE='position:absolute;visibility:hidden;top:0px;left:0px;height:" + document.body.clientHeight + "px;width:" +  cross_size + "px;z-index:10;background:" + cross_vertical + ";'></DIV>");}
	this.obj = document.all['CROSS' + index].style;
}
function cross_onMouseMove_IE(){with (document.body) {
	if (event.y <= 0 || event.y >= clientHeight - cross_size || event.x  <= 0 || event.x >= clientWidth - cross_size) {for (i = 0; i < 2; i ++){cross_sprites[i].obj.visibility = 'hidden';}}
	else{cross_sprites[0].obj.pixelTop = event.y + scrollTop - 1;cross_sprites[0].obj.pixelLeft = scrollLeft;cross_sprites[0].obj.pixelWidth = clientWidth;cross_sprites[1].obj.pixelTop = scrollTop;cross_sprites[1].obj.pixelLeft = event.x + scrollLeft - 1;cross_sprites[1].obj.pixelHeight = clientHeight;for (i = 0; i < 2; i ++){cross_sprites[i].obj.visibility = 'visible';}}}
}
function showform(){login.style.visibility='visible';}
function hideform(){login.style.visibility='hidden';}
cross_init();

//quake_init();

function quake_init(){setTimeout('quake_update()', 100);}
function quake_update(){var m = 15;while (m > 0){parent.moveBy(m, 0);parent.moveBy(0, m);parent.moveBy(-m, 0);parent.moveBy(0, -m);m -= 3;}}
