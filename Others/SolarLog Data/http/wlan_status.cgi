<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<script language="JavaScript">
%b
%s // ssidList wird durch cgifact2 ausgefüllt


document.write("<script type='text/JavaScript' src='lang_"+Lang+".js'><\/script>")
</script>

<script language="JavaScript">
var check_timer=0;	// Timer um den Wlan-Status periodisch zu überprüfen
var wlan_RSSI=0;



function initbody()
{
	// Konfiguration von Logger auslesen
	document.body.style.backgroundColor = "#0000ff";
	wlanIssueRequest('init');
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
	if(parameter=="init")
	{
	}
//	document.getElementById("statusText").innerHTML = "";


    if (ajax.init())
	{
		ajax.setUserFunc("wlanCheckStatus_return");
        ajax.request("wlan_status1.html?q=none");
    }
	else
	{
		alert("Fehler bei Ajax-Initialisierung !");
	}
	
	if(check_timer!=0)window.clearTimeout(check_timer);
    
}


function wlanCheckStatus_return(returnValue)
{
	//alert("Returned <"+ returnValue +">");
	var stattext= document.getElementById("StatusText");
	
	var fpos=0;
	var lpos=0;
	
	lpos= returnValue.indexOf(";",fpos);
	var retstat= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	lpos= returnValue.indexOf(";",fpos);
	var retrssitext= returnValue.substring(fpos,lpos);
	fpos=lpos+1;
	
	var retrssi=parseInt(retrssitext);
	wlan_RSSI=retrssi;
	
	//alert("Status is <" + retstat +"> rssi is <"+ retrssi + ">");
	
	if(retstat=="0")
		{
			document.body.style.backgroundColor = "#aaaaFF";
			stattext.innerHTML=getText(LBL_WLAN_INITIALIZING);
		}
	else if(retstat=="1")
		{
			document.body.style.backgroundColor = "#777777";
			stattext.innerHTML=getText(LBL_WLAN_DEACTIVATED);
		}
	else if(retstat=="2")
		{
			document.body.style.backgroundColor = "#FFaaaa";
			stattext.innerHTML=getText(LBL_WLAN_NOTCONNECTED);
		}
	else if(retstat=="3")
		{
			document.body.style.backgroundColor = "#99dd99";
			stattext.innerHTML=getText(LBL_WLAN_CONNECTED) +" (" + retrssi + "%)";
		}
	else if(retstat=="4")
		{
			document.body.style.backgroundColor = "#ddddAA";
			stattext.innerHTML=getText(LBL_WLAN_CONNECTING);
		}
	else
		{
			document.body.style.backgroundColor = "#FFaaFF";
			stattext.innerHTML=getText(LBL_WLAN_SLOFFLINE);
		}
	
	
	
	check_timer=window.setTimeout("wlanIssueRequest('init')",1000);
/*    if (returnValue == "0")
    {
		document.body.style.backgroundColor = "#FF0000";
    }
    else
    {
		document.body.style.backgroundColor = "#00FF00"; 
    }*/
}

</script>
</head>
<body onLoad="initbody()"  style="padding:0px 0px 0px 0px;margin: 2px 0px 0px 4px;font-family: Arial, Helvetica, sans-serif; font-size: 11px; line-height: 16px; color: #524d4d;">
<span id="StatusText">Test</span><br>
</body>
</html>
