import itertools
class Utilisateur:
    compteur = itertools.count() #Pour que ça compte à chaque nouvel utilisateur créer
    def __init__(self,id,nom,email,role,mdp_hash): 
        self.id = next(Utilisateur.compteur) #Car c'est un attribut qui est dans la classe et pas dans la def 
        self.nom = nom
        self.email = email
        self.role = role
        self.mdp_hash = mdp_hash

class Produit : 
    id_produit = itertools.count()
    def __init__(self, id, nom, categorie, prix, stock, notes, tags):
        self.id = next(Produit.id_produit)
        self.nom = nom 
        self.categorie = categorie
        self.prix = prix
        self.stock = stock
        self.notes = notes 
        self.tags = tags


    

