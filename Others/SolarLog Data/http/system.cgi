<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_SYSTEM#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
function LoadCfm(f){
if (confirm("%#LABEL_CONFIRM_RESTORE_SYSTEM#")) {
document.getElementById("ProgressBar").style.display="";
f.submit()
}
}
function ResCfm(f){
if (confirm("%#LABEL_CONFIRM_RESET_SYSTEM#")) {
document.getElementById("ProgressBar").style.display="";
window.location.href='reset.dat';
}
}
function WRCfm(f){
if (confirm("Wechselrichter wirklich neu erkennen?\r\n\r\n(Diese Funktion sollte immer dann verwendet werden, wenn ein Wechselrichter ausgetauscht wurde oder sich die Anzahl Wechselrichter geändert hat.\r\nACHTUNG!\r\n Es werden alle Ertragsdaten gelöscht und die Angaben unter 'Konfiguration/Basis/Wechselrichter' müssen überprüft bzw. ergänzt werden. Daher immer zuerst eine Datensicherung durchführen und evtl. auch die Daten der WR-Konfiguration notieren.")) {
document.getElementById("ProgressBar").style.display="";
window.location.href='resetwr.dat';
}
}
</script>
<style>
#ProgressBar{padding:5px;font-size:18px;width:200px;text-align:center;left:40%;top:40%;position:absolute;border:2px solid #666;background-color:#FFF;}
</style>
</head>
<body>
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
                    showSubMenu("12")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_INTERNAL# // %#MENU_SYSTEM#</h1>
			<script>
			document.write("<form action='http://"+window.location.host+"' enctype='multipart/form-data' method='POST'>")
			</script>
			<input type="hidden" name="DESTINATION-PATH" value="b:\\sysrestore.dat"><input type="hidden" name="REDIRECT-PATH" value="sysrestore.html">
				<strong>%#LABEL_SYSTEM_BACKUP#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_SAVE_SYSTEM_DATA_HD#</td>
						<td><input value="%#LABEL_CREATE#" name="save" class="button" onClick="window.location.href='system.dat'" type="button">%s</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_RESTORE_SYSTEM_SETTINGS#</td>
						<td><input name="FILE-CONTENT" class="einzeilig" type="file" style="width:300px"></td>
					</tr>
					<tr>
						<td></td>
						<td><input value="%#LABEL_LOAD#" class="button" onClick="LoadCfm(this.form)" type="button"></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_CONFIRM_RESET_FACTORY#</td>
						<td><input value="%#LABEL_RESET#" name="reset" class="button" onclick="ResCfm(this.form)" type="button"></td>
					</tr>
				</table>
			</form>
			<br /><br />
			<form method="post" action="system_post.html">
				<strong>%#LABEL_SYSTEM_SETTINGS#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_CHOOSE_COUNTRY#</td>
						<td><select name="country" class="select_einzeilig^"></select>&nbsp;&nbsp;
						<input value="%#LABEL_COUNTRY_LOAD#" class="button" type="submit"></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_CHOOSE_LANG#</td>
						<td><select name="lang" class="select_einzeilig^"></select></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_CURRENT_SERIAL#</td>
						<td><input readonly="readonly" name="seriennr" type="text" class="einzeiligshort" value="%s"></td>
					</tr>
					<tr>
						<td>%#LABEL_LICENCE_KEY#</td>
						<td><input name="lizenz" maxlength="18" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_SAVE_INTERVAL#</td>
						<td><input type="radio" name="intervall" value="i_1~" />&nbsp;&nbsp;5%#LABEL_MINUTE_SHORT2#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" value="i_2~" />&nbsp;&nbsp;10%#LABEL_MINUTE_SHORT2#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" value="i_3~" />&nbsp;&nbsp;15%#LABEL_MINUTE_SHORT2#</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_TIMEZONE#</td>
						<td><input name="zeitzone" maxlength="12" type="text" class="einzeiligshort" value="%s"> (%#LABEL_CENTRAL_EUROPE#)</td>
					</tr>
					<tr>
						<td>%#LABEL_DATE_TIME#</td>
						<td><input disabled="disabled" name="datum1" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_NEW#</td>
						<td><input name="datum2" maxlength="20" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_DST_SETTING#</td>
						<td><select name="dst" class="select_einzeilig^"></select>&nbsp;&nbsp;
					</tr>
				</table>
				</table>
				<br />
				<br />
				<strong>%#MENU_CONFIGURATION#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_ADDITIONAL_PW#</td>
						<td><input type="checkbox" name="check_pw" value="check_pw~" /></td>
					</tr>
					<tr>
						<td>%#LABEL_OLD_PW#</td>
						<td><input name="old_pw" maxlength="19" type="password" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_NEW_PW#</td>
						<td><input name="new_pw" maxlength="19" type="password" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_REPEAT_PW#</td>
						<td><input name="new_pw2" maxlength="19" type="password" class="einzeiligshort" value="%s" /></td>
					</tr>
				</table>
				<br /><br />
				<input type="submit" class="button" value="%#LABEL_SAVE#" />
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
