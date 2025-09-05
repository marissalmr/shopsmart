from class_shopsmart import Utilisateur 
users = []

def inscription():
    nom = input("Quel est votre nom ? ")
    email = input("Quel est votre email ? ")
    role = input("Voulez vous etre admin ou client ? ")
    while role != 'admin' and role != 'client':
        role = input("Voulez vous etre admin ou client ? ")
    
    mdp = input("Choisisez un mdp")
    nouvel_utilisateur = Utilisateur(id, nom, email,role,mdp)
    users.append(nouvel_utilisateur)
    return nouvel_utilisateur

inscription()
print(users)
