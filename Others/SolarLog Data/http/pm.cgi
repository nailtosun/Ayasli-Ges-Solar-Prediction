<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_PM_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var qtyEntries
var max_entry=16
%b
function initbody() {
 var i, ip
 // alle belegten IP-Adressen sichtbar machen plus 1
 for( i=1; i<10; i++ ) {
     ip=document.getElementsByName("a"+i+"_ip")[0].value
     if( ip!="" && ip!="0.0.0.0" )
        document.getElementById("a"+i).style.display = ""
     else
        break
 }
 if( i<10 ) {
    document.getElementById("a"+i).style.display = ""
    i++
 }
 if( i<10 ) {
    document.getElementById("a"+i).style.display = ""
    i++
 }
 for( ; i<10; i++ ) {
    document.getElementById("a"+i).style.display = "none"
    document.getElementsByName("a"+i+"_ip")[0].value = "0.0.0.0"
 }
 
 // zugelassene OEMs?
 if(OEMTyp == 0 || OEMTyp==1 || OEMTyp==6 )
 {
   document.getElementById("pm_reactive_power_control").style.display = ""
   if ((SLHW&4096) == 0)
    document.getElementById("reactive_powerb").style.display = ""
  else
    document.getElementById("reactive_powera").style.display = ""

   for(i=0;i<5;i++) 
   {
      if( document.getElementsByName("reactive_power")[i].checked )
      {
        showarea(i)
        break
      }
    }
  }
}
function showarea(nr) {
 if(nr==0) {
   document.getElementById("fix_cos").style.display = ""
   document.getElementById("fix_rap").style.display = "none"
   document.getElementById("var_cos").style.display = "none"
   document.getElementById("var_rap").style.display = "none"
   document.getElementById("control_cos").style.display = "none"
 }
 if(nr==1) {
   document.getElementById("fix_cos").style.display = "none"
   document.getElementById("fix_rap").style.display = ""
   document.getElementById("var_cos").style.display = "none"
   document.getElementById("var_rap").style.display = "none"
   document.getElementById("control_cos").style.display = "none"
 }
 if(nr==2) {
   document.getElementById("fix_cos").style.display = "none"
   document.getElementById("fix_rap").style.display = "none"
   document.getElementById("var_cos").style.display = ""
   document.getElementById("var_rap").style.display = "none"
   document.getElementById("control_cos").style.display = "none"
 }
 if(nr==3) {
   document.getElementById("fix_cos").style.display = "none"
   document.getElementById("fix_rap").style.display = "none"
   document.getElementById("var_cos").style.display = "none"
   document.getElementById("var_rap").style.display = ""
   document.getElementById("control_cos").style.display = "none"
 }
 if(nr==4) {
   document.getElementById("fix_cos").style.display = "none"
   document.getElementById("fix_rap").style.display = "none"
   document.getElementById("var_cos").style.display = "none"
   document.getElementById("var_rap").style.display = "none"
   document.getElementById("control_cos").style.display = ""
   qtyEntries=document.getElementById("qty_entries").value;
   showEntries()
 }
}

function showEntries(){
  var i
  for (i=0;i<qtyEntries;i++){
      document.getElementById("entry"+i).style.display=""
   }
  for (i=qtyEntries;i < max_entry;i++){
      document.getElementById("entry"+i).style.display="none"
    }

  if (qtyEntries == max_entry)
      document.getElementById("addentry").style.display="none"
  else
      document.getElementById("addentry").style.display=""
      
}

function RemoveEntry(entry){
  var qty,i,i1
  var cos1,cos2,cos3,cos4
  //Einträge verschieben
  for(i=entry+1;i<max_entry;i++)
  {
    i1=i+1
    document.getElementsByName("step"+i+"_cos1")[0].checked = document.getElementsByName("step"+i1+"_cos1")[0].checked
    document.getElementsByName("step"+i+"_cos2")[0].checked = document.getElementsByName("step"+i1+"_cos2")[0].checked
    document.getElementsByName("step"+i+"_cos3")[0].checked = document.getElementsByName("step"+i1+"_cos3")[0].checked
    document.getElementsByName("step"+i+"_cos4")[0].checked = document.getElementsByName("step"+i1+"_cos4")[0].checked
    document.getElementById("contr_cos"+i).value = document.getElementById("contr_cos"+i1).value
    document.getElementsByName("under_exc_cos"+i)[0].checked = document.getElementsByName("under_exc_cos"+i1)[0].checked

  }
  // letzten Eintrag loeschen
  document.getElementsByName("step"+qtyEntries+"_cos1")[0].checked = false
  document.getElementsByName("step"+qtyEntries+"_cos2")[0].checked = false
  document.getElementsByName("step"+qtyEntries+"_cos3")[0].checked = false
  document.getElementsByName("step"+qtyEntries+"_cos4")[0].checked = false
  document.getElementById("contr_cos"+qtyEntries).value = "1"
  document.getElementsByName("under_exc_cos"+qtyEntries)[0].checked = false

  qtyEntries--
  qty = document.getElementById("qty_entries");
  qty.value = qtyEntries;
  showEntries()
 }
function AddEntry() {
  var qty
  qtyEntries++
  qty = document.getElementById("qty_entries");
  qty.value = qtyEntries;
  showEntries()
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
                    showSubMenu("16")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_EXPERT# // %#LABEL_PM_TITEL#</h1>
			<form method="post" action="pm_post.html">
				<strong>%#LABEL_PM_MONITORING#</strong><br />
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
				<strong>%#LABEL_PM_INV#</strong><br />
				%#LABEL_PM_INV_NOTE#<br />
                <br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td></td>
						<td>
							<input type="radio" name="iactive" id="iactive1" value="active~" />
							&nbsp;&nbsp;%#LABEL_ACTIVATED#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="radio" name="iactive" id="iactive2" value="inactive~" />
							&nbsp;&nbsp;%#LABEL_DEACTIVATED#
						</td>
					</tr>
				</table>
				<br />
				<strong>%#LABEL_PM_RELAIS_CONF#</strong><br />
				%#LABEL_PM_DESC1# %#LABEL_PM_DESC2#<br />
                <br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_PM_RELAY#</td>
						<td>%#LABEL_PM_C1#</td>
						<td>%#LABEL_PM_C2#</td>
						<td>%#LABEL_PM_C3#</td>
						<td>%#LABEL_PM_C4#</td>
						<td>%#LABEL_PM_POWER#</td>
					</tr>
					<tr>
						<td>%#LABEL_PM_DIGI_IN#</td>
						<td>%#LABEL_PM_DIGI_1#</td>
						<td>%#LABEL_PM_DIGI_2#</td>
						<td>%#LABEL_PM_DIGI_3#</td>
						<td>%#LABEL_PM_DIGI_4#</td>
						<td></td>
					</tr>
					<tr>
						<td>%#LABEL_PM_STEP1#</td>
						<td align="left"><input name="step1_c1" id="step1_c1" size="2" maxlength="1" type="checkbox" value="step1_c~"></td>
						<td align="left"><input name="step1_c2" id="step1_c2" size="2" maxlength="1" type="checkbox" value="step1_c~"></td>
						<td align="left"><input name="step1_c3" id="step1_c3" size="2" maxlength="1" type="checkbox" value="step1_c~"></td>
						<td align="left"><input name="step1_c4" id="step1_c4" size="2" maxlength="1" type="checkbox" value="step1_c~"></td>
						<td><input name="power1" id="power1" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
					</tr>
					<tr>
						<td>%#LABEL_PM_STEP2#</td>
						<td align="left"><input name="step2_c1" id="step2_c1" size="2" maxlength="1" type="checkbox" value="step2_c~"></td>
						<td align="left"><input name="step2_c2" id="step2_c2" size="2" maxlength="1" type="checkbox" value="step2_c~"></td>
						<td align="left"><input name="step2_c3" id="step2_c3" size="2" maxlength="1" type="checkbox" value="step2_c~"></td>
						<td align="left"><input name="step2_c4" id="step2_c4" size="2" maxlength="1" type="checkbox" value="step2_c~"></td>
						<td><input name="power2" id="power2" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
					</tr>
					<tr>
						<td>%#LABEL_PM_STEP3#</td>
						<td align="left"><input name="step3_c1" id="step3_c1" size="2" maxlength="1" type="checkbox" value="step3_c~"></td>
						<td align="left"><input name="step3_c2" id="step3_c2" size="2" maxlength="1" type="checkbox" value="step3_c~"></td>
						<td align="left"><input name="step3_c3" id="step3_c3" size="2" maxlength="1" type="checkbox" value="step3_c~"></td>
						<td align="left"><input name="step3_c4" id="step3_c4" size="2" maxlength="1" type="checkbox" value="step3_c~"></td>
						<td><input name="power3" id="power3" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
					</tr>
					<tr>
						<td>%#LABEL_PM_STEP4#</td>
						<td align="left"><input name="step4_c1" id="step4_c1" size="2" maxlength="1" type="checkbox" value="step4_c~"></td>
						<td align="left"><input name="step4_c2" id="step4_c2" size="2" maxlength="1" type="checkbox" value="step4_c~"></td>
						<td align="left"><input name="step4_c3" id="step4_c3" size="2" maxlength="1" type="checkbox" value="step4_c~"></td>
						<td align="left"><input name="step4_c4" id="step4_c4" size="2" maxlength="1" type="checkbox" value="step4_c~"></td>
						<td><input name="power4" id="power4" size="4" maxlength="3" type="text" class="einzeiligshort" value="%s"></td>
					</tr>
					<tr>
						<td></td>
						<th colspan="3" style="font-weight: normal;">%#LABEL_PM_RELAIS#</th>
						<td align="left"><input name="step4_relais" id="step4_relais" size="2" maxlength="1" type="checkbox" value="step4_r~"></td>
						<td></td>
					</tr>
				</table>
                <br>
				%#LABEL_PM_PWR_CHG#<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_PM_PWR_CHG_PROZ#</td>
						<td><input name="change" id="change" type="text" class="einzeiligshort" maxlength="3" value="%s">&nbsp;&nbsp;% (10-100)</td>
					</tr>
				</table>
                <br>

				<strong>%#LABEL_PM_NETTING#</strong><br />
				%#LABEL_PM_NET_DESC1#&nbsp;%#LOGGER_NAME#&nbsp;%#LABEL_PM_NET_DESC2#<br />
                <br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td align="center">%#LOGGER_NAME#</td>
						<td>%#LABEL_PM_IPADRESS#</td>
					</tr>
					<tr style="display:none" id="a1">
						<td align="center">1</td>
						<td><input name="a1_ip" id="a1_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a2">
						<td align="center">2</td>
						<td><input name="a2_ip" id="a2_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a3">
						<td align="center">3</td>
						<td><input name="a3_ip" id="a3_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a4">
						<td align="center">4</td>
						<td><input name="a4_ip" id="a4_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a5">
						<td align="center">5</td>
						<td><input name="a5_ip" id="a5_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a6">
						<td align="center">6</td>
						<td><input name="a6_ip" id="a6_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a7">
						<td align="center">7</td>
						<td><input name="a7_ip" id="a7_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a8">
						<td align="center">8</td>
						<td><input name="a8_ip" id="a8_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
					<tr style="display:none" id="a9">
						<td align="center">9</td>
						<td><input name="a9_ip" id="a9_ip" size="20" maxlength="19" type="text" class="einzeiligshort" onchange="initbody()" value="%s"></td>
					</tr>
				</table>
				
				<br />
				<div style="display:none">
				<strong>%#LABEL_PM_LOAD_MANAGE#</strong><br />
				%#LABEL_PM_LOAD_MAN_DESC#<br />
            <br>
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td></td>
						<td>
							<input type="radio" name="lmactive" id="lmactive1" value="active~" />
							&nbsp;&nbsp;%#LABEL_ACTIVATED#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="radio" name="lmactive" id="lmactive2" value="inactive~" />
							&nbsp;&nbsp;%#LABEL_DEACTIVATED#
						</td>
					</tr>
				</table>
				<br />
				</div>
    		<div style="display:none" id="pm_reactive_power_control">
				<strong>%#LABEL_PM_REACTIVE_POWER_CONTROL#</strong><br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td><input type="radio" name="reactive_power" id="reactive_power" value="r_0~" onclick="showarea(0)" />
						&nbsp;&nbsp;%#LABEL_PM_FIX_COS_PHI#
						<br /></td>
					</tr>
					<tr style="display:none">
						<td><input type="radio" name="reactive_power" id="reactive_power" value="r_1~" onclick="showarea(1)" />
						&nbsp;&nbsp;%#LABEL_PM_FIX_REACTIVE_POWER#
						</td>
					</tr>
    				<tr>
						<td><input type="radio" name="reactive_power" id="reactive_power" value="r_2~" onclick="showarea(2)" />
						&nbsp;&nbsp;%#LABEL_PM_LINE_COS_PHI#
    				</td>
            </tr>
					<tr style="display:none">
						<td><input type="radio" name="reactive_power" id="reactive_power" value="r_3~" onclick="showarea(3)" />
						&nbsp;&nbsp;%#LABEL_PM_LINE_REACTIVE_POWER#
    				</td>
            </tr>
    				<tr id = "reactive_powera" style="display:none">
						<td><input type="radio" name="reactive_power" id="reactive_power" value="r_4~" onclick="showarea(4)" />
						&nbsp;&nbsp;%#LABEL_PM_CONTR_COS_PHI#&nbsp;&nbsp;&nbsp;&nbsp;
						</td>
    				</tr>
    				<tr id = "reactive_powerb" style="display:none">
						<td style="color:#aaa"><input type="radio" name="reactive_power" id="reactive_power_none" disabled/>
						&nbsp;&nbsp;%#LABEL_PM_CONTR_COS_PHI#&nbsp;&nbsp;&nbsp;&nbsp;%#LABEL_HARDWARE_UPDATE#
						</td>
    				</tr>
				</table>

        <br />
				<div style="display:none" id="fix_cos">
  				%#LABEL_PM_COS_PHI#  
 					<td><input name="cos_phi" id="cos_phi" type="text" size="4" class="einzeiligshort" maxlength="4" value="%s">&nbsp;&nbsp;</td>
 					<td><input type="checkbox" name="under_exc" id="under_exc" value="u~"/>&nbsp;&nbsp;</td>
          %#LABEL_PM_UNDER_EXCITED#
        </div>
				<div style="display:none" id="fix_rap">
  				%#LABEL_PM_REACTIVE_POWER#  
 					<td><input name="rap1" id="rap1" type="text" size="5" class="einzeiligshort" maxlength="8" value="%s">&nbsp;</td>
          %#LABEL_PM_VAR#&nbsp;&nbsp;
 					<td><input type="checkbox" name="under_exc_q" id="under_exc_q" value="u~"/>&nbsp;</td>
          %#LABEL_PM_UNDER_EXCITED#
        </div>
				<div style="display:none" id="var_cos">
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img src="kennlinie_cos.jpg" width="300" height="200">
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_COS_LINE1#
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_COS_LINE2#
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_COS_LINE3#
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
				<tr>
          <td>%#LABEL_PM_FROM# %#LABEL_PM_P_PN#</td>
 					<td><input name="pn1" id="pn1" type="text" size="4" class="einzeiligshort" maxlength="4" value="%s"></td>
 					<td>%#LABEL_PM_COS_PHI# <input name="cos_phi1" id="cos_phi1" type="text" size="4" class="einzeiligshort" maxlength="4" value="%s"></td>
 					<td><input type="checkbox" name="under_exc1" id="under_exc1" value="u1~"/></td>
          <td>%#LABEL_PM_UNDER_EXCITED#</td>
        </tr>
          <br />
          <br />
        <tr>
          <td>%#LABEL_PM_TO# %#LABEL_PM_P_PN#</td>
 					<td><input name="pn2" id="pn2" type="text" size="4" class="einzeiligshort" maxlength="4" value="%s"></td>
 					<td>%#LABEL_PM_COS_PHI# <input name="cos_phi2" id="cos_phi2" type="text" size="4" class="einzeiligshort" maxlength="4" value="%s"></td>
 					<td><input type="checkbox" name="under_exc2" id="under_exc2" value="u2~"/></td>
          <td>%#LABEL_PM_UNDER_EXCITED#</td>
        </tr>
        </table>
        </div>
				<div style="display:none" id="var_rap">
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img src="kennlinie_rap.jpg" width="300" height="200">
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_RAP_LINE1#
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_RAP_LINE2#
          <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        %#LABEL_PM_EXAMPLE_RAP_LINE3#
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
        <tr>
 					<td>%#LABEL_PM_FROM# %#LABEL_PM_ACTIVE_POWER#</td> 
          <td><input name="wl1" id="wl1" type="text" size="5" class="einzeiligshort" maxlength="8" value="%s">&nbsp;&nbsp;W</td>
 					<td>%#LABEL_PM_REACTIVE_POWER#&nbsp;<input name="rap2" id="rap2" type="text" size="5" class="einzeiligshort" maxlength="8" value="%s">&nbsp;%#LABEL_PM_VAR#</td>
 					<td><input type="checkbox" name="under_exc_q1" id="under_exc_q1" value="u1~"/></td>
          <td>%#LABEL_PM_UNDER_EXCITED#</td>
        </tr>
          <br />
          <br />
        <tr>
 					<td>%#LABEL_PM_TO# %#LABEL_PM_ACTIVE_POWER#</td>
          <td><input name="wl2" id="wl2" type="text" size="5" class="einzeiligshort" maxlength="8" value="%s">&nbsp;&nbsp;W</td>
 					<td>%#LABEL_PM_REACTIVE_POWER#&nbsp;<input name="rap3" id="rap3" type="text" size="5" class="einzeiligshort" maxlength="8" value="%s">&nbsp;%#LABEL_PM_VAR#</td>
 					<td><input type="checkbox" name="under_exc_q2" id="under_exc_q2" value="u1~"/></td>
          <td>%#LABEL_PM_UNDER_EXCITED#</td>
        </tr>
        </table>
        </div>
				<div style="display:none" id="control_cos">
        <input name="qty_entries" id="qty_entries" style="display:none" value="%s"">
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_PM_RELAY#</td>
						<td>%#LABEL_PM_C1#</td>
						<td>%#LABEL_PM_C2#</td>
						<td>%#LABEL_PM_C3#</td>
						<td>%#LABEL_PM_C4#</td>
						<td>%#LABEL_PM_COS_PHI#</td>
            <td>%#LABEL_PM_UNDER_EXCITED#</td>
					<tr>
						<td>%#LABEL_PM_DIGI_IN#</td>
						<td>%#LABEL_PM_DIGI_1#</td>
						<td>%#LABEL_PM_DIGI_2#</td>
						<td>%#LABEL_PM_DIGI_3#</td>
						<td>%#LABEL_PM_DIGI_4#</td>
						<td></td>
					</tr>
					<tr style="display:none" id="entry0" >
						<td>%#LABEL_PM_STEP# 1</td>
						<td align="left"><input name="step1_cos1" id="step1_cos1" size="2" maxlength="1" type="checkbox" value="step1_cos1~"></td>
						<td align="left"><input name="step1_cos2" id="step1_cos2" size="2" maxlength="1" type="checkbox" value="step1_cos2~"></td>
						<td align="left"><input name="step1_cos3" id="step1_cos3" size="2" maxlength="1" type="checkbox" value="step1_cos3~"></td>
						<td align="left"><input name="step1_cos4" id="step1_cos4" size="2" maxlength="1" type="checkbox" value="step1_cos4~"></td>
						<td><input name="contr_cos1" id="contr_cos1" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos1" id="under_exc_cos1" value="uc1~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(0)" value="-" /></td>
					</tr>
					<tr style="display:none" id="entry1">
						<td>%#LABEL_PM_STEP# 2</td>
						<td align="left"><input name="step2_cos1" id="step2_cos1" size="2" maxlength="1" type="checkbox" value="step2_cos1~"></td>
						<td align="left"><input name="step2_cos2" id="step2_cos2" size="2" maxlength="1" type="checkbox" value="step2_cos2~"></td>
						<td align="left"><input name="step2_cos3" id="step2_cos3" size="2" maxlength="1" type="checkbox" value="step2_cos3~"></td>
						<td align="left"><input name="step2_cos4" id="step2_cos4" size="2" maxlength="1" type="checkbox" value="step2_cos4~"></td>
						<td><input name="contr_cos2" id="contr_cos2" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos2" id="under_exc_cos2" value="uc2~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(1)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry2">
						<td>%#LABEL_PM_STEP# 3</td>
						<td align="left"><input name="step3_cos1" id="step3_cos1" size="2" maxlength="1" type="checkbox" value="step3_cos1~"></td>
						<td align="left"><input name="step3_cos2" id="step3_cos2" size="2" maxlength="1" type="checkbox" value="step3_cos2~"></td>
						<td align="left"><input name="step3_cos3" id="step3_cos3" size="2" maxlength="1" type="checkbox" value="step3_cos3~"></td>
						<td align="left"><input name="step3_cos4" id="step3_cos4" size="2" maxlength="1" type="checkbox" value="step3_cos4~"></td>
						<td><input name="contr_cos3" id="contr_cos3" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos3" id="under_exc_cos3" value="uc3~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(2)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry3">
						<td>%#LABEL_PM_STEP# 4</td>
						<td align="left"><input name="step4_cos1" id="step4_cos1" size="2" maxlength="1" type="checkbox" value="step4_cos1~"></td>
						<td align="left"><input name="step4_cos2" id="step4_cos2" size="2" maxlength="1" type="checkbox" value="step4_cos2~"></td>
						<td align="left"><input name="step4_cos3" id="step4_cos3" size="2" maxlength="1" type="checkbox" value="step4_cos3~"></td>
						<td align="left"><input name="step4_cos4" id="step4_cos4" size="2" maxlength="1" type="checkbox" value="step4_cos4~"></td>
						<td><input name="contr_cos4" id="contr_cos4" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos4" id="under_exc_cos4" value="uc4~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(3)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry4">
						<td>%#LABEL_PM_STEP# 5</td>
						<td align="left"><input name="step5_cos1" id="step5_cos1" size="2" maxlength="1" type="checkbox" value="step5_cos1~"></td>
						<td align="left"><input name="step5_cos2" id="step5_cos2" size="2" maxlength="1" type="checkbox" value="step5_cos2~"></td>
						<td align="left"><input name="step5_cos3" id="step5_cos3" size="2" maxlength="1" type="checkbox" value="step5_cos3~"></td>
						<td align="left"><input name="step5_cos4" id="step5_cos4" size="2" maxlength="1" type="checkbox" value="step5_cos4~"></td>
						<td><input name="contr_cos5" id="contr_cos5" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos5" id="under_exc_cos5" value="uc5~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(4)" value="-" /></td>
					</tr>
				 	<tr style="display:none"  id="entry5">
						<td>%#LABEL_PM_STEP# 6</td>
						<td align="left"><input name="step6_cos1" id="step6_cos1" size="2" maxlength="1" type="checkbox" value="step6_cos1~"></td>
						<td align="left"><input name="step6_cos2" id="step4_cos2" size="2" maxlength="1" type="checkbox" value="step6_cos2~"></td>
						<td align="left"><input name="step6_cos3" id="step4_cos3" size="2" maxlength="1" type="checkbox" value="step6_cos3~"></td>
						<td align="left"><input name="step6_cos4" id="step4_cos4" size="2" maxlength="1" type="checkbox" value="step6_cos4~"></td>
						<td><input name="contr_cos6" id="contr_cos6" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos6" id="under_exc_cos6" value="uc6~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(5)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry6">
						<td>%#LABEL_PM_STEP# 7</td>
						<td align="left"><input name="step7_cos1" id="step7_cos1" size="2" maxlength="1" type="checkbox" value="step7_cos1~"></td>
						<td align="left"><input name="step7_cos2" id="step7_cos2" size="2" maxlength="1" type="checkbox" value="step7_cos2~"></td>
						<td align="left"><input name="step7_cos3" id="step7_cos3" size="2" maxlength="1" type="checkbox" value="step7_cos3~"></td>
						<td align="left"><input name="step7_cos4" id="step7_cos4" size="2" maxlength="1" type="checkbox" value="step7_cos4~"></td>
						<td><input name="contr_cos7" id="contr_cos7" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos7" id="under_exc_cos7" value="uc7~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(6)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry7">
						<td>%#LABEL_PM_STEP# 8</td>
						<td align="left"><input name="step8_cos1" id="step8_cos1" size="2" maxlength="1" type="checkbox" value="step8_cos1~"></td>
						<td align="left"><input name="step8_cos2" id="step8_cos2" size="2" maxlength="1" type="checkbox" value="step8_cos2~"></td>
						<td align="left"><input name="step8_cos3" id="step8_cos3" size="2" maxlength="1" type="checkbox" value="step8_cos3~"></td>
						<td align="left"><input name="step8_cos4" id="step8_cos4" size="2" maxlength="1" type="checkbox" value="step8_cos4~"></td>
						<td><input name="contr_cos8" id="contr_cos8" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos8" id="under_exc_cos8" value="uc8~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(7)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry8">
						<td>%#LABEL_PM_STEP# 9</td>
						<td align="left"><input name="step9_cos1" id="step9_cos1" size="2" maxlength="1" type="checkbox" value="step9_cos1~"></td>
						<td align="left"><input name="step9_cos2" id="step9_cos2" size="2" maxlength="1" type="checkbox" value="step9_cos2~"></td>
						<td align="left"><input name="step9_cos3" id="step9_cos3" size="2" maxlength="1" type="checkbox" value="step9_cos3~"></td>
						<td align="left"><input name="step9_cos4" id="step9_cos4" size="2" maxlength="1" type="checkbox" value="step9_cos4~"></td>
						<td><input name="contr_cos9" id="contr_cos9" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos9" id="under_exc_cos9" value="uc9~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(8)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry9">
						<td>%#LABEL_PM_STEP# 10</td>
						<td align="left"><input name="step10_cos1" id="step10_cos1" size="2" maxlength="1" type="checkbox" value="step10_cos1~"></td>
						<td align="left"><input name="step10_cos2" id="step10_cos2" size="2" maxlength="1" type="checkbox" value="step10_cos2~"></td>
						<td align="left"><input name="step10_cos3" id="step10_cos3" size="2" maxlength="1" type="checkbox" value="step10_cos3~"></td>
						<td align="left"><input name="step10_cos4" id="step10_cos4" size="2" maxlength="1" type="checkbox" value="step10_cos4~"></td>
						<td><input name="contr_cos10" id="contr_cos10" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos10" id="under_exc_cos10" value="uc10~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(9)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry10">
						<td>%#LABEL_PM_STEP# 11</td>
						<td align="left"><input name="step11_cos1" id="step11_cos1" size="2" maxlength="1" type="checkbox" value="step11_cos1~"></td>
						<td align="left"><input name="step11_cos2" id="step11_cos2" size="2" maxlength="1" type="checkbox" value="step11_cos2~"></td>
						<td align="left"><input name="step11_cos3" id="step11_cos3" size="2" maxlength="1" type="checkbox" value="step11_cos3~"></td>
						<td align="left"><input name="step11_cos4" id="step11_cos4" size="2" maxlength="1" type="checkbox" value="step11_cos4~"></td>
						<td><input name="contr_cos11" id="contr_cos11" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos11" id="under_exc_cos11" value="uc11~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(10)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry11">
						<td>%#LABEL_PM_STEP# 12</td>
						<td align="left"><input name="step12_cos1" id="step12_cos1" size="2" maxlength="1" type="checkbox" value="step12_cos1~"></td>
						<td align="left"><input name="step12_cos2" id="step12_cos2" size="2" maxlength="1" type="checkbox" value="step12_cos2~"></td>
						<td align="left"><input name="step12_cos3" id="step12_cos3" size="2" maxlength="1" type="checkbox" value="step12_cos3~"></td>
						<td align="left"><input name="step12_cos4" id="step12_cos4" size="2" maxlength="1" type="checkbox" value="step12_cos4~"></td>
						<td><input name="contr_cos12" id="contr_cos12" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos12" id="under_exc_cos12" value="uc12~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(11)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry12">
						<td>%#LABEL_PM_STEP# 13</td>
						<td align="left"><input name="step13_cos1" id="step13_cos1" size="2" maxlength="1" type="checkbox" value="step13_cos1~"></td>
						<td align="left"><input name="step13_cos2" id="step13_cos2" size="2" maxlength="1" type="checkbox" value="step13_cos2~"></td>
						<td align="left"><input name="step13_cos3" id="step13_cos3" size="2" maxlength="1" type="checkbox" value="step13_cos3~"></td>
						<td align="left"><input name="step13_cos4" id="step13_cos4" size="2" maxlength="1" type="checkbox" value="step13_cos4~"></td>
						<td><input name="contr_cos13" id="contr_cos13" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos13" id="under_exc_cos13" value="uc13~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(12)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry13">
						<td>%#LABEL_PM_STEP# 14</td>
						<td align="left"><input name="step14_cos1" id="step14_cos1" size="2" maxlength="1" type="checkbox" value="step14_cos1~"></td>
						<td align="left"><input name="step14_cos2" id="step14_cos2" size="2" maxlength="1" type="checkbox" value="step14_cos2~"></td>
						<td align="left"><input name="step14_cos3" id="step14_cos3" size="2" maxlength="1" type="checkbox" value="step14_cos3~"></td>
						<td align="left"><input name="step14_cos4" id="step14_cos4" size="2" maxlength="1" type="checkbox" value="step14_cos4~"></td>
						<td><input name="contr_cos14" id="contr_cos14" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos14" id="under_exc_cos14" value="uc14~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(13)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry14">
						<td>%#LABEL_PM_STEP# 15</td>
						<td align="left"><input name="step15_cos1" id="step15_cos1" size="2" maxlength="1" type="checkbox" value="step15_cos1~"></td>
						<td align="left"><input name="step15_cos2" id="step15_cos2" size="2" maxlength="1" type="checkbox" value="step15_cos2~"></td>
						<td align="left"><input name="step15_cos3" id="step15_cos3" size="2" maxlength="1" type="checkbox" value="step15_cos3~"></td>
						<td align="left"><input name="step15_cos4" id="step15_cos4" size="2" maxlength="1" type="checkbox" value="step15_cos4~"></td>
						<td><input name="contr_cos15" id="contr_cos15" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos15" id="under_exc_cos15" value="uc15~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(14)" value="-" /></td>
					</tr>
					<tr style="display:none"  id="entry15">
						<td>%#LABEL_PM_STEP# 16</td>
						<td align="left"><input name="step16_cos1" id="step16_cos1" size="2" maxlength="1" type="checkbox" value="step16_cos1~"></td>
						<td align="left"><input name="step16_cos2" id="step16_cos2" size="2" maxlength="1" type="checkbox" value="step16_cos2~"></td>
						<td align="left"><input name="step16_cos3" id="step16_cos3" size="2" maxlength="1" type="checkbox" value="step16_cos3~"></td>
						<td align="left"><input name="step16_cos4" id="step16_cos4" size="2" maxlength="1" type="checkbox" value="step16_cos4~"></td>
						<td><input name="contr_cos16" id="contr_cos16" size="4" maxlength="4" type="text" class="einzeiligshort" value="%s"></td>
   					<td><input type="checkbox" name="under_exc_cos16" id="under_exc_cos16" value="uc16~"/></td>
            <td><input type="button" class="button" onClick="RemoveEntry(15)" value="-" /></td>
					</tr>
					<tr style="display:none" id="addentry">
						<td></td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
            <td><input type="button" class="button" onClick="AddEntry()" value="+" /></td>
					</tr>
        </table>
        </div>
        </div>
        

				<br />
				
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
