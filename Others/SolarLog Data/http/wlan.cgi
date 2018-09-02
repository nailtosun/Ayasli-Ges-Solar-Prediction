<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>%#LABEL_WLAN_TITEL#</title>
<link href="style.css" rel="stylesheet" type="text/css" />
<style type="text/css">
	#ProgressBar{padding:5px;font-size:18px;width:200px;text-align:center;left:40%;top:40%;position:absolute;border:2px solid #666;background-color:#FFF;}
#shadow {
    display:none;
    background-color:#000;
    opacity:0.4;
    -moz-opacity:0.4;
    filter:Alpha(opacity=40);
    position:absolute;
    z-index:1;
    top:0px;
    left:0px;
    width:2000px;
    height:1000px;
}
#status {
    display:none;
    background-color:#FFF;
    position:absolute;
    z-index:2;
    top:0px;
    left:0px;
    width:300px;
    padding:15px 20px 15px 20px;
    border-top:1px solid #BBB;
    border-left:1px solid #BBB;
    border-right:1px solid #555;
    border-bottom:1px solid #555;
}
</style>
<script language="JavaScript" src="popup.js"></script>
<script language="JavaScript" src="showsubm.js"></script>
<script language="JavaScript">
var winPC
%b
%s // ssidList wird durch cgifact2 ausgefüllt

document.write("<script type='text/JavaScript' src='lang_"+Lang+".js'><\/script>")
</script>

<script language="JavaScript">

var wrTab=new Array(AnzahlWR)
var cntVisiWR, chooser=0
var fktPtr
var ssid_index=0;
var wlan_Connection=0;
var wlan_SSID="";
var wlan_BSSID="";
var wlan_Encryption="0";
var wlan_Key="";

var wlan_IPDHCP=1;
var wlan_IPAddress="";
var wlan_IPNetmask="";
var wlan_IPGateway="";
var wlan_IPDNS="";
var wlan_DNSUSE=0;
var wlan_AutoSecurity=1;

var selectindex=0;

	
	
	

function SaveCfm(f)
{
	f.submit();
}

function Reset(f)
{
	document.getElementById("SSID").value=wlan_SSID;
	document.getElementById("BSSID").value=wlan_BSSID;
	document.getElementById("KEY").value=wlan_Key;
	
	setEncryption();
	setConnection();
	
	document.getElementById("IPDHCP").value=wlan_IPDHCP;
	document.getElementById("IPADDRESS").value=wlan_IPAddress;
	document.getElementById("IPNETMASK").value=wlan_IPNetmask;
	document.getElementById("IPGATEWAY").value=wlan_IPGateway;
	document.getElementById("IPDNS").value=wlan_IPDNS;
	document.getElementById("DNSUSE").value=wlan_DNSUSE;
	document.getElementById("AutoSecurity").value=wlan_AutoSecurity;

	setEncryption();
	toggleEncryption(wlan_Encryption);
	setConnection();
	setDHCP();
	toggleDHCP();
	toggleDNSUSE();
	setSecurity();
	
	
}

function initbody()
{
	fillInEncryptions();

	// Konfiguration von Logger auslesen
	document.getElementById("statusText").innerHTML = getText(LBL_WLAN_READCONFIG);
	fktPtr=window.setTimeout("wlanIssueRequest('readconfig')", 1000);

    document.getElementById("wlan_einstellungen").style.display='inline';
	document.getElementById("SSIDLISTSELECT").style.display='none';
	document.getElementById("shadow").style.display='inline';
	document.getElementById("status").style.display='inline';
	
	CheckStatus();
	toggleEncryption(wlan_Encryption);
	
}


var ajax = {
  xmlHttp: null,
  userFunc: null,
  
  init: function() {
    if(window.XMLHttpRequest) {
        ajax.xmlHttp = new XMLHttpRequest();
    } else {
        if(window.ActiveXObject) {
            ajax.xmlHttp = new ActiveXObject("Microsoft.XMLHTTP"); 
        }
    }

    if (ajax.xmlHttp == null)
        return false;

    ajax.xmlHttp.onreadystatechange = ajax.processRequest;
    return true;
  },
  
  setUserFunc: function(f) {
    ajax.userFunc = f;
  },
  
  request: function(url) {
    if (ajax.xmlHttp == null)
        ajax.xmlHttp.abort();
    ajax.xmlHttp.onreadystatechange = ajax.processRequest;
    ajax.xmlHttp.open("GET", url+"&random="+(Math.random()*99999),true); // random for IE to stop caching...stupid ie
    ajax.xmlHttp.send(null);
  },
  
  processRequest: function() {

    if (ajax.xmlHttp.readyState == 4 && ajax.xmlHttp.status == 200) {
        returnFunc = ajax.userFunc+"(ajax.xmlHttp.responseText, 1)";
        eval(returnFunc);
    }
    if (ajax.xmlHttp.readyState == 4 && ajax.xmlHttp.status != 200) {
        returnFunc = ajax.userFunc+"('', 0)";
        eval(returnFunc);
    }		
  }  

}

// Anwendungsbeispiel
function wlanIssueRequest(parameter)
{
	var selectindex=document.getElementById("SSIDLISTSELECT").value;

	if(parameter=="init")
	{
		ssidList=new Array();
		ssid_index=0;
		ssidList[ssid_index]="";
		ssid_index++;
	}
//	document.getElementById("statusText").innerHTML = "";


    if (ajax.init())
	{
		if(parameter=="scanconfig")
		{
			document.getElementById("statusText").innerHTML = getText(LBL_WLAN_READDATA);
			document.getElementById("shadow").style.display='inline';
			document.getElementById("status").style.display='inline';
			ajax.setUserFunc("wlanScanBaseSettings_return");
		}
		else if(parameter=="readconfig")
		{
			document.getElementById("statusText").innerHTML = getText(LBL_WLAN_READCONFIG);
			ajax.setUserFunc("wlanReadConfig_return");
		}
		else
		{
			ajax.setUserFunc("wlanScanAvailable_return");
		}
        ajax.request("wlan_params.html?action="+parameter+"&num="+(selectindex-1));
    }
	else
	{
		alert("Fehler bei Ajax-Initialisierung !");
	}
}

function changeSSID()
{
	wlan_AutoSecurity=0;
	setSecurity();
	setEncryption();
	toggleEncryption(wlan_Encryption);
}

function leave(){
      nacherkennung("exit");
}

// Callback function to handle returned configuration data
// 
function wlanReadConfig_return(returnValue)
{
//	alert("Received Configuration: <" + returnValue + ">");
	document.getElementById("shadow").style.display='none';
	document.getElementById("status").style.display='none';
	
	
	var tmpstring;
	var fpos=0;
	var lpos=0;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_Connection= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;
	

	lpos= returnValue.indexOf(";",fpos);
	wlan_Encryption= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;

	
	lpos= returnValue.indexOf(";",fpos);
	wlan_SSID= returnValue.substring(fpos,lpos);
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_Key= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_BSSID= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_IPDHCP= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_IPAddress= returnValue.substring(fpos,lpos);
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_IPNetmask= returnValue.substring(fpos,lpos);
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_IPGateway= returnValue.substring(fpos,lpos);
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_IPDNS= returnValue.substring(fpos,lpos);
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_AutoSecurity= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;

	lpos= returnValue.indexOf(";",fpos);
	wlan_DNSUSE= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;

	document.getElementById("SSID").value=wlan_SSID;
	document.getElementById("BSSID").value=wlan_BSSID;
	document.getElementById("KEY").value=wlan_Key;
	
	
//	alert("wlanDHCP is:"+wlan_IPDHCP);


	document.getElementById("IPADDRESS").value=wlan_IPAddress;
	document.getElementById("IPNETMASK").value=wlan_IPNetmask;
	document.getElementById("IPGATEWAY").value=wlan_IPGateway;
	document.getElementById("IPDNS").value=wlan_IPDNS;
	document.getElementById("DNSUSE").value=wlan_DNSUSE;

	if(wlan_IPDHCP)document.getElementById("IPDHCP").checked="checked";
	else document.getElementById("IPDHCP").checked="";

	if(wlan_DNSUSE)document.getElementById("DNSUSE").checked="checked";
	else document.getElementById("DNSUSE").checked="";

	document.getElementById("AutoSecurity").value=wlan_AutoSecurity;
	if(wlan_AutoSecurity)document.getElementById("AutoSecurity").checked="checked";
	else document.getElementById("AutoSecurity").checked="";
	
	//alert("wlan_Autosecurity is:"+ wlan_AutoSecurity);
	
	
	setConnection();
	
/*	if(wlan_AutoSecurity)
	{
		changeSSID();
	}*/
	
	toggleEncryption(wlan_Encryption);
	setEncryption();
	
	setConnection();
	setDHCP();
	//setSecurity();
	
}

function wlanScanBaseSettings_return(returnValue)
{
//	alert("Received Net Info: <" + returnValue + ">");

	var tmpstring;
	var fpos=0;
	var lpos=0;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_SSID= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_BSSID= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	lpos= returnValue.indexOf(";",fpos);
	wlan_Encryption= parseInt(returnValue.substring(fpos,lpos));
	fpos=lpos+1;
	
//	alert("SSID:" + wlan_SSID);
//  alert("BSSID:" + wlan_BSSID);
//	alert("Encryption: " + wlan_Encryption);

	document.getElementById("shadow").style.display='none';
	document.getElementById("status").style.display='none';


	document.getElementById("SSID").value=wlan_SSID;
	document.getElementById("BSSID").value=wlan_BSSID;
		
	setEncryption();
	toggleEncryption(wlan_Encryption);
	

}

function setConnection()
{
	var conarr=document.getElementsByName("CONNECTION");
	
	for(var i=0;i!=conarr.length;i++)
	{
		conarr[i].checked="";
	}
	
	for(var i=0;i!=conarr.length;i++)
	{
		if( conarr[i].value == wlan_Connection )
		{
			conarr[i].checked="checked";
		}
		else
		{
		}
	}
}


function setEncryption()
{
	var encdiv=document.getElementById("ENCDIV");
	
	if(wlan_AutoSecurity==1)
	{
		encdiv.style.display="none";
	}
	else
	{
		encdiv.style.display="inline";
	}
	
	var Auswahlliste = document.getElementsByName("ENCRYPTION")[0];

	
	if(wlan_Encryption==1 || wlan_Encryption==2)wlan_Encryption=3;

	for(var i=0;i!=6;i++)
	{
		if (Auswahlliste[i].value==wlan_Encryption)
		{
			Auswahlliste[i].selected="selected";
//			alert("Setting selected for entry Nr." + i + ", Enctype="+ wlan_Encryption +"!!!");
		}
		else Auswahlliste[i].selected="";
	}
	
}


function changeEncryption()
{
	var Auswahlliste = document.getElementsByName("ENCRYPTION")[0];
		

	for(var i=0;i!=6;i++)
	{
//		alert("list @" + i +" is "+ Auswahlliste[i].selected)
		if (Auswahlliste[i].selected!=0)
		{
			wlan_Encryption=Auswahlliste[i].value;
			toggleEncryption(wlan_Encryption);
			//alert("Ecryption set to "+ wlan_Encryption +"!");
			break;
		}
	}
}


function wlanScanAvailable_return(returnValue){
    if (returnValue == "eof" || returnValue == "fault" || returnValue=="nomanual")
    {
		clearTimeout(fktPtr);
		if (returnValue == "nomanual")alert("%#LABEL_WLAN_NO_MANUAL#")
		document.getElementById("shadow").style.display='none';
		document.getElementById("status").style.display='none';
		fillInSSIDs();
		document.getElementById("SSIDLISTSELECT").style.display='inline';
     // window.location.href="wlan.html";
    }
    else
    {
		ssidList[ssid_index]=returnValue;
		ssid_index++;
		
        document.getElementById("statusText").innerHTML = returnValue;
        fktPtr=window.setTimeout("wlanIssueRequest('state')", 100);
		//alert("wlanScanAvailable_return: got <" + returnValue + ">")
    }
}

function fillInSSIDs()
{
	//var listholder   = document.getElementById=("SSIDLISTSELECT");
    var Auswahlliste = document.getElementsByName("Auswahl")[0];

	
	while(Auswahlliste.length!=0)
	{
		Auswahlliste[Auswahlliste.length-1]=null;
	}
	//alert("starting to fill in");
	for(var i=0;i!=ssidList.length;i++)
	{
		//alert("filling in <" + ssidList[i] + ">");
		var toption=document.createElement("option");
		toption.text=ssidList[i];
		toption.value=i;
		 var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;

	//	listholder.add(toption,FolgendeOption);
		Auswahlliste.add(toption,FolgendeOption);
	}
	
}

function fillInEncryptions()
{
	var Auswahlliste = document.getElementsByName("ENCRYPTION")[0];

	
	while(Auswahlliste.length!=0)
	{
		Auswahlliste[Auswahlliste.length-1]=null;
	}
	//alert("starting to fill in");

	var toption0=document.createElement("option");
		toption0.text="keine";
		toption0.value=0;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption0,FolgendeOption);

	var toption3=document.createElement("option");
		toption3.text="WEP";
		toption3.value=3;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption3,FolgendeOption);
	
		var toption4=document.createElement("option");
		toption4.text="WPA-AES";
		toption4.value=4;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption4,FolgendeOption);
	
		var toption5=document.createElement("option");
		toption5.text="WPA-TKIP";
		toption5.value=5;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption5,FolgendeOption);
	
		var toption6=document.createElement("option");
		toption6.text="WPA2-AES";
		toption6.value=6;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption6,FolgendeOption);


	var toption7=document.createElement("option");
		toption7.text="WPA2-TKIP";
		toption7.value=7;

		var FolgendeOption = null;
		  if (document.all)
			FolgendeOption = Auswahlliste.length;
	Auswahlliste.add(toption7,FolgendeOption);

	
}

function fillInForms()
{
	selectindex=document.getElementById("SSIDLISTSELECT").value;
	wlanIssueRequest('scanconfig');
	
	
	//document.getElementById("ENCRYPTION").value=wlanEncryption;
}

function go()
{
	document.getElementById("statusText").innerHTML = getText(LBL_WLAN_SEARCHNW);

	wlan_AutoSecurity=1;
	setEncryption();
	setSecurity();
	
	window.setTimeout("wlanIssueRequest('init')",1000);
	//document.getElementById("WLAN_SCAN_BUTTON").style.display='none'
	document.getElementById("shadow").style.display='inline';
	document.getElementById("status").style.display='inline';
	try
	{
		window.scrollTo(0, 0);
	}
	catch(e)
	{
	}
}

function toggleEncryption(new_enc)
{
	var key_div=document.getElementById("KEYDIV");
	
	//alert("Toggling encryption from" + wlan_Encryption + " to "+ new_enc +"!");
		
	wlan_Encryption=new_enc;

	if(wlan_Encryption==1 || wlan_Encryption==2)wlan_Encryption=3;
	
	if(wlan_Encryption==0)
	{
			key_div.style.display='none';
	}
	else
	{
			key_div.style.display='inline';
	}
}

function setDHCP()
{
	var dhcp_cb=document.getElementById("IPDHCP");
	if(wlan_IPDHCP)dhcp_cb.checked="checked";
	else dhcp_cb.checked="";
	
	toggleDHCP();
}

function setSecurity()
{
	//alert("Setting AutoSec to " + wlan_AutoSecurity);
	var sec_cb=document.getElementById("AutoSecurity");
	if(wlan_AutoSecurity)
	{
		sec_cb.checked="checked";
		sec_cb.value=1;
	}
	else 
	{
		sec_cb.checked="";
		sec_cb.value=0;
	}
}


function toggleDHCP()
{
	var dhcp_cb=document.getElementById("IPDHCP");
	
	if(dhcp_cb.checked)
	{
		
		//alert("hiding");
		dhcp_cb.value="1";
		wlan_DHCP=1;
		//ip_div.style.visibility='hidden';
	}
	else
	{
		//alert("showing");
		dhcp_cb.value="0";
		wlan_DHCP=0;
		//ip_div.style.visibility='visible';
	}
	
}

function toggleDNSUSE()
{
	var dns_cb=document.getElementById("DNSUSE");
	
	if(dns_cb.checked)
	{
		//alert("hiding");
		dns_cb.value="1";
		wlan_DNSUSE=1;
		//ip_div.style.visibility='hidden';
	}
	else
	{
		//alert("showing");
		dns_cb.value="0";
		wlan_DNSUSE=0;
		//ip_div.style.visibility='visible';
	}
	
}

function toggleSecurity()
{
//	var encselect=document.getElementById("ENCRYPTION");
	
	
	
}

function CheckStatus()
			{
				var statusframe= document.getElementById("StatusIframe");
				statusframe.src="wlan_status.html";
				
				//if(check_timer!=0)window.clearTimeout(check_timer);
				//check_timer=window.setTimeout("CheckStatus()",5000);
			}

</script>
</head>
<body onLoad="initbody()">
<div id="shadow"></div>
  
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
                    showSubMenu("20")
                </script>
			</ul>
		</div>
		<div id="contentright">
			<div id="ProgressBar" style="display: none;"><br>%#LABEL_PLEASE_WAIT#<br><br><img src="progress-bar.gif"></div>
			<h1>%#MENU_CONFIGURATION# // %#MENU_BASIC# // %#MENU_WLAN#</h1>
<div style="position:relative;">
<div id="status">
    <b>%#MENU_WLAN# - %#MENU_CONFIGURATION#</b><br>
    <br>
    <img src="/working.gif" width="16" height="16" alt="">
    <div id="statusText" style="display:inline; padding-left:10px" >&nbsp;</div>
    <br />
    <br />
		<input type="reset" class="button" onClick="leave()" value="%#LABEL_CANCEL#" />
		<br />
</div>
</div>
			<div id="wlan_einstellungen" style="display:inline">
			
			<form action="wlan_post.html" method="post">
				<strong>%#MENU_WLAN#</strong><br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
				<tr>
						<td></td>
						<td>
							<input type="radio" name="CONNECTION" value=1 checked="checked" />
							&nbsp;&nbsp;%#LABEL_ACTIVATED#
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="radio" name="CONNECTION" value=0 />
							&nbsp;&nbsp;%#LABEL_DEACTIVATED#
						</td>
				</tr>
				<tr>
						<td width="200">%#LABEL_STATUS#</td>
						<td><iframe style="width:190px;height:20px;padding:0px 0px 0px 0px;margin: 0px;border: 1px solid #ababab;" id="StatusIframe"></iframe></td>
				</tr>
				</table>
		        <strong>%#LABEL_WLAN_SELECT#</strong><br />
				<br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">
							<input type ="button" style="display:inline;" name="WLANSCANBUTTON "id="WLAN_SCAN_BUTTON" value="%#LABEL_WLAN_SCANNING#"" onclick="go()">
						</td>
						<td>
							<select name="Auswahl" class="select_einzeilig" size="1" id="SSIDLISTSELECT" style="display:none;width:190px;height:20px;" onchange="fillInForms()"></select><br />
						</td>
					</tr>
					<tr>
						<td width="200">%#LABEL_WLAN_NAME#</td>
						<td><input name="SSID" class="einzeiligshort" type="text" size="32" id="SSID" onkeydown="changeSSID()" onchange="changeSSID()"> </td>
					</tr>
				</table>
				<div id="ENCDIV" style="display:none;">
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_WLAN_ENCRYPTION#</td>
						<td>
							<select name="ENCRYPTION" class="select_einzeilig" size="1" id="ENCRYPTION" style="width:193px;height:20px;" onchange="changeEncryption()"></select><br />
						</td>
					</tr>
				</table>
				</div>
				<div id="KEYDIV">
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_WLAN_KEY#</td>
						<td><input name="KEY" class="einzeiligshort" type="password" type="text" size="32" id="KEY"> </td>
					</tr>
				</table>
				</div>
				<br />
				<br />
				<strong>%#LABEL_LAN_SETTINGS#</strong><br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_DHCP#</td>
						<td>
							<input name="IPDHCP" type="checkbox" size="32" id="IPDHCP" onchange="toggleDHCP()">
						</td>
					</tr>
				</table>
				<div id="IPDIV">
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table">
					<tr>
						<td width="200">%#LABEL_IP_ADR#</td>
						<td><input name="IPADDRESS" class="einzeiligshort" type="text" size="32" id="IPADDRESS"> </td>
					</tr>
					<tr>
						<td width="200">%#LABEL_SUBNET#</td>
						<td><input name="IPNETMASK" class="einzeiligshort" type="text" size="32" id="IPNETMASK"> </td>
					</tr>
					<tr>
						<td width="200">%#LABEL_GATEWAY#</td>
						<td><input name="IPGATEWAY" class="einzeiligshort" type="text" size="32" id="IPGATEWAY"> </td>
					</tr>
					<tr>
							<td>%#LABEL_DNS_SERVER#</td>
							<td><input type="checkbox" name="DNSUSE" id="DNSUSE" onchange="toggleDNSUSE()"/>
								%#LABEL_ACTIVE#&nbsp;&nbsp;&nbsp;
								<input name="IPDNS" size="16" maxlength="15" type="text" class="einzeiligshort" id="IPDNS"  /></td>
					</tr>
				</table>
				</div>
				<br />
				<br />
				<strong style="display:none;">HIDDEN SETTINGS</strong><br />
				<table width="500" border="0" cellspacing="0" cellpadding="0" class="form_table" style="display:none;">
					<tr>
						<td width="200">AutoSecurity</td>
						<td>
							<input name="AutoSecurity" type="checkbox" size="32" id="AutoSecurity">
						</td>
					</tr>
					<tr> 
						<td width="200">BSSID</td>
						<td><input name="BSSID" class="einzeiligshort" type="text" size="32" id="BSSID"> </td>
					</tr>
				</table>
				<br />
				<br />
				<input type="button" class="button" onClick="SaveCfm(this.form)" value="%#LABEL_SAVE#" />
				&nbsp;&nbsp;
				<input type="reset" class="button" onClick="Reset(this.form)" value="%#LABEL_CANCEL#" />
				<br /><br />
			</form>
			</div>
		</div>
		<div style="clear: left;"></div>
	</div>
	<div id="footer">
		%#COMPANY# | <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
	</div>
</div>
</body>
</html>
