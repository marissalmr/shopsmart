from class_shopsmart import Utilisateur 
import hashlib
import os
users = []



def menu():
     while True : 
          print("Menu : /n 1. Pour vous inscrire /n 2. Pour vous connecter /n")
          choix_user = int(input("Faites votre choix"))
          return choix_user

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
    return nouvel_utilisateur #Permet de pouvoir l'utiliser plus tard, pas concerné par la portée des variables


def connexion():
    tentative_pseudo = input("Entrez votre pseudonyme")
    tentative_mdp = input("Entrez votre mot de passe")
    verification = verifier_mdp(tentative_mdp)
    while verification == False : 
            verification = verifier_mdp(tentative_mdp)


def verifier_mdp(mdp_hasher): #Obligé car on peut pas comparer un mdp hasher à un mdp normal 
    sel = mdp_hasher[:32] #extraction du sel car c'est les 32 premier caractères
    cle = mdp_hasher[32:] #extraction de la clé = 32 dernier caractères
    tentative_mdp = connexion() #Je récuppere la tentative de l'user
    nouvelle_cle =  hashlib.pbkdf2_hmac( #Je refais le meme hash, sur la tentative en utilisant le meme sel
        'sha256',
        tentative_mdp.encode('utf-8'),
        sel,
        100000
        )
    if cle != nouvelle_cle :
        print("Le mot de passe est incorret")
    return nouvelle_cle == cle

choix_user = int(input("Faites votre choix"))
while choix_user != "stop":
     choix_menu = menu()
     if choix_menu == 1 :
        inscription()
     elif choix_menu == 2 : 
        connexion()