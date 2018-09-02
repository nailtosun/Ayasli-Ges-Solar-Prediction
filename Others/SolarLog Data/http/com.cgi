<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><meta http-equiv="content-type" content="text/html; charset=ISO-8859-1"><title>Schnittstellen</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><link rel="stylesheet" type="text/css" href="roh2.css"></head>
<body style="color: rgb(0, 0, 0); background-color: rgb(79, 135, 220);" alink="#dec3a9" link="#3d4548" vlink="#7d653c"><a name="top"></a><table style="width: 730px; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="0" cellspacing="0"><tbody><tr><td rowspan="6" style="background-color: rgb(173, 193, 254);" valign="top" width="150"><p><br><img style="width: 150px; height: 110px;" src="%#COMPANY_LOGO#" alt=""></p><p>&nbsp;</p>
<p align="center"><a href="lan.html"><span style="font-weight: bold;">Lan</span></a><br>
<a href="inverter.html">Wechselrichter</a><br>
<a href="basic.html">Prognose</a><br>
<a href="visual.html">Grafik</a><br>
</p></td><td rowspan="6" width="15">&nbsp;</td>
</tr><tr><td height="5"></td></tr><tr><td style="vertical-align: top; background-color: rgb(173, 193, 254);"><p align="right">| <a href="index.html">Ertragsdaten</a>
| <a href="events.html">Diagnose</a> | <span style="font-weight: bold;">Konfiguration</span>
|&nbsp;&nbsp;<br>
| <span style="font-weight: bold;">Basis</span>
|&nbsp;<a href="homepage.html">Erweitert
</a>| <a href="backup.html">Intern</a>
|&nbsp;&nbsp;</p>
</td></tr><tr><td height="5"></td></tr><tr><td style="padding: 10px; background-color: rgb(173, 193, 254);" valign="top" width="548"><form action="lan_post.html" method="post"><table style="width: 100%;" border="0"><tbody><tr><td width="32%"><div align="left"><b>Wechselrichter</b></div>
</td><td height="10" width="68%"><br></td></tr><tr><td width="32%"><div align="right">RS485-A</div>
</td><td width="68%"><span style="font-family: Arial;"><select name="rs485a^"></select></span></td></tr><tr><td width="32%"><div align="right">RS485/422-B</div>
</td><td width="68%"><span style="font-family: Arial;"><select name="rs485b^"></select></span></td></tr><tr><td width="32%"><b>Internetzugang</b></td><td width="68%">
</td></tr><tr><td></td><td><table style="text-align: left; width: 100%;" border="1" cellpadding="0" cellspacing="0"><tbody><tr><td><input name="active" value="active~" type="radio">Lan</td><td><table style="width: 100%;" border="0"><tbody><tr><td>
<input name="internet" value="i_0~" type="radio">Breitbandzugang
(DSL, Kabel)<br>
<input name="internet" value="i_1~" type="radio">ISDN-Router<br>
<input name="internet" value="i_2~" type="radio">Analog-Modem-Router<br>
<input name="internet" value="i_3~" type="radio">UMTS/GPRS/GSM-Router<br>
</td></tr></tbody></table></td></tr><tr><td><input name="active" value="active~" type="radio">RS232</td><td><input name="internet" value="i_10~" type="radio">Analog-Modem
(Hayes komp.)<br>
<input name="internet" value="i_11~" type="radio">GPRS-Modem
Siemens MC35i</td></tr><tr><td><input name="active" value="active~" type="radio">Kein
Internet</td><td></td></tr></tbody></table></td></tr><tr><td width="32%">
<div align="left"><b>S0-Impulseingang</b></div>
</td><td height="10" width="68%"><br></td></tr><tr><td width="32%"><div align="right">Stromz&auml;hler</div>
</td><td width="68%"><div align="left"><table style="text-align: left; width: 100%;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td><input name="active" value="active~" type="radio"><span style="font-weight: bold;">Aktiviert</span>
</td><td><input name="active" value="inactive~" type="radio"><span style="font-weight: bold;">Deaktiviert</span></td></tr></tbody></table></div></td>
</tr><tr><td width="32%"><div align="right">Impulsfaktor</div>
</td><td width="68%"><div align="left"><input readonly="readonly" name="imp_in" size="7" maxlength="6" value="%s"> / kWh</div></td></tr><tr><td width="32%"></td><td width="68%"></td></tr><tr><td width="32%">
<div align="left"><b>S0-Impulsausgang</b></div>
</td><td height="10" width="68%">(f&uuml;r
Gro&szlig;display)<br></td></tr><tr><td width="32%"><div align="right"><br></div>
</td><td width="68%"><div align="left"><table style="text-align: left; width: 100%;" border="0" cellpadding="2" cellspacing="2"><tbody><tr><td><input name="active" value="active~" type="radio"><span style="font-weight: bold;">Aktiviert</span>
</td><td><input name="active" value="inactive~" type="radio"><span style="font-weight: bold;">Deaktiviert</span></td></tr></tbody></table></div></td></tr><tr><td width="32%"><div align="right">Impulsfaktor</div>
</td><td width="68%"><div align="left"><input readonly="readonly" name="imp_in" size="7" maxlength="6" value="%s">&nbsp;/ kWh</div></td></tr><tr><td></td>
<td></td></tr><tr><td width="32%"></td><td width="68%"><div align="right"><input value=" Speichern" type="submit"> <input value=" Abbrechen" type="reset"></div></td></tr><tr><td align="center"></td><td style="text-align: left;">%s</td>
</tr></tbody></table></form></td></tr><tr><td height="15" width="565">&nbsp;</td>
</tr><tr><td style="background-color: rgb(173, 193, 254);">&nbsp;</td>
<td>&nbsp;</td>
<td style="background-color: rgb(173, 193, 254);" valign="top" width="565"><p align="left">%#COMPANY#
<a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a><br>
&nbsp;</p>
</td></tr></tbody></table></body></html>