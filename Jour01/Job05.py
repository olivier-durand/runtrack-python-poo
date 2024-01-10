class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée horizontale (x) est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée verticale (y) est : {self.y}")

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Exemple d'utilisation
point = Point(3, 5)

# Affichage des coordonnées initiales
point.afficherLesPoints()

# Affichage de x et y séparément
point.afficherX()
point.afficherY()

# Changement des coordonnées
point.changerX(7)
point.changerY(10)

# Affichage des nouvelles coordonnées
point.afficherLesPoints()
