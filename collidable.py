from v2 import v2,null2
from cm2 import cm2
from block import Block,block_p

collidables=[]

def raycast(r):
	fh=r.l
	fn=null2
	for m in collidables:
		h,n=m.push_point(r)
		if h<fh:
			fh=h
			fn=n
	return fh,fn

class Collidable:#lets do some inheritance
	def __init__(self,p,o,s,c,a):
		self.block=Block()
		self.i=len(collidables)
		collidables.append(cm2([null2]))
		self.transform(p,o,s,c,a)

	def __del__(self):
		return
		print('del',self)

	def transform(self,p,o,s,c,a):
		self.block.transform(p,o,s,c,a)
		i8=8*self.block.i
		collidables[self.i].update_vertices([
			v2(block_p[i8+0],block_p[i8+1]),
			v2(block_p[i8+2],block_p[i8+3]),
			v2(block_p[i8+4],block_p[i8+5]),
			v2(block_p[i8+6],block_p[i8+7])
		])