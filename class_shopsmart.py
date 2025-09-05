import itertools
class Utilisateur:
    compteur = itertools.count() #Pour que ça compte à chaque nouvel utilisateur créer
    def __init__(self,id,nom,email,role,mdp): 
        self.id = next(Utilisateur.compteur) #Car c'est un attribut qui est dans la classe et pas dans la def 
        self.nom = nom
        self.email = email
        self.role = role
        self.mdp = mdp 


    

