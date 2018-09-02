<!DOCTYPE HTML PUBLIC"-// W3C//DTD HTML 4.01 Transitional//EN">
<html>
   <head>
      <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
      <title>%#TITEL_LOGIN#
      </title>
      <link href="style.css" rel="stylesheet" type="text/css"/>
<script language="JavaScript">
function buildCode() {
 var numLang=%s
 // insert "Var" Code
 // var chooseLang=new Array("Sprache Wählen",...)
 // var lang=new Array("deutsch",...)
 %s
 var i, code="", label, spaces="                    "
 // build code for choosing languages dynamically
 for( i=0; i<numLang; i++ ) {
  code+="<tr>"
  code+="<td width='30%'>"
  code+="<div align='left'>"+chooseLang[i]+"</div>"
  code+="</td>"
  code+="<td width='70%'>"
  code+="<div align='left'>"
  label="  "+lang[i]+"  "
  code+="<input value=' "+label+"' type='button' onclick='window.location.href=\"index.html?lang="+(i+1)+"\"'>"
  code+="</div>"
  code+="</td>"
  code+="</tr>"
 }
 return code
}
</script>
   </head>
   <body style="color: rgb(0, 0, 0);" alink="#dec3a9" link="#3d4548" vlink="#7d653c">
      <a name="top">
      </a>
      <table style="width: 730px; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="0" cellspacing="0">

         <tbody>
            <tr>
               <td rowspan="3" style="" valign="top" width="150">
                  <p>
                     <img style="width: 150px; height: 110px;" src="%#COMPANY_LOGO#" alt="">
                  </p>
                  <p>&nbsp;
                  </p>
                  <p align="center">
                     <a href="login.html">
                        <span style="font-weight: bold;">
                        </span>
                     </a>
                     <br>
                  </p>
               </td>
               <td rowspan="3" width="15">&nbsp;
               </td>
            </tr>
            <tr>
               <td style="padding: 10px; " valign="top" width="548">
                  <form action="login_post.html" method="post">
                     <table style="width: 100%;" border="0">
                        <tbody>
                           <tr>
                              <td width="30%">
                                 <div align="left">
                                    <h1>%#LOGGER_FORMAT#<sup>%#LOGGER_FORMAT2#</sup></h1>

                                    <br>
                                 </div>
                              </td>
                              <td height="10" width="70%">
                                 <br>
                                 <br>
                              </td>
                           </tr>
                           <tr>
                              <td width="30%">
                              </td>
                              <td height="10" width="70%">
                              </td>
                           </tr>
                           <script language="JavaScript">
                              document.write( buildCode() )
                           </script>
                           <tr>
                              <td align="center">
                              </td>
                              <td style="text-align: left;">%s
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </form>
               </td>
            </tr>
            <tr>
               <td height="15" width="565">&nbsp;
               </td>
            </tr>
            <tr>
               <td style="">&nbsp;
               </td>
               <td>&nbsp;
               </td>
               <td style="" valign="top" width="565">
                  <p align="left">%#COMPANY#| <a href="mailto:%#COMPANY_EMAIL#" onfocus="this.blur()">%#COMPANY_EMAIL#</a>
                     <br>
                     &nbsp;
                  </p>
               </td>
            </tr>
         </tbody>
      </table>

   </body>
</html>