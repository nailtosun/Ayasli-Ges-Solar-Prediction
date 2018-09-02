<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_DEFINE_FORECAST#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b

function initbody() {
 if( AnzahlGrp==0 )
   document.getElementById("jahressoll").style.display = ""
 else
   document.getElementById("jahressoll").style.display = "none"
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
                    showSubMenu("4")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_FORECAST#</h1>
			<form action="basic_post.html" method="post">
				<strong>%#LABEL_SITE_DATA#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_SITE_SIZE#</td>
						<td><input name="groesse" id="groesse" type="text" class="einzeiligshort" maxlength="8" value="%s">&nbsp;&nbsp;WP</td>
					</tr>
					<tr>
						<td>%#LABEL_SUBSIDARY#</td>
						<td><input name="verguetung" type="text" class="einzeiligshort" id="verguetung" maxlength="5" value="%s" />&nbsp;&nbsp;<script language="JavaScript">document.write( CurrencySub )</script></td>
            
					</tr>
				</table>
				<br />
				<br />
				<strong>%#LABEL_TARGET_CURRENT#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr style="display:none" id="jahressoll">
						<td width="200">%#LABEL_YEARLY_TARGET#</td>
						<td><input name="jahressoll" id="jahressoll" type="text" class="einzeiligshort" maxlength="5" value="%s">&nbsp;&nbsp;kWh/kWp</td>
					</tr>
				</table>
      		<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_MONTHLY_PORTIONS# % (%#LABEL_IN_TOTAL# = 100%)</td>
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
						<td><input name="ant_01" id="ant_01" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_02" id="ant_02" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_03" id="ant_03" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_04" id="ant_04" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_05" id="ant_05" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_06" id="ant_06" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
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
						<td><input name="ant_07" id="ant_07" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_08" id="ant_08" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_09" id="ant_09" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_10" id="ant_10" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_11" id="ant_11" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
						<td><input name="ant_12" id="ant_12" size="2" maxlength="2" type="text" class="einzeilig" value="%s"></td>
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
