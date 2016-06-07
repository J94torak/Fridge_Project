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
		if rsponso['class'] != [u'm_item', u'recette_sponso']:
			m = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"+str(i)+"_m_linkTitle"
			recettes = soup.find('a', id =m)
			print recettes['title']
			liste_recette[recettes['title']] = recettes['href']
		i+=1
	return liste_recette

def affiche(liste):
	for k in liste.keys():
	     	print(k)

def recette(n, liste):
	j =u'é'
	l=u'é'
	#if j == l:
	#	print j
	for k in liste.keys():
		print k
		print n
		if n == k:
			site = "http://www.marmiton.org"+liste[n]
			recette = requests.get(site)
			r = recette.text
			soup = BeautifulSoup(r, 'html.parser')
			print recette.url
			ingredients =soup.find('span',itemprop="ingredients")
			print ingredients.contents
			#for span in soup.findAll('span',itemprop="ingredients"):
			#	print span.contents[0]
			#print soup.findAll('span',itemprop="ingredients")
		
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
	print titleTag.string
	print description.contents[0]
	print calorie.contents[0] + " " + calorie.contents[2] + " Pour 100g"
