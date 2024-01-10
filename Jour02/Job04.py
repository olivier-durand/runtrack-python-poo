class Student:
    def __init__(self, nom="", prenom="", numeroetudiants=0, nombrecredits=0):
        
        
        self.__numeroetudiants = numeroetudiants
        self.__nombrecredits = nombrecredits

    def add_credits(self, credits):
        # Vérifier que la valeur passée en argument est supérieure à zéro
        if credits > 0:
            self.__nombrecredits += credits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def get_total_credits(self):
        return self.__nombrecredits

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def studentEval(self):
        if self.__nombrecredits >= 90:
            return "Excellent"
        elif self.__nombrecredits >= 80:
            return "Très bien"
        elif self.__nombrecredits >= 70:
            return "Bien"
        elif self.__nombrecredits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom = {}".format(self.__nom))
        print("Prenom = {}".format(self.__prenom))
        print("Id = {}".format(self.__numeroetudiants))
        print("Niveau = {}".format(self.studentEval()))

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student(nom="Doe", prenom="John", numeroetudiants=145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(13)
john_doe.add_credits(7)

# Impression des informations de l'étudiant
john_doe.student_info()
