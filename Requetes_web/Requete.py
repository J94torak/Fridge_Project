# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests 
import shutil


##################################################################################################
class Produit:

    site = "http://fr.openfoodfacts.org/produit/"        
    def __init__(self,codebarre):

        self.codebarre = codebarre
        self.nom = ""
        self.description =""
        self.calories = ""
        self.image= ""
        
    def detection(self):
        produit = Produit.site + self.codebarre
        r = requests.get(produit)
        k = r.text
        soup = BeautifulSoup(k, 'html.parser') 
        if soup.html.head.title.string != 'Erreur':
            #NOM DESCRIPTION CALORIES DU PRODUIT
            self.nom = soup.html.head.title.string
            self.description = soup.find('span', itemprop="description").contents[0]
            c = soup.find('td', property="food:energyPer100g")
            if c != None:
                self.calories = c.contents[0] + " " + c.contents[2] + " Pour 100g"
            else: 
                self.calories ="Calories inconnu"
            #IMAGE DU PRODUIT
            balise = soup.find('meta', property="og:image")
            if balise != None:
                url = balise['content']
                response = requests.get(url)
                #extension
                url =url[::-1]
                indice = url.find('.')
                extension = url[0:indice+1]
                ext =extension[::-1]
                nom_image = "../Requetes_web/Pictures/"+self.codebarre + ext
                self.image=self.codebarre + ext
                f = open(nom_image, 'wb')
                f.write(response.content)
                f.close()
            else :
                print "Image inconnu"
            return 1
        else :
            print "Code barre invalide "
            return 0
        

##########################################################################################
class Recettes:

    def __init__(self,ing_frigo,plat):
        
        self.ing_frigo =ing_frigo
        self.plat =plat
        self.recettes ={}
        self.ing_recette = ""
        self.pourcentage = 0
        
    def choix(self):
        
        n = self.ing_frigo[0]
        for k in self.ing_frigo:
            if k != self.ing_frigo[0]:
                n = n +"-"+k
                
        ingre = {'aqt': n, 'dt' : self.plat}
        r = requests.get("http://www.marmiton.org/recettes/recherche.aspx/get", params=ingre)
        k = r.text
        soup = BeautifulSoup(k, 'html.parser')
        liste_recette = {}
        i =0
        while i<12:
            if i<10:
                s = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl0"
            else:
                s = "ctl00_cphMainContent_m_ctrlSearchEngine_m_ctrlSearchListDisplay_rptResultSearch_ctl"
            sponso = s +str(i)+"_m_panelResul"
            rsponso =  soup.find('div', id =sponso)
            if rsponso !=None:
                if rsponso['class'] == ['m_item','recette_classique']:
                    m = s+str(i)+"_m_linkTitle"
                    recettes = soup.find('a', id =m)
                    self.recettes[recettes['title']] = recettes['href']
            else :
                print "Aucune recette trouvée"
            i+=1
    
    def ingredients(self,choix_recette):
    
        choix_recette = unicode(choix_recette,'utf-8')
        for k in self.recettes.keys():
            if choix_recette == k:
                site = "http://www.marmiton.org"+self.recettes[choix_recette]
                recette = requests.get(site)
                r = recette.text
                #soup = BeautifulSoup(''.join(r))
                soup = BeautifulSoup(r, 'html.parser')
                i = soup.find('div', class_ ="m_content_recette_ingredients m_avec_substitution")
                if i != None:
                    for child in i.strings:
                        self.ing_recette += child
                else :
                    print "Ingredients introuvable"
                 
                return self.ing_recette
            
                
    def do_pourcentage(self):
        
            ingre_recette =0
            i = 0
            ingre_frigo =0 
            #recette = unicode(recette,'utf-8')
            for aliments in self.ing_frigo :
                if aliments in self.ing_recette: 
                    ingre_frigo +=1
                    
            while i < len(self.ing_recette):
                if self.ing_recette[i] =="-":
                    ingre_recette +=1 
                i += 1
            
            self.pourcentage = ingre_frigo*100/ingre_recette
    
    def aff_choix(self):
        for k in self.recettes.keys():
            print(k)
    
    def aff_ingredients(self):
        print(self.ing_recette)
    
    def aff_pourcentage(self):
        print(self.pourcentage)
    
