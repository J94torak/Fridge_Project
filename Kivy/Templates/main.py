import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from connected import ConnectedApp

class Login(Screen):
	def do_login(self, loginText, passwordText):
		print("login : %s || pass : %s" % (loginText, passwordText) )
		self.manager.current = self.manager.next()

	def resetForm(self):
		self.ids['login'].text = ""
		self.ids['password'].text = ""

class LoginApp(App):
	def build(self):
		manager = ScreenManager()

		# ajout de l'instance de login
		manager.add_widget(Login(name='login'))

		# ajout de la vue 'connected'
		app = ConnectedApp()
		app.load_kv()
		connectedView = app.build()
		manager.add_widget(connectedView)

		manager.transition = SlideTransition(direction="left")
		return manager

if __name__ == '__main__':
	LoginApp().run()
