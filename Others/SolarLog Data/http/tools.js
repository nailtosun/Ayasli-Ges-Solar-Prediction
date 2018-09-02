function checkUrl(sUrl) {
 sUrl=rightTrim(leftTrim(sUrl))
 if(sUrl.toLowerCase().substring(0,5)=="http:")
  sUrl=sUrl.substring(5)
 sUrl=replChar(sUrl,"\\","/")
 sUrl=stripFront(sUrl,"/:")
 sUrl=stripBack(sUrl,"/")
 return sUrl
}
function checkDom(sUrl) {
 sUrl=rightTrim(leftTrim(sUrl))
 if(sUrl.toLowerCase().substring(0,5)=="http:")
  sUrl=sUrl.substring(5)
 sUrl=replChar(sUrl,"\\","")
 sUrl=replChar(sUrl,"/","")
 sUrl=stripFront(sUrl,":")
 return sUrl
}
function checkDir(sDir) {
 sDir=rightTrim(leftTrim(sDir))
 sDir=replChar(sDir,"\\","/")
 sDir=stripBack(sDir,"/")
 return sDir
}
function replChar(sString, sChar1, sChar2) {
 while(1) {
  i=sString.indexOf(sChar1)
  if(i>=0)
   sString=sString.substring(0,i)+sChar2+sString.substring(i+1)
  else
   break
  }
  return sString
}
function stripFront(sString, sChars) {
 for(i=0;i<sString.length;i++) {
  i2=sChars.indexOf(sString.substr(i,1))
  if(i2>=0)
    sString=sString.substring(0,i)+sString.substring(i+1)
  else
   break
 }
 return sString
}
function stripBack(sString, sChars) {
 for(i=sString.length-1;i>=0;i--) {
  i2=sChars.indexOf(sString.substr(i,1))
  if(i2>=0)
    sString=sString.substring(0,i)+sString.substring(i+1)
  else
   break
 }
 return sString
}
function leftTrim(sString) {
 while (sString.substring(0,1) == ' ')
 {
  sString = sString.substring(1, sString.length);
 }
 return sString;
}
function rightTrim(sString) {
 while (sString.substring(sString.length-1, sString.length) == ' ')
 {
  sString = sString.substring(0,sString.length-1);
 }
 return sString;
}