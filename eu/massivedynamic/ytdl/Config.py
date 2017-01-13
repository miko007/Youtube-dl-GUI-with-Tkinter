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
		lines = []
		for option in self.options:
			lines.append(option + ':' + self.options[option] + '\n')
		with open(Config.File, "rw+") as filepointer:
			filepointer.truncate()
			filepointer.writelines(lines)
			filepointer.close()