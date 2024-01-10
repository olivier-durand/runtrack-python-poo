class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

# Création d'une instance de la classe
operation_instance = Operation(12, 3)

# Impression de l'operation
print("Le nombre1 est", operation_instance.nombre1, "et le nombre2 est", operation_instance.nombre2)

# Exécution de l'addition
resultat_addition = operation_instance.addition()
print("Addition:", resultat_addition)