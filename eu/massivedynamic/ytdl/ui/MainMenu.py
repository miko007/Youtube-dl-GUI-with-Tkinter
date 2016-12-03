# -*- coding: utf-8 -*-

from Tkinter import Menu
import tkFileDialog

class MainMenu(Menu):
	def __init__(self, root):
		self.root = root
		Menu.__init__(self)
		self.setup()

	def setup(self):
		self.file = Menu(self, tearoff=0)
		self.add_cascade(label="YouTube-DL", menu=self.file)
		self.file.add_command(label="Speicherort wählen...", command=self.open)
		self.file.add_separator()
		self.file.add_command(label="Beenden", command=self.master.destroy)

	def open(self):
		dir = tkFileDialog.askdirectory(initialdir=self.root.root.config.options["path"])
		self.root.root.config.options["path"] = dir
		self.root.root.config.save()