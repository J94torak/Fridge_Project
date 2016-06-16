from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
import requests

racine=Builder.load_string('''
<Ecran>
    FloatLayout:
        Button:
            text: 'Bouton'
            size_hint: 0.33, 0.33
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: root.requete()
''')
 
class Ecran(FloatLayout):
 
    def requete(self):
        r =requests.get("http://fr.openfoodfacts.org/produit/")
        print  r.status_code
            
class MonAppli(App):
 
    def build(self):
        return Ecran()
 
MonAppli().run()