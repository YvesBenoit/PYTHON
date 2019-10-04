# Pour chaque prénom, afficher la longueur du prénom avec la fonction len. 
# Ajouter une variable maximum au début du programme qui vaut 0 au début. 
# Pour chaque prénom, si la longueur du prénom est supérieur au maximum, remplacer maximum par cette valeur. 
# Afficher le prénom le plus long à la fin avec un message : "le prénom le plus long est <prénom>, il possède <nb_lettres> lettres"

prenoms_promo = ["Andrea", "Carole", "Nicolas", "Franck L", "Franck T", "Vincent", "Jean-Marc", "Nicolas", "Guillaume",
"Philippe", "Yves", "Benoît", "Pierre", "Sylvain", "Frédéric"]

prenoms_promo.sort()

maximum = 0
plus_long_prenom =""

for apprenant in prenoms_promo :
    print(apprenant +" : lg = "+ str(len(apprenant)))
    if len(apprenant)>maximum :
        maximum=len(apprenant)
        plus_long_prenom=apprenant

print ("le prénom le plus long est "+plus_long_prenom)
print (" il possede "+str(maximum)+" lettres ")
print(" il peut y en avoir d'aussi long mais il seront apres "+plus_long_prenom+" par ordre alphabetique")