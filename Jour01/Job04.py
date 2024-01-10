#Créez une classe Personne avec les attributs nom et prenom
class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        
        print(f"Je suis {self.nom} {self.prenom}")


#Ajoutez une méthode SePresenter qui retourne le nom et le prénom de la personne

		
#Instanciez plusieurs personnes avec les valeurs de construction de votre choix 

personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")
personne1.sePresenter()


#Faites appel à la méthode SePresenter afin de vérifier que tout fonctionne correctement.
print("SePresenter")




