#!/usr/bin/python
import wx
import wx.lib.agw.hyperlink as hl
 
class VentanaHija2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.NewId(), "Acerca del desarrollador",
						  pos=(130,130), size=(400,300))
        
        
        
        
        static_text = wx.StaticText(self,-1,u"En mi vida de dasarrolador de aplicaciones e ido evolucionando mas y\n mas dentro del mundo del desarrollo tanto consola como web pero\n mi punto de elevacion en la programacion de consola fue cuando \n conoci python un lenguaje de programacion sumamente extenso y\n a la ves entretenido como podran ver esta aplicacion esta hecha en\n python es muy util sin embargo les invito a conocer python y que se \ndiviertan aqui les dejo el link de app.Gracias... :) !.")
        hipervinculo = hl.HyperLinkCtrl(self,-1, u"Repositorio de Github donde esta la app", pos = (80,150), URL = 'https://github.com/AdonisClaros/Parcial_3_youtube_dl.git')
 
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.al_cerrar)
        
    def al_cerrar(self, event):
		
		self.Destroy()

        
       
       
 
 
if __name__ == '__main__':
    app= wx.App(0)
    ventana = VentanaHija2(None)
    ventana.Show()
    app.MainLoop()
