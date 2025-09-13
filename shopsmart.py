from class_shopsmart import Utilisateur 
from class_shopsmart import Produit
import hashlib
import os
import json 
import itertools

users = []

def menu():
     while True : 
          print("Menu : \n 1. Pour vous inscrire \n 2. Pour vous connecter \n 3. Afficher les produits")
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
    mdp_hash = salage + clé
    
    return mdp_hash #Concaténation du sel et clé 

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
    return nouvel_utilisateur, mdp #Permet de pouvoir l'utiliser plus tard, pas concerné par la portée des variables


def connexion():
    utilisateur_trouvé = None
    mdp_trouvé = None
    while utilisateur_trouvé is None : 
        tentative_pseudo = input("Entrez votre pseudonyme")
        for utilisateurs in users : 
            if tentative_pseudo == utilisateurs.nom : #Car on accede au nom de l'objet utilisateur
                utilisateur_trouvé = utilisateurs 
            else : 
                print("Utilisateur introuvable veuillez réessayer")
                tentative_pseudo 
    mdp_stocké = None
    
    while mdp_trouvé == None : 
        for utilisateurs in users : 
            mdp_stocké = utilisateurs.mdp_hash
            

        tentative_mdp = input("Entrez votre mot de passe")
        verification = verifier_mdp(tentative_mdp, mdp_stocké )
        if verification is True : 
            print("Vous etes co")
        else : 
            print("Mot de passe incorrect, veuillez réessayer")
            tentative_mdp

   
def verifier_mdp(tentative_mdp, mdp_stocké): #Obligé car on peut pas comparer un mdp hasher à un mdp normal 
    mdp_stocké = None
    for utilisateur in users : 
        mdp_stocké = utilisateur.mdp_hash
    sel = mdp_stocké[:32] #extraction du sel car c'est les 32 premier caractères
    cle = mdp_stocké[32:] #extraction de la clé = 32 dernier caractères
    nouvelle_cle =  hashlib.pbkdf2_hmac( #Je refais le meme hash, sur la tentative en utilisant le meme sel
        'sha256',
        tentative_mdp.encode('utf-8'),
        sel,
        100000
        )
   
    return nouvelle_cle == cle


page = 0
liste_produits = produits = [
    {"id": 1, "nom": "T-shirt Oversize", "categorie": "mode", "prix": 19.90, "stock": 20, "tags": ["unisex","coton"]},
    {"id": 2, "nom": "Sneakers Nova", "categorie": "mode", "prix": 79.00, "stock": 12, "tags": ["running"]},
    {"id": 3, "nom": "Mug Émail", "categorie": "maison", "prix": 8.50, "stock": 50, "tags": ["café"]},
    {"id": 4, "nom": "Casque Studio", "categorie": "tech", "prix": 129.00, "stock": 7, "tags": ["audio"]},
    {"id": 5, "nom": "Clavier Mécanique", "categorie": "tech", "prix": 95.00, "stock": 9, "tags": ["RGB"]},
    {"id": 6, "nom": "Lampe de Bureau", "categorie": "maison", "prix": 24.90, "stock": 30, "tags": ["LED"]},
    {"id": 7, "nom": "Jean Slim", "categorie": "mode", "prix": 49.90, "stock": 25, "tags": ["denim","unisex"]},
    {"id": 8, "nom": "Pull Cachemire", "categorie": "mode", "prix": 119.00, "stock": 15, "tags": ["hiver","premium"]},
    {"id": 9, "nom": "Sac à Dos Urban", "categorie": "mode", "prix": 59.90, "stock": 18, "tags": ["voyage","unisex"]},
    {"id": 10, "nom": "Chaussures de Ville", "categorie": "mode", "prix": 89.00, "stock": 10, "tags": ["cuir"]},
    {"id": 11, "nom": "Bougie Parfumée", "categorie": "maison", "prix": 14.50, "stock": 40, "tags": ["décoration","bien-être"]},
    {"id": 12, "nom": "Plaid Doux", "categorie": "maison", "prix": 29.90, "stock": 35, "tags": ["hiver","confort"]},
    {"id": 13, "nom": "Table Basse Bois", "categorie": "maison", "prix": 149.00, "stock": 5, "tags": ["salon","design"]},
    {"id": 14, "nom": "Oreiller Mémoire", "categorie": "maison", "prix": 39.90, "stock": 22, "tags": ["sommeil","confort"]},
    {"id": 15, "nom": "Mixeur Blender", "categorie": "maison", "prix": 69.90, "stock": 14, "tags": ["cuisine","électro"]},
    {"id": 16, "nom": "Smartphone Alpha", "categorie": "tech", "prix": 699.00, "stock": 8, "tags": ["android","5G"]},
    {"id": 17, "nom": "Tablette Orion", "categorie": "tech", "prix": 349.00, "stock": 11, "tags": ["android","wifi"]},
    {"id": 18, "nom": "Souris Gaming", "categorie": "tech", "prix": 49.90, "stock": 26, "tags": ["RGB","ergonomique"]},
    {"id": 19, "nom": "Écran 27 pouces", "categorie": "tech", "prix": 229.00, "stock": 13, "tags": ["fullHD","gaming"]},
    {"id": 20, "nom": "Enceinte Bluetooth", "categorie": "tech", "prix": 59.90, "stock": 21, "tags": ["portable","audio"]},
    {"id": 21, "nom": "Veste Cuir", "categorie": "mode", "prix": 199.00, "stock": 6, "tags": ["cuir","premium"]},
    {"id": 22, "nom": "Robe Été", "categorie": "mode", "prix": 39.00, "stock": 28, "tags": ["léger","femme"]},
    {"id": 23, "nom": "Set de Verres", "categorie": "maison", "prix": 22.00, "stock": 32, "tags": ["verrerie","cuisine"]},
    {"id": 24, "nom": "Aspirateur Compact", "categorie": "maison", "prix": 129.00, "stock": 9, "tags": ["ménage","électro"]}
]


with open('base_de_donnees.json', 'w') as produits : 
    json.dump(liste_produits, produits, indent=4 )
    
with open('base_de_donnees.json', 'r') as product : 
    data_charger = json.load(product)
    


def affichage_produit():

    for produit in liste_produits:
        if produit['id']<7:
            print(produit['id'], produit['nom'], produit['prix'])   
    choix_page = input("Voulez vous voir la page suivante ? ")

    liste_slice_page1 = liste_produits[5:12]

    if choix_page == 'oui' :
        print(liste_slice_page1[0:6])   
    choix_page = input("Voulez vous voir la page suivante ? ")

    liste_slice_page2 = liste_produits[11:19]
    
    if choix_page == 'oui':
        print(liste_slice_page2[0:6])
    choix_page = input("Voulez vous voir la page suivante ? ")

    
    liste_slice_page3 = liste_produits[17:25]

    if choix_page=='oui' :
        print(liste_slice_page3[0:6])





choix_user = int(input("Faites votre choix"))
while choix_user != "stop":
     choix_menu = menu()
     if choix_menu == 1 :
        inscription()
     elif choix_menu == 2 : 
        connexion()
     elif choix_menu == 3 : 
         affichage_produit()