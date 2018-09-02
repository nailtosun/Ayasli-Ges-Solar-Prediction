<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#MENU_GROUPS#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="popup.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
var wrTab=new Array(AnzahlWR)
var cntVisiWR, chooser=0, grpI
if( AnzahlGrp==0 )
    var AnlagenGrp=new Array()
for(grpI=0;grpI<10;grpI++) {    // fehlende Gruppen "auffüllen"
 if( grpI+1>AnlagenGrp.length ) {
    AnlagenGrp[grpI]=new Array("",null,0,0)
    AnlagenGrp[grpI][1]=new Array()
 }
}

function addWR(f) {
  grpI=parseInt(f.name.substring(4))
  chooseWR(grpI,0)
}
function delWR(f) {
  grpI=parseInt(f.name.substring(4))
  chooseWR(grpI,1)
}
function checkNum(v) {
  var i, Char
  var ValidChars = "0123456789"
  for( i=0; i<v.length; i++ ) {
    Char = v.charAt(i)
    if( ValidChars.indexOf(Char) == -1)  
       return false
  }
  return true
}
function chooseWR(grpI,mode) {
// mode:0=add, 1=del
var i,i2,code,adr
// alle WR ermitteln, die noch nicht zugeordnet sind
for(i=0;i<AnzahlWR;i++) {
 wrTab[i]=0
 // Sensor rausnehmen
 if( WRInfo[i][11]==1 )
    wrTab[i]=-1
}
for(i=0;i<AnzahlGrp;i++) {
 for(i2=0;i2<AnlagenGrp[i][1].length;i2++) {
// alert("Gruppe="+i+", WR="+AnlagenGrp[i][1][i2])
   wrTab[ AnlagenGrp[i][1][i2]-1 ]=i+1
 }
}
cntVisiWR=0
code=""
if(mode==0) {
    for(i=0;i<AnzahlWR;i++) {
     if(wrTab[i]==0) {
       cntVisiWR++
       code=code+"<input name=\'btn_"+i+"\' id=\'idbtn_"+i+"\' value=\'#"+(i+1)
       adr=parseInt(WRInfo[i][1])
       if( checkNum(WRInfo[i][1]) && !isNaN(adr) && adr<255)
         code=code+" (%#LABEL_ADRESS#:"+adr+")"
       else
         code=code+" (%#LABEL_SERIALNR#:"+WRInfo[i][1]+")"
       code=code+"\' type=\'button\' style=\'display:\' onclick=\'addOneWR("+grpI+","+i+")\'>"
     }
    }
    if( cntVisiWR>0 ) {
       if( !chooser ) {
           new popUp(320 , 100+grpI*20 , 200 , 300 , "chooser" , code , "white" , "black" , "10pt sans-serif" , "%#LABEL_ADD_INV#" , "#0F72BB" , "white" , "lightgrey", "#6DBAF3" , "black" , true , true , false , true , false , false , 'min.gif' , 'max.gif' , 'close.gif' , 'resize.gif');
           chooser=1
       }
       else {
           movePopup('chooser',320,100+grpI*20)
           showbox('chooser')
           changecontent('chooser',code)
       }
    }
    else {
        alert("%#LABEL_ALL_INV_ADDED#")
    }
}
else {
    for(i=0;i<AnzahlWR;i++) {
     if(wrTab[i]==grpI) {
       cntVisiWR++
       code=code+"<input name=\'btn_"+i+"\' id=\'idbtn_"+i+"\' value=\'#"+(i+1)
       adr=parseInt(WRInfo[i][1])
       if(checkNum(WRInfo[i][1]) && !isNaN(adr) && adr<255)
         code=code+" (%#LABEL_ADRESS#:"+adr+")"
       else
         code=code+" (%#LABEL_SERIALNR#:"+WRInfo[i][1]+")"
       code=code+"\' type=\'button\' style=\'display:\' onclick=\'delOneWR("+grpI+","+i+")\'>"
     }
    }
    if( cntVisiWR>0 ) {
       if( !chooser ) {
           new popUp(320 , 100+grpI*20 , 200 , 300 , "chooser" , code , "white" , "black" , "10pt sans-serif" , "%#LABEL_REMOVE_INV#" , "#0F72BB" , "white" , "lightgrey", "#6DBAF3" , "black" , true , true , false , true , false , false , 'min.gif' , 'max.gif' , 'close.gif' , 'resize.gif');
           chooser=1
       }
       else {
           movePopup('chooser',320,100+grpI*20)
           showbox('chooser')
           changecontent('chooser',code)
       }
    }
    else {
        alert("%#LABEL_NO_INV#")
    }
}
}

function addOneWR(grpI,wrI) {
 var oldvalue,i
 i=AnlagenGrp[grpI-1][1].length
 if(i==15) {
    alert("Maximale Anzahl erreicht.")
    return
 }
 AnlagenGrp[grpI-1][1][ i ]=wrI+1
 oldvalue=document.getElementsByName("wr_"+grpI)[0].value
 if( oldvalue.length>0 )
    oldvalue+=","
 oldvalue+=""+(wrI+1)
 document.getElementsByName("wr_"+grpI)[0].value=oldvalue
 if( grpI>AnzahlGrp )
    AnzahlGrp=grpI
 document.getElementById("idbtn_"+wrI).style.display = "none"
 cntVisiWR--
 if(cntVisiWR==0)
   hidebox('chooser')
}

function ArrDel( a, p ) {
   return a.slice(0,p).concat(a.slice(p+1,a.length))
}

function delOneWR(grpI,wrI) {
 var i,l,newvalue=""
 l=AnlagenGrp[grpI-1][1].length
 for(i=0;i<l;i++) {
   if(AnlagenGrp[grpI-1][1][i]==wrI+1) {
     AnlagenGrp[grpI-1][1]=ArrDel(AnlagenGrp[grpI-1][1],i)
     l--
     i--
     continue
   }
   if(newvalue.length>0)
      newvalue+=","
   newvalue+=""+(AnlagenGrp[grpI-1][1][i])
 }
 if(l==0) {
    if( AnzahlGrp==grpI )
       AnzahlGrp--
 }
 document.getElementsByName("wr_"+grpI)[0].value=newvalue
 document.getElementById("idbtn_"+wrI).style.display = "none"
 cntVisiWR--
 if(cntVisiWR==0)
   hidebox('chooser')

}

function initbody() {
if( document.getElementsByName("gruppe")[0].checked ) {
  hideGroups()
}
else {
  showGroups()
}
}

function hideGroups() {
  document.getElementById("gruppe1").style.display="none"
  document.getElementById("gruppe2").style.display="none"
}
function showGroups() {
  document.getElementById("gruppe1").style.display=""
  document.getElementById("gruppe2").style.display=""
}
</script>
</head>
<body onLoad="initbody()">
<div id="rap">
	<div id="inhalt">
		<div id="head">
			<div id="logo"><img src="%#COMPANY_LOGO#"></div>
			<div id="headright">
				<table cellpadding="0" cellspacing="0" border="0" class="menu">
					<tr>
						<td align="center" valign="middle" class="in-act"><a href="index.html">%#MENU_YIELD_DATA#</a></td>
						<td align="center" valign="middle" class="in-act"><a href="events.html">%#MENU_DIAGNOSIS#</a></td>
                        <script language="JavaScript" src="menu.js"></script>
                        <script language="JavaScript">
                            showMainMenuConfig(true, "%#MENU_CONFIGURATION#" )
                        </script>
						<td height="30" align="center" valign="middle" class="in-act">&nbsp;</td>
					</tr>
				</table>
			</div>
			<div style="clear: left;"></div>
		</div>
		<div id="contentleft">
			<ul class="submenu">
                <script language="JavaScript">
                    showSubMenu("2")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_GROUPS#</h1>
			<form action="group_post.html" method="post">
				<strong>%#LABEL_GROUPS#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_NO_GROUPS#</td>
						<td><input type="radio" name="gruppe" id="gruppe" value="g_0~" onclick="hideGroups()" /></td>
					</tr>
					<tr>
						<td>%#LABEL_GROUPS_ON#</td>
						<td><input type="radio" name="gruppe" id="gruppe" value="g_1~" onClick="showGroups()" /></td>
					</tr>
				</table>
				<div id="gruppe1">
					<br />
					<br />
					<strong>%#LABEL_GROUP_DEF#</strong><br />
				</div>
				<div id="gruppe2">
				<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
						<tr>
							<td>Nr.</td>
							<td>%#LABEL_DESC#</td>
							<td>%#LABEL_MAX_INV#</td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td></td>
							<td>%#LABEL_SUBSIDARY# (<script language="JavaScript">document.write( CurrencySub )</script>)</td>
							<td>%#LABEL_YEARLY_TARGET# (kWh/kWp)</td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>1</td>
							<td><input name="bez_1" maxlength="19" type="text" class="einzeilig" id="bez_1" value="%s" /></td>
							<td><input name="wr_1" type="text" class="einzeilig" id="wr_1" value="%s" readonly="readonly" /></td>
							<td><input name="add_1" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_1" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_1" size="5" maxlength="5" type="text" class="einzeilig" id="verg_1" value="%s" /></td>
							<td><input name="soll_1" size="5" maxlength="5" type="text" class="einzeilig" id="soll_1" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>2</td>
							<td><input name="bez_2" maxlength="19" type="text" class="einzeilig" id="bez_2" value="%s" /></td>
							<td><input name="wr_2" type="text" class="einzeilig" id="wr_2" value="%s" readonly="readonly" /></td>
							<td><input name="add_2" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_2" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_2" size="5" maxlength="5" type="text" class="einzeilig" id="verg_2" value="%s" /></td>
							<td><input name="soll_2" size="5" maxlength="5" type="text" class="einzeilig" id="soll_2" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>3</td>
							<td><input name="bez_3" maxlength="19" type="text" class="einzeilig" id="bez_3" value="%s" /></td>
							<td><input name="wr_3" type="text" class="einzeilig" id="wr_3" value="%s" readonly="readonly" /></td>
							<td><input name="add_3" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_3" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_3" size="5" maxlength="5" type="text" class="einzeilig" id="verg_3" value="%s" /></td>
							<td><input name="soll_3" size="5" maxlength="5" type="text" class="einzeilig" id="soll_3" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>4</td>
							<td><input name="bez_4" maxlength="19" type="text" class="einzeilig" id="bez_4" value="%s" /></td>
							<td><input name="wr_4" type="text" class="einzeilig" id="wr_4" value="%s" readonly="readonly" /></td>
							<td><input name="add_4" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_4" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_4" size="5" maxlength="5" type="text" class="einzeilig" id="verg_4" value="%s" /></td>
							<td><input name="soll_4" size="5" maxlength="5" type="text" class="einzeilig" id="soll_4" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>5</td>
							<td><input name="bez_5" maxlength="19" type="text" class="einzeilig" id="bez_5" value="%s" /></td>
							<td><input name="wr_5" type="text" class="einzeilig" id="wr_5" value="%s" readonly="readonly" /></td>
							<td><input name="add_5" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_5" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_5" size="5" maxlength="5" type="text" class="einzeilig" id="verg_5" value="%s" /></td>
							<td><input name="soll_5" size="5" maxlength="5" type="text" class="einzeilig" id="soll_5" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>6</td>
							<td><input name="bez_6" maxlength="19" type="text" class="einzeilig" id="bez_6" value="%s" /></td>
							<td><input name="wr_6" type="text" class="einzeilig" id="wr_6" value="%s" readonly="readonly" /></td>
							<td><input name="add_6" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_6" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_6" size="5" maxlength="5" type="text" class="einzeilig" id="verg_6" value="%s" /></td>
							<td><input name="soll_6" size="5" maxlength="5" type="text" class="einzeilig" id="soll_6" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>7</td>
							<td><input name="bez_7" maxlength="19" type="text" class="einzeilig" id="bez_7" value="%s" /></td>
							<td><input name="wr_7" type="text" class="einzeilig" id="wr_7" value="%s" readonly="readonly" /></td>
							<td><input name="add_7" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_7" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_7" size="5" maxlength="5" type="text" class="einzeilig" id="verg_7" value="%s" /></td>
							<td><input name="soll_7" size="5" maxlength="5" type="text" class="einzeilig" id="soll_7" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>8</td>
							<td><input name="bez_8" maxlength="19" type="text" class="einzeilig" id="bez_8" value="%s" /></td>
							<td><input name="wr_8" type="text" class="einzeilig" id="wr_8" value="%s" readonly="readonly" /></td>
							<td><input name="add_8" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_8" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_8" size="5" maxlength="5" type="text" class="einzeilig" id="verg_8" value="%s" /></td>
							<td><input name="soll_8" size="5" maxlength="5" type="text" class="einzeilig" id="soll_8" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>9</td>
							<td><input name="bez_9" maxlength="19" type="text" class="einzeilig" id="bez_9" value="%s" /></td>
							<td><input name="wr_9" type="text" class="einzeilig" id="wr_9" value="%s" readonly="readonly" /></td>
							<td><input name="add_9" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_9" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_9" size="5" maxlength="5" type="text" class="einzeilig" id="verg_9" value="%s" /></td>
							<td><input name="soll_9" size="5" maxlength="5" type="text" class="einzeilig" id="soll_9" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>10</td>
							<td><input name="bez_10" maxlength="19" type="text" class="einzeilig" id="bez_10" value="%s" /></td>
							<td><input name="wr_10" type="text" class="einzeilig" id="wr_10" value="%s" readonly="readonly" /></td>
							<td><input name="add_10" type="button" class="button" value="%#LABEL_ADD#" onClick="addWR(this)" /></td>
							<td><input name="del_10" type="button" class="button" value="%#LABEL_DEL#" onClick="delWR(this)" /></td>
						</tr>
						<tr>
							<td></td>
							<td><input name="verg_10" size="5" maxlength="5" type="text" class="einzeilig" id="verg_10" value="%s" /></td>
							<td><input name="soll_10" size="5" maxlength="5" type="text" class="einzeilig" id="soll_10" value="%s" /></td>
							<td></td>
							<td></td>
						</tr>
					</table>
				</div>
				<br><br>
				<input type="submit" class="button" value="%#LABEL_SAVE#" />
				&nbsp;&nbsp;
				<input type="reset" class="button" value="%#LABEL_CANCEL#" />
				<br /><br />
				%s
			</form>
		</div>
		<div style="clear: left;"></div>
	</div>
	<div id="footer">
		%#COMPANY# | <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
	</div>
</div>
</body>
</html>
