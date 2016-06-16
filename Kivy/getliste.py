from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
import requests
from bs4 import BeautifulSoup

racine=Builder.load_string('''
<Ecran>
    FloatLayout:
        Button:
            text: 'Liste elements'
            size_hint: 0.33, 0.33
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: root.requete()
''')
 
class Ecran(FloatLayout):
 
    def requete(self):
        k = """
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>Liste des ingredients dans le frigo</title>
            </head>
            <body>
            <table>
                <tr>
                    <td>Nom</td>
                    <td>Description</td>
                    <td>Calories</td>
                </tr>
                <tr>
                    <td>Moutarde</td>
                    <td>Moutarde de Dijon fabrique en France</td>
                    <td>100 kcal pour 100g</td>
                    <td><img src="images/montagne.jpg" alt="Photo de montagne" /></td>
                </tr>
            </table> 
            </body>
        </html>"""
        soup = BeautifulSoup(k, 'html.parser')
        texte =soup.text
        t =soup.findAll('tr')
        tab =[]
        for link in soup.findAll('tr'):
            elem =[]
            for l in link.findAll('td'):
                texte = str(l.get_text())
                elem.append(texte)
            tab.append(elem)
        print tab
            
class MonAppli(App):
 
    def build(self):
        return Ecran()
 
MonAppli().run()