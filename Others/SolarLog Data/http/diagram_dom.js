function _Draw(theDrawColor, theTextColor, isScaleText, theTooltipText, theAction, theGridColor, theSubGridColor)
{ var x0,y0,i,j,itext,l,x,y,r,u,fn,dx,dy,xr,yr,invdifx,invdify,deltax,deltay,id=this.ID,lay=0,selObj="",divtext="",ii=0,oo,k,sub,sshift;
var c151="&#151;", nbsp=(_IE)? "&nbsp;" : "";
if (_nvl(theGridColor,"")!="") { this.XGridColor=theGridColor; this.YGridColor=theGridColor; }
if (_nvl(theSubGridColor,"")!="") { this.XSubGridColor=theSubGridColor; this.YSubGridColor=theSubGridColor; }
lay--; 
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
if (selObj) lay--;
if (lay<-1)
selObj.title=_nvl(theTooltipText,"");
else
_DiagramTarget.document.writeln("<div id='"+this.ID+"' title='"+_nvl(theTooltipText,"")+"'>"); 
if (_IsImage(theDrawColor))
divtext="<div id='"+this.ID+"i"+eval(ii++)+"' onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute; left:"+eval(this.left)+"px; width:"+eval(this.right-this.left+_dSize)+"px; top:"+eval(this.top)+"px; height:"+eval(this.bottom-this.top+_dSize)+"px; color:"+theTextColor+"; border-style:solid; border-width:1px; z-index:"+this.zIndex+"'><img src='"+theDrawColor+"' width="+eval(this.right-this.left-1)+" height="+eval(this.bottom-this.top-1)+"></div>";
else
divtext="<div id='"+this.ID+"i"+eval(ii++)+"' onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute; left:"+eval(this.left)+"px; width:"+eval(this.right-this.left+_dSize)+"px; top:"+eval(this.top)+"px; height:"+eval(this.bottom-this.top+_dSize)+"px; background-color:"+theDrawColor+"; color:"+theTextColor+"; border-style:solid; border-width:1px; z-index:"+this.zIndex+"'>&nbsp;</div>"; 
if ((this.XScale==1)||(isNaN(this.XScale)))
{ u="";
fn="";
if (isNaN(this.XScale))
{ if (this.XScale.substr(0,9)=="function ") fn=eval("window."+this.XScale.substr(9));
else u=this.XScale;
}
dx=(this.xmax-this.xmin);
if (Math.abs(dx)>0)
{ invdifx=(this.right-this.left)/(this.xmax-this.xmin);
r=1;
while (Math.abs(dx)>=100) { dx/=10; r*=10; }
while (Math.abs(dx)<10) { dx*=10; r/=10; }
if (Math.abs(dx)>=50) { this.SubGrids=5; deltax=10*r*_sign(dx); }
else
{ if (Math.abs(dx)>=20) { this.SubGrids=5; deltax=5*r*_sign(dx); }
else { this.SubGrids=4; deltax=2*r*_sign(dx); }
}
if (this.XGridDelta!=0) deltax=this.XGridDelta;
if (this.XSubGrids!=0) this.SubGrids=this.XSubGrids;
sub=deltax*invdifx/this.SubGrids;
sshift=0;
if ((this.XScalePosition=="top-left")||(this.XScalePosition=="bottom-left")) sshift=-Math.abs(deltax*invdifx/2);
if ((this.XScalePosition=="top-right")||(this.XScalePosition=="bottom-right")) sshift=Math.abs(deltax*invdifx/2);
x=Math.floor(this.xmin/deltax)*deltax;
itext=0;
if (deltax!=0) this.MaxGrids=Math.floor(Math.abs((this.xmax-this.xmin)/deltax))+2;
else this.MaxGrids=0;
for (j=this.MaxGrids; j>=-1; j--)
{ xr=x+j*deltax;
x0=Math.round(this.left+(-this.xmin+xr)*invdifx);
if (this.XSubGridColor)
{ for (k=1; k<this.SubGrids; k++)
{ if ((x0-k*sub>this.left+1)&&(x0-k*sub<this.right-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+Math.round(x0-k*sub)+"px; top:"+eval(this.top+1)+"px; z-index:"+this.zIndex+"; width:1px; height:"+eval(this.bottom-this.top-1)+"px; background-color:"+this.XSubGridColor+"; font-size:1pt'></div>";
}
if (this.SubGrids==-1)
for (k=0; k<8; k++)
{ if ((x0-this.logsub[k]*sub*_sign(deltax)>this.left+1)&&(x0-this.logsub[k]*sub*_sign(deltax)<this.right-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+Math.round(x0-this.logsub[k]*sub*_sign(deltax))+"px; top:"+eval(this.top+1)+"px; z-index:"+this.zIndex+"; width:1px; height:"+eval(this.bottom-this.top-1)+"px; background-color:"+this.XSubGridColor+"; font-size:1pt'></div>";
}
}
if ((x0>=this.left)&&(x0<=this.right))
{ itext++;
if ((itext!=2)||(!isScaleText))
{ if (r>1) 
{ if (fn) l=fn(xr)+"";
else l=xr+""+u; 
}
else 
{ if (fn) l=fn(Math.round(10*xr/r)/Math.round(10/r))+"";
else l=Math.round(10*xr/r)/Math.round(10/r)+""+u; 
}
if (l.charAt(0)==".") l="0"+l;
if (l.substr(0,2)=="-.") l="-0"+l.substr(1,100);
}
else l=this.xtext;
if (this.XScalePosition.substr(0,3)!="top")
{ if ((x0+sshift>=this.left)&&(x0+sshift<=this.right))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center style='position:absolute; left:"+eval(x0-50+sshift)+"px; width:102px; top:"+eval(this.bottom+8)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.bottom-5)+"px; z-index:"+this.zIndex+"; width:1px; height:12px; background-color:"+theTextColor+"; font-size:1pt'></div>";
}
else
{ if ((x0+sshift>=this.left)&&(x0+sshift<=this.right))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center style='position:absolute; left:"+eval(x0-50+sshift)+"px; width:102px; top:"+eval(this.top-24)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.top-5)+"px; z-index:"+this.zIndex+"; width:1px; height:12px; background-color:"+theTextColor+"; font-size:1pt'></div>";
}
if ((this.XGridColor)&&(x0>this.left)&&(x0<this.right)) divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.top+1)+"px; z-index:"+this.zIndex+"; width:1px; height:"+eval(this.bottom-this.top-1)+"px; background-color:"+this.XGridColor+"; font-size:1pt'></div>";
}
}
}
}
if ((!isNaN(this.XScale))&&(this.XScale>1))
{ dx=(this.xmax-this.xmin);
if (Math.abs(dx)>0)
{ invdifx=(this.right-this.left)/(this.xmax-this.xmin);
deltax=this.DateInterval(Math.abs(dx))*_sign(dx);
if (this.XGridDelta!=0) deltax=this.XGridDelta;
if (this.XSubGrids!=0) this.SubGrids=this.XSubGrids;
sub=deltax*invdifx/this.SubGrids;
sshift=0;
if ((this.XScalePosition=="top-left")||(this.XScalePosition=="bottom-left")) sshift=-Math.abs(deltax*invdifx/2);
if ((this.XScalePosition=="top-right")||(this.XScalePosition=="bottom-right")) sshift=Math.abs(deltax*invdifx/2); 
x=Math.floor(this.xmin/deltax)*deltax;
itext=0;
if (deltax!=0) this.MaxGrids=Math.floor(Math.abs((this.xmax-this.xmin)/deltax))+2;
else this.MaxGrids=0;
for (j=this.MaxGrids; j>=-2; j--)
{ xr=x+j*deltax;
x0=Math.round(this.left+(-this.xmin+x+j*deltax)*invdifx);
if (this.XSubGridColor)
{ for (k=1; k<this.SubGrids; k++)
{ if ((x0-k*sub>this.left+1)&&(x0-k*sub<this.right-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+Math.round(x0-k*sub)+"px; top:"+eval(this.top+1)+"px; z-index:"+this.zIndex+"; width:1px; height:"+eval(this.bottom-this.top-1)+"px; background-color:"+this.XSubGridColor+"; font-size:1pt'></div>";
}
} 
if ((x0>=this.left)&&(x0<=this.right))
{ itext++;
if ((itext!=2)||(!isScaleText)) l=_DateFormat(xr, Math.abs(deltax), this.XScale);
else l=this.xtext;
if (this.XScalePosition.substr(0,3)!="top")
{ if ((x0+sshift>=this.left)&&(x0+sshift<=this.right))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center style='position:absolute; left:"+eval(x0-50+sshift)+"px; width:102px; top:"+eval(this.bottom+8)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.bottom-5)+"px; z-index:"+this.zIndex+"; width:1px; height:12px; background-color:"+theTextColor+"; font-size:1pt'></div>";
}
else
{ if ((x0+sshift>=this.left)&&(x0+sshift<=this.right))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center style='position:absolute; left:"+eval(x0-50+sshift)+"px; width:102px; top:"+eval(this.top-24)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.top-5)+"px; z-index:"+this.zIndex+"; width:1px; height:12px; background-color:"+theTextColor+"; font-size:1pt'></div>";
}
if ((this.XGridColor)&&(x0>this.left)&&(x0<this.right)) divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+x0+"px; top:"+eval(this.top+1)+"px; z-index:"+this.zIndex+"; width:1px; height:"+eval(this.bottom-this.top-1)+"px; background-color:"+this.XGridColor+"; font-size:1pt'></div>";
}
}
}
}
if ((this.YScale==1)||(isNaN(this.YScale)))
{ u="";
fn="";
if (isNaN(this.YScale))
{ if (this.YScale.substr(0,9)=="function ") fn=eval("window."+this.YScale.substr(9));
else u=this.YScale;
}
dy=this.ymax-this.ymin;
if (Math.abs(dy)>0)
{ invdify=(this.bottom-this.top)/(this.ymax-this.ymin);
r=1;
while (Math.abs(dy)>=100) { dy/=10; r*=10; }
while (Math.abs(dy)<10) { dy*=10; r/=10; }
if (Math.abs(dy)>=50) { this.SubGrids=5; deltay=10*r*_sign(dy); }
else
{ if (Math.abs(dy)>=20) { this.SubGrids=5; deltay=5*r*_sign(dy); }
else { this.SubGrids=4; deltay=2*r*_sign(dy); }
} 
if (this.YGridDelta!=0) deltay=this.YGridDelta;
if (this.YSubGrids!=0) this.SubGrids=this.YSubGrids;
sub=deltay*invdify/this.SubGrids;
sshift=0;
if ((this.YScalePosition=="left-top")||(this.YScalePosition=="right-top")) sshift=-Math.abs(deltay*invdify/2);
if ((this.YScalePosition=="left-bottom")||(this.YScalePosition=="right-bottom")) sshift=Math.abs(deltay*invdify/2); 
y=Math.floor(this.ymax/deltay)*deltay;
itext=0;
if (deltay!=0) this.MaxGrids=Math.floor(Math.abs((this.ymax-this.ymin)/deltay))+2;
else this.MaxGrids=0;
for (j=-1; j<=this.MaxGrids; j++)
{ yr=y-j*deltay;
y0=Math.round(this.top+(this.ymax-yr)*invdify);
if (this.YSubGridColor)
{ for (k=1; k<this.SubGrids; k++)
{ if ((y0+k*sub>this.top+1)&&(y0+k*sub<this.bottom-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left+1)+"px; top:"+Math.round(y0+k*sub)+"px; z-index:"+this.zIndex+"; height:1px; width:"+eval(this.right-this.left-1)+"px; background-color:"+this.YSubGridColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
if (this.SubGrids==-1)
{ for (k=0; k<8; k++)
{ if ((y0+this.logsub[k]*sub*_sign(deltay)>this.top+1)&&(y0+this.logsub[k]*sub*_sign(deltay)<this.bottom-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left+1)+"px; top:"+Math.round(y0+this.logsub[k]*sub*_sign(deltay))+"px; z-index:"+this.zIndex+"; height:1px; width:"+eval(this.right-this.left-1)+"px; background-color:"+this.YSubGridColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
}
}
if ((y0>=this.top)&&(y0<=this.bottom))
{ itext++;
if ((itext!=2)||(!isScaleText))
{ if (r>1)
{ if (fn) l=fn(yr)+"";
else l=yr+""+u;
} 
else
{ if (fn) l=fn(Math.round(10*yr/r)/Math.round(10/r))+"";
else l=Math.round(10*yr/r)/Math.round(10/r)+""+u;
} 
if (l.charAt(0)==".") l="0"+l;
if (l.substr(0,2)=="-.") l="-0"+l.substr(1,100);
}
else l=this.ytext;
if (this.YScalePosition.substr(0,5)!="right")
{ if ((y0+sshift>=this.top)&&(y0+sshift<=this.bottom))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=right style='position:absolute; left:"+eval(this.left-100)+"px; width:89px; top:"+eval(y0-9+sshift)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left-5)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:11px; background-color:"+theTextColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
else
{ if ((y0+sshift>=this.top)&&(y0+sshift<=this.bottom))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=left style='position:absolute; left:"+eval(this.right+10)+"px; width:89px; top:"+eval(y0-9+sshift)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.right-5)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:11px; background-color:"+theTextColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
if ((this.YGridColor)&&(y0>this.top)&&(y0<this.bottom)) divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left+1)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:"+eval(this.right-this.left-1)+"px; background-color:"+this.YGridColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
}
}
}
if ((!isNaN(this.YScale))&&(this.YScale>1))
{ dy=this.ymax-this.ymin;
if (Math.abs(dy)>0)
{ invdify=(this.bottom-this.top)/(this.ymax-this.ymin);
deltay=this.DateInterval(Math.abs(dy))*_sign(dy);
if (this.YGridDelta!=0) deltay=this.YGridDelta;
if (this.YSubGrids!=0) this.SubGrids=this.YSubGrids;
sub=deltay*invdify/this.SubGrids;
sshift=0;
if ((this.YScalePosition=="left-top")||(this.YScalePosition=="right-top")) sshift=-Math.abs(deltay*invdify/2);
if ((this.YScalePosition=="left-bottom")||(this.YScalePosition=="right-bottom")) sshift=Math.abs(deltay*invdify/2); 
y=Math.floor(this.ymax/deltay)*deltay;
itext=0;
if (deltay!=0) this.MaxGrids=Math.floor(Math.abs((this.ymax-this.ymin)/deltay))+2;
else this.MaxGrids=0;
for (j=-2; j<=this.MaxGrids; j++)
{ yr=y-j*deltay;
y0=Math.round(this.top+(this.ymax-y+j*deltay)*invdify);
if (this.YSubGridColor)
{ for (k=1; k<this.SubGrids; k++)
{ if ((y0+k*sub>this.top+1)&&(y0+k*sub<this.bottom-1))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left+1)+"px; top:"+Math.round(y0+k*sub)+"px; z-index:"+this.zIndex+"; height:1px; width:"+eval(this.right-this.left-1)+"px; background-color:"+this.YSubGridColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
}
if ((y0>=this.top)&&(y0<=this.bottom))
{ itext++;
if ((itext!=2)||(!isScaleText)) l=_DateFormat(yr, Math.abs(deltay), this.YScale);
else l=this.ytext;
if (this.YScalePosition.substr(0,5)!="right")
{ if ((y0+sshift>=this.top)&&(y0+sshift<=this.bottom))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=right style='position:absolute; left:"+eval(this.left-100)+"px; width:89px; top:"+eval(y0-9+sshift)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left-5)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:11px; background-color:"+theTextColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
else
{ if ((y0+sshift>=this.top)&&(y0+sshift<=this.bottom))
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=left style='position:absolute; left:"+eval(this.right+10)+"px; width:89px; top:"+eval(y0-9+sshift)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+l+"</div>";
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.right-5)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:11px; background-color:"+theTextColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
if ((this.YGridColor)&&(y0>this.top)&&(y0<this.bottom)) divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' style='position:absolute; left:"+eval(this.left+1)+"px; top:"+eval(y0)+"px; z-index:"+this.zIndex+"; height:1px; width:"+eval(this.right-this.left-1)+"px; background-color:"+this.YGridColor+"; font-size:1pt;line-height:1pt'>"+nbsp+"</div>";
}
}
}
}
if (this.XScalePosition.substr(0,3)!="top") 
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute; left:"+this.left+"px; width:"+eval(this.right-this.left)+"px; top:"+eval(this.top-20)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+this.title+"</div>";
else
divtext+="<div id='"+this.ID+"i"+eval(ii++)+"' align=center onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute; left:"+this.left+"px; width:"+eval(this.right-this.left)+"px; top:"+eval(this.bottom+4)+"px; color:"+theTextColor+";"+this.Font+" z-index:"+this.zIndex+"'>"+this.title+"</div>"; 
if (lay<-1)
selObj.innerHTML=divtext;
else
_DiagramTarget.document.writeln(divtext+"</div>");
}
function Bar(theLeft, theTop, theRight, theBottom, theDrawColor, theText, theTextColor, theTooltipText, theAction)
{ this.ID="Bar"+_N_Bar; _N_Bar++; _zIndex++;
this.left=theLeft;
this.top=theTop;
this.width=theRight-theLeft;
this.height=theBottom-theTop;
this.DrawColor=theDrawColor;
this.Text=String(theText);
this.TextColor=theTextColor;
this.BorderWidth="";
this.BorderColor="";
this.Action=theAction;
this.SetVisibility=_SetVisibility;
this.SetColor=_SetBarColor;
this.SetText=_SetBarText;
this.SetTitle=_SetTitle;
this.MoveTo=_MoveTo;
this.ResizeTo=_ResizeTo;
this.Delete=_Delete;
if (_nvl(theText,"")!="")
{ var tt=theText;
if (_IsImage(theText)) tt="<img src='"+theText+"' width="+eval(theRight-theLeft-1)+" height="+eval(theBottom-theTop-1)+">";
_DiagramTarget.document.writeln("<div id='"+this.ID+"' onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+theLeft+"px;top:"+theTop+"px;width:"+eval(theRight-theLeft)+"px;height:"+eval(theBottom-theTop)+"px;background-color:"+theDrawColor+";color:"+theTextColor+";"+_BFont+"z-index:"+_zIndex+"'; title='"+_nvl(theTooltipText,"")+"' align=center>"+tt+"</div>");
}
else _DiagramTarget.document.writeln("<div id='"+this.ID+"' onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+theLeft+"px;top:"+theTop+"px;width:"+eval(theRight-theLeft)+"px;height:"+eval(theBottom-theTop)+"px;background-color:"+theDrawColor+";font-size:1pt;line-height:1pt;font-family:Verdana;font-weight:normal;z-index:"+_zIndex+"'; title='"+_nvl(theTooltipText,"")+"'>&nbsp;</div>");
return(this);
}
function _SetBarColor(theColor)
{ var id=this.ID, selObj;
this.DrawColor=theColor;
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
selObj.style.backgroundColor=theColor;
}
function _SetBarText(theText)
{ var id=this.ID, selObj;
this.Text=String(theText);
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
var tt=theText;
if (_IsImage(theText))
{ var ww=0;
if (this.BorderWidth) ww=this.BorderWidth;
tt="<img src='"+theText+"' width="+eval(this.width-2*ww)+" height="+eval(this.height-2*ww)+">";
}
selObj.innerHTML=tt;
}
function _SetVisibility(isVisible)
{ var ll, id=this.ID, selObj;
if (document.all)
{ selObj=eval("_DiagramTarget.document.all."+id);
if (isVisible) selObj.style.visibility="visible";
else selObj.style.visibility="hidden";
}
else
{ selObj=_DiagramTarget.document.getElementById(id);
if (isVisible) selObj.style.visibility="visible";
else selObj.style.visibility="hidden";
if (id.substr(0,3)=='Dia')
{ var ii=0;
selObj=_DiagramTarget.document.getElementById(id+'i'+eval(ii++));
while (selObj!=null)
{ if (isVisible) selObj.style.visibility="visible";
else selObj.style.visibility="hidden";
selObj=_DiagramTarget.document.getElementById(id+'i'+eval(ii++));
}
}
}
}
function _SetTitle(theTitle)
{ var id=this.ID, selObj;
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
selObj.title=theTitle;
}
function _MoveTo(theLeft, theTop)
{ var id=this.ID, selObj;
if (theLeft!="") this.left=theLeft;
if (theTop!="") this.top=theTop;
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
with (selObj.style)
{ if (theLeft!="") left=theLeft+"px";
if (theTop!="") top=theTop+"px";
visibility="visible";
}
}
function _ResizeTo(theLeft, theTop, theWidth, theHeight)
{ var id=this.ID, selObj, ww=0;
if (this.BorderWidth) ww=this.BorderWidth;
if (theLeft!="") this.left=theLeft;
if (theTop!="") this.top=theTop;
if (theWidth!="") this.width=theWidth;
if (theHeight!="") this.height=theHeight;
if (_IsImage(this.Text)) this.SetText(this.Text);
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
with (selObj.style)
{ if (theLeft!="") left=theLeft+"px";
if (theTop!="") top=theTop+"px";
if (theWidth!="") width=eval(theWidth-ww+ww*_dSize)+"px";
if (theHeight!="") height=eval(theHeight-ww+ww*_dSize)+"px";
visibility="visible";
}
}
function _Delete()
{ var id=this.ID, selObj;
if (document.all)
{ selObj=eval("_DiagramTarget.document.all."+id);
selObj.outerHTML="";
}
else
{ selObj=_DiagramTarget.document.getElementById(id); 
selObj.parentNode.removeChild(selObj);
}
}
function _SetColor(theColor)
{ this.Color=theColor;
if ((theColor!="")&&(theColor.length<this.Color.length)) this.Color="#"+theColor;
else this.Color=theColor;
this.ResizeTo("", "", "", "");
}
//You can delete the following 3 functions, if you do not use Line objects
function Line(theX0, theY0, theX1, theY1, theColor, theSize, theTooltipText, theAction)
{ this.ID="Line"+_N_Line; _N_Line++; _zIndex++;
this.X0=theX0;
this.Y0=theY0;
this.X1=theX1;
this.Y1=theY1;
this.Color=theColor;
if ((theColor!="")&&(theColor.length==6)) this.Color="#"+theColor;
this.Size=Number(_nvl(theSize,1));
this.Action=theAction;
this.SetVisibility=_SetVisibility;
this.SetColor=_SetColor;
this.SetTitle=_SetTitle;
this.MoveTo=_LineMoveTo;
this.ResizeTo=_LineResizeTo;
this.Delete=_Delete;
var xx0, yy0, xx1, yy1, ll, rr, tt, bb, ww, hh, ccl, ccr, cct, ccb;
var ss2=Math.floor(this.Size/2), nbsp="";//(_IE)? "&nbsp;" : "";
var ddir=(((this.Y1>this.Y0)&&(this.X1>this.X0))||((this.Y1<this.Y0)&&(this.X1<this.X0))) ? true : false;
if (theX0<=theX1) { ll=theX0; rr=theX1; }
else { ll=theX1; rr=theX0; }
if (theY0<=theY1) { tt=theY0; bb=theY1; }
else { tt=theY1; bb=theY0; }
ww=rr-ll; hh=bb-tt;
_DiagramTarget.document.write("<div id='"+this.ID+"' style='position:absolute;left:"+eval(ll-ss2)+"px;top:"+eval(tt-ss2)+"px; width:"+eval(ww+this.Size)+"px; height:"+eval(hh+this.Size)+"px; z-index:"+_zIndex+";' title='"+_nvl(theTooltipText,"")+"'>");
if ((ww==0)||(hh==0))
_DiagramTarget.document.write("<div onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:0px;top:0px;width:"+eval(ww+this.Size)+"px;height:"+eval(hh+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>");
else
{ if (ww>hh)
{ ccr=0;
cct=0;
while (ccr<ww)
{ ccl=ccr;
while ((Math.round(ccr*hh/ww)==cct)&&(ccr<=ww)) ccr++;
if (ddir)
_DiagramTarget.document.write("<div onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+ccl+"px;top:"+cct+"px;width:"+eval(ccr-ccl+this.Size)+"px;height:"+this.Size+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>");
else
_DiagramTarget.document.write("<div onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+eval(ww-ccr)+"px;top:"+cct+"px;width:"+eval(ccr-ccl+this.Size)+"px;height:"+this.Size+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>");
cct++;
}
}
else
{ ccb=0;
ccl=0;
while (ccb<hh)
{ cct=ccb;
while ((Math.round(ccb*ww/hh)==ccl)&&(ccb<hh)) ccb++;
if (ddir)
_DiagramTarget.document.write("<div onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+ccl+"px;top:"+cct+"px;width:"+this.Size+"px;height:"+eval(ccb-cct+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>");
else
_DiagramTarget.document.write("<div onClick='"+_nvl(theAction,"")+"' style='"+_cursor(theAction)+"position:absolute;left:"+eval(ww-ccl)+"px;top:"+cct+"px;width:"+this.Size+"px;height:"+eval(ccb-cct+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>");
ccl++;
}
}
}
_DiagramTarget.document.writeln("</div>");
return(this);
}
function _LineResizeTo(theX0, theY0, theX1, theY1)
{ var xx0, yy0, xx1, yy1, ll, rr, tt, bb, ww, hh, ccl, ccr, cct, ccb, id=this.ID,lay=0,selObj="",divtext="";
var ss2=Math.floor(this.Size/2), nbsp="";//(_IE)? "&nbsp;" : "";
if (theX0!="") this.X0=theX0;
if (theY0!="") this.Y0=theY0;
if (theX1!="") this.X1=theX1;
if (theY1!="") this.Y1=theY1;
var ddir=(((this.Y1>this.Y0)&&(this.X1>this.X0))||((this.Y1<this.Y0)&&(this.X1<this.X0))) ? true : false;
if (this.X0<=this.X1) { ll=this.X0; rr=this.X1; }
else { ll=this.X1; rr=this.X0; }
if (this.Y0<=this.Y1) { tt=this.Y0; bb=this.Y1; }
else { tt=this.Y1; bb=this.Y0; }
ww=rr-ll; hh=bb-tt;
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
with (selObj.style)
{ left=eval(ll-ss2)+"px";
top=eval(tt-ss2)+"px";
width=eval(ww+this.Size)+"px";
height=eval(hh+this.Size)+"px";
}
if ((ww==0)||(hh==0))
divtext+="<div onClick='"+_nvl(this.Action,"")+"' style='"+_cursor(this.Action)+"position:absolute;left:0px;top:0px;width:"+eval(ww+this.Size)+"px;height:"+eval(hh+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>";
else
{ if (ww>hh)
{ ccr=0;
cct=0;
while (ccr<ww)
{ ccl=ccr;
while ((Math.round(ccr*hh/ww)==cct)&&(ccr<=ww)) ccr++;
if (ddir)
divtext+="<div onClick='"+_nvl(this.Action,"")+"' style='"+_cursor(this.Action)+"position:absolute;left:"+ccl+"px;top:"+cct+"px;width:"+eval(ccr-ccl+this.Size)+"px;height:"+this.Size+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>";
else
divtext+="<div onClick='"+_nvl(this.Action,"")+"' style='"+_cursor(this.Action)+"position:absolute;left:"+eval(ww-ccr)+"px;top:"+cct+"px;width:"+eval(ccr-ccl+this.Size)+"px;height:"+this.Size+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>";
cct++;
}
}
else
{ ccb=0;
ccl=0;
while (ccb<hh)
{ cct=ccb;
while ((Math.round(ccb*ww/hh)==ccl)&&(ccb<hh)) ccb++;
if (ddir)
divtext+="<div onClick='"+_nvl(this.Action,"")+"' style='"+_cursor(this.Action)+"position:absolute;left:"+ccl+"px;top:"+cct+"px;width:"+this.Size+"px;height:"+eval(ccb-cct+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>";
else
divtext+="<div onClick='"+_nvl(this.Action,"")+"' style='"+_cursor(this.Action)+"position:absolute;left:"+eval(ww-ccl)+"px;top:"+cct+"px;width:"+this.Size+"px;height:"+eval(ccb-cct+this.Size)+"px;background-color:"+this.Color+";font-size:1pt;line-height:1pt;'>"+nbsp+"</div>";
ccl++;
}
}
}
selObj.innerHTML=divtext;
}
function _LineMoveTo(theLeft, theTop)
{ var id=this.ID, selObj;
var ss2=Math.floor(this.Size/2);
if (theLeft!="") this.left=theLeft;
if (theTop!="") this.top=theTop;
if (document.all) selObj=eval("_DiagramTarget.document.all."+id);
else selObj=_DiagramTarget.document.getElementById(id);
with (selObj.style)
{ if (theLeft!="") left=eval(theLeft-ss2)+"px";
if (theTop!="") top=eval(theTop-ss2)+"px";
visibility="visible";
}
}
