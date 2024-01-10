class Livre:
    def __init__(self, titre="", auteur="", nombredepages=0):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombredepages = nombredepages
        self.__disponible = True
#Ajouter une méthode verification
    def verification(self):
        return self.__disponible
#Ajouter une méthode emprunter
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a ete emprunte.")
        else:
            print("Le livre n'est pas disponible.")
#Ajouter une méthode rendre
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a ete rendu.")
        else:
            print("Le livre est deja disponible.")


livre1 = Livre("Titre du Livre", "Auteur du Livre", 200)
print("Le livre est disponible :", livre1.verification())

livre1.emprunter()
print("Le livre est disponible apres l'emprunt :", livre1.verification())

livre1.rendre()
print("Le livre est disponible apres le rendu :", livre1.verification())


