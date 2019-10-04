# Correction de l'exercice maudit
def affiche_numero_couleur(carte_nb) :
    couleur = ["pique", "coeur", "carreau", "trefle"]
    valeur = ["7", "8", "9", "10", "valet", "dame", "roi", "as"]

    couleur_nb = carte_nb // 8
    valeur_nb = carte_nb % 8

    print("la carte est : "+valeur[valeur_nb] + " de " + couleur[couleur_nb])

print()
affiche_numero_couleur(12)