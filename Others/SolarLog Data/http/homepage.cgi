<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_TITEL_INTERNET#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="tools.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function showarea(nr) {
 if(nr==0) {
   document.getElementById("homepage").style.display = "none"
 }
 if(nr==1) {
   document.getElementById("homepage").style.display = "none"
 }
 if(nr==2) {
   document.getElementById("homepage").style.display = ""
 }
 if(nr==3) {
   document.getElementById("homepage").style.display = ""
 }
}
function initbody() {
 var i
 // SL-WEB - zugelassene OEMs?
 if( OEMTyp==0 || OEMTyp==1 || OEMTyp==6 ) {
    document.getElementById("slweb").style.display = ""
    for(i=0;i<4;i++) {
       if( document.getElementsByName("web")[i].checked ) {
         showarea(i)
         break
       }
    }
 }
 else { // nur Homepage zeigen
   showarea(3)
 }
}
function CheckValid(f){
f.link.value=checkUrl(f.link.value)
f.submit()
}
</script>
</head>
<body onload="initbody()">
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
                    showSubMenu("6")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#MENU_INTERNET#</h1>
			<form action="homepage_post.html" method="post">
				<br />
				<div style="display:none" id="slweb">
   				<strong>%#LABEL_SOLARLOG_WEB#</strong><br />
   				<br />
   				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
   					<tr>
   						<td width="200">%#LABEL_WEB_FULL#</td>
   						<td><input type="radio" name="web" id="web" value="i_0~" onclick="showarea(0)" />
   						<br /></td>
   					</tr>
   					<tr>
   						<td width="200">%#LABEL_WEB_CLASSIC2#</td>
   						<td><input type="radio" name="web" id="web" value="i_1~" onclick="showarea(1)" /></td>
   					</tr>
       				<tr>
       				    <td>%#LABEL_WEB_SELF#</td>
       					<td><input type="radio" name="web" id="web" value="i_2~" onclick="showarea(2)" /></td>
       				</tr>
       				<tr>
       				    <td>%#LABEL_WEB_CLASSIC1#</td>
       					<td><input type="radio" name="web" id="web" value="i_3~" onclick="showarea(3)" /></td>
       				</tr>
   				</table>
				</div>

				<div style="display:none" id="homepage">
   				<br />
   				<strong>%#LABEL_HOMEPAGE#</strong><br />
   				<br />
   				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
   					<tr>
   						<td width="200">%#LABEL_TITEL#</td>
   						<td><input name="titel" id="titel" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_OPERATOR#</td>
   						<td><input name="betreiber" id="betreiber" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#MENU_EMAIL#</td>
   						<td><input name="email" id="email" maxlength="39" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_LOCATION#</td>
   						<td><input name="standort" id="standort" maxlength="39" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_MODULS#</td>
   						<td><input name="modul" id="modul" maxlength="79" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#MENU_INVERTER#</td>
   						<td><input name="wr" id="wr" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_INST_POWER#</td>
   						<td><input name="leistung" id="leistung" maxlength="39" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_START_OPERATION#</td>
   						<td><input name="inbetrieb" id="inbetrieb" maxlength="39" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_ORIENTATION#</td>
   						<td><input name="ausricht" id="ausricht" maxlength="39" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   				</table>
   				<br />
   				<br />
   				<strong>%#LABEL_EVENTPROT#</strong><br />
   				<br />
   					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
   						<tr>
   							<td width="200">%#LABEL_VISABLE_ON_HP#</td>
   							<td><input type="checkbox" name="event" id="event" value="event~" /></td>
   						</tr>
   					</table>
   				<br />
   				<br />
   				<strong>%#LABEL_BANNER#</strong><br />
   				<br />
   				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
   					<tr>
   						<td width="200">%#LABEL_LINE1#</td>
   						<td><input name="zeile1" id="zeile1" maxlength="29" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_LINE2#</td>
   						<td><input name="zeile2" id="zeile2" maxlength="29" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_LINE3#</td>
   						<td><input name="zeile3" id="zeile3" maxlength="29" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   					<tr>
   						<td>%#LABEL_LINK_HP#</td>
   						<td><input name="link" id="link" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
   					</tr>
   				</table>
				</div>
				<br /><br />
				<input type="button" class="button" value="%#LABEL_SAVE#" onClick="CheckValid(this.form)" />
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
