<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_EXCHANGE_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<style type="text/css">
	#ProgressBar{padding:5px;font-size:18px;width:200px;text-align:center;left:40%;top:40%;position:absolute;border:2px solid #666;background-color:#FFF;}
#shadow {
    display:none;
    background-color:#000;
    opacity:0.4;
    -moz-opacity:0.4;
    filter:Alpha(opacity=40);
    position:absolute;
    z-index:1;
    top:0px;
    left:0px;
    width:2000px;
    height:1000px;
}
#status {
    display:none;
    background-color:#FFF;
    position:absolute;
    z-index:2;
    top:0px;
    left:0px;
    width:300px;
    padding:15px 20px 15px 20px;
    border-top:1px solid #BBB;
    border-left:1px solid #BBB;
    border-right:1px solid #555;
    border-bottom:1px solid #555;
}
</style>
<script language="JavaScript" src="popup.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
%s // wrBez wird definiert
%s // wrBezNeu wird definiert
%s // wrIF wird definiert
%s // wrListe=true,false
var wrTab=new Array(AnzahlWR)
var cntVisiWR, chooser=0
var fktPtr
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
        // alle "values" umbauen
        for( i=0; i<AnzahlWR; i++ ) {
            document.getElementsByName("bez2_"+(i+1))[0].value=wrTab[i]
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
     if( wrIF[i]!=wrIF[grpI-1] || wrBez[i]==wrBezNeu[i] )
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
       code=code+" "+wrBezNeu[i]
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
 document.getElementsByName("bez2_"+grpI)[0].value = wrBezNeu[wrI]
 hidebox('chooser')
}

function delOneWR(grpI) {
 wrTab[grpI-1]=0
 document.getElementsByName("bez2_"+grpI)[0].value = ""
    hidebox('chooser')

}

function initbody() {
  if (wrListe==true){
    document.getElementById("tausch_liste").style.display='inline';
    for(i=0;i<AnzahlWR;i++) {
      if (wrBez[i] == wrBezNeu[i]){
         wrTab[i]=i+1;  
      }
   }
  }
}


var ajax = {
  xmlHttp: null,
  userFunc: null,
  
  init: function() {
    if(window.XMLHttpRequest) {
        ajax.xmlHttp = new XMLHttpRequest();
    } else {
        if(window.ActiveXObject) {
            ajax.xmlHttp = new ActiveXObject("Microsoft.XMLHTTP"); 
        }
    }

    if (ajax.xmlHttp == null)
        return false;

    ajax.xmlHttp.onreadystatechange = ajax.processRequest;
    return true;
  },
  
  setUserFunc: function(f) {
    ajax.userFunc = f;
  },
  
  request: function(url) {
    if (ajax.xmlHttp == null)
        ajax.xmlHttp.abort();
    ajax.xmlHttp.onreadystatechange = ajax.processRequest;
    ajax.xmlHttp.open("GET", url+"&random="+(Math.random()*99999),true); // random for IE to stop caching...stupid ie
    ajax.xmlHttp.send(null);
  },
  
  processRequest: function() {

    if (ajax.xmlHttp.readyState == 4 && ajax.xmlHttp.status == 200) {
        returnFunc = ajax.userFunc+"(ajax.xmlHttp.responseText, 1)";
        eval(returnFunc);
    }
    if (ajax.xmlHttp.readyState == 4 && ajax.xmlHttp.status != 200) {
        returnFunc = ajax.userFunc+"('', 0)";
        eval(returnFunc);
    }		
  }  

}

// Anwendungsbeispiel
function nacherkennung(parameter) {
    if (ajax.init()) {
        ajax.setUserFunc("UserFuncNacherkennung");
        ajax.request("wr_nacherkennung.html?action="+parameter);
    }
}

function leave(){
      nacherkennung("exit");
}
function UserFuncNacherkennung(returnValue) {
    if (returnValue == "eof" || returnValue == "fault" || returnValue=="nomanual")
    {
      clearTimeout(fktPtr);
      if (returnValue == "nomanual")
        alert("%#LABEL_EXCHANGE_NO_MANUAL#")
      document.getElementById("shadow").style.display='none';
      document.getElementById("status").style.display='none';
      window.location.href="tausch.html";
    }
    else
    {
        document.getElementById("statusText").innerHTML = returnValue;
        fktPtr=window.setTimeout("nacherkennung('state')", 1000);
    }
}

function go()
{
  window.setTimeout("nacherkennung('init')",1000);
  document.getElementById("Nacherkennung_button").style.display='none'
  document.getElementById("shadow").style.display='inline';
  document.getElementById("status").style.display='inline';
  try{
  window.scrollTo(0, 0);
  }
  catch(e)
  {
  }
}

</script>
</head>
<body onLoad="initbody()">
<div id="shadow"></div>
  
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
                    showSubMenu("18")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_EXCHANGE#</h1>
			<input type ="button" style="display:inline;" id="Nacherkennung_button" value="%#LABEL_EXCHANGE_SCANNING#"" onclick="go()">
<div style="position:relative;">
<div id="status">
    <b>%#LABEL_EXCHANGE_SCANNING#</b><br>
    <br>
    <img src="/working.gif" width="16" height="16" alt="">
    <div id="statusText" style="display:inline; padding-left:10px" >&nbsp;</div>
    <br />
    <br />
		<input type="reset" class="button" onClick="leave()" value="%#LABEL_CANCEL#" />
		<br />
</div>
</div>
			<div id="tausch_liste" style="display:none">
			<form action="tausch_post.html" method="post">
		        %#LABEL_EXCHANGE_DESC1#%#LABEL_EXCHANGE_DESC2#<br />
        <br />
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
                                if (wrBez[i] != wrBezNeu[i])
                                {
                                  document.write("<td><input name='bez2_"+(i+1)+"' type='text' class='einzeilig' id='wr_"+(i+1)+"' value='                ' readonly='readonly' /></td>")
                                  document.write("<td><input name='add_"+(i+1)+"' type='button' class='button' value='%#LABEL_ADD#' onClick='addWR(this)' /></td>")
                                  document.write("<td><input name='del_"+(i+1)+"' type='button' class='button' value='%#LABEL_DEL#' onClick='delWR(this)' /></td>")
                                }
                                else
                                {
                                  document.write("<td><input name='bez2_"+(i+1)+"' type='text' class='einzeilig' id='wr_"+(i+1)+"' value=\""+wrBezNeu[i]+"\" readonly='readonly' /></td>")
                                }
                                document.write("</tr>")
                            }
                        </script>
					</table>
				<br>
				<br>
				<input type="button" class="button" onClick="SaveCfm(this.form)" value="%#LABEL_SAVE#" />
				&nbsp;&nbsp;
				<input type="reset" class="button" onClick="Reset(this.form)" value="%#LABEL_CANCEL#" />
				<br /><br />
				%s
			</form>
			</div>
		</div>
		<div style="clear: left;"></div>
	</div>
	<div id="footer">
		%#COMPANY# | <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
	</div>
</div>
</body>
</html>
