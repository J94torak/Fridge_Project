#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import Recette
import Produit


# produit1 = Produit.Produit("20056124")
# produit2 = Produit.Produit("3254560045217")
#  
# produit1.detection()
# nom = produit1.nom
# description = produit1.description
# calories = produit1.calories
# 
# print nom
# print description
# print calories  
#       
liste =["tomate","salade","concombre","citron","thon","basilic frais"]
plat ="entree"

recettes = Recette.Recettes(liste,plat)
recettes.choix()
recettes.aff_choix()
choix_recette ="Salade d'été d'Elvire"

recettes.ingredients(choix_recette)
recettes.aff_ingredients()

recettes.do_pourcentage()
recettes.aff_pourcentage()