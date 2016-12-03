class Config():
	File = "ytdl.cnf"
	def __init__(self):
		self.options = {}
		self.load()

	def load(self):
		with open(Config.File) as filepointer:
			for line in filepointer:
				if (line.isspace()):
					continue
				data = line.split(':')
				self.options[data[0]] = data[1].strip()

	def save(self):
		filepointer = open(Config.File, "rw+")
		for option in self.options:
			filepointer.write(option + ':' + self.options[option] + '\n')
