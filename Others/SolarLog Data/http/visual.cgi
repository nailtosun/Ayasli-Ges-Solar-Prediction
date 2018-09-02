<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_CONFIG_GRAPHICS#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
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
                    showSubMenu("5")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_GRAPHICS#</h1>
			<form method="post" action="visual_post.html">
				<strong>%#LABEL_VISUAL#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_XSCALE# %#LABEL_START_DAY# (%#LABEL_TIME_IN# %#LABEL_HOUR#)</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_JAN#</td>
						<td>%#LABEL_FEB#</td>
						<td>%#LABEL_MAR#</td>
						<td>%#LABEL_APR#</td>
						<td>%#LABEL_MAY#</td>
						<td>%#LABEL_JUN#</td>
					</tr>
					<tr>
						<td><input name="start_01" id="start_01" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_02" id="start_02" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_03" id="start_03" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_04" id="start_04" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_05" id="start_05" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_06" id="start_06" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_JUL#</td>
						<td>%#LABEL_AUG#</td>
						<td>%#LABEL_SEP#</td>
						<td>%#LABEL_OCT#</td>
						<td>%#LABEL_NOV#</td>
						<td>%#LABEL_DEC#</td>
					</tr>
					<tr>
						<td><input name="start_07" id="start_07" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_08" id="start_08" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_09" id="start_09" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_10" id="start_10" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_11" id="start_11" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="start_12" id="start_12" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
					</tr>
				</table>
				<br><br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_XSCALE# %#LABEL_END_DAY# (%#LABEL_TIME_IN# %#LABEL_HOUR#)</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_JAN#</td>
						<td>%#LABEL_FEB#</td>
						<td>%#LABEL_MAR#</td>
						<td>%#LABEL_APR#</td>
						<td>%#LABEL_MAY#</td>
						<td>%#LABEL_JUN#</td>
					</tr>
					<tr>
						<td><input name="end_01" id="end_01" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_02" id="end_02" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_03" id="end_03" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_04" id="end_04" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_05" id="end_05" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_06" id="end_06" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_JUL#</td>
						<td>%#LABEL_AUG#</td>
						<td>%#LABEL_SEP#</td>
						<td>%#LABEL_OCT#</td>
						<td>%#LABEL_NOV#</td>
						<td>%#LABEL_DEC#</td>
					</tr>
					<tr>
						<td><input name="end_07" id="end_07" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_08" id="end_08" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_09" id="end_09" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_10" id="end_10" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_11" id="end_11" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
						<td><input name="end_12" id="end_12" size="5" maxlength="5" type="text" class="einzeilig" value="%s"></td>
					</tr>
				</table>
				<br /><br />
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
