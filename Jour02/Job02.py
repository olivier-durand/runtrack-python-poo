# Créer la classe Livre qui prend en attributs privés un titre, un auteur et un nombre de pages
class Livre:
    def __init__(self, titre, auteur, nombredepages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombredepages = nombredepages

    # Créer les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les attributs.

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombredepages(self):
        return self.__nombredepages

    def set_nombredepages(self, nombredepages):
        # Pour changer le nombre de pages, Ce dernier doit être un nombre entier positif
        if isinstance(nombredepages, int) and nombredepages > 0:
            self.__nombredepages = nombredepages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")

# Exemple d'utilisation de la classe Livre
livre = Livre("titre", "auteur", 2)
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nombredepages())

livre.set_titre("Nouveau titre")
livre.set_auteur("Nouvel auteur")
livre.set_nombredepages(380)

print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nombredepages())


print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nombredepages())




       
        




