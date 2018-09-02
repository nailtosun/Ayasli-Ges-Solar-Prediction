<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_FAILURE#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function do_submit(f){
var e=document.getElementById("statuscodes")
e.value=e.value.substring(0,200) // if too long Beck-WEBserver breaks
e=document.getElementById("fehlercodes")
e.value=e.value.substring(0,200) // if too long Beck-WEBserver breaks
f.submit()
}
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
                    showSubMenu("10")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#MENU_FAILURE#</h1>
			<form action="stoerung_post.html" method="post">
				<strong>%#MENU_INVERTER#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200"></td>
						<td>
							<select name="nummer" class="select_einzeilig" onChange="window.location.href='stoerung.html?'+this.form.nummer.options.selectedIndex^"></select>
						</td>
					</tr>
					<tr>
						<td style="vertical-align:top">%#LABEL_LIST_STATUS#</td>
						<td>
							<textarea id='statuscodes' class="einzeilig" readonly="readonly" name="statuscodes" cols="40" rows="5">%c</textarea>
						</td>
					</tr>
					<tr>
						<td style="vertical-align:top">%#LABEL_LIST_ERROR#</td>
						<td>
							<textarea id='fehlercodes' class="einzeilig" readonly="readonly" name="fehlercodes" cols="40" rows="5">%f</textarea>
						</td>
					</tr>
				</table>
				<br />
				<table width="540" border="0" cellspacing="0" cellpadding="0" class="std_table">
					<tr>
						<td align="center"><strong>%#LABEL_NUMBER#</strong></td>
						<td align="center"><strong>%#LABEL_ACTIVE#</strong></td>
						<td align="center"><strong>%#LABEL_STATUS#</strong></td>
						<td align="center"><strong>%#LABEL_ERROR#</strong></td>
						<td align="center"><strong>%#LABEL_FROM# %#LABEL_CODE#</strong></td>
						<td align="center"><strong>%#LABEL_UNTIL# %#LABEL_CODE#</strong></td>
						<td align="center"><strong>%#MENU_EMAIL#</strong></td>
						<td align="center"><strong>%#MENU_SMS#</strong></td>
						<td align="center"><strong>%#LABEL_AFTER_N# %#LABEL_ACTIVATE_MEASURE#</strong></td>
						<td align="center"><strong>%#LABEL_MAX_EACH_DAY#</strong></td>
					</tr>
					<tr>
						<td align="center"><strong>1</strong></td>
						<td align="center"><input name="aktiv1" value="aktiv~" type="checkbox"></td>
						<td align="center"><input name="typ1" value="status~" type="radio"></td>
						<td align="center"><input name="typ1" value="fehler~" type="radio"></td>
						<td align="center"><input name="von1" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="bis1" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="email1" value="email~" type="checkbox"></td>
						<td align="center"><input name="sms1" value="sms~" type="checkbox"></td>
						<td align="center"><input name="dauer1" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="anzahl1" size="2" maxlength="2" value="%s"></td>
					</tr>
					<tr>
						<td align="center"><strong>2</strong></td>
						<td align="center"><input name="aktiv2" value="aktiv~" type="checkbox"></td>
						<td align="center"><input name="typ2" value="status~" type="radio"></td>
						<td align="center"><input name="typ2" value="fehler~" type="radio"></td>
						<td align="center"><input name="von2" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="bis2" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="email2" value="email~" type="checkbox"></td>
						<td align="center"><input name="sms2" value="sms~" type="checkbox"></td>
						<td align="center"><input name="dauer2" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="anzahl2" size="2" maxlength="2" value="%s"></td>
					</tr>
					<tr>
						<td align="center"><strong>3</strong></td>
						<td align="center"><input name="aktiv3" value="aktiv~" type="checkbox"></td>
						<td align="center"><input name="typ3" value="status~" type="radio"></td>
						<td align="center"><input name="typ3" value="fehler~" type="radio"></td>
						<td align="center"><input name="von3" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="bis3" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="email3" value="email~" type="checkbox"></td>
						<td align="center"><input name="sms3" value="sms~" type="checkbox"></td>
						<td align="center"><input name="dauer3" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="anzahl3" size="2" maxlength="2" value="%s"></td>
					</tr>
					<tr>
						<td align="center"><strong>4</strong></td>
						<td align="center"><input name="aktiv4" value="aktiv~" type="checkbox"></td>
						<td align="center"><input name="typ4" value="status~" type="radio"></td>
						<td align="center"><input name="typ4" value="fehler~" type="radio"></td>
						<td align="center"><input name="von4" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="bis4" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="email4" value="email~" type="checkbox"></td>
						<td align="center"><input name="sms4" value="sms~" type="checkbox"></td>
						<td align="center"><input name="dauer4" size="3" maxlength="3" value="%s"></td>
						<td align="center"><input name="anzahl4" size="2" maxlength="2" value="%s"></td>
					</tr>
				</table>
				<br /><br />
				<input type="button" class="button" value="%#LABEL_SAVE#" onClick="do_submit(this.form)" />
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
