last_frame = {
    "depth": [],
    "image": [],
    "reserved": True,
}

class Adv_queue:
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

seen = Adv_queue()

visualize = Adv_queue()

playing = True