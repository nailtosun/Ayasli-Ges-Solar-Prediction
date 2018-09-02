<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_SORT_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<style>
	#ProgressBar{padding:5px;font-size:18px;width:200px;text-align:center;left:40%;top:40%;position:absolute;border:2px solid #666;background-color:#FFF;}
</style>
<script language="JavaScript" src="popup.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
%s // wrBez wird definiert
%s // wrIF wird definiert
var wrTab=new Array(AnzahlWR)
var cntVisiWR, chooser=0
Reset()

function SaveCfm(f){
  var i, alle=true
  // alle WR zugeordnet?
  for( i=0; i<AnzahlWR; i++ ) {
     if( wrTab[i]==0 ) {
        alle=false
        break
     }
  }
  if( alle ) {
     if( confirm("%#LABEL_SORT_CONFIRM#")) {
        alert("%#LABEL_SORT_RESTARTMSG#")
        document.getElementById("ProgressBar").style.display="";
        // alle "values" umbauen
        for( i=0; i<AnzahlWR; i++ ) {
//            document.getElementsByName("bez2_"+(i+1))[0].value=wrTab[i]
            document.getElementsByName("bez2_"+wrTab[i])[0].value=i+1
        }
        f.submit()
     }
  }
  else {
     alert("%#LABEL_SORT_MISSING#")
  }
}

function Reset(f) {
 var i
 for( i=0; i<AnzahlWR; i++ ) {
    wrTab[i]=0
 }
}

function addWR(f) {
  grpI=parseInt(f.name.substring(4))
  chooseWR(grpI,0)
}
function delWR(f) {
  grpI=parseInt(f.name.substring(4))
  delOneWR(grpI)
}
function chooseWR(grpI,mode) {
// mode:0=add
var i,i2,code,adr
cntVisiWR=0
code=""
if(mode==0) {
    for(i=0;i<AnzahlWR;i++) {
     if( wrIF[i]!=wrIF[grpI-1] )
        continue
     found=false
     for( i2=0;i2<AnzahlWR;i2++ ) {
        if( wrTab[i2]==i+1 ) {
           found=true
           break
        }
     }
     if(!found) {
       cntVisiWR++
       code=code+"<input name=\'btn_"+i+"\' id=\'idbtn_"+i+"\' value=\'#"+(i+1)
       code=code+" "+wrBez[i]
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

}

function addOneWR(grpI,wrI) {
 wrTab[grpI-1]=wrI+1
 document.getElementsByName("bez2_"+grpI)[0].value = document.getElementsByName("bez1_"+(wrI+1))[0].value
 hidebox('chooser')
}

function delOneWR(grpI) {
 wrTab[grpI-1]=0
 document.getElementsByName("bez2_"+grpI)[0].value = ""
 if( chooser ) {
    chooser=0
    hidebox('chooser')
 }

}

function initbody() {

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
                    showSubMenu("15")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_SORT#</h1>
			<form action="sort_post.html" method="post">
		        %#LABEL_SORT_DESC1#%#LABEL_SORT_DESC2#<br />
				<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
						<tr>
							<td></td>
							<td><strong>%#LABEL_CURRENT#</strong></td>
							<td><strong>%#LABEL_NEW#</strong></td>
							<td></td>
							<td></td>
						</tr>
						<tr>
							<td>%#LABEL_SORT_POS#</td>
							<td>%#LABEL_DESC#</td>
							<td>%#LABEL_DESC#</td>
							<td></td>
							<td></td>
						</tr>
                        <script language="JavaScript">
                            var farben=new Array("#e6f98e","#f4b02d","#f1590e","#CC4C0C","#A63E0A")
                            for( i=0; i<AnzahlWR; i++ ) {
                                document.write("<tr style='background-color:"+farben[wrIF[i]]+"'>")
                                document.write("<td>"+(i+1)+"</td>")
                                document.write("<td><input name='bez1_"+(i+1)+"' maxlength='19' type='text' class='einzeilig' id='bez_"+(i+1)+"' value=\""+wrBez[i]+"\" disabled='disabled' readonly='readonly' /></td>")
                                document.write("<td><input name='bez2_"+(i+1)+"' type='text' class='einzeilig' id='wr_"+(i+1)+"' value='                ' readonly='readonly' /></td>")
                                document.write("<td><input name='add_"+(i+1)+"' type='button' class='button' value='%#LABEL_ADD#' onClick='addWR(this)' /></td>")
                                document.write("<td><input name='del_"+(i+1)+"' type='button' class='button' value='%#LABEL_DEL#' onClick='delWR(this)' /></td>")
                                document.write("</tr>")
                            }
                        </script>
					</table>
				<br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="40"><input type="radio" name="gruppe" id="reorg" value="g_1~" /></td>
						<td>%#LABEL_SORT_NOREORG#</td>
					</tr>
					<tr>
						<td><input type="radio" name="gruppe" id="reorg" value="g_2~" /></td>
						<td>%#LABEL_SORT_REORG#</td>
					</tr>
					<tr>
						<td><input type="radio" name="gruppe" id="reorg" value="g_3~" /></td>
						<td>%#LABEL_SORT_INIT#</td>
					</tr>
				</table>
				<br>
				<input type="button" class="button" onClick="SaveCfm(this.form)" value="%#LABEL_SAVE#" />
				&nbsp;&nbsp;
				<input type="reset" class="button" onClick="Reset(this.form)" value="%#LABEL_CANCEL#" />
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
