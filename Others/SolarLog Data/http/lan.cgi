<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_LAN_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
function showarea(nr) {
 if(nr==0) {
   document.getElementById("router").style.display = "none"
   document.getElementById("analog").style.display = "none"
   document.getElementById("gprs").style.display = "none"
 }
 if(nr==1) {
   document.getElementById("router").style.display = ""
   document.getElementById("analog").style.display = "none"
   document.getElementById("gprs").style.display = "none"
 }
 if(nr==2) {
   document.getElementById("router").style.display = "none"
   document.getElementById("analog").style.display = ""
   document.getElementById("gprs").style.display = "none"
 }
 if(nr==3) {
   document.getElementById("router").style.display = "none"
   document.getElementById("analog").style.display = "none"
   document.getElementById("gprs").style.display = ""
 }
}

var apns=new Array()
apns[0]=new Array("internet.eplus.de","eplus","eplus")
apns[1]=new Array("surfo2","","")
apns[2]=new Array("internet.t-mobile","t-mobile","tm")
apns[3]=new Array("web.vodafone.de","","")
apns[4]=new Array("","","")

function chooseApn(i) {
 if(i<apns.length-1) {
   document.getElementsByName("apn")[0].value=apns[i][0]
   if (apns[i][1] != "" ) document.getElementsByName("gprsuser")[0].value=apns[i][1]
   if (apns[i][2] != "" ) document.getElementsByName("gprspassword")[0].value=apns[i][2]
 }
}

function initbody() {
 var i,apn
 if( SLTyp==800 || SLTyp==1000 ) {
   if( SLHW&16384 ) { // GPRS-Intern
     document.getElementById("gprs_radio").style.display = ""
     document.getElementById("gprs_int").style.display = ""
     document.getElementById("gprs_int2").style.display = ""
   }
   else {
     document.getElementById("analog_radio").style.display = ""
     document.getElementById("gprs_radio").style.display = ""
     document.getElementById("gprs_ext").style.display = ""
     document.getElementById("gprs_ext2").style.display = ""
   }
 }
 if( SLTyp==200 ) {
   if( SLHW&16384 ) { // GPRS-Intern
     document.getElementById("gprs_radio").style.display = ""
     document.getElementById("gprs_int").style.display = ""
     document.getElementById("gprs_int2").style.display = ""
   }
 }
 for(i=0;i<4;i++) {
    if( document.getElementsByName("internet")[i].checked ) {
      showarea(i)
      break
    }
 }
 apn=document.getElementsByName("apn")[0].value
 for(i=0;i<apns.length;i++){
   if(apn==apns[i][0]) {
     document.lanform.apnchoose.selectedIndex=i
     chooseApn(i)
     break
   }
 }
 if( i==apns.length ) {
    document.lanform.apnchoose.selectedIndex=i-1
    chooseApn(apns.length);
 }
 // zugelassene OEMs?
 if(OEMTyp == 0 || OEMTyp==1 || OEMTyp==6 ) {
    document.getElementById("smsdirect").style.display = ""
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
                    showSubMenu("1")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_LAN#</h1>
			<form name="lanform" action="lan_post.html" method="post">
				<strong>%#LABEL_LAN_SETTINGS#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_IP_ADR#</td>
						<td><input name="ip" size="16" maxlength="15" type="text" class="einzeiligshort" id="ip" value="%s" /></td>
					</tr>
					<tr>
						<td>%#LABEL_SUBNET#</td>
						<td><input name="mask" size="16" maxlength="15" type="text" class="einzeiligshort" id="mask" value="%s" /></td>
					</tr>
				</table>
				<br />
				<br />
				<strong>%#LABEL_INTERNET_ACCESS#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_NO_INTERNET#</td>
						<td><input type="radio" name="internet" id="internet" value="i_0~" onclick="showarea(0)" />
						<br /></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_ROUTER# %#LABEL_ROUTER2#</td>
						<td><input type="radio" name="internet" id="internet" value="i_1~" onclick="showarea(1)" /></td>
					</tr>
    				<tr style="display:none" id="analog_radio">
    				    <td>%#LABEL_ANALOG_MODEM#</td>
    					<td><input type="radio" name="internet" id="internet" value="i_2~" onclick="showarea(2)" /></td>
    				</tr>
    				<tr style="display:none" id="gprs_radio">
    				    <td><div style="display:none" id="gprs_ext">%#LABEL_GPRS_MODEM#</div><div style="display:none" id="gprs_int">%#LABEL_GPRS_MODEM_INTERN#</div></td>
    					<td><input type="radio" name="internet" id="internet" value="i_3~" onclick="showarea(3)" /></td>
    				</tr>
				</table>
				<div style="display:none" id="router">
					<br />
					<br />
					<strong>%#LABEL_ROUTER#</strong> %#LABEL_ROUTER2#<br />
					<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
						<tr>
							<td width="200">%#LABEL_IP_ADR#</td>
							<td><input type="checkbox" name="dhcpuse" id="dhcpuse" value="dhcpuse~" />
								%#LABEL_DHCP#<br /></td>
						</tr>
						<tr>
							<td>%#LABEL_GATEWAY#</td>
							<td><input name="gateway" size="16" maxlength="15" type="text" class="einzeiligshort" id="gateway" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_DNS_SERVER#</td>
							<td><input type="checkbox" name="dnsuse" id="dnsuse" value="dnsuse~" />
								%#LABEL_ACTIVE#&nbsp;&nbsp;&nbsp;
								<input name="dnsip" size="16" maxlength="15" type="text" class="einzeiligshort" id="dnsip" value="%s" /></td>
						</tr>
					</table>
				</div>
				<div style="display:none" id="analog">
					<br />
					<br />
					<strong>%#LABEL_ANALOG_MODEM#</strong> (%#LOGGER_NAME#%#LABEL_MODEM_PACK#)<br />
					<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
						<tr>
							<td width="200">%#LABEL_I-BY-CALL#</td>
							<td><input name="ibycall" maxlength="29" type="text" class="einzeiligshort" id="ibycall" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_USERNAME#</td>
							<td><input name="modemuser" maxlength="59" type="text" class="einzeiligshort" id="modemuser" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_PASSWORD#</td>
							<td><input name="modempassword" maxlength="20" type="password" class="einzeiligshort" id="modempassword" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_DIAL0#</td>
							<td><input type="checkbox" name="dial0" id="dial0" value="dial0~" /></td>
						</tr>
						<tr>
							<td>%#LABEL_NO_DIALTONE#</td>
							<td><input type="checkbox" name="dialtone" id="dialtone" value="dialtone~" /></td>
						</tr>
						<tr>
							<td>%#LABEL_ALLOW_DIALIN#</td>
							<td><input type="checkbox" name="dialin" id="dialin" value="dialin~" /></td>
						</tr>
						<tr>
							<td>%#LABEL_DIALIN_PW#</td>
							<td><input name="dialinpw" maxlength="20" type="password" class="einzeiligshort" id="dialinpw" value="%s" /></td>
						</tr>
					</table>
				</div>
				<div style="display:none" id="gprs">
					<br />
					<br />
					<div style="display:none" id="gprs_ext2"><strong>%#LABEL_GPRS_MODEM#</strong> (%#LOGGER_NAME#%#LABEL_GPRS_PACK#)<br /></div>
					<div style="display:none" id="gprs_int2"><strong>%#LABEL_GPRS_MODEM_INTERN#</strong><br /></div>
					<br />
					<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
						<tr>
							<td width="200">%#LABEL_CHOOSE_GPRS_PROV#</td>
							<td>
								<select name="apnchoose" class="select_einzeilig" onchange="chooseApn(this.form.apnchoose.options[this.form.apnchoose.selectedIndex].value)">
											<option value="0">eplus (z.B. Simyo)</option>
											<option value="1">O2 (E/D1)</option>
											<option value="2">T-Mobile (D1)</option>
											<option value="3">Vodafone (D2)</option>
											<option value="4">Andere...</option>
								 </select>
							</td>
						</tr>
						<tr>
							<td>APN</td>
							<td><input name="apn" maxlength="29" type="text" class="einzeilig" id="apn" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_USERNAME#</td>
							<td><input name="gprsuser" maxlength="59" type="text" class="einzeilig" id="gprsuser" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_PASSWORD#</td>
							<td><input name="gprspassword" maxlength="20" type="password" class="einzeilig" id="gprspassword" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_SIM_PIN#</td>
							<td><input name="simpin" maxlength="4" type="password" class="einzeilig" id="simpin" value="%s" /></td>
						</tr>
						<tr>
							<td>%#LABEL_CONN_TIME#</td>
							<td><input type="checkbox" name="keeponline" id="keeponline" value="keeponline~" />
								%#LABEL_KEEP_ONLINE#<br /></td>
						</tr>
						<tr style="display:none" id="smsdirect">
							<td>%#LABEL_SMS_DIRECT#</td>
							<td><input type="checkbox" name="smsdirect" id="smsdirect" value="smsdirect~" /></td>
						</tr>
					</table>
				</div>
				<br><br>
				<input type="submit" class="button" value="%#LABEL_SAVE#" onClick="alert('%#LOGGER_FORMAT# %#LABEL_LAN_REBOOT#')" />
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
