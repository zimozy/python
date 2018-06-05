#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class tasko:
	def delete_event(self, widget, event, data=None):
		print "delete event occured"
		return False
	def destroy(self, widget, data=None):
		print "destroy event occured"
		gtk.main_quit()
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.connect("delete_event", self.delete_event)

        	self.window.connect("destroy", self.destroy)

		self.window.set_border_width(5)

		self.button = self.gtk.Button("Hey, There!")

     		   # This packs the button into the window (a GTK container).
		self.window.add(self.button)
    
        # The final step is to display this newly created widget.
		self.button.show()
    
        # and the window
		self.window.show()	

	def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
		gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
#if __name__ == "__main__":
#    hello = HelloWorld()
#    hello.main()
