#-*- coding:utf-8 -*-
import requete


produit1 = requete.detection("20056124")
produit2 = requete.detection("3254560045217")

for p in  produit1:
    print p
for p in produit2:
    print p
    
    
liste =["tomate","salade","concombre","citron","thon","basilic frais"]
plat ="entree"
recettes = requete.ingredients(liste,plat)
requete.affiche(recettes)
choix ="Salade de concombres au thon"
ingredients = requete.recette(choix, recettes)
print ingredients 

pourcentage = requete.pourcentage(ingredients,liste)
print pourcentage