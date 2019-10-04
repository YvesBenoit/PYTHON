import math

def calcul_aire_triangle(base,hauteur) :
    return(base*hauteur/2)


base=10
hauteur=3
aire=calcul_aire_triangle(base,hauteur)
print("base : "+str(base)+" hauteur : "+str(hauteur)+" ==> aire : "+str(aire))
print(f"base : {base} hauteur : {hauteur} ==> aire : {aire}")

def calcul_volume_sphere(rayon) :
    return(4/3*math.pi*(rayon**3))
print(f"sphere (Une decimale arrondie) : {round(calcul_volume_sphere(10),1)}")

volume=calcul_volume_sphere(10)
print("sphere :"+str(volume))

def calcul_IMC(prenom,taille,poid) :
    return(poid/(taille/100)**2)

imc=calcul_IMC("Yves",179,77)
print("IMC :"+str(imc))
