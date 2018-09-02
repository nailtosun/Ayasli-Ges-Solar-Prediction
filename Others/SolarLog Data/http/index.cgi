<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#INDEX_TITLE# %#LOGGER_NAME#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
if( SCB==true ) {
   // reload config for SCB if active
  var sc=new Array(), isc=0
  document.write("<script language='JavaScript' src='scb_vars.js?cur=1'><\/script>")
}
// Number inverters/meters/sensors
var numInv=0, numMeter=0, numSensor=0
for( i=0; i<AnzahlWR; i++ ) {
  if( WRInfo[i][11]==0 )
    numInv++
  else if( WRInfo[i][11]==1 )
    numSensor++
  else if( WRInfo[i][11]==2 )
    numMeter++
}
//
function visuPC(f){
        if( AnzahlWR>0 ) {
                winPC=window.open('index_pc.html','fenster3','left=0,top=0,width=1060,height=650,location=yes,resizable=yes')
                winPC.focus()
        }
        else
                alert("%#NO_YIELD_DATA#")
}
function visuPalm(f){
        if( AnzahlWR>0 ) {
                winPALM=window.open('palm.html','fenster4','width=321,height=290,toolbar=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no')
                winPALM.focus()
        }
        else
                alert("%#NO_YIELD_DATA#")
}
function visuDCF(f){
        winDCF=window.open('dcf.html','fenster5','width=230,height=100,toolbar=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no')
        winDCF.focus()
}
function getHWOption(){
  var s=""
  if( SLHW&1024 ) s=s+"PM"
  if( SLHW&4096 ) s=s+"+"
  if( SLHW&16384 ) s=s+(s==""?"":"/")+"GPRS"
  if( SLHW&8192 ) s=s+(s==""?"":"/")+"Wifi"
  if( SLHW&512 ) s=s+(s==""?"":"/")+"BT"
  return s
}
</script>
<script language="JavaScript">
function visuSCB(f){
   // count SCBs
   var i, cnt=0
   if( SCBActive==true ) {
      for( i=0; i<SCBInfo.length; i++ ) {
         if( SCBInfo[i][0]==1 )
            cnt++
      }
   }
        if( cnt>0 ) {
                winSCB=window.open('scb_mon.html','fenster6','width=900,height=600,toolbar=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes')
                winSCB.focus()
        }
        else
                alert("%#LABEL_SCB_NO_DATA#")
}
</script>

</head>
<body>
<div id="rap">
        <div id="inhalt">
                <div id="head">
                        <div id="logo"><img src="%#COMPANY_LOGO#"></div>
                        <div id="headright">
                                <table cellpadding="0" cellspacing="0" border="0" class="menu">
                                        <tr>
                                                <td align="center" valign="middle" class="act"><a href="index.html">%#MENU_YIELD_DATA#</a></td>
                                                <td align="center" valign="middle" class="in-act"><a href="events.html">%#MENU_DIAGNOSIS#</a></td>
                        <script language="JavaScript" src="menu.js"></script>
                        <script language="JavaScript">
                            showMainMenuConfig(false, "%#MENU_CONFIGURATION#" )
                        </script>
                                                <td height="30" align="center" valign="middle" class="in-act">&nbsp;</td>
                                        </tr>
                                </table>
                        </div>
                        <div style="clear: left;"></div>
                </div>
                <div id="contentleft">
                        <ul class="submenu">
                                <li><a href="javascript:visuPC()">%#VISU_PC#</a></li>
                                <li><a href="javascript:visuPalm()">%#VISU_PDA#</a></li>
                                <script language="JavaScript">
                     if( SCB==true ) {
                        document.write("<li><a href='javascript:visuSCB()'>%#VISU_SCB#</a></li>")
                     }
                                </script>
                        </ul>
                </div>
                <div id="contentright">
                        <h1>%#LABEL_WELCOME# %#LOGGER_FORMAT#<sup>%#LOGGER_FORMAT2# <script language="JavaScript">document.write(getHWOption())</script></sup></h1>
                        <p><br>%#LABEL_MENU_NAVIG#</p>
                        <script language="JavaScript">
                        if(isOnline!=0) {
                                document.write("<br>%#LOGGER_FORMAT# %#LABEL_LOGGING_DATA#<br>")
                        }
                        </script>
            <br>
            <h2>%#LABEL_MORE_INFO#</h2>
                        <script language="JavaScript">
                                var msg=""
                                if( AnzahlWR==0 ) {
                                        if( Boot==1 )
                                                msg="%#MSG_READING_SYSTIME#"
                                        document.write("<br><br><p style='font-weight:bold; background-color: rgb(255,255,102);'>"+msg+"</p>")
                                }
                        </script>
            <div style="float: left; width: 420px;">
              <table width="380" border="0" cellspacing="0" cellpadding="0" class="std_table">
                <tr>
                  <td>%#LABEL_NUM_INV#</td>
                  <td>
                  <script language="JavaScript">
                      if( numInv==0 )
                          document.write( "%#LABEL_NO_INVERTERS#" )
                      else
                          document.write( numInv )
                  </script>
                  </td>
                </tr>
                <tr style="display:none" id="meter">
                  <td>%#LABEL_NUM_METER#</td>
                  <td>
                  <script language="JavaScript">
                     document.write( numMeter )
                  </script>
                  </td>
                </tr>
                <tr style="display:none" id="sensor">
                  <td>%#LABEL_NUM_SENSOR#</td>
                  <td>
                  <script language="JavaScript">
                     document.write( numSensor )
                  </script>
                  </td>
                </tr>
                <script language="JavaScript">
                  if( numMeter>0 )
                     document.getElementById("meter").style.display = ""
                  if( numSensor>0 )
                     document.getElementById("sensor").style.display = ""
                </script>
                <tr>
                  <td>%#LABEL_PLANT_SIZE#</td>
                  <td>
                  <script language="JavaScript">
                     document.write( Math.floor((AnzahlWR!=0?AnlagenKWP:0)/100)/10 + " kWp" )
                  </script>
                                  </td>
                </tr>
                <tr>
                  <td width="150">%#LABEL_FIRMWARE#</td>
                  <td>
                  <script language="JavaScript">
                     document.write( Firmware + " - " + FirmwareDate )
                  </script>
                                  </td>
                </tr>
                <tr>
                  <td>%#LABEL_SERIALNUM#</td>
                  <td>
                  <script language="JavaScript">
                     document.write( Serialnr )
                  </script>
                                  </td>
                </tr>
              </table>
            </div>

            <div style="clear: left;"> </div>

                </div>
                <div style="clear: left;"></div>
        </div>
        <div id="footer">
                %#COMPANY# | <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
        </div>
</div>
</body>
</html>