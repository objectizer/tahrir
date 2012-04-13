import gtk

class Settings(gtk.Window):
	"""class Settings() mainly controls the preferences of the text editor, offering a GUI for the user allowing him to edit the 
		preferences freely."""
		
	def __init__(self, handler):
		"""Constructs instance of Settings()."""
		super(Settings, self).__init__()
		self.set_title('Maximus - Settings Manager')
		self.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.resize(450,300)
		self.handler = handler
		self.set_layout()
		self.connect('delete-event', self.on_delete_event)

		
	def set_layout(self):
		"""Constructs the layout of Settings dialog window."""
		tabView = gtk.Notebook()
		## Tab 'view'
		mainBox = gtk.VBox()
		#Show Lines Number
		firstOption = gtk.HBox()
		showLinesNumber = gtk.CheckButton('Show lines number')
		if self.handler.get_option('show_line_numbers') == 'True':
			showLinesNumber.set_active(True)
		else:
			showLinesNumber.set_active(False)
		showLinesNumber.connect('toggled', self.handler.set_show_line_numbers)
		firstOption.pack_start(showLinesNumber, False, False, 0)
		#TextView background
		secOption = gtk.HBox(False, False)
		textViewBgLabel = gtk.Label('Change text editor \'s background')
		textViewColorDialog = gtk.ColorButton()
		secOption.pack_start(textViewBgLabel, False, False, 0)
		secOption.pack_start(textViewColorDialog, False, False, 0)
		#TextView Color
		thirdOption = gtk.HBox(False, False)
		textViewFcLabel = gtk.Label('Change text editor \'s font color')
		textViewFColorDialog = gtk.ColorButton()
		thirdOption.pack_start(textViewFcLabel, False, False, 0)
		thirdOption.pack_start(textViewFColorDialog, False, False, 0)
		#
		mainBox.pack_start(firstOption, False, False, 0)
		mainBox.pack_start(secOption, False, False, 0)
		mainBox.pack_start(thirdOption, False, False, 0)
		tabView.append_page(mainBox, gtk.Label('view'))
		## End of tab 'view'
		
		self.add(tabView)
		tabView.show_all()
		
	def run(self):
		self.show_all()
		
	def on_delete_event(self, widget):
		self.hide_all()
