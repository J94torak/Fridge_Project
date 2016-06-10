#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requete
import Produit

detection = Produit()
produit1 = Produit.Produit("20056124")
produit2 = Produit.Produit("3254560045217")
 
produit1.detection()
nom = produit1.nom
description = produit1.description
calories = produit1.calories

print nom
print description
print calories  
      
# liste =["tomate","salade","concombre","citron","thon","basilic frais"]
# plat ="entree"
# recettes = requete.ingredients(liste,plat)
# requete.affiche(recettes)
# choix ="Salade d'été d'Elvire"
# ingredients = requete.recette(choix, recettes)
# print ingredients 
#  
# pourcentage = requete.pourcentage(ingredients,liste)
# print pourcentage