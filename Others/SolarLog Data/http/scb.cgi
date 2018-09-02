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
function DuplicateCfm(f){
 quant=document.getElementsByName("cntan")[0].value
 for( i=1; i<=quant; i++ ) {
  document.getElementsByName("a"+i+"_off")[0].value = document.getElementsByName("a1_off")[0].value
  document.getElementsByName("a"+i+"_stei")[0].value = document.getElementsByName("a1_stei")[0].value
  document.getElementsByName("a"+i+"_pow")[0].value = document.getElementsByName("a1_pow")[0].value
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
        <strong>%#LABEL_INGENERAL#</strong><br />
        <br />
        <table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
          <tr>
            <td></td>
            <td>
              <input type="radio" name="mactive" id="mactive1" value="active~" />
              &nbsp;&nbsp;%#LABEL_ACTIVATED#
              &nbsp;&nbsp;&nbsp;&nbsp;
              <input type="radio" name="mactive" id="mactive2" value="inactive~" />
              &nbsp;&nbsp;%#LABEL_DEACTIVATED#
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
              <td width="200">%#LABEL_QUANT_ANALOG#</td>
              <td><input name="cntan" id="cntan" maxlength="3" type="text" class="einzeiligshort" value="%s" onchange="initbody()" /></td>
          </tr>
          <tr>
              <td width="200">%#LABEL_QUANT_DIGITAL#</td>
              <td><input name="cntdig" id="cntdig" maxlength="3" type="text" class="einzeiligshort" value="%s" onchange="initbody()" /></td>
          </tr>
          <tr>
              <td width="200">%#LABEL_INST_DC_POWER#</td>
              <td><input name="conpowersum" id="conpowersum" maxlength="7" type="text" class="einzeiligshort" value="%s" onChange="checkPower()" /></td>
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
            <td>%#LABEL_ANALOG#</td>
            <td>%#LABEL_ACTIVE#</td>
            <td>%#LABEL_TYPE#</td>
            <td>%#LABEL_OFFSET#</td>
            <td>%#LABEL_SLOPE#</td>
            <td>%#LABEL_INST_DC_POWER#</td>
          </tr>
          <tr style="display:none" id="a1">
            <td align="center">1</td>
            <td align="left"><input name="a1_act" id="a1_act" size="2" maxlength="1" type="checkbox" value="a1_act~"></td>
            <td align="left"><select name="a1_typ" id="a1_typ" class="select_einzeilig^"></select></td>
            <td><input name="a1_off" id="a1_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a1_stei" id="a1_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a1_pow" id="a1_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()">&nbsp;&nbsp;&nbsp;<input type="button" class="button" value="%#LABEL_DUPLICATE#" onClick="DuplicateCfm(this)" /></td>
          </tr>
          <tr style="display:none" id="a2">
            <td align="center">2</td>
            <td align="left"><input name="a2_act" id="a2_act" size="2" maxlength="1" type="checkbox" value="a2_act~"></td>
            <td align="left"><select name="a2_typ" id="a2_typ" class="select_einzeilig^"></select></td>
            <td><input name="a2_off" id="a2_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a2_stei" id="a2_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a2_pow" id="a2_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a3">
            <td align="center">3</td>
            <td align="left"><input name="a3_act" id="a3_act" size="2" maxlength="1" type="checkbox" value="a3_act~"></td>
            <td align="left"><select name="a3_typ" id="a3_typ" class="select_einzeilig^"></select></td>
            <td><input name="a3_off" id="a3_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a3_stei" id="a3_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a3_pow" id="a3_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a4">
            <td align="center">4</td>
            <td align="left"><input name="a4_act" id="a4_act" size="2" maxlength="1" type="checkbox" value="a4_act~"></td>
            <td align="left"><select name="a4_typ" id="a4_typ" class="select_einzeilig^"></select></td>
            <td><input name="a4_off" id="a4_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a4_stei" id="a4_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a4_pow" id="a4_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a5">
            <td align="center">5</td>
            <td align="left"><input name="a5_act" id="a5_act" size="2" maxlength="1" type="checkbox" value="a5_act~"></td>
            <td align="left"><select name="a5_typ" id="a5_typ" class="select_einzeilig^"></select></td>
            <td><input name="a5_off" id="a5_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a5_stei" id="a5_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a5_pow" id="a5_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a6">
            <td align="center">6</td>
            <td align="left"><input name="a6_act" id="a6_act" size="2" maxlength="1" type="checkbox" value="a6_act~"></td>
            <td align="left"><select name="a6_typ" id="a6_typ" class="select_einzeilig^"></select></td>
            <td><input name="a6_off" id="a6_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a6_stei" id="a6_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a6_pow" id="a6_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a7">
            <td align="center">7</td>
            <td align="left"><input name="a7_act" id="a7_act" size="2" maxlength="1" type="checkbox" value="a7_act~"></td>
            <td align="left"><select name="a7_typ" id="a7_typ" class="select_einzeilig^"></select></td>
            <td><input name="a7_off" id="a7_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a7_stei" id="a7_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a7_pow" id="a7_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a8">
            <td align="center">8</td>
            <td align="left"><input name="a8_act" id="a8_act" size="2" maxlength="1" type="checkbox" value="a8_act~"></td>
            <td align="left"><select name="a8_typ" id="a8_typ" class="select_einzeilig^"></select></td>
            <td><input name="a8_off" id="a8_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a8_stei" id="a8_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a8_pow" id="a8_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a9">
            <td align="center">9</td>
            <td align="left"><input name="a9_act" id="a9_act" size="2" maxlength="1" type="checkbox" value="a9_act~"></td>
            <td align="left"><select name="a9_typ" id="a9_typ" class="select_einzeilig^"></select></td>
            <td><input name="a9_off" id="a9_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a9_stei" id="a9_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a9_pow" id="a9_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a10">
            <td align="center">10</td>
            <td align="left"><input name="a10_act" id="a10_act" size="2" maxlength="1" type="checkbox" value="a10_act~"></td>
            <td align="left"><select name="a10_typ" id="a10_typ" class="select_einzeilig^"></select></td>
            <td><input name="a10_off" id="a10_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a10_stei" id="a10_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a10_pow" id="a10_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a11">
            <td align="center">11</td>
            <td align="left"><input name="a11_act" id="a11_act" size="2" maxlength="1" type="checkbox" value="a11_act~"></td>
            <td align="left"><select name="a11_typ" id="a11_typ" class="select_einzeilig^"></select></td>
            <td><input name="a11_off" id="a11_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a11_stei" id="a11_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a11_pow" id="a11_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a12">
            <td align="center">12</td>
            <td align="left"><input name="a12_act" id="a12_act" size="2" maxlength="1" type="checkbox" value="a12_act~"></td>
            <td align="left"><select name="a12_typ" id="a12_typ" class="select_einzeilig^"></select></td>
            <td><input name="a12_off" id="a12_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a12_stei" id="a12_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a12_pow" id="a12_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a13">
            <td align="center">13</td>
            <td align="left"><input name="a13_act" id="a13_act" size="2" maxlength="1" type="checkbox" value="a13_act~"></td>
            <td align="left"><select name="a13_typ" id="a13_typ" class="select_einzeilig^"></select></td>
            <td><input name="a13_off" id="a13_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a13_stei" id="a13_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a13_pow" id="a13_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a14">
            <td align="center">14</td>
            <td align="left"><input name="a14_act" id="a14_act" size="2" maxlength="1" type="checkbox" value="a14_act~"></td>
            <td align="left"><select name="a14_typ" id="a14_typ" class="select_einzeilig^"></select></td>
            <td><input name="a14_off" id="a14_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a14_stei" id="a14_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a14_pow" id="a14_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a15">
            <td align="center">15</td>
            <td align="left"><input name="a15_act" id="a15_act" size="2" maxlength="1" type="checkbox" value="a15_act~"></td>
            <td align="left"><select name="a15_typ" id="a15_typ" class="select_einzeilig^"></select></td>
            <td><input name="a15_off" id="a15_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a15_stei" id="a15_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a15_pow" id="a15_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a16">
            <td align="center">16</td>
            <td align="left"><input name="a16_act" id="a16_act" size="2" maxlength="1" type="checkbox" value="a16_act~"></td>
            <td align="left"><select name="a16_typ" id="a16_typ" class="select_einzeilig^"></select></td>
            <td><input name="a16_off" id="a16_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a16_stei" id="a16_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a16_pow" id="a16_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a17">
            <td align="center">17</td>
            <td align="left"><input name="a17_act" id="a17_act" size="2" maxlength="1" type="checkbox" value="a17_act~"></td>
            <td align="left"><select name="a17_typ" id="a17_typ" class="select_einzeilig^"></select></td>
            <td><input name="a17_off" id="a17_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a17_stei" id="a17_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a17_pow" id="a17_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a18">
            <td align="center">18</td>
            <td align="left"><input name="a18_act" id="a18_act" size="2" maxlength="1" type="checkbox" value="a18_act~"></td>
            <td align="left"><select name="a18_typ" id="a18_typ" class="select_einzeilig^"></select></td>
            <td><input name="a18_off" id="a18_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a18_stei" id="a18_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a18_pow" id="a18_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a19">
            <td align="center">19</td>
            <td align="left"><input name="a19_act" id="a19_act" size="2" maxlength="1" type="checkbox" value="a19_act~"></td>
            <td align="left"><select name="a19_typ" id="a19_typ" class="select_einzeilig^"></select></td>
            <td><input name="a19_off" id="a19_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a19_stei" id="a19_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a19_pow" id="a19_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a20">
            <td align="center">20</td>
            <td align="left"><input name="a20_act" id="a20_act" size="2" maxlength="1" type="checkbox" value="a20_act~"></td>
            <td align="left"><select name="a20_typ" id="a20_typ" class="select_einzeilig^"></select></td>
            <td><input name="a20_off" id="a20_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a20_stei" id="a20_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a20_pow" id="a20_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a21">
            <td align="center">21</td>
            <td align="left"><input name="a21_act" id="a21_act" size="2" maxlength="1" type="checkbox" value="a21_act~"></td>
            <td align="left"><select name="a21_typ" id="a21_typ" class="select_einzeilig^"></select></td>
            <td><input name="a21_off" id="a21_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a21_stei" id="a21_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a21_pow" id="a21_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a22">
            <td align="center">22</td>
            <td align="left"><input name="a22_act" id="a22_act" size="2" maxlength="1" type="checkbox" value="a22_act~"></td>
            <td align="left"><select name="a22_typ" id="a22_typ" class="select_einzeilig^"></select></td>
            <td><input name="a22_off" id="a22_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a22_stei" id="a22_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a22_pow" id="a22_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a23">
            <td align="center">23</td>
            <td align="left"><input name="a23_act" id="a23_act" size="2" maxlength="1" type="checkbox" value="a23_act~"></td>
            <td align="left"><select name="a23_typ" id="a23_typ" class="select_einzeilig^"></select></td>
            <td><input name="a23_off" id="a23_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a23_stei" id="a23_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a23_pow" id="a23_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr style="display:none" id="a24">
            <td align="center">24</td>
            <td align="left"><input name="a24_act" id="a24_act" size="2" maxlength="1" type="checkbox" value="a24_act~"></td>
            <td align="left"><select name="a24_typ" id="a24_typ" class="select_einzeilig^"></select></td>
            <td><input name="a24_off" id="a24_off" size="5" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a24_stei" id="a24_stei" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
            <td><input name="a24_pow" id="a24_pow" size="6" maxlength="5" type="text" class="einzeiligshort" value="%s" onChange="checkPower()"></td>
          </tr>
          <tr>
            <td>%#LABEL_DIGITAL#</td>
            <td>%#LABEL_ACTIVE#</td>
            <td>%#LABEL_TYPE#</td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d1">
            <td align="center">1</td>
            <td align="left"><input name="d1_act" id="d1_act" size="2" maxlength="1" type="checkbox" value="d1_act~"></td>
            <td align="left"><select name="d1_typ" id="d1_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d2">
            <td align="center">2</td>
            <td align="left"><input name="d2_act" id="d2_act" size="2" maxlength="1" type="checkbox" value="d2_act~"></td>
            <td align="left"><select name="d2_typ" id="d2_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d3">
            <td align="center">3</td>
            <td align="left"><input name="d3_act" id="d3_act" size="2" maxlength="1" type="checkbox" value="d3_act~"></td>
            <td align="left"><select name="d3_typ" id="d3_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d4">
            <td align="center">4</td>
            <td align="left"><input name="d4_act" id="d4_act" size="2" maxlength="1" type="checkbox" value="d4_act~"></td>
            <td align="left"><select name="d4_typ" id="d4_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d5">
            <td align="center">5</td>
            <td align="left"><input name="d5_act" id="d5_act" size="2" maxlength="1" type="checkbox" value="d5_act~"></td>
            <td align="left"><select name="d5_typ" id="d5_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d6">
            <td align="center">6</td>
            <td align="left"><input name="d6_act" id="d6_act" size="2" maxlength="1" type="checkbox" value="d6_act~"></td>
            <td align="left"><select name="d6_typ" id="d6_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d7">
            <td align="center">7</td>
            <td align="left"><input name="d7_act" id="d7_act" size="2" maxlength="1" type="checkbox" value="d7_act~"></td>
            <td align="left"><select name="d7_typ" id="d7_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
          <tr style="display:none" id="d8">
            <td align="center">8</td>
            <td align="left"><input name="d8_act" id="d8_act" size="2" maxlength="1" type="checkbox" value="d8_act~"></td>
            <td align="left"><select name="d8_typ" id="d8_typ" class="select_einzeilig^"></select></td>
            <td></td>
            <td></td>
          </tr>
        </table>
                <br>
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