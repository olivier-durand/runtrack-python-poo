class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def calculer_perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def calculer_surface(self):
        return self.__longueur * self.__largeur

# Exemple d'utilisation de la classe Rectangle
rectangle1 = Rectangle(5, 3)

perimetre_rectangle1 = rectangle1.calculer_perimetre()
surface_rectangle1 = rectangle1.calculer_surface()

print(f"Perimetre du rectangle : {perimetre_rectangle1}")
print(f"Surface du rectangle : {surface_rectangle1}")