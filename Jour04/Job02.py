class Personne:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def afficherAge(self):
        print("L'age de la personne est de :", self.get_age(), "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.set_age(nouvel_age)

# L'age par défaut
personne1 = Personne(14)
personne1.afficherAge()
personne1.bonjour()

# Afficher l'âge actuel
personne1.afficherAge()

# Modifier l'âge
personne1.modifierAge(15)

# Afficher le nouvel âge
personne1.afficherAge()

# Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
class Eleve(Personne):
    def __init__(self):
        # Appeler le constructeur de la classe parente avec un âge par défaut
        super().__init__(14)

    def allerEnCours(self):
        print("Je vais en cours")

eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.afficherAge()

# Créer une classe Professeur qui hérite de la classe Personne
class Professeur(Personne):
    def __init__(self, age):
        # Appeler le constructeur de la classe parente avec l'âge fourni
        super().__init__(age)

    def enseigner(self):
        print("Le cours commence")

# Créer un objet Professeur, 40 ans
professeur = Professeur(40)
professeur.bonjour()
professeur.enseigner()
