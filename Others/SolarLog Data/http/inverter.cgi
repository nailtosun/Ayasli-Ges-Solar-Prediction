<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_CONFIG_INV#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
%b
function calcSkal( obj ) {
var v, leistung=obj.generator.value
v=Math.floor((leistung*0.9)/100+0.5)*100+100
obj.maxy_1.value=v
v=Math.floor((leistung*6.5)/5000+0.5)*5000
obj.maxy_2.value=v/1000
v=Math.floor((leistung*6.5*31*.8)/50000+0.5)*50000
obj.maxy_3.value=v/1000
v=Math.floor((leistung*6.5*365*.4)/500000+0.5)*500000
obj.maxy_4.value=v/1000
}
var meterActive = new Array(2)
function initbody() {

// Bei IEC870 müssen die Schlüssel zum Auslesen erscheinen
 	if (document.getElementsByName("WRType")[0].value == "31") // 31 = Landis+Gyr / IEC60870
	{
		document.getElementById("IECkeys").style.display = ""
	}

  if (document.getElementsByName("WRType")[0].value=="21") // M&T Sensor
  {
    document.getElementById("SensorDates").style.display=""
  }
  
	if (document.getElementsByName("WRFunc")[0].value == "3") // 3 = Eigenstromzähler
	{
		document.getElementById("AdrSn").style.display = "none"
		document.getElementById("AdrBezug").style.display = ""
		document.getElementById("AdrProduktion").style.display = ""

		document.getElementById("Monitoring").style.display = "none"
		document.getElementById("Table_modules").style.display = "none"
	}

// 
 	if (document.getElementsByName("WRType")[0].value == "31") // 31 = Landis+Gyr / IEC60870
	{
		document.getElementById("Monitoring").style.display = "none"
		document.getElementById("Table_modules").style.display = "none"
	}
 	if (document.getElementsByName("WRType")[0].value == "9") // 9 = S0
	{
		meterActive[0] = document.getElementsByName("active")[0].checked	// Zustand 'Active-Monitoring' merken beim allerersten Aufruf
		meterActive[1] = document.getElementsByName("active")[1].checked
		for( i=0;i<3; i++ ) {
			if( document.getElementsByName("meter_type")[i].checked ) {
				break
			}
		}
		shows0(i)
	}
}
function shows0( typ ) {
		if( document.getElementsByName("meter_type")[0].checked ) {
			document.getElementsByName("active")[0].checked = meterActive[0]
			document.getElementsByName("active")[1].checked = meterActive[1]
			document.getElementById("Monitoring").style.display = ""
		}
		else {
			document.getElementsByName("active")[0].checked = false
			document.getElementsByName("active")[1].checked = true
			document.getElementById("Monitoring").style.display = "none"
		}
		document.getElementById("Table_modules").style.display = "none"
		document.getElementById("Radio_S0").style.display = ""
		document.getElementById("Modul_S0").style.display = ""
		document.getElementById("Impuls_S0").style.display = ""
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
                    showSubMenu("3")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_INVERTER#</h1>
			<form method="post" action="inverter_post.html">
				<strong>%#LABEL_INV#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_NUMBER#</td>
							<td>
								<select name="nummer" id="idnummer" class="select_einzeilig" onChange="window.location.href='inverter.html?'+this.form.nummer.options.selectedIndex^"></select>
                                <div id="NewNumber" style="display: none;">
								&nbsp;&nbsp;&nbsp;%#LABEL_NEW_NUMBER#&nbsp;<input type="text" class="einzeiligshort" size="3" disabled="disabled" name="neunr" maxlength="2" value="%s">
								<script language="JavaScript">
									//wrtyp= WRInfo[document.getElementById("idnummer").options.selectedIndex][10]
									//if((wrtyp==1 || wrtyp==6 || wrtyp==16 || wrtyp==18 || wrtyp==19)&&AnzahlWR>1)
									//document.getElementsByName("neunr")[0].disabled=false
								</script>
                                </div>
							</td>
					</tr>
					<tr>
						<td>%#LABEL_DEVICE_NAME#</td>
						<td><input name="geraet" id="geraet" type="text" class="einzeiligshort" value="%s" disabled="disabled" readonly="readonly" /></td>
					</tr>
					<tr id="AdrSn">
						<td>%#LABEL_ADR_SN#</td>
						<td><input name="serial" id="serial" type="text" class="einzeiligshort" value="%s" disabled="disabled" readonly="readonly" /></td>
					</tr>
					<tr id="AdrBezug" style="display: none;">
						<td>%#LABEL_METER_ADDR_FEEDIN#</td>
						<td><input name="serialBezug" id="serialBezug" type="text" class="einzeiligshort" value="%s" disabled="disabled" readonly="readonly" /></td>
					</tr>
					<tr  id="AdrProduktion" style="display: none;">
						<td>%#LABEL_METER_ADDR_PRODUCE#</td>
						<td><input name="serialProduktion" id="serialProduktion" type="text" class="einzeiligshort" value="%s" disabled="disabled" readonly="readonly" /></td>
					</tr>
					
					<tr>
						<td>%#LABEL_INST_DC_POWER#</td>
						<td>
							<input name="generator" maxlength="7" id="generator" type="text" class="einzeiligshort" value="%s" onChange="calcSkal(this.form)" />
							&nbsp;&nbsp;Wp
						</td>
					</tr>
					<tr>
						<td>%#LABEL_PAC_CORR_FACTOR#</td>
						<td>
							<input name="korrektur" maxlength="6" id="korrektur" type="text" class="einzeiligshort" value="%s" />
							&nbsp;(%#LABEL_CORR_FACT_INFO#)
						</td>
					</tr>
					<tr>
						<td>%#LABEL_DESC#</td>
						<td><input name="bez" maxlength="19" id="bez" type="text" class="einzeilig" value="%s" /></td>
					</tr>
               <script language="JavaScript">
                  if( (SLHW&1024)!=0 ) {
                     document.write("<tr>")
                     document.write("<td>%#LABEL_PM_WHICH_PHASE#</td>")
                     document.write("<td><input name='phasegroup' maxlength='2' id='phasegroup' type='text' class='einzeiligshort' value='%s' />")
                     document.write("&nbsp;%#LABEL_PM_WHICH_PHASE2#</td>")
                     document.write("</tr>")
                  }
               </script>
					
					<!-- Modulfeld: wird bei S0 in abgespeckter Form angezeigt -->
					<tr id="Modul_S0" style="display: none;">
						<td>%#LABEL_MODULFIELD#</td>
						<td><input name="modulfield" id="modulfield" type="text" class="einzeiligshort" value="%s" /></td>
					</tr>
					<tr id="Impuls_S0" style="display: none;">
						<td>%#LABEL_IMPULSFACTOR#</td>
						<td><input name="impuls" id="impuls" type="text" class="einzeiligshort" value="%s"/></td>
					</tr>
				</table>
				<div id="Radio_S0" style="display: none;">
				<br />
				<br />
				<strong>%#LABEL_DIGITAL_COUNTER_AVAIL#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_ENERGY_METER_INV#</td>
						<td><input type="radio" name="meter_type" id="meter_type" onclick="shows0(0)" value="i_0~" /></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_ENERGY_METER_YIELD#</td>
						<td><input type="radio" name="meter_type" id="meter_type" onclick="shows0(1)" value="i_1~" /></td>
					</tr>
					<tr>
						<td width="200">%#LABEL_ENERGY_METER_USAGE#</td>
						<td><input type="radio" name="meter_type" id="meter_type" onclick="shows0(2)" value="i_2~" /></td>
					</tr>
				</table>
				
				</div>
				<table id="Table_modules" width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td></td>
						<td>%#LABEL_MODUL#<br />%#LABEL_FIELD#</td>
						<td>%#LABEL_CONNECTED#<br />%#LABEL_DC_POWER#</td>
						<td>%#LABEL_DESC#<br />&nbsp;</td>
					</tr>
					<tr>
						<td>%#LABEL_INV_SHORT#</td>
						<td><input name="feld_wr" maxlength="2" id="feld_wr" type="text" class="einzeilig" value="%s^" size="5" /></td>
						<td></td>
						<td></td>
					</tr>
					<tr>
						<td>%#LABEL_MPP1#</td>
						<td><input name="felds1" maxlength="1" id="felds1" type="text" class="einzeilig" value="%s^" size="5" /></td>
						<td><input name="generators1" maxlength="6" id="generators1" type="text" class="einzeilig" value="%s^" size="9" /></td>
						<td><input name="bezs1" maxlength="19" id="bezs1" type="text" class="einzeilig" value="%s^" /></td>
					</tr>
					<tr>
						<td>%#LABEL_MPP2#</td>
						<td><input name="felds2" maxlength="1" id="felds2" type="text" class="einzeilig" value="%s^" size="5" /></td>
						<td><input name="generators2" maxlength="6" id="generators2" type="text" class="einzeilig" value="%s^" size="9" /></td>
						<td><input name="bezs2" maxlength="19" id="bezs2" type="text" class="einzeilig" value="%s^" /></td>
					</tr>
					<tr>
						<td>%#LABEL_MPP3#</td>
						<td><input name="felds3" maxlength="1" id="felds3" type="text" class="einzeilig" value="%s^" size="5" /></td>
						<td><input name="generators3" maxlength="6" id="generators3" type="text" class="einzeilig" value="%s^" size="9" /></td>
						<td><input name="bezs3" maxlength="19" id="bezs3" type="text" class="einzeilig" value="%s^" /></td>
					</tr>
				</table>

        <div id="SensorDates" style="display: none;">
        <br />
        <br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
					    <td width="250">%#LABEL_SENSOR_OUTSIDE_TEMP#</td>
						  <td><input type="checkbox" name="sensorbox_tmp" id="sensorbox_tmp" value="sens_tmp~" /></td>
					</tr>
					<tr>
					    <td width="250">%#LABEL_SENSOR_WIND#</td>
						  <td><input type="checkbox" name="sensorbox_wind" id="sensorbox_wind" value="sens_wind~" /></td>
					</tr>
				</table>
        </div>
        
				<!-- Schlüssel für IEC870 standardmäßig erstmal aus -->
				<div id="IECkeys" style="display: none;">
				<br />
				<br />
				<strong>%#LABEL_ACCESS_KEY#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table" id="accesskey">
					<tr>
						<td>%#LABEL_ACCESS_KEY_I#</td>
						<td><input name="ieckey1" maxlength="9" id="ieckey1" type="text" class="einzeilig" value="%s^" size="9" /></td>
					</tr>
					<tr id="IECkey2" style="display: none;">
						<td>%#LABEL_ACCESS_KEY_II#</td>
						<td><input name="ieckey2" maxlength="9" id="ieckey2" type="text" class="einzeilig" value="%s^" size="9" /></td>
					</tr>
					<tr>
						<td>%#LABEL_ACCESS_KEY_III#</td>
						<td><input name="ieckey3" maxlength="9" id="ieckey3" type="text" class="einzeilig" value="%s^" size="9" /></td>
					</tr>
					<tr>
						<td>%#LABEL_ACCESS_KEY_CUR#</td>
						<td><input name="ieckeycur" maxlength="9" id="ieckeycur" type="text" class="einzeilig" value="%s^" size="9" /></td>
					</tr>
				</table>
				</div>



				<div id="Monitoring" style="display:">
				<br />
				<br />
				<strong>%#LABEL_MONITORING#</strong> (%#LABEL_MONI_INFO#)<br />
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
					<tr>
						<td></td>
						<td>
							%#LABEL_NO_SHADOW#&nbsp;<input name="unv_von" maxlength="5" id="unv_von" type="text" class="einzeiligshort" size="5" value="%s">
							&nbsp;&nbsp;
							%#LABEL_UNTIL#&nbsp;<input name="unv_bis" maxlength="5" id="unv_bis" type="text" class="einzeiligshort" size="5" value="%s">
							&nbsp;%#LABEL_CLOCK#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_MIN_POWER#&nbsp;<input name="pacmin" maxlength="2" id="pacmin" type="text" class="einzeiligshort" size="2" value="%s">
							&nbsp;%&nbsp;%#LABEL_OF_DC_POWER#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_MSG_AS_EMAIL#&nbsp;&nbsp;<input name="email" id="email" value="email~" type="checkbox">
							&nbsp;&nbsp;&nbsp;&nbsp;
							%#LABEL_SMS#&nbsp;&nbsp;<input name="sms" id="sms" value="sms~" type="checkbox">
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_FROM#&nbsp;<input name="abw" maxlength="2" id="abw" type="text" class="einzeiligshort" size="2" value="%s">
							&nbsp;%&nbsp;%#LABEL_DIFF#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_PERIOD_ERR#&nbsp;<input name="dauer" maxlength="2" id="dauer" type="text" class="einzeiligshort" size="2" value="%s">
							&nbsp;%#LABEL_MINUTE#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_MAXIMUM#&nbsp;<input name="anzahl" id="anzahl" size="2" maxlength="2" type="text" class="einzeiligshort" value="%s">
							&nbsp;%#LABEL_MAX_MSG_DAY#
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							%#LABEL_IS_SNOW#<br />
							<input name="schnee" id="schnee" value="ja~" type="radio">&nbsp;&nbsp;%#LABEL_YES#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input name="schnee" id="schnee" value="nein~" type="radio">&nbsp;&nbsp;%#LABEL_NO#
						</td>
					</tr>
				</table>
				</div>
				<br />
				<br />
				<strong>%#LABEL_SCALE#</strong><br />
				<br />
				%#LABEL_DEFINITION#<br />%#LABEL_YSCALE#<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td>%#LABEL_VIEW_FOR#<br />&nbsp;</td>
						<td>%#LABEL_DAY#<br />W</td>
						<td>%#LABEL_MONTH#<br />kWh</td>
						<td>%#LABEL_YEAR#<br />kWh</td>
						<td>%#LABEL_ALLYEARS#<br />kWh</td>
					</tr>
					<tr>
						<td>%#LABEL_MAX_YSCALE#</td>
						<td><input name="maxy_1" id="maxy_1" type="text" class="einzeilig" size="7" maxlength="7" value="%s"></td>
						<td><input name="maxy_2" id="maxy_2" type="text" class="einzeilig" size="7" maxlength="7" value="%s"></td>
						<td><input name="maxy_3" id="maxy_3" type="text" class="einzeilig" size="7" maxlength="7" value="%s"></td>
						<td><input name="maxy_4" id="maxy_4" type="text" class="einzeilig" size="7" maxlength="7" value="%s"></td>
					</tr>
				</table>
				<br><br>
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
	<div id="hiddendata" style="display: none;">
	<input name="WRType" maxlength="2" id="WRType" type="text" class="einzeilig" value="%s^" size="5" />
	<input name="WRFunc" maxlength="2" id="WRFunc" type="text" class="einzeilig" value="%s^" size="5" />
	</div>
</div>
</body>
</html>
