#geometric functions
class V:
	def project(a,n):
		return a-a.dot(n)*n

	def reflect(a,n):
		return a-2*a.dot(n)*n