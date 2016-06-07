#/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests 
import re 


def ingredients(n):
	
	liste = n[0]
	for k in n:
		if k != n[0]:
			liste = liste +"-"+k
	
	ingre = {'aqt': liste}
	r = requests.get("http://www.marmiton.org/recettes/recherche.aspx?", params=ingre)
	k = r.text
	soup = BeautifulSoup(''.join(k))
	list_recette = 0
	i =0
	while i<9:
	
		sponso = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"+str(i)+"_m_panelResul"
		rsponso =  soup.find('div', id =sponso)
		if rsponso['class'] != ['m_item','recette_sponso']:
			m = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"+str(i)+"_m_linkTitle"
			recettes = soup.find('a', id =m)
			liste_recette[recettes['title']] = recettes['href']
		i+=1
	print liste_recette

def recette(n):
	#liste = n[0]
	#for k in n:
	#	if k != n[0]:
	#		liste = liste +"-"+k
	#recette = requests.get("http://www.marmiton.org/recettes/recette_", params = liste)
	#k = r.text
	#soup = BeautifulSoup(''.join(k))
	#print r.url
	a = ["jambon","oeuf"]
	j = ingredients(a)
	return j
		
		
def detection(n):

	site = "http://fr.openfoodfacts.org/produit/"
	codebarre = n
	produit = site + codebarre
	r = requests.get(produit)
	k = r.text
	soup = BeautifulSoup(''.join(k))
	titleTag = soup.html.head.title 
	calorie = soup.find('td', property="food:energyPer100g")
	description = soup.find('span', itemprop="description")
	return [titleTag.string, description.contents[0], calorie.contents[0] + " " + calorie.contents[2] + " Pour 100g"]
	
