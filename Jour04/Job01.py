#Créer une classe Personne qui aura comme attribut age prenant un entier et initialisé à 14 par défaut. 

class Personne:
    def __init__(self, age):
        self.__age = 14

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age
        
# Ajouter une méthode afficherAge qui affichera en console l'âge de la personne
    def afficherAge(self):
        print("L'age de la personne est de :", self.get_age(), "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.set_age(nouvel_age)

 # L'age par défaut 
personne1 = Personne() 
personne1.afficherAge()
personne1.bonjour()

# Créer l'instance de la classe Personne

# Afficher l'âge actuel
personne1.afficherAge()

# Modifier l'âge
personne1.modifierAge(25)

# Afficher le nouvel âge
personne1.afficherAge()

#Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut 
class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

#Creer une méthode publique allerEnCours qui affiche : “Je vais en cours” ainsi qu’une méthodeafficherAge qui écrit en console : “J’ai XX ans”.
    def allerEnCours(self):
        print("Je vais en cours")

eleve = Eleve()
eleve.allerEnCours()
eleve.afficherAge()

#Créer une classe Professeur avec un attribut privé matiereEnseignée, qui indiquera la matière du professeur, 

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = () 

    def get_matiereEnseignee(self):
        return self.__matiereEnseignee
    
    def set_matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = ()


#Créer une méthode publique enseigner qui affiche : “Le cours va commencer”.
def enseigner(self):
    print("Le cours va commencer")

