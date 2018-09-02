<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_CONFIG_SCB#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function initbody() {
 var quant, i, maxan=24, maxdig=8
 // Analog
 quant=document.getElementsByName("cntan")[0].value
 if( quant<0 || quant>maxan )
  quant=0
 for( i=1; i<=maxan; i++ ) {
  if( i<=quant )
   document.getElementById("a"+i).style.display = ""
  else
   document.getElementById("a"+i).style.display = "none"
 }
 // Digital
 quant=document.getElementsByName("cntdig")[0].value
 if( quant<0 || quant>maxdig )
  quant=0
 for( i=1; i<=maxdig; i++ ) {
  if( i<=quant )
   document.getElementById("d"+i).style.display = ""
  else
   document.getElementById("d"+i).style.display = "none"
 }
 checkPower()
}
function checkPower() {
 var psum=0, i, col
 quant=document.getElementsByName("cntan")[0].value
 for( i=1; i<=quant; i++ ) {
  psum+=1*document.getElementsByName("a"+i+"_pow")[0].value
 }
 if( document.getElementsByName("conpowersum")[0].value!=psum )
  col="red"
 else
  col="#524d4d;"
 // todo "Background Color" setzen
 document.getElementById("conpowersum").style.color = col
 for( i=1; i<=quant; i++ ) {
  document.getElementById("a"+i+"_pow").style.color = col
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
                    showSubMenu("17")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#LABEL_SCB_TITEL#</h1>
			<form method="post" action="scb_post.html">
				<strong>%#LABEL_INGENERAL# (%#LABEL_KNBX#)</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>
							<input type="radio" name="mactive" id="mactive1" value="active~" />
							&nbsp;&nbsp;%#LABEL_ACTIVATED#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="radio" name="mactive" id="mactive2" value="inactive~" />
							&nbsp;&nbsp;%#LABEL_DEACTIVATED#
						</td>
						<td></td>
					</tr>
					<tr>
						<td></td>
						<td></td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_INTERFACE485#</td>
	    					<td>
						    <select name="rs485" id="rs485" class="select_einzeilig^"></select>
						</td>
					</tr>
				</table>
				<br />
         <table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
            <tr>
              <td width="200">%#LABEL_ACT_AUTO_CALIBR#</td>
              <td><input type="checkbox" name="calib" id="calib" value="calib~" /></td>
            </tr>
            <tr>
              <td width="200"></td>
                <td><input name="time" id="time" size="8" maxlength="5" type="text" class="einzeiligshort" value="%s" />&nbsp;%#LABEL_CLOCK#</td>
            </tr>
          </table>


				<strong>%#LABEL_SCB_CONFIG#</strong><br />
                <br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_CHOOSE#</td>
						<td>
								<select name="nummer" id="idnummer" class="select_einzeilig" onChange="window.location.href='scb.html?'+this.form.nummer.options.selectedIndex^"></select>
						</td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_CONNECTED2#</td>
						<td><input type="checkbox" name="connected" id="connected" value="conn~" /></td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_WORKING#</td>
						<td><input type="checkbox" name="working" id="working" value="work~" /></td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_DESC#</td>
    					<td><input name="desc" id="desc" maxlength="20" type="text" class="einzeilig" value="%s" /></td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_ADRESS2#</td>
    					<td><input name="adress" id="adress" maxlength="16" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_DEDICATED_INV#</td>
    					<td>
						    <select name="dedinv" id="dedinv" class="select_einzeilig^"></select>
						</td>
					</tr>
					<tr>
					    <td width="200">%#LABEL_SENSORBOX#</td>
						  <td><input type="checkbox" name="sensorbox" id="sensorbox" value="sens~" /></td>
					</tr>
				</table>
				<table style="text-indent:1em" width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
					    <td width="250">%#LABEL_SENSOR_OUTSIDE_TEMP#</td>
						  <td><input type="checkbox" name="sensorbox_tmp" id="sensorbox_tmp" value="sens_tmp~" /></td>
					</tr>
					<tr>
					    <td width="250">%#LABEL_SENSOR_WIND#</td>
						  <td><input type="checkbox" name="sensorbox_wind" id="sensorbox_wind" value="sens_wind~" /></td>
					</tr>
				</table>


        <br />
        <strong>%#LABEL_CHAN_CONFIG#</strong><br />
                <br>
        <table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
          <tr>
            <td align="center">%#LABEL_STRING#</td>
            <td align="left">%#LABEL_ACTIVE#</td>
          </tr>
          <tr id="a1">
            <td align="center">1</td>
            <td align="left"><input name="a1_act" id="a1_act" size="2" maxlength="1" type="checkbox" value="a1_act~"></td>
          </tr>
          <tr id="a2">
            <td align="center">2</td>
            <td align="left"><input name="a2_act" id="a2_act" size="2" maxlength="1" type="checkbox" value="a2_act~"></td>
          </tr>
          <tr id="a3">
            <td align="center">3</td>
            <td align="left"><input name="a3_act" id="a3_act" size="2" maxlength="1" type="checkbox" value="a3_act~"></td>
          </tr>
          <tr id="a4">
            <td align="center">4</td>
            <td align="left"><input name="a4_act" id="a4_act" size="2" maxlength="1" type="checkbox" value="a4_act~"></td>
          </tr>
          <tr id="a5">
            <td align="center">5</td>
            <td align="left"><input name="a5_act" id="a5_act" size="2" maxlength="1" type="checkbox" value="a5_act~"></td>
          </tr>
          <tr id="a6">
            <td align="center">6</td>
            <td align="left"><input name="a6_act" id="a6_act" size="2" maxlength="1" type="checkbox" value="a6_act~"></td>
          </tr>
          <tr id="a7">
            <td align="center">7</td>
            <td align="left"><input name="a7_act" id="a7_act" size="2" maxlength="1" type="checkbox" value="a7_act~"></td>
          </tr>
          <tr id="a8">
            <td align="center">8</td>
            <td align="left"><input name="a8_act" id="a8_act" size="2" maxlength="1" type="checkbox" value="a8_act~"></td>
          </tr>
          <tr id="a9">
            <td align="center">9</td>
            <td align="left"><input name="a9_act" id="a9_act" size="2" maxlength="1" type="checkbox" value="a9_act~"></td>
          </tr>
          <tr id="a10">
            <td align="center">10</td>
            <td align="left"><input name="a10_act" id="a10_act" size="2" maxlength="1" type="checkbox" value="a10_act~"></td>
          </tr>
          <tr id="a11">
            <td align="center">11</td>
            <td align="left"><input name="a11_act" id="a11_act" size="2" maxlength="1" type="checkbox" value="a11_act~"></td>
          </tr>
          <tr id="a12">
            <td align="center">12</td>
            <td align="left"><input name="a12_act" id="a12_act" size="2" maxlength="1" type="checkbox" value="a12_act~"></td>
          </tr>
          <tr id="a13">
            <td align="center">13</td>
            <td align="left"><input name="a13_act" id="a13_act" size="2" maxlength="1" type="checkbox" value="a13_act~"></td>
          </tr>
          <tr id="a14">
            <td align="center">14</td>
            <td align="left"><input name="a14_act" id="a14_act" size="2" maxlength="1" type="checkbox" value="a14_act~"></td>
          </tr>
          <tr id="a15">
            <td align="center">15</td>
            <td align="left"><input name="a15_act" id="a15_act" size="2" maxlength="1" type="checkbox" value="a15_act~"></td>
          </tr>
          <tr id="a16">
            <td align="center">16</td>
            <td align="left"><input name="a16_act" id="a16_act" size="2" maxlength="1" type="checkbox" value="a16_act~"></td>
          </tr>
        </table>



				<br />
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
