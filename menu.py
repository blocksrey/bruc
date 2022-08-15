import os
from json import load
import pyglet

data=load(open('settings.json'))


pyglet.options['vsync']=True

background_color=(1,1,1)

pyglet.font.add_directory(f"gui/fonts/{data['font-family']}")

font=data['font-family']
font=font.replace('sans-alternates','Montserrat Alternates')
font=font.replace('sans-serif','Playfair Display')
font=font.replace('sans','Montserrat')

data={
	'song':'Bruc said what?',
	'music':0,
	'effects':0,
	'fps':0,
	'username':None,
}

player_stats=f'''
<h5>Player statistics</h5>
<br>
<em>Kills:</em> 0
<br>
<em>Gold:</em> 100
<br>
<em>Wins:</em> 5
<br>
<em>Defeats:</font></em> 1
</font>
'''

screen=pyglet.canvas.Display().get_default_screen() # Get pyglet screen

title=pyglet.resource.image('gui/title.png')
play=pyglet.resource.image('gui/play.png')
exit=pyglet.resource.image('gui/exit.png')
blue_button_normal=pyglet.resource.image('gui/blue_button_normal.png')
blue_button_hover=pyglet.resource.image('gui/blue_button_hover.png')
blue_button_press=pyglet.resource.image('gui/blue_button_press.png')
checkbox_true=pyglet.resource.image('gui/checkbox_true.png')
checkbox_false=pyglet.resource.image('gui/checkbox_false.png')
checkbox_hover=pyglet.resource.image('gui/checkbox_hover.png')

music={
	'Bruc said what?':'sounds/track1.ogg',
	'Yeah Bruc said that':'sounds/track2.ogg',
	'What you say to Bruc':'sounds/track3.ogg'
}

pyglet.options['advanced_font_features']=True


class TextWidget:
	def __init__(self,text,x,y,width,window,font):
		self.document=pyglet.text.document.UnformattedDocument(text)
		self.document.set_style(0,len(self.document.text),dict(color=(0,0,0,255),font_name=font))

		font=self.document.get_font()
		height=font.ascent-font.descent+15

		self.layout=pyglet.text.layout.IncrementalTextLayout(self.document,width,height)
		self.layout.position=x,y+10
		self.layout.anchor_y='center'

		self.caret=pyglet.text.caret.Caret(self.layout)

		# Rectangular outline
		pad=5

		self.rectangle=pyglet.shapes.BorderedRectangle(x-pad,y-pad+7,width+pad,height+pad,3,border_color=(148,148,148))

		window.push_handlers(self)

	def draw(self):
		self.rectangle.draw()
		self.layout.draw()

	def on_mouse_motion(self,x,y,dx,dy):
		self.rectangle.border_color=148,148,148

		if self.hit_test(x,y):
			self.rectangle.border_color=100,100,100

	def on_mouse_press(self,x,y,buttons,modifiers):
		if self.hit_test(x,y):
			self.layout.document.text=''

	def hit_test(self,x,y):
		return \
			0<x-self.layout.x<self.layout.width and \
			0<y-self.layout.y<self.layout.height


class Window(pyglet.window.Window):

	def __init__(self,*args,**kwargs):
		pyglet.window.Window.__init__(self,666,519,'',0,style=Window.WINDOW_STYLE_DIALOG)

		self.batch=pyglet.graphics.Batch()

		self.entry=TextWidget('Enter username',333,229,230,self,font)

		self.frame=pyglet.gui.Frame(self)

		try:
			self.background=pyglet.graphics.OrderedGroup(0)
		except:
			self.background=pyglet.graphics.Group(order=0)

		self.play_button=pyglet.gui.PushButton(450,93,
												 blue_button_press,
												 blue_button_normal,
												 blue_button_hover,
												 batch=self.batch,
												 group=self.background
												)

		self.exit_button=pyglet.gui.PushButton(450,23,
												 blue_button_press,
												 blue_button_normal,
												 blue_button_hover,
												 batch=self.batch,
												 group=self.background
												)

		self.music_button=pyglet.gui.ToggleButton(333,440,
													checkbox_false,
													checkbox_true,
													checkbox_true,
													batch=self.batch
												   )

		self.effects_button=pyglet.gui.ToggleButton(333,380,
													  checkbox_false,
													  checkbox_true,
													  checkbox_true,
													  batch=self.batch
													 )

		self.fps_button=pyglet.gui.ToggleButton(333,320,
												  checkbox_false,
												  checkbox_true,
												  checkbox_true,
												  batch=self.batch
												 )

		self.frame.add_widget(self.play_button)
		self.frame.add_widget(self.exit_button)
		self.frame.add_widget(self.music_button)
		self.frame.add_widget(self.effects_button)
		self.frame.add_widget(self.fps_button)

		try:
			self.foreground=pyglet.graphics.OrderedGroup(1)
		except:
			self.foreground=pyglet.graphics.Group(0)

		self.play_label=pyglet.text.Label('Play',font_name=font,font_size=14,
											 x=500,y=113,color=(0,0,0,255),
											 batch=self.batch,group=self.foreground)

		self.exit_label=pyglet.text.Label('Exit',font_name=font,font_size=14,
											x=500,y=43,color=(0,0,0,255),
											batch=self.batch,group=self.foreground)

		self.music_label=pyglet.text.Label('Play music',font_name=font,font_size=12,
											 x=393,y=450,color=(0,0,0,255),
											 batch=self.batch,group=self.foreground)
		self.effects_label=pyglet.text.Label('Play effects',font_name=font,font_size=12,
											 x=393,y=390,color=(0,0,0,255),
											 batch=self.batch,group=self.foreground)
		self.effects_label=pyglet.text.Label('Show fps',font_name=font,font_size=12,
											 x=393,y=330,color=(0,0,0,255),
											 batch=self.batch,group=self.foreground)

		self.player_stats=pyglet.text.HTMLLabel(player_stats,x=23,y=200,
												  multiline=True,width=280,
												  batch=self.batch
												 )
		self.credits=pyglet.text.Label('Gameplay and design by Team 7Teen.',
										 font_name=font,font_size=9,
										 x=23,y=20,color=(0,0,0,255),
										 batch=self.batch
										)

		self.title=pyglet.sprite.Sprite(title,20,self.height-100,batch=self.batch)
		self.play=pyglet.sprite.Sprite(play,456,101.5,batch=self.batch,group=self.foreground)
		self.exit=pyglet.sprite.Sprite(exit,456,31,batch=self.batch,group=self.foreground)

		self.play.scale=0.75
		self.exit.scale=0.75

		self.labels=[]

		x=425

		for value in music:
			x -= 20
			label=pyglet.text.Label(value,font_name=font,font_size=11,
									  x=28,y=x,color=(0,0,0,255),
									  batch=self.batch,group=self.foreground)
			self.labels.append(label)

		self.box=pyglet.shapes.BorderedRectangle(23,230,280,195,border=3,batch=self.batch)

		self.play_button.set_handler('on_release',self._play)
		self.exit_button.set_handler('on_release',self._exit)
		self.music_button.set_handler('on_toggle',self.music)
		self.effects_button.set_handler('on_toggle',self.effects)
		self.fps_button.set_handler('on_toggle',self.fps)

		self.music_button.value=True
		self.effects_button.value=True
		self.fps_button.value=True

	def _play(self):
		'Called when the play button is pressed.'

		data['username']=self.entry.layout.document.text
		self.close()

	def _exit(self):
		'Called when the exit button is pressed.'

		os._exit(0)

	def music(self,value):
		'Called when the music checkbox is pressed.'

		print(value)

		data['music']=value

	def effects(self,value):
		'Called when the effects checkbox is pressed.'

		data['effects']=value

	def fps(self,value):
		'Called when the fps checkbox is pressed.'

		data['fps']=value

	def on_draw(self):
		pyglet.gl.glClearColor(1,1,1,1)

		self.clear()
		self.batch.draw()
		self.entry.draw()

	def on_mouse_motion(self,x,y,dx,dy):
		for label in self.labels:
			if \
				x>label.x-label.content_width and \
				x<label.x+label.content_width and \
				y>label.y-label.content_height and \
				y<label.y+label.content_height:
				label.document.set_style(0,len(label.text),dict(font_size=12))
			else:
				label.document.set_style(0,len(label.text),dict(font_size=11))

	def on_mouse_press(self,x,y,button,modifiers):
		for label in self.labels:
			if \
				x>label.x-label.content_width/2 and \
				x<label.x+label.content_width/2 and \
				y>label.y-label.content_height/2 and \
				y<label.y+label.content_height/2:
				label.document.set_style(0,len(label.text),dict(bold=True))
				data['song']=music[label.document.text]

				for _label in self.labels:
					if _label==label:
						break
					_label.document.set_style(0,len(label.text),dict(bold=0))
			else:
				label.document.set_style(0,len(label.text),dict(bold=0))

		self.entry.caret.on_mouse_press(x,y,button,modifiers)

	def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
		self.entry.caret.on_mouse_drag(x,y,dx,dy,buttons,modifiers)

	def on_text(self,text):
		self.entry.caret.on_text(text)

	def on_text_motion(self,motion):
		self.entry.caret.on_text_motion(motion)

	def on_text_motion_select(self,motion):
		self.entry.caret.on_text_motion_select(motion)

	def on_close(self):
		# Break out of the whole application event loop
		os._exit(0)

Window()

#pyglet.app.run()