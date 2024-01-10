class Ville:
    def __init__(self, nom="", nombrehabitants=0):
        self.__nom = nom
        self.__nombrehabitants = nombrehabitants

    def augmenter_population(self, nombre):
        self.__nombrehabitants += nombre

    def get_nombrehabitants(self):
        return self.__nombrehabitants

class Personne:
    def __init__(self, nom="", age=0, ville=None):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        if self.__ville is not None:
            self.__ville.augmenter_population()
            print("La population de la ville a été augmentée de 1.")
        else:
            print("La personne n'est associée à aucune ville.")

# Créer un objet Ville avec comme arguments “Paris” et 1000000.
ville_paris = Ville("Paris", 1000000)

# Afficher en console le nombre d’habitants de la ville de Paris.
print("Population de la ville de Paris :", ville_paris.get_nombrehabitants())

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
ville_marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille.
print("Population de la ville de Marseille :", ville_marseille.get_nombrehabitants())

# Créer les objets suivants :
john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
# - Chloé, 18 ans, habitant à Marseille.
chloe = Personne("Chloé", 18, ville_marseille)

ville_paris.augmenter_population(2)
ville_marseille.augmenter_population(1)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.

print("Mise a jour de la population de la ville de Paris :", ville_paris.get_nombrehabitants())
print("Mise a jour de la population de la ville de Marseille :", ville_marseille.get_nombrehabitants())
