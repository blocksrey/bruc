class Sorter:
	def __init__(self):
		self.scores = []
		self.values = {}
		self.sorted = {}

	def set(self, score, value):
		try:
			if self.values[score]:
				print("Score already exists: ", score)
		except:
			self.scores.append(score)
			self.values[score] = value
			self.sort() # update state :L (even if it doesn't need to be updated)

		def delete():
			self.scores.remove(score)
			del self.values[score]
			self.sort() # update state :L (even if it doesn't need to be updated)

		return delete

	def sort(self):
		self.scores.sort()
		self.sorted = {}
		index = 0
		for score in self.scores:
			self.sorted[index] = self.values[score]
			index += 1