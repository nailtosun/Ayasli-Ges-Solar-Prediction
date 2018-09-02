<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_BEGIN_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function initbody() {
 if( SLTyp==200 && (SLHW&512) ) { // SMA-Bluetooth available?
   document.getElementById("sma-bt").style.display = ""
 }
 if( SLTyp==200 && (SLHW&64) ) { // S0 available?
   document.getElementById("s0").style.display = ""
 }
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
                    showSubMenu("14")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_START# // %#MENU_BEGIN#</h1>
			<form name="beginform" action="begin_post.html" method="post">
				<strong>%#LABEL_SYSTEM_SETTINGS#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_TIMEZONE#</td>
						<td><input name="zeitzone" maxlength="12" type="text" class="einzeilig" value="%s"> (%#LABEL_CENTRAL_EUROPE#)</td>
					</tr>
					<tr>
						<td>%#LABEL_DATE_TIME#</td>
						<td><input disabled="disabled" name="datum1" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_NEW#</td>
						<td><input name="datum2" maxlength="18" type="text" class="einzeilig" value="%s" /></td>
					</tr>
				</table>
				<br />
				<div style="display:none" id="sma-bt">
				    <strong>%#LABEL_SMABT#</strong><br />
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
    						<td width="200">%#LABEL_SMABT_SERIAL#</td>
    						<td><input name="btinv" id="btinv" maxlength="29" type="text" class="einzeilig" value="%s" /></td>
    					</tr>
    				</table>
    				<br />
            </div>
				<strong>%#LABEL_CHOOSE_INV_B#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_PLEASE_CHOOSE#</td>
						<td><select name="inv_b" class="select_einzeilig^"></select></td>
					</tr>
				</table>
				<br />

				<strong>%#LABEL_CHOOSE_INV_E#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_PLEASE_CHOOSE#</td>
						<td><select name="inv_e" class="select_einzeilig^"></select></td>
					</tr>
				</table>
				<br />
				<div style="display:none" id="s0">
				    <strong>%#LABEL_DIGITAL_COUNTER_AVAIL#</strong><br />
    				<br />
    				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
    					<tr>
    						<td></td>
    						<td>
    							<input type="radio" name="actives0" id="actives0" value="active~" />
    							&nbsp;&nbsp;%#LABEL_YES#
    							&nbsp;&nbsp;&nbsp;&nbsp;
    							<input type="radio" name="actives0" id="actives0" value="inactive~" />
    							&nbsp;&nbsp;%#LABEL_NO#
    						</td>
    					</tr>
    				</table>
    				<br />
            </div>

				<br><br>
				<input type="submit" class="button" value="%#LABEL_SAVE#"  />
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
