
from gi.repository import Gtk


@Gtk.Template(resource_path='/com/arteeh/Companion/window.ui')
class WaspCompanionWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'WaspCompanionWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
