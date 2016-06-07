import requete

liste =["tomate","salade","concombre","citron"]
plat ="entree"
recettes = requete.ingredients(liste,plat)
requete.affiche(recettes)
choix ="Salade de tomates et concombres sauce menthe"
requete.recette(choix, recettes)
