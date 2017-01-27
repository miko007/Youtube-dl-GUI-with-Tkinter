# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import time
from eu.massivedynamic.ytdl.ui.MainMenu import MainMenu
from eu.massivedynamic.ytdl.ui.UIButton import UIButton

class Window(Tk):
	def __init__(self, root, *args, **kwargs):
		self.root = root
		Tk.__init__(self, *args, **kwargs)
		icon        = PhotoImage(file="icons/yt.png")
		self.radios = []
		self.tk.call("wm", "iconphoto", self._w, icon)
		self.tk.call("wm", "title", self._w, "Youtube-DL")
		self.title("YouTube-DL")
		self.setup()

	def setup(self):
		self.minsize(width=500, height=400)
		self.configure(padx=5, pady=5)

		self.grid_columnconfigure(0, weight=2)
		self.grid_columnconfigure(1, weight=0)
		self.grid_rowconfigure(0, weight=2)

		self.menu     = MainMenu(self)
		self.buttons  = Frame(self, padx=15)

		self.add      = UIButton(self.buttons, text="add Link", command=self.root.showAddLink)
		self.delete   = Button(self.buttons, text="Delete", command=self.deleteItem)
		self.start    = Button(self.buttons, text="Start Download", command=self.startDownload)

		self.progress = ttk.Progressbar(self)
		self.list     = Listbox(self,selectmode=MULTIPLE)

		self.progress.grid(column=0, row=1, columnspan=2, sticky=N+S+E+W, pady=5)

		self.list.grid(row=0, column=0, sticky=N+S+E+W)
		self.buttons.grid(row=0, column=1, sticky=N+S+E+W)

		self.coverImage = PhotoImage(file="https://img.youtube.com/vi/_zp2Etvvlrk/3.jpg")
		self.cover  = Label(self.buttons, image=self.coverImage)

		self.add.pack(fill=BOTH)
		self.delete.pack(fill=BOTH)
		self.start.pack(fill=BOTH, pady=(0,20))
		self.config(menu=self.menu)

		for option in self.root.outputFormats:
			b = Radiobutton(self.buttons, text=option, value=option, command=lambda option=option: self.setOutputFormat(option))
			self.radios.append(b)
			if (option == self.root.defaultFormat):
				b.select()
			b.pack(anchor=W)

		self.cover.pack(fill=BOTH)

	def setOutputFormat(self, format):
		self.root.defaultFormat            = format
		self.root.config.options["format"] = format
		self.root.config.save()

	def refreshList(self):
		self.list.delete(0, END)
		for item in self.root.list:
			self.list.insert(END, item.title)

	def setUIStatus(self, status):
		self.add.config(state=status)
		self.delete.config(state=status)
		self.start.config(state=status)
		self.list.config(state=status)
		for radio in self.radios:
			radio.config(state=status)

	def deleteItem(self):
		self.root.removeLink(self.list.curselection())
		self.refreshList()

	def setProgress(self, percent):
		self.progress["value"] = percent
		self.progress.update_idletasks()

	def startDownload(self):
		self.setUIStatus("disabled")
		self.setProgress(1)
		time.sleep(.10)
		self.root.download()
		time.sleep(.20)
		self.setProgress(0)
		self.setUIStatus("normal")
		self.refreshList()

class InputBox(Toplevel):
	isVisible = False
	def __init__(self, root):
		self.root = root
		Toplevel.__init__(self, width=300, height=100)
		self.setup()
		InputBox.isVisible = True

	def setup(self):
		self.configure(padx=5, pady=5)
		self.title("add Link")
		self.label  = Label(self, text="insert a new Link:")
		self.input  = Entry(self, width=50)
		self.ok     = Button(self, command=self.submit, text="OK")
		self.cancel = Button(self, command=self.cancelAction, text="Cancel")

		self.label.grid(column=0, row=0, columnspan=3, sticky=W, pady=5)
		self.input.grid(column=0, row=1, columnspan=3)
		self.ok.grid(column=0, row=3, sticky=W+E, pady=(20, 0))
		self.cancel.grid(column=2, row=3, sticky=W+E, pady=(20, 0))

		self.input.focus()

	def close(self):
		InputBox.isVisible = False
		self.destroy()

	def submit(self):
		result = self.root.addLink(self.input.get())

		if (result):
			self.master.refreshList()
			self.close()

	def cancelAction(self):
		self.close()

class AboutWindow(Toplevel):
	IsVisible = False
	AboutText = "YouTube-DL – Graphical Userinterface\n\n" \
				"(C) 2016, Massive Dynamic by Michael Ochmann"
	def __init__(self, root):
		self.root = root
		Toplevel.__init__(self, width=300, height=100)
		self.setup()
		InputBox.IsVisible = True

	def setup(self):
		self.configure(padx=5, pady=5,)
		self.title("About Youtube-DL")
		self.icon          = PhotoImage(file="icons/logo_mike-ochmann.de.png")
		self.label    = Label(self, text=AboutWindow.AboutText)
		self.branding = Label(self, image=self.icon)
		self.ok       = Button(self, text="OK", command=self.destroy)

		self.label.grid(column=0, row=0, columnspan=3, pady=(40,0), padx=20, sticky=W)
		self.branding.grid(column=1, row=1, sticky=W+E, pady=30)
		self.ok.grid(column=1, row=2, sticky=W+E, pady=(0,10))