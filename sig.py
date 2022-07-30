class Signal:
	def __init__(signal):
		signal.callbacks = {}

	def connect(signal, func):
		signal.callbacks[func] = None

		def disconnect():
			del signal.callbacks[func]

		return disconnect

	def fire(signal, *args):
		for func in signal.callbacks:
			func(*args)