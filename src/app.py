import sys
import gi
import threading

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Handy','1')
from gi.repository import Handy

# return true to prevent other signal handlers from deleting objects from the builder
class Handler:
	def _btnQuit(self, *args):
		# exit gtk
		Gtk.main_quit()
		# exit all threads
		os._exit(1)
		return True
	
	def _btnAbout(self, *args):
		o("windowAbout").show()
		return True
	
	def _closeAbout(self, *args):
		o("windowAbout").hide()
		return True

def o(name):
	for i in range(0,len(objects)):
		if objects[i].get_name() == name:
			return objects[i]
	return -1

def init():
	print("initializing")
	Gtk.init()
	Handy.init()
	global builder
	builder = Gtk.Builder()
	builder.add_from_file("app.ui")
	builder.connect_signals(Handler())
	global objects
	objects = builder.get_objects()
	o("window").show_all()
	print("initialized")

def threadGtk():
	print("gtk thread started")
	Gtk.main()
	print("gtk thread ended")

def threadWasptool():
	print("wasptool thread started")
	
	print("wasptool thread ended")

init()
threadG = threading.Thread(target=threadGtk)
threadW = threading.Thread(target=threadWasptool)
threadG.start()
threadW.start()
