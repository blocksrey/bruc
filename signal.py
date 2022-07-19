class signal:
	def __init__(self):
		self.callbacks = {}

	def connect(self, func):
		self.callbacks[func] = None

		def disconnect():
			del self.callbacks[func]

		return disconnect

	def fire(self, *args):
		for func in self.callbacks:
			func(*args)