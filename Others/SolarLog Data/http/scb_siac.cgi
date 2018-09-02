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
				<strong>%#LABEL_INGENERAL# (%#LABEL_SIAC#)</strong><br />
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
				</table>


        <br />
        <strong>%#LABEL_CHAN_CONFIG#</strong><br />
                <br>
        <table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
          <tr>
            <td align="center">%#LABEL_STRING#</td>
            <td align="left">%#LABEL_ACTIVE#</td>
          </tr>
          <tr id="d1">
            <td align="center">1</td>
            <td align="left"><input name="d1_act" id="d1_act" size="2" maxlength="1" type="checkbox" value="d1_act~"></td>
          </tr>
          <tr id="d2">
            <td align="center">2</td>
            <td align="left"><input name="d2_act" id="d2_act" size="2" maxlength="1" type="checkbox" value="d2_act~"></td>
          </tr>
          <tr id="d3">
            <td align="center">3</td>
            <td align="left"><input name="d3_act" id="d3_act" size="2" maxlength="1" type="checkbox" value="d3_act~"></td>
          </tr>
          <tr id="d4">
            <td align="center">4</td>
            <td align="left"><input name="d4_act" id="d4_act" size="2" maxlength="1" type="checkbox" value="d4_act~"></td>
          </tr>
          <tr id="d5">
            <td align="center">5</td>
            <td align="left"><input name="d5_act" id="d5_act" size="2" maxlength="1" type="checkbox" value="d5_act~"></td>
          </tr>
          <tr id="d6">
            <td align="center">6</td>
            <td align="left"><input name="d6_act" id="d6_act" size="2" maxlength="1" type="checkbox" value="d6_act~"></td>
          </tr>
          <tr id="d7">
            <td align="center">7</td>
            <td align="left"><input name="d7_act" id="d7_act" size="2" maxlength="1" type="checkbox" value="d7_act~"></td>
          </tr>
          <tr id="d8">
            <td align="center">8</td>
            <td align="left"><input name="d8_act" id="d8_act" size="2" maxlength="1" type="checkbox" value="d8_act~"></td>
          </tr>
          <tr id="d9">
            <td align="center">9</td>
            <td align="left"><input name="d9_act" id="d9_act" size="2" maxlength="1" type="checkbox" value="d9_act~"></td>
          </tr>
          <tr id="d10">
            <td align="center">10</td>
            <td align="left"><input name="d10_act" id="d10_act" size="2" maxlength="1" type="checkbox" value="d10_act~"></td>
          </tr>
          <tr id="d11">
            <td align="center">11</td>
            <td align="left"><input name="d11_act" id="d11_act" size="2" maxlength="1" type="checkbox" value="d11_act~"></td>
          </tr>
          <tr id="d12">
            <td align="center">12</td>
            <td align="left"><input name="d12_act" id="d12_act" size="2" maxlength="1" type="checkbox" value="d12_act~"></td>
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
