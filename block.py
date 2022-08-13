from v2 import v2,null2
from v3 import null3

block_l=0
block_p=[]
block_c=[]

class Block:
	def __init__(self):
		global block_l
		self.i=block_l
		block_l+=1
		block_p.extend( 8*[None])
		block_c.extend(16*[None])
		self.transform(null2,null2,null2,null3,0)

	def __del__(self):
		return
		print('del',self)

	def transform(self,p,o,s,c,a):
		rx,ry=0.5*s.x,0.5*s.y
		r,g,b=c.x,c.y,c.z
		i8 = 8*self.i
		i16=16*self.i
		block_p[i8+0],block_p[i8+1]=(p+o.cmul(v2(+rx,+ry))).dump()
		block_p[i8+2],block_p[i8+3]=(p+o.cmul(v2(+rx,-ry))).dump()
		block_p[i8+4],block_p[i8+5]=(p+o.cmul(v2(-rx,-ry))).dump()
		block_p[i8+6],block_p[i8+7]=(p+o.cmul(v2(-rx,+ry))).dump()
		block_c[i16+ 0],block_c[i16+ 1],block_c[i16+ 2],block_c[i16+ 3]=r,g,b,a
		block_c[i16+ 4],block_c[i16+ 5],block_c[i16+ 6],block_c[i16+ 7]=r,g,b,a
		block_c[i16+ 8],block_c[i16+ 9],block_c[i16+10],block_c[i16+11]=r,g,b,a
		block_c[i16+12],block_c[i16+13],block_c[i16+14],block_c[i16+15]=r,g,b,a