import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Handy','1')
from gi.repository import Handy

def o(name):
	for i in range(0,len(objects)):
		if objects[i].get_name() == name:
			return objects[i]
	return -1

# return true to prevent other signal handlers from deleting objects from the builder
class Handler:
	def _btnQuit(self, *args):
		Gtk.main_quit()
		return True
	
	def _btnAbout(self, *args):
		o("windowAbout").show()
		return True
	
	def _closeAbout(self, *args):
		o("windowAbout").hide()
		return True

Gtk.init()
Handy.init()
builder = Gtk.Builder()
builder.add_from_file("app.ui")
builder.connect_signals(Handler())
objects = builder.get_objects()

o("window").show_all()

Gtk.main()
