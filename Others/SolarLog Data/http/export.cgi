<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#TITEL_EXPORT#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="tools.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function CheckValid(f){
f.ftp.value=checkDom(f.ftp.value)
f.dir.value=checkDir(f.dir.value)
f.submit()
}
function TestCfm(f){
if (confirm("%#LABEL_START_FTP#")) {
window.location.href="testnet?1"
}}
function SaveCfm(typ){
 if (confirm("%#LABEL_START_CSV#")) {
  document.getElementById("ProgressBar").style.display="";
  window.location.href="expcsv.dat?"+typ
 }
}
function initbody() {
 // SL-WEB - set intervals
 if( IPlatform==0 || IPlatform==1 || IPlatform==3 ) {
   document.getElementById("i10").style.display = ""
   document.getElementById("i15").style.display = ""
 }
 else {
   document.getElementById("i10").style.display = "none"
   document.getElementById("i15").style.display = "none"
   //
   if( document.getElementsByName("intervall")[0].checked ||
       document.getElementsByName("intervall")[1].checked ) {
      document.getElementsByName("intervall")[2].checked=true
   }
 }
}
</script>
<style>
#ProgressBar{ padding:5px;font-size:18px;width:200px;text-align:center;left:40%;top:40%;position:absolute;border:2px solid #666;background-color:#FFF; }
</style>
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
                    showSubMenu("9")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#MENU_EXPORT#</h1>
			<form method="post" action="export_post.html">
				<strong>%#LABEL_DATA_EXPORT#</strong><br />
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
						<td><input name="password" id="password" maxlength="59" type="password" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_DIRECTORY#</td>
						<td><input name="dir" id="dir" maxlength="40" type="text" class="einzeilig" value="%s" /></td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
                  <td width="200">%#LABEL_UPDATE_INTERVAL#</td>
						<td></td>
					</tr>
   				<tr style="display:none" id="i10">
   				   <td></td>
   					<td><input type="radio" name="intervall" id="intervall" value="int_1~" />&nbsp;&nbsp;10%#LABEL_MINUTE_SHORT#</td>
      			</tr>
   				<tr  style="display:none" id="i15">
   				   <td></td>
   					<td><input type="radio" name="intervall" id="intervall" value="int_2~" />&nbsp;&nbsp;15%#LABEL_MINUTE_SHORT#</td>
   				</tr>
   				<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_3~" />&nbsp;&nbsp;30%#LABEL_MINUTE_SHORT#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_4~" />&nbsp;&nbsp;1%#LABEL_HOUR_SHORT#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_5~" />&nbsp;&nbsp;2%#LABEL_HOUR_SHORT#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_6~" />&nbsp;&nbsp;4%#LABEL_HOUR_SHORT#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_7~" />&nbsp;&nbsp;8%#LABEL_HOUR_SHORT#</td>
					</tr>
					<tr>
						<td></td>
						<td><input type="radio" name="intervall" id="intervall" value="int_8~" />&nbsp;&nbsp;%#LABEL_DAILY#</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_DATAFORMAT#</td>
						<td>
							<input type="checkbox" name="solarlog" id="solarlog" value="solarlog~" />&nbsp;&nbsp;%#LOGGER_FORMAT#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							<input type="checkbox" name="csv" id="csv" value="csv~" />&nbsp;&nbsp;%#LABEL_CSV_FORMAT#
						</td>
					</tr>
				</table>
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
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
			<br />
			<br />
			<form enctype="multipart/form-data" method="post" action="expcsvmin.html">
				<strong>%#LABEL_MANUAL_EXPORT# (%#LABEL_CSV_FORMAT2#)</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_CURRENT_VALUES#<br />(%#LABEL_MAX_30_DAYS#)</td>
						<td>
							<input value="%#LABEL_SAVE#" name="save" class="button" onClick="SaveCfm(1)" type="button">%s
						</td>
					</tr>
				</table>
			</form>
			<form enctype="multipart/form-data" method="post" action="expcsvday.html">
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_DAILY_VALUES#<br />(%#LABEL_ALL_INV_INDIVID#)</td>
						<td>
							<input value="%#LABEL_SAVE#" name="save" class="button" onClick="SaveCfm(2)" type="button">%s
						</td>
					</tr>
				</table>
			</form>
			<script language="JavaScript">
			//<form enctype="multipart/form-data" method="post" action="expcsvdayall.html"><table style="width: 100%;" border="0" cellpadding="0"><tbody></tbody><tbody></tbody><tbody><tr><td style="text-align: right; width: 32%;">%#LABEL_DAILY_VALUES#<br>(%#LABEL_ALL_INV_SUM#)</td>
			//<td><table style="width: 100%;" border="0"><tbody><tr><td style="height: 20px; width: 68%;">
			//<input value="%#LABEL_SAVE#" name="save" onclick="SaveCfm(3)" type="button">%s
			//<br></td></tr></tbody></table></td></tr></tbody><tbody></tbody></table></form>
			</script>
		</div>
		<div style="clear: left;"></div>
	</div>
	<div id="footer">
		%#COMPANY# | <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
	</div>
</div>
</body>
</html>
