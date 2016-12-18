# -*- coding: utf-8 -*-
import wx
import youtube_dl
import sys
from subprocess import call
from HOLA import VentanaHija
from Acerca import VentanaHija2

class Miaplicacion(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent=parent, title=title, size=(800,600))
		panel = wx.Panel(self)
		
		
	
		self.r1 = wx.CheckBox(self,-1, "MP4 (720 x 1280)",(320,100))
		self.r2 = wx.CheckBox(self,-1, "WEBM (720 x 1280)",(320,120))
		self.r3 = wx.CheckBox(self,-1, "MP4 (360 x 640)",(320,140))
		self.r4 = wx.CheckBox(self,-1, "MP3 Audio",(320,160))
	
		
		self.texto = wx.TextCtrl(self, style=wx.TE_MULTILINE, pos=(200,30), size=(400,20))
		boton = wx.Button(self,-1,u"Download", pos=(250,50), size=(100,-1))
		boton2 = wx.Button(self,-1,u"Cancelar", pos=(450,50), size=(100,-1))
		
		
		barra_menu = wx.MenuBar()
		
		menu_Ayuda = wx.Menu()
		m_usar = menu_Ayuda.Append(-1, "Uso de la aplicacion")
		
		menu_Acerca = wx.Menu()
		m_acerca = menu_Acerca.Append(-1, "Hacerca del desarrollador")
		
		menu_Actualizar = wx.Menu()
		m_ac = menu_Actualizar.Append(-1, "Actualizar la aplicacion")
		
		barra_menu.Append(menu_Ayuda,"Ayuda")
		barra_menu.Append(menu_Acerca,"Acerca de")
		barra_menu.Append(menu_Actualizar,"Actualizar")
		
		self.Bind(wx.EVT_BUTTON, self.onClickButton1, boton)
		self.Bind(wx.EVT_BUTTON, self.onClickButton2, boton2)
		self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox1, self.r1)
		self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox2, self.r2)
		self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox3, self.r3)
		self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox4, self.r4)
		self.Bind(wx.EVT_MENU, self.usar,m_usar)		
		self.Bind(wx.EVT_MENU, self.acerca, m_acerca)
		self.Bind(wx.EVT_MENU, self.Actualizar, m_ac)
		self.SetMenuBar(barra_menu)
		self.Layout()
		self.Center(True)
		self.Show()
	
	def EvtCheckBox1(self, event):
		t = "-f 22"
		txt = self.texto.GetValue()
		command ="youtube-dl",t,txt 
		call(command, shell=False)
	
	def EvtCheckBox2(self, event):
		t = "-f 45"
		txt = self.texto.GetValue()
		command ="youtube-dl",t,txt 
		call(command, shell=False)
		
	def EvtCheckBox3(self, event):
		t = "-f 18"
		txt = self.texto.GetValue()
		command ="youtube-dl",t,txt 
		call(command, shell=False)
		
	def EvtCheckBox4(self, event):
		txt = self.texto.GetValue()
		command ="youtube-dl -x --audio-format mp3 "+txt 
		call(command.split(), shell = False)
		
   
	def onClickButton1(self,event):
		
		txt = self.texto.GetValue()
		command ="youtube-dl",txt 
		call(command, shell=False)
		
	def onClickButton2(self,event):
		self.Destroy()
		
	def usar(self, event):
		vnt = VentanaHija(self)
		
		vnt.Show()
		
	def acerca(self, event):
		pnt = VentanaHija2(self)
		
		pnt.Show()
		
	def Actualizar(self, event):
		command ="youtube-dl -U" 
		call(command.split(), shell=False)
		
if __name__ =='__main__':
	app = wx.App()
	#frame = Miaplicacion(None,u"Youtube Downloader")
	ventana = Miaplicacion(None,u"Youtube Downloader")
	ventana.Show()
	app.MainLoop()
