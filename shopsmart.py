from class_shopsmart import Utilisateur 
import hashlib
import os
users = []

def hash_mot_de_passe(mdp):
    salage = os.urandom(32) #On gènere un sel(valeurs aléatoire avant le hash) de 32 bytes car plus difficile pour un hackeur de pré-calculer avec un rainbow-table. Plus il est long, plus le risque d'avoir le meme sel qu'un autre utilisateur est faible.
    clé = hashlib.pbkdf2_hmac( #Applique le hashage sha en boucle plein de fois sur le mdp + sel
        'sha256', #Algorithme de hachage utilisé
        mdp.encode('utf-8'), #Mot de passe transformé en bytes
        salage, #Le sel généré avant
        100000 #Nb d'itérations pour ralentir le calcul du hachage, un attaquant peut tester milliards de mdp par seconde, la il doit faire 100000x plus de calculs par essai. 
    )
    return salage + clé #Concaténation du sel et clé 

def inscription():
    nom = input("Quel est votre nom ? ")
    email = input("Quel est votre email ? ")
    role = input("Voulez vous etre admin ou client ? ")
    while role != 'admin' and role != 'client':
        role = input("Voulez vous etre admin ou client ? ")
    
    mdp = input("Choisisez un mdp")
    mdp_hasher = hash_mot_de_passe(mdp)
    nouvel_utilisateur = Utilisateur(id, nom, email,role,mdp_hasher)
    users.append(nouvel_utilisateur)
    print(mdp_hasher)
    return nouvel_utilisateur

inscription()
print(users)
