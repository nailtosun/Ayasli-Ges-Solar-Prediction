// MENU MANAGEMENT
// functions
function delEntry( entry, search ) {
var i
 for( i=2; i<entry.length; i++ ) {
  if( entry[i]==search ) {
    entry.splice(i,1)
    break
  }
 }
}

// menu structure
var entryID = new Array()
var entryName = new Array()
var entryHtml = new Array()
entryID[0] = "1"
entryName[0] = "%#MENU_LAN#"
entryHtml[0] = "lan.html"
entryID[19] = "20"
entryName[19] = "%#MENU_WLAN#"
entryHtml[19] = "wlan.html"

entryID[1] = "2"
entryName[1] = "%#MENU_GROUPS#"
entryHtml[1] = "group.html"
entryID[14] = "15"
entryName[14] = "%#MENU_SORT#"
entryHtml[14] = "sort.html"
entryID[17] = "18"
entryName[17] = "%#MENU_EXCHANGE#"
entryHtml[17] = "tausch.html"
entryID[2] = "3"
entryName[2] = "%#MENU_INVERTER#"
entryHtml[2] = "inverter.html"
entryID[3] = "4"
entryName[3] = "%#MENU_FORECAST#"
entryHtml[3] = "basic.html"
entryID[4] = "5"
entryName[4] = "%#MENU_GRAPHICS#"
entryHtml[4] = "visual.html"

entryID[5] = "6"
entryName[5] = "%#MENU_INTERNET#"
entryHtml[5] = "homepage.html"
entryID[6] = "7"
entryName[6] = "%#MENU_EMAIL#"
entryHtml[6] = "email.html"
entryID[7] = "8"
entryName[7] = "%#MENU_SMS#"
entryHtml[7] = "sms.html"
entryID[8] = "9"
entryName[8] = "%#MENU_EXPORT#"
entryHtml[8] = "export.html"
entryID[9] = "10"
entryName[9] = "%#MENU_FAILURE#"
entryHtml[9] = "stoerung.html"
entryID[16] = "17"
entryName[16] = "%#MENU_SCB#"
entryHtml[16] = "scb.html"
entryID[15] = "16"
entryName[15] = "%#MENU_PM#"
entryHtml[15] = "pm.html"

entryID[10] = "11"
entryName[10] = "%#MENU_BACKUP#"
entryHtml[10] = "backup.html"
entryID[11] = "12"
entryName[11] = "%#MENU_SYSTEM#"
entryHtml[11] = "system.html"
entryID[12] = "13"
entryName[12] = "%#MENU_UPDATE#"
entryHtml[12] = "firmware.html"

entryID[13] = "14"
entryName[13] = "%#MENU_BEGIN#"
entryHtml[13] = "begin.html"

var mStart=0, mBasic=0, mExpert=1, mInternal=2
var menuEntryCnt = 3
var menuEntry=new Array(menuEntryCnt)
menuEntry[0] = new Array( "%#MENU_BASIC#", "lan.html", "1", "20", "2", "15","18", "3", "4", "5" )
if( OEMTyp==0 || OEMTyp==1 || OEMTyp==6 ) {
    menuEntry[1] = new Array( "%#MENU_EXPERT#", "homepage.html", "6", "9", "7", "8", "10", "17", "16" )
}
else { // alte Darstellung fuer OEMs
    menuEntry[1] = new Array( "%#MENU_EXPERT#", "homepage.html", "6", "7", "8", "9", "10", "17", "16" )
}
menuEntry[2] = new Array( "%#MENU_INTERNAL#", "backup.html", "11", "12", "13" )

// SolarLog500 und vergleichbare: Anlagengruppen entfernen
if( SLTyp==800 || SLTyp==1000 ) {
}
else {
    delEntry(menuEntry[mBasic],"2")
}
// SolarLog200 und vergleichbare: WR-Reihenfolge entfernen
if( SLTyp==200 && OEMTyp!=5 ) {
    delEntry(menuEntry[mBasic],"15")
}
// SolarLog200 (neues Design)
if( OEMTyp==0 && SLBV==22 && SLTyp==200 ) {
    menuEntryCnt++
    menuEntry.unshift( new Array( "%#MENU_START#", "begin.html", "14" ) )
    mBasic=1
    mExpert=2
    mInternal=3
}
if( (SLHW&8192)==0) // WLAN?
{
   delEntry(menuEntry[mBasic],"20")
}

// Kein PowerReducing-PiggyBack? Menuepunkt entfernen
if( (SLHW&1024)==0 ) {
    delEntry(menuEntry[mExpert],"16")
}

// OEM specific
if( OEMTyp==5 && SLBV==1 && (SLTyp==200 || SLTyp==400) ) { // SW ohne Display?
    menuEntryCnt++
    menuEntry.unshift( new Array( "%#MENU_START#", "begin.html", "14" ) )
    mBasic=1
    mExpert=2
    mInternal=3
}
if( OEMTyp!=0 ) // WR-Tausch nur für SDS
{
   delEntry(menuEntry[mBasic],"18")
}
// SCB Dialoge?
if( SCB==false ) {
    // Nein, iSCB entfernen
    delEntry(menuEntry[mExpert],"17")
}

