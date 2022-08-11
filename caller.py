class caller:
	def __init__(self):
		self._c={}

	def connect(self,f):
		self._c[f]=None
		def d():
			del self._c[f]
		return d

	def fire(self,*a):
		for f in self._c:
			f(*a)