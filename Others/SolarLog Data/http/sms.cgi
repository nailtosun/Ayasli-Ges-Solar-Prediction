<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_SMS#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="tools.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function CheckValid(f){
f.smtp.value=checkDom(f.smtp.value)
f.submit()
}
function TestCfm(f){
if (confirm("%#LABEL_START_TESTSMS#")) {
window.location.href="testnet?3"
}}
</script>
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
                    showSubMenu("8")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#MENU_SMS#</h1>
			<form name="sms_form" method="post" action="sms_post.html">
				<strong>%#LABEL_SMS_BASIC_SETTING#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_SMTP_SERVER#</td>
						<td><input name="smtp" id="smtp" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
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
						<td>%#LABEL_EMAIL_FROM#</td>
						<td><input name="email_von" id="email_von" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_EMAIL_TO#</td>
						<td><input name="email_nach" id="email_nach" maxlength="59" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_KEYWORD_SUBJECT#</td>
						<td><input name="subject" id="subject" maxlength="20" type="text" class="einzeilig" value="%s" /></td>
					</tr>
				</table>
				<br />
				<br />
				<strong>%#LABEL_SMS_NOTIFIC#</strong><br />
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
						<td width="200">%#LABEL_SEND_TIME#</td>
						<td><input name="time" id="time" maxlength="8" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_1" id="versand_1" value="versand_1~" />&nbsp;&nbsp;%#LABEL_MONDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_2" id="versand_2" value="versand_2~" />&nbsp;&nbsp;%#LABEL_TUESDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_3" id="versand_3" value="versand_3~" />&nbsp;&nbsp;%#LABEL_WEDNESDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_4" id="versand_4" value="versand_4~" />&nbsp;&nbsp;%#LABEL_THURSDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_5" id="versand_5" value="versand_5~" />&nbsp;&nbsp;%#LABEL_FRIDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_6" id="versand_6" value="versand_6~" />&nbsp;&nbsp;%#LABEL_SATURDAY#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="checkbox" name="versand_7" id="versand_7" value="versand_7~" />&nbsp;&nbsp;%#LABEL_SUNDAY#</td>
					</tr>
					</table>
					<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_YIELD_IN_SUBJECT#</td>
						<td>
							<input type="checkbox" name="ertragbetreff" id="ertragbetreff" value="ertragbetreff~" />
						</td>
					</tr>
					<tr>
						<td width="200">%#LABEL_LAST_TRANS#</td>
						<td>
							<input name="date" id="date" type="text" class="einzeiligshort" value="%s" readonly="readonly" />
						</td>
					</tr>
					<tr>
						<td>%#LABEL_STATUS#</td>
						<td>
							<input name="status" id="status" type="text" class="einzeiligshort" value="%s" readonly="readonly" />
						</td>
					</tr>
				</table>
				<br /><br />
				<input type="button" class="button" value="%#LABEL_SAVE#" onClick="CheckValid(this.form)" />
				&nbsp;&nbsp;
				<input type="reset" class="button" value="%#LABEL_CANCEL#" />
				<br /><br />
				<input type="button" class="button" value="%#LABEL_START_TRANS#" onClick="TestCfm(this)" />
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
