import os
import subprocess
import sys
import gi
import threading

# UI library
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# Mobile GTK widgets
gi.require_version('Handy','1')
from gi.repository import Handy
# Music player control
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib
# Gio
from gi.repository import Gio

# return true to prevent other signal handlers from deleting objects from the builder
class Handler:
	def _btnClose(self, *args):
		# destroy window
		app.window.destroy()
		# set app.window to none, prompting window re-creation on next activation
		app.window = None
		return True

	def _btnQuit(self, *args):
		# release app (stop keeping it alive)
		app.release()
		# properly quit the app
		app.quit()
		# exit all threads
		os._exit(1)

	def _btnAbout(self, *args):
		o("windowAbout").show()
		return True
	
	def _closeAbout(self, *args):
		o("windowAbout").hide()
		return True

class Companion(Gtk.Application):
	def __init__(self):
		Gtk.Application.__init__(self,
			application_id="com.arteeh.Companion",
			flags=Gio.ApplicationFlags.FLAGS_NONE)
		self.window = None

	def do_startup(self):
		Gtk.Application.do_startup(self)
		self.hold()

		self.in_startup = True
		# declare that the application is currently starting up. Certain variables are not available yet.

		self.create_window()
		self.threadW = threading.Thread(target=threadWasptool, args=[self])

		self.threadW.start()

		self.in_startup = False

	def do_activate(self):
		if not self.window:
			self.create_window()
		self.window.present()

# change the parts of the UI relevant to syncing: Sync spinner and sync label.
	def set_syncing(self, active, desc="Checking if time is synced..."):
		if active:
			self.o("spnInitializing").start()
		else:
			self.o("spnInitializing").stop()
		self.o("lblInitializing").set_label(desc)
		self.sync_desc_str = desc
		self.sync_activity = active

		print(self.sync_activity)

	def create_window(self):
		Gtk.init()
		Handy.init()
		global builder
		builder = Gtk.Builder()
		builder.add_from_file("/app/bin/app.ui")
		builder.connect_signals(Handler())
		self.objects = builder.get_objects()
		self.window = self.o("window")
		self.window.set_application(self)

		if not self.in_startup:
			# skip in startup because sync_activity and sync_desc_str are not available yet
			self.set_syncing(self.sync_activity, self.sync_desc_str)

		self.window.show_all()

	def o(self, name):
		for i in range(0, len(self.objects)):
			if self.objects[i].get_name() == name:
				return self.objects[i]
		return -1

# Fuction for grabbing UI objects
def o(name):
	for i in range(0,len(app.objects)):
		if app.objects[i].get_name() == name:
			return app.objects[i]
	return -1

# Set the time
def rtc():
	app.set_syncing(True)
	output=subprocess.check_output(['/app/bin/wasptool','--check-rtc'],universal_newlines=True)
	if output.find("delta 0") >= 0:
		print("time is already synced")
	else:
		app.set_syncing(True, desc="Syncing time...")
		#output=subprocess.check_output(['/app/bin/wasptool','--rtc'],universal_newlines=True)
		print(output)
	app.set_syncing(False, desc="Done!")

# Thread for calling wasptool
def threadWasptool(app):
	print("wasptool thread started")
	rtc()
	print("wasptool thread ended")

if __name__ == "__main__":
	global app
	app = Companion()
	app.run(sys.argv)

