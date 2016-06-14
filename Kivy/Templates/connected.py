import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Connected(Screen):
	def disconnect(self):
		self.manager.transition = SlideTransition(direction="right")
		self.manager.current = 'login'
		self.manager.get_screen('login').resetForm()

class ConnectedApp(App):
	def build(self):
		screen = Connected()
		screen.name = 'connected'
		return screen

# standalone usage
if __name__ == '__main__':
	ConnectedApp().run()
