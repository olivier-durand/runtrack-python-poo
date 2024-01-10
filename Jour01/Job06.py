class Animal:

    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self, nouveau_nom):
        self.nom = nouveau_nom

# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'age initial
print(f"Age initial de l'animal : {mon_animal.age}")

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de l'age apres avoir vieilli
print(f"Age de l'animal après avoir vieilli : {mon_animal.age}")

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print(f"L'animal se nomme : {mon_animal.nom}")

