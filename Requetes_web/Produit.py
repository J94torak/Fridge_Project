# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests 
import shutil

class Produit:

	site = "http://fr.openfoodfacts.org/produit/"		
	def __init__(self,codebarre):

		self.codebarre = codebarre
		self.nom = ""
		self.description =""
		self.calories = ""
		
		
	def detection(self):
		produit = Produit.site + self.codebarre
		r = requests.get(produit)
		k = r.text
		soup = BeautifulSoup(k, 'html.parser')
		self.nom = soup.html.head.title.string 
		self.description = soup.find('span', itemprop="description").contents[0]
		c = soup.find('td', property="food:energyPer100g")
		self.calories = c.contents[0] + " " + c.contents[2] + " Pour 100g"
		
		
		balise = soup.find('meta', property="og:image")
		url = balise['content']
		response = requests.get(url)
		nom_image = '/Users/Clemence/git/Fridge_Project/Requetes_web/Pictures/'+self.codebarre + '.png'
		if response.status_code == 200:
			f = open(nom_image, 'wb')
			f.write(response.content)
			f.close()
