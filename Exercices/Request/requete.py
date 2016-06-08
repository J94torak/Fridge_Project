#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests 
import re 


def ingredients(n,plat):
	
	liste = n[0]
	for k in n:
		if k != n[0]:
			liste = liste +"-"+k
			
	ingre = {'aqt': liste, 'dt' : plat}
	r = requests.get("http://www.marmiton.org/recettes/recherche.aspx/get", params=ingre)
	k = r.text
	#soup = BeautifulSoup(''.join(k))
	soup = BeautifulSoup(k, 'html.parser')
	liste_recette = {}
	i =0
	while i<9:
	
		sponso = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"+str(i)+"_m_panelResul"
		rsponso =  soup.find('div', id =sponso)
		if rsponso['class'] != ['m_item','recette_sponso']:
			m = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"+str(i)+"_m_linkTitle"
			recettes = soup.find('a', id =m)
			liste_recette[recettes['title']] = recettes['href']
		i+=1
	return liste_recette


def affiche(liste):
	for k in liste.keys():
	     	print(k)

def recette(n, liste):
	for k in liste.keys():
		if n in k:
			site = "http://www.marmiton.org"+liste[n]
			recette = requests.get(site)
			r = recette.text
			#soup = BeautifulSoup(''.join(r))
			soup = BeautifulSoup(r, 'html.parser')
			i = soup.find('div', class_ ="m_content_recette_ingredients m_avec_substitution")
			
			ingredients =""
			
			for child in i.strings:
				ingredients = ingredients + child
			
			return ingredients
		
			
def pourcentage(recette,frigo):
	
		ingre_recette =0
		i = 0
		ingre_frigo =0 
		
		for aliments in frigo :
			if aliments in recette: 
				ingre_frigo +=1
				
		while i < len(recette):
			if recette[i] =="-":
				ingre_recette +=1 
			i += 1
		
		pourcentage = ingre_frigo*100/ingre_recette
		return pourcentage
			
			
			
def detection(n):

	site = "http://fr.openfoodfacts.org/produit/"
	codebarre = n
	produit = site + codebarre
	r = requests.get(produit)
	k = r.text
	soup = BeautifulSoup(k, 'html.parser')
	titleTag = soup.html.head.title 
	calorie = soup.find('td', property="food:energyPer100g")
	description = soup.find('span', itemprop="description")
	return [titleTag.string,description.contents[0], calorie.contents[0] + " " + calorie.contents[2] + " Pour 100g"]
