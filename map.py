from collidable import Collidable
from v2 import v2,cang
from v3 import v3

spawns=[]

char_c={}
char_c['w']=v3(41,200,18)/255
char_c['C']=v3(0.7,0.9,0.7)
char_c['-']=v3(0.8,0.5,0.4)

char_c['^']=v3(242,27,63)/255
char_c['>']=v3(242,27,63)/255
char_c['<']=v3(242,27,63)/255

char_c['J']=v3(255,153,20)/255

char_c['|']=v3(0.5,0.75,1)

char_c['W']=v3(8,189,189)/255

char_c['P']=v3(0,0,0.2)

class Map:
	def __init__(self,path):
		iy=0
		for row in open(path).readlines():
			ix1=0

			ix=0
			ch=row[0]

			for ch1 in row:
				if ch!=ch1:
					sx=ix1-ix

					p=v2(2*ix,-4*iy)
					s=v2(2*sx,4)

					if ch=='-':
						Collidable(p+0.5*s+v2(0,0.45*s.y),cang(0),v2(s.x,0.1*s.y),char_c[ch],1)
					elif ch!=' ':#newline case is handled naturally :P:P
						Collidable(p+0.5*s,cang(0),s,char_c[ch],1)

					if ch=='P':
						spawns.append(p+0.5*s)

					ix=ix1
					ch=ch1

				ix1+=1
			iy+=1

