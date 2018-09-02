<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_BACKUP#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript" src="tools.js"></script>
<script language="JavaScript">
%b
function CheckValid(f){
f.ftp.value=checkDom(f.ftp.value)
f.dir.value=checkDir(f.dir.value)
f.submit()
}
function LoadCfm(f){
if (confirm("%#LABEL_CONFIRM_BACKUP#")) {
document.getElementById("ProgressBar").style.display="";
f.submit();
}
}
function ImportCfm(f){
if (confirm("%#LABEL_CONFIRM_IMPORT#")) {
document.getElementById("ProgressBar").style.display="";
f.submit()
}
}
function SaveCfm(f){
if (confirm("%#LABEL_CONFIRM_SAVE_BACKUP#")) {
document.getElementById("ProgressBar").style.display="";
window.location.href='backup.dat'
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
                    showSubMenu("11")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_INTERNAL# // %#MENU_BACKUP#</h1>
			<form method="post" action="backup_post.html">
				<strong>%#LABEL_BACKUP# (%#LABEL_AUTOMATICALLY#)</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td></td>
						<td>
							<input type="radio" name="active" id="active" value="active~" />
							&nbsp;&nbsp;%#LABEL_ACTIVATED#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="radio" name="active" id="active" value="inactive~" />
							&nbsp;&nbsp;%#LABEL_DEACTIVATED#
						</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_FTP_SERVER#</td>
						<td><input name="ftp" id="ftp" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_USERNAME#</td>
						<td><input name="user" id="user" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_PASSWORD#</td>
						<td><input name="password" id="password" maxlength="20" type="password" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_DIRECTORY#</td>
						<td><input name="dir" id="dir" maxlength="40" type="text" class="einzeilig" value="%s" /></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_BACKUP_INTERVAL#</td>
						<td><input name="intervall" value="day~" type="radio">&nbsp;&nbsp;%#LABEL_DAILY2#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="intervall" value="week~" type="radio">&nbsp;&nbsp;%#LABEL_WEEKLY#</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200"></td>
						<td><input name="weekday" value="day_1~" type="radio">&nbsp;&nbsp;%#LABEL_MONDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_2~" type="radio">&nbsp;&nbsp;%#LABEL_TUESDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_3~" type="radio">&nbsp;&nbsp;%#LABEL_WEDNESDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_4~" type="radio">&nbsp;&nbsp;%#LABEL_THURSDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_5~" type="radio">&nbsp;&nbsp;%#LABEL_FRIDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_6~" type="radio">&nbsp;&nbsp;%#LABEL_SATURDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input name="weekday" value="day_7~" type="radio">&nbsp;&nbsp;%#LABEL_SUNDAY#</td>
					</tr>
				</table>
				<br /><br />
				<input type="button" class="button" value="%#LABEL_SAVE#" onClick="CheckValid(this.form)" />
				&nbsp;&nbsp;
				<input type="reset" class="button" value="%#LABEL_CANCEL#" />
				<br /><br />
				%s
			</form>
			<br />
			<br />
			<script>
			document.write("<form action='http://"+window.location.host+"' enctype='multipart/form-data' method='POST'>")
			</script>
			<input type="hidden" name="DESTINATION-PATH" value="b:\\restore.dat"><input type="hidden" name="REDIRECT-PATH" value="restore.html">
				<strong>%#LABEL_BACKUP# (%#LABEL_MANUALLY#)</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_SAVE_DATA_HD#</td>
						<td><input value="%#LABEL_CREATE#" name="save" class="button" onClick="SaveCfm(this.form)" type="button">%s</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_LOAD_DATA_HD#</td>
						<td><input name="FILE-CONTENT" class="einzeilig" type="file" style="width:300px"></td>
					</tr>
					<tr>
						<td></td>
						<td><input value="%#LABEL_LOAD#" class="button" onClick="LoadCfm(this.form)" type="button"></td>
					</tr>
				</table>
			</form>
			<br />
			<br />
			<form method="post" action="correct_result.html">
				<strong>%#LABEL_DATA_CORRECTION#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200" style="vertical-align:top">%#LABEL_DATE#</td>
						<td><input name="datum" id="datum" maxlength="8" type="text" class="einzeiligshort" value="%s" /> <br />(%#LABEL_FOR_EXAMPLE# %s)</td>
					</tr>
					<tr>
						<td style="vertical-align:top">%#LABEL_DAILY_YIELD#</td>
						<td><input name="wert" id="wert" maxlength="6" type="text" class="einzeiligshort" value="%s" /> kWh <br />(%#LABEL_FOR_EXAMPLE# 48.1)</td>
					</tr>
					<tr>
						<td></td>
						<td><input value="%#LABEL_ADJUST#" class="button" type="submit"></td>
					</tr>
				</table>
			</form>
			<br />
			<br />
			<script>
			document.write("<form action='http://"+window.location.host+"' enctype='multipart/form-data' method='POST'>")
			</script>
			<input type="hidden" name="DESTINATION-PATH" value="b:\\import.csv"><input type="hidden" name="REDIRECT-PATH" value="import.html">
				<strong>%#LABEL_DATA_IMPORT#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_INITAL_INVENTORY#<br />(<script language="JavaScript">document.write(DateFormat)</script>; %#LABEL_DAY_YIELD_IN# Wh);<br />d=%#LABEL_DAY# m=%#LABEL_MONTH# y=%#LABEL_YEAR#</td>
						<td style="vertical-align:bottom"><input name="FILE-CONTENT" class="einzeilig" type="file" style="width:300px"></td>
					</tr>
					<tr>
						<td></td>
						<td><input value="%#LABEL_LOAD#" class="button" onClick="ImportCfm(this.form)" type="button"></td>
					</tr>
				</table>
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
