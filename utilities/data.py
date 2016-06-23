last_frame = {
    "depth": [],
    "image": [],
    "reserved": True,
}

class Seen:
	value = []
	anything = False
	def add(self, item):
		self.value.append(item)
		self.anything = True

	def get(self):
		export = self.value
		self.value = []
		self.anything = False
		return export

seen = Seen()

playing = True