# Créer un programme qui va lire le fichier villes-france.txt
# et indiquer combien de fois apparaît TOULOUSE dans le fichier.
oh_toulouse = 0

with open('villes-france.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.rstrip()
        if ligne == 'TOULOUSE' :
            oh_toulouse = oh_toulouse + 1

print("\n---------- Comptage TOULOUSE ----------")
print(f"TOULOUSE apparaît {oh_toulouse} fois dans le fichier.")

# Créer un programme qui va lire le fichier villes-france.txt
# et créer un nouveau fichier sans doublons
# (après modification, le nouveau fichier ne doit contenir
# qu'une seule fois le même nom de ville).
villes = []

fichier_propre = open('./output/villes-france-clear.txt', 'w')

with open('villes-france.txt', 'r') as f:
    for ligne in f:
        if ligne not in villes:
            fichier_propre.write(ligne)
            villes.append(ligne)

fichier_propre.close()

# Créer un programme qui va lire le fichier villes-france.txt
# et créer un nouveau fichier dans lequel chaque ligne donnera
# le nom d'une ville en affichant le nombre d’occurrence dans
# le fichier de départ. Ce fichier devra être trié par ordre
# alphabétique.

villes = {}

fichier_propre = open('./output/villes-france-comptees.txt', 'w')

with open('villes-france.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.rstrip()
        if ligne not in villes:
            villes[ligne] = 1
        else :
            villes[ligne] = villes[ligne] + 1

for nom_ville in villes.keys() :
    fichier_propre.write(f'{nom_ville} : {villes[nom_ville]} occurences.\n')

fichier_propre.close()