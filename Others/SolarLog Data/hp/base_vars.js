var Boot=99
var AnlagenKWP=5000
var time_start = new Array(8,8,6,6,6,6,6,7,7,7,7,8)
var time_end = new Array(17,18,20,21,21,22,22,21,20,19,17,17)
var sollMonth = new Array(2,6,9,11,11,13,13,12,10,6,4,3)
var SollYearKWP=890
var AnzahlWR = 7
var MaxWRP=new Array(AnzahlWR)
MaxWRP[0]=new Array(5000,40000,700000,5000000)
MaxWRP[1]=new Array(5300,40000,950000,5500000)
MaxWRP[2]=new Array(3000,20000,500000,3000000)
MaxWRP[3]=new Array(3300,25000,600000,3500000)
MaxWRP[4]=new Array(3300,25000,600000,3500000)
MaxWRP[5]=new Array(3000,20000,500000,3000000)
MaxWRP[6]=new Array(3300,25000,600000,3500000)
var WRInfo = new Array(AnzahlWR)
WRInfo[0]=new Array("SENS0500","      1554",5002,0,"WR 1",1,null,null,0,null,1,1,0,1000,null)
WRInfo[0][14]=new Array(0,0)
WRInfo[1]=new Array("WR50MS09","1100024461",5820,0,"WR 2b",3,null,null,0,null,1,0,0,960,null)
WRInfo[1][6]=new Array("String 1","String 2","String 3")
WRInfo[1][7]=new Array(2,1,1)
WRInfo[1][9]=new Array(1940,1940,1940)
WRInfo[2]=new Array("WR30-005","2000045565",3241,0,"WR 3ab",1,null,null,0,null,1,0,0,960,null)
WRInfo[3]=new Array("WR30-008","2000051199",3601,0,"WR 4",1,null,null,0,null,1,0,0,960,null)
WRInfo[4]=new Array("WR30-008","2000054353",3600,0,"WR 5",1,null,null,0,null,1,0,0,960,null)
WRInfo[5]=new Array("WR30-008","2000067623",3240,0,"WR 6",1,null,null,0,null,1,0,0,960,null)
WRInfo[6]=new Array("WR30-008","2000069376",3600,0,"WR 7",1,null,null,0,null,1,0,0,960,null)
var HPTitel="Solaranlage der Familie ..."
var HPBetreiber="Familie ..."
var HPEmail="eigene_email_adresse"
var HPStandort="99999 Musterort"
var HPModul="28 polykristalline Solarmodule Conergy (Sharp) C160P - 2 Strings"
var HPWR="SMA SunnyBoy 4200 TL"
var HPLeistung="4,48 kWp"
var HPInbetrieb="12.01.2005"
var HPAusricht="S�d-Ost, 40 Grad Dachneigung"
var BannerZeile1="Familie ..."
var BannerZeile2="4,5 kWp in 99999 Musterort"
var BannerZeile3="im Netz seit Januar 2005"
var BannerLink="www.solarlog-home3.de/karwath4"
var StatusCodes = new Array(7)
var FehlerCodes = new Array(7)
StatusCodes[0] = "DATA"
FehlerCodes[0] = "----"
StatusCodes[1] = "Offset,Stop,Netzueb.,Warten,Der. T. WR,Der. T. DC,Riso,Mpp,Stoer.,Fehler,U-Konst,Derating,R12,I-Konst,Mpp Peak,Der. Idc,"
FehlerCodes[1] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,NUW-dI,DC-BFS,EEPROM dBh,ROM,RAM,DC-A def.,DC-B def.,DC-C def.,DCBFS Version,OFFSET,Uac-Bfr,Fac-Bfr,dFac-Bfr,Zac-Bfr,dZac-Bfr,EeRestore,CAN,Varistor,Kom DC-BFS,Riso,EEPROM,Uzwk,dI-Bfr,dI-Mess,Watchdog,Imax DC,MWE Defekt DC,DCBFS-Startup,Rechner,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,Imax,SRR7,dI-Srr,Relais1,Relais2,Relais3,Relais4,SRR13,L-Netz,N-WR,N-Netz,L<->N,NUW-Timeout,HW-Signal,SRR20,SRR21,SRR22,SRR23,Shutdown,UDiff,IGBTs,SRR27,Uzkposneg<10,dI-Test,SRR30,Watchdog Srr,SRR32,"
StatusCodes[2] = "Offset,Stop,Netzueb.,Warten,U-Konst,I-Konst,Mpp-Such,Mpp,Stoer.,Fehler,Mpp-Peak,Derating,Res1,Res2,Res3,Res4,"
FehlerCodes[2] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,K1-Trenn,K2-Trenn,EEPROM dBh,ROM,B1,B2,B3,B4,B5,EeRestore,Teamfehler,ST-REL defekt,Team def.,Iac-DC_Offs-Bfr,OFFSET,EEPROM,Bfr-Srr,K1-Schliess,Watchdog,Uzwk,UpvMax,Riso,dI-Mess,dI,Uac-Bfr,Fac-Bfr,Zac-Bfr,dZac-Bfr,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,Iac-DC_Offs-Srr,Imax,Shut-Down,dI-Srr,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,NUW-Timeout,"
StatusCodes[3] = "Offset,Stop,Netzueb.,Warten,U-Konst,Turbine,Mpp-Such,Mpp,Stoer.,Fehler,Mpp-Peak,Derating,Res1,Res2,Res3,Res4,"
FehlerCodes[3] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,K1-Trenn,K2-Trenn,EEPROM dBh,ROM,B1,B2,B3,Team instabil,Team Konfig,EeRestore,Teamchef Konfig,Team Trennung,Team Kopplung,Iac-DC_Offs-Bfr,OFFSET,EEPROM,Bfr-Srr,K1-Schliess,Watchdog,Uzwk,UpvMax,Riso,dI-Mess,dI,Uac-Bfr,Fac-Bfr,Zac-Bfr,dZac-Bfr,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,Iac-DC_Offs-Srr,Imax,Shut-Down,dI-Srr,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,NUW-Timeout,"
StatusCodes[4] = "Offset,Stop,Netzueb.,Warten,U-Konst,Turbine,Mpp-Such,Mpp,Stoer.,Fehler,Mpp-Peak,Derating,Res1,Res2,Res3,Res4,"
FehlerCodes[4] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,K1-Trenn,K2-Trenn,EEPROM dBh,ROM,B1,B2,B3,Team instabil,Team Konfig,EeRestore,Teamchef Konfig,Team Trennung,Team Kopplung,Iac-DC_Offs-Bfr,OFFSET,EEPROM,Bfr-Srr,K1-Schliess,Watchdog,Uzwk,UpvMax,Riso,dI-Mess,dI,Uac-Bfr,Fac-Bfr,Zac-Bfr,dZac-Bfr,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,Iac-DC_Offs-Srr,Imax,Shut-Down,dI-Srr,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,NUW-Timeout,"
StatusCodes[5] = "Offset,Stop,Netzueb.,Warten,U-Konst,Turbine,Mpp-Such,Mpp,Stoer.,Fehler,Mpp-Peak,Derating,Res1,Res2,Res3,Res4,"
FehlerCodes[5] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,K1-Trenn,K2-Trenn,EEPROM dBh,ROM,B1,B2,B3,Team instabil,Team Konfig,EeRestore,Teamchef Konfig,Team Trennung,Team Kopplung,Iac-DC_Offs-Bfr,OFFSET,EEPROM,Bfr-Srr,K1-Schliess,Watchdog,Uzwk,UpvMax,Riso,dI-Mess,dI,Uac-Bfr,Fac-Bfr,Zac-Bfr,dZac-Bfr,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,Iac-DC_Offs-Srr,Imax,Shut-Down,dI-Srr,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,NUW-Timeout,"
StatusCodes[6] = "Offset,Stop,Netzueb.,Warten,U-Konst,Turbine,Mpp-Such,Mpp,Stoer.,Fehler,Mpp-Peak,Derating,Res1,Res2,Res3,Res4,"
FehlerCodes[6] = "-------,NUW-UAC,NUW-FAC,NUW-ZAC,K1-Trenn,K2-Trenn,EEPROM dBh,ROM,B1,B2,B3,Team instabil,Team Konfig,EeRestore,Teamchef Konfig,Team Trennung,Team Kopplung,Iac-DC_Offs-Bfr,OFFSET,EEPROM,Bfr-Srr,K1-Schliess,Watchdog,Uzwk,UpvMax,Riso,dI-Mess,dI,Uac-Bfr,Fac-Bfr,Zac-Bfr,dZac-Bfr,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,Iac-DC_Offs-Srr,Imax,Shut-Down,dI-Srr,Uac-Srr,Fac-Srr,Zac-Srr,dZac-Srr,NUW-Timeout,"
var Verguetung=4921
var Serialnr =       4711
var Firmware = "1.0.0 Build 7"
var FirmwareDate = "01.11.2007"
var WRTyp = "MULTIPROTOCOL"
var SLTyp = "800"
var SLVer = 2
var Intervall = 300
var SLDatum = "03.11.07"
var SLUhrzeit = "17:22:33"
var isTemp=true
var isOnline=false
var eventsHP=1
var Lang="DE"
var AnlagenGrp=new Array()
AnlagenGrp[0]=new Array("Haus",null,0,0)
AnlagenGrp[0][1]=new Array()
AnlagenGrp[0][1][0]=2
AnlagenGrp[1]=new Array("Garage",null,0,0)
AnlagenGrp[1][1]=new Array()
AnlagenGrp[1][1][0]=3
AnlagenGrp[1][1][1]=5
AnlagenGrp[2]=new Array("Scheune",null,0,0)
AnlagenGrp[2][1]=new Array()
AnlagenGrp[2][1][0]=4
AnlagenGrp[2][1][1]=6
AnlagenGrp[2][1][2]=7
var AnzahlGrp=3