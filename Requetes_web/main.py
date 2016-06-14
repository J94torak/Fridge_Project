#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import Recette
import Produit
import Requete

produit1 = Requete.Produit("20056124")
produit2 = Requete.Produit("3254560045217")
  
valide = produit2.detection()
if valide ==1:
    nom = produit2.nom
    description = produit2.description
    calories = produit2.calories

    print nom
    print description
    print calories 
 
       
liste =["tomate","salade","concombre","citron","thon","basilic frais","mais"]
plat ="entree"

recettes = Requete.Recettes(liste,plat)
recettes.choix()
recettes.aff_choix()
choix_recette ="Salade d'été d'Elvire"

recettes.ingredients(choix_recette)
recettes.aff_ingredients()

recettes.do_pourcentage()
recettes.aff_pourcentage()