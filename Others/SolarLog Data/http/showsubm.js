//
// Create and show submenu structure
//
function getMenuEntry( id ) {
   var i
   for( i=0; i<entryID.length; i++ ) {
      if( entryID[i]==id )
         break
   }
   return i
}

// SubMenustruktur aufbauen und anzeigen
function showSubMenu( curID ) {
    var i, i2, i3, found
    for( i=0; i<menuEntryCnt; i++ ) {
        found = false
        for( i2=2; i2<menuEntry[i].length; i2++ ) {
            if( menuEntry[i][i2]==curID ) {
                found = true
                break;
            }
        }
        if( found ) {   // Menu aufklappen?
            // menu header
            document.write("<li><a href='"+menuEntry[i][1]+"' class='act'>"+menuEntry[i][0]+"</a><ul>")
            // menu list
            for( i2=2; i2<menuEntry[i].length; i2++ ) {
                i3 = getMenuEntry( menuEntry[i][i2] )
                if( menuEntry[i][i2]==curID ) {
                    // aktiver Dialog
                    document.write("<li><a href='"+entryHtml[i3]+"' class='act'>"+entryName[i3]+"</a></li>")
                }
                else {
                    // inaktiver Dialog
                    document.write("<li><a href='"+entryHtml[i3]+"'>"+entryName[i3]+"</a></li>")
                }
            }
            document.write("</ul></li>")
        }
        else {  // nur Hauptmenupunkt zeigen
            // menu header
            document.write("<li><a href='"+menuEntry[i][1]+"'>"+menuEntry[i][0]+"</a></li>")
        }
    }
}

// Show-Mainmenu on top for config. (active = true/false)
function showMainMenuConfig( active, menutext ) {
    document.write("<td align='center' valign='middle'"+(active?" class='act'":"")+"><a href='"+menuEntry[0][1]+"'>"+menutext+"</a></td>")
}
