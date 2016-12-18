import wx
 
class VentanaHija(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.NewId(), "Uso de Youtube downloader",
                          pos=(130,130), size=(400,300))
 
       
       
        static_text = wx.StaticText(self,-1,u"He aqui como usar youtube downloader, primero copias el link de tu video de youtube,despues si quieres descarga en formato normal del video presiona el boton 'Download', si desea descarga en formato diferente solo chekee cualquier formato que desee de los que muestran en pantalla y la descarga empezara automaticamente.")
        
        
        
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.al_cerrar)
        
    def al_cerrar(self, event):
		
		self.Destroy()
       
 
 
if __name__ == '__main__':
    app= wx.App(0)
    ventana = VentanaHija(None)
    ventana.Show()
    app.MainLoop()
