class Caller:
	def __init__(caller):
		caller.callbacks = {}

	def connect(caller, func):
		caller.callbacks[func] = None

		def disconnect():
			del caller.callbacks[func]

		return disconnect

	def fire(caller, *args):
		for func in caller.callbacks:
			func(*args)