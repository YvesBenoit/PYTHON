print ("Ex 1")
mystery1 = 8+6
mystery2 = 8-6

print("mystery2 = "+str(mystery2))
print()

print ("Ex 2")
zebrasInZoo =8
giraffeInZoo = 4
animalsInbZoo = zebrasInZoo+giraffeInZoo
print(animalsInbZoo)
print()



print ("Ex 3")
prixInitial = 1500
tva = 0.20
prixFinal =prixInitial+prixInitial*tva
print(prixFinal)

print()


print ("Ex 4.1")
nbOeufsParBoite = 6
nbOeufsTotal = 145

nbBoites=nbOeufsTotal//nbOeufsParBoite
nbOeufRestant = nbOeufsTotal%nbOeufsParBoite
print("nbBoites :"  +str( nbBoites))
print("nbOeufRestant :"  +str(nbOeufRestant))
print()

print("Ex 4.2")

numeroCarteMystere = 28
numeroCouleur=numeroCarteMystere//8
print(numeroCouleur)
numeroFigure=(numeroCarteMystere-(numeroCouleur*8))
print(numeroFigure)

print()

print ("Ex 5")
budget=2000
budgetSuffisant =budget>=(prixInitial*tva)
print("budget suffisant ? :"+str(budgetSuffisant))

print()


print ("Ex 6")
songsA = 9
songsB = 9
albumLengthA = 41
albumLengthB = 53
sameSongs=songsA==songsB
print(sameSongs)
sameAlbumLength = albumLengthA==albumLengthB
print(sameAlbumLength)

print()


print ("Ex 7")


formateur = 'Jules'
langage = 'java'
version = 1.8

description="Mon formateur "+formateur+" est fan de "+langage+", surtout depuis la version "+str(version)
print(description)