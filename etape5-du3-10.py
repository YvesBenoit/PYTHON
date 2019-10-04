
prenoms_promo = ["Andrea", "Carole", "Nicolas", "Franck L", "Franck T", "Vincent", "Jean-Marc", "Nicolas", "Guillaume",
"Philippe", "Yves", "Benoît", "Pierre", "Sylvain", "Frédéric"]
prenoms_promo.sort()
print ("prenoms promo entiere")
print (prenoms_promo [0:])  

print ("prenoms promo impairs")
print (prenoms_promo[1::2])

lgliste =len(prenoms_promo)
lglisteentier=int(lgliste/2)

print(lgliste)
print(lglisteentier)

groupe1 = prenoms_promo [ 0 : int(lgliste/2)+1 ]
groupe2 = prenoms_promo[int(lgliste/2)+1:]

print ("groupe1")
print (groupe1)

print ("groupe2")
print (groupe2)

