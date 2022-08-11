#variables should represent an idea
class sorty:
	def __init__(self):
		self.s=[]#scores
		self.v={}#values
		self.sorted={}#sorted

	def set(self,s,v):
		try:
			if self.v[s]:
				print('score already exists:',s)
		except:
			self.s.append(s)
			self.v[s]=v
			self.sort()#update state :L (even if it doesn't need to be updated)

		def 消():
			self.s.remove(s)
			del self.v[s]
			self.sort()#update state :L (even if it doesn't need to be updated)

		return 消

	def sort(self):
		self.s.sort()
		self.sorted={}
		i=0
		for s in self.s:
			self.sorted[i]=self.v[s]
			i+=1