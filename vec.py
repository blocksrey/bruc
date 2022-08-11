#geometric functions
class Vec:
	def project(a,n):
		return a-n*a.dot(n)

	def reflect(a,n):
		return a-n*a.dot(n)*2