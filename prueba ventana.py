# coding=utf8
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

ventana = Gtk.Window()
ventana.set_title ("hola soy  raul")
ventana.connect("delete-event" , Gtk.main_quit)
ventana.show()

caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caja.show()
ventana.add(caja)

etiqueta = Gtk.Label("hola amigos")
etiqueta.show()
caja.pack_start(etiqueta, True, True,0)

boton = Gtk.Button("hola soy  raul")
boton.show()
caja.pack_start(boton, True, True, 0)

Gtk.main()

