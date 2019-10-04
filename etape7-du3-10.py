# Etape 7 : Entrées / Sorties

#     Créer un programme qui demande à l'utilisateur de se présenter : prénom, nom et age. 
#           Utilisez la console pour afficher un message d'accueil personnalisé du type "Bonjour Jules Grand tu as 30 ans c'est bien ça ?"
#     Créer un programme qui fera la même chose tout en écrivant les informations reçues dans un fichier texte. Le fichier devra être nommé prenom-nom.txt
#     Créer un programme qui va lire le fichier films-2018.txt et indiquer combien il y a de films sortis en 2018.

# Bonus

#     Créer un programme qui va lire le fichier villes-france.txt et indiquer combien de fois apparaît TOULOUSE dans le fichier.
#     Créer un programme qui va lire le fichier villes-france.txt et créer un nouveau fichier sans doublons (après modification, 
#           le nouveau fichier ne doit contenir qu'une seule fois le même nom de ville).
#     Créer un programme qui va lire le fichier villes-france.txt et créer un nouveau fichier dans lequel chaque 
#       ligne donnera le nom d'une ville en affichant le nombre d’occurrence dans le fichier de départ. Ce fichier devra être trié par ordre alphabétique.
def afficher_utilisateur(prenom, nom , age):
    print( "From afficher  : Bonjour " + prenom + " " + nom + " tu as " + str(age) + " ans c'est bien ça ? " )

def questionner_utilisateur(prenom, nom , age):
    # return [prenom_utilisateur, nom_utilisateur, age_utilisateur]
    # prenom = input("Bonjour, quel est ton prénom ? ")
    # nom = input("          quel est ton nom ? ")
    # age = input("          quel est ton age ? ")
    prenom ="Yves"
    nom="Benoit"
    age=53
    
    return prenom, nom, age

prenom_utilisateur="init prenom"
nom_utilisateur="init nom"
age_utilisateur=0

questionner_utilisateur(prenom_utilisateur, nom_utilisateur ,age_utilisateur)
afficher_utilisateur(prenom_utilisateur, nom_utilisateur ,age_utilisateur) 

fic_name = prenom_utilisateur+"-"+nom_utilisateur
print(fic_name)

f = open('~/Bureau/PYTHON/'+fic_name, 'w')
f.write(prenom_utilisateur , nom_utilisateur , age_utilisateur)
f.close()
