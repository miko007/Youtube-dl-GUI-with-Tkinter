from eu.massivedynamic.ytdl.ui.Window import *
from eu.massivedynamic.ytdl.yt.Video import Title
from eu.massivedynamic.ytdl.Config import Config
from subprocess import call
import re
import time

class Item:
	def __init__(self, url, title):
		self.url = url
		self.title = title

class App:
	def __init__(self):
		self.outputFormats = [
			"best",
			"aac",
			"vorbis",
			"mp3",
			"m4a",
			"opus",
			"wav"
		]
		self.config = Config()
		self.defaultFormat = self.config.options["format"]
		self.list = []
		self.mainwindow = Window(self)
		self.run()

	def showAddLink(self):
		if (not InputBox.isVisible):
			self.input = InputBox(self)

	def addLink(self, link):
		if (len(link) == 0 or not re.search(r"https://www\.youtube\.com/watch\?v=[a-zA-Z0-9]+", link)):
			return False
		title = Title(link)
		self.list.append(Item(link, title.title()))

		return True

	def removeLink(self, selection):
		temp = []
		i = 0
		for item in self.list:
			if (not i in selection):
				temp.append(item)
			i = i + 1
		self.list = temp

	def download(self):
		amount = len(self.list)
		i = 0
		for item in self.list:
			call(["youtube-dl", "--extract-audio", "--audio-format", self.defaultFormat, item.url, "-o", self.config.options["path"] + "/%(title)s.%(ext)s"])
			i = i + 1
			self.mainwindow.setProgress(i * 100 / amount)
			time.sleep(.300)
		self.list = []

	def run(self):
		self.mainwindow.mainloop()

	def inputNewLink(self):
		popup = InputBox(self)