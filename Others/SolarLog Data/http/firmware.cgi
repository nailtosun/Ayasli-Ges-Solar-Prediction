<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_UPDATE_FIRMWARE#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function UpdateCfm(f){
if (confirm("%#LABEL_CONFIRM_FIRM_UPD1#")) {
    if (confirm("%#LABEL_CONFIRM_FIRM_UPD2#")) {
        if (confirm("%#LABEL_CONFIRM_FIRM_UPD3#")) {
            document.getElementById("ProgressBar").style.display="";
            f.submit()
        }
    }
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
                    showSubMenu("13")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display:none;"><br>%#LABEL_PLEASE_WAIT#<br><br /><img src="progress-bar.gif" /></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_INTERNAL# // %#MENU_UPDATE#</h1>
			<script>
			document.write("<form action='http://"+window.location.host+"' enctype='multipart/form-data' method='POST'>")
			</script>
			<input type="hidden" name="DESTINATION-PATH" value="b:\\firmware_update.bin">
			<input type="hidden" name="REDIRECT-PATH" value="firmware_result.html">
				<strong>%#LABEL_UPDATE_FIRMWARE#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td><strong>%#LABEL_DO_DATA_BACKUP0#</strong> %#LABEL_DO_DATA_BACKUP1# <strong>%#LABEL_DO_DATA_BACKUP2#</strong> %#LABEL_DO_DATA_BACKUP3#</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_UPDATE_INFO1# %#LOGGER_FORMAT# %#LABEL_UPDATE_INFO2# <a href="http://%#COMPANY_FIRMWARE#" target="_blank">%#COMPANY_FIRMWARE#</a> %#LABEL_UPDATE_INFO3#<br />%#LABEL_UPDATE_INFO4#<br />%#LABEL_UPDATE_INFO5#</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_CURRENT_FIRMWARE#</td>
						<td><strong><script language="JavaScript">document.write(Firmware+" %#LABEL_FIRMWARE_DATE_FROM# "+FirmwareDate)</script></strong></td>
					</tr>
					<tr>
						<td></td>
						<td><input name="FILE-CONTENT" class="einzeilig" type="file" style="width:300px"></td>
					</tr>
					<tr>
						<td></td>
						<td><input value="%#LABEL_LOAD2#" class="button" onClick="UpdateCfm(this.form)" type="button"></td>
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
