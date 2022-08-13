class Caller:
	def __init__(self):
		self.callers={}

	def connect(self,fn):
		self.callers[fn]=None
		def delete():
			del self.callers[fn]
		return delete

	def fire(self,*args):
		for fn in self.callers:
			fn(*args)