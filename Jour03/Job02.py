class CompteBancaire:
    def __init__(self, numerodecompte, nom, prenom, solde, decouvert = False):
        self.__numerodecompte = numerodecompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def detail(self):
        details = f"Numéro de compte : {self.__numerodecompte}\nNom : {self.__nom}\nPrénom : {self.__prenom}\nSolde : {self.__solde}"
        return details

    def afficherSolde(self):
        print("Le solde de votre compte est de :", self.__solde)

    def Montantverse(self, montant):
        self.__solde += montant
        print("Le nouveau solde de votre compte apres votre versement est de :", self.__solde)

    def Montantretire(self, montant):
        if montant > self.__solde:
            print("Erreur : Montant disponible ne peut pas etre inferieur a votre retrait.")
        else:
            self.__solde -= montant
            print("Le nouveau solde de votre compte apres votre retrait est de :", self.__solde)
    
    def Montantdisponible(self, montant):
        self.__solde -= montant
        print("Votre compte ne permet plus d'effectuer de retrait :", self.__solde)
    
    def agios(self, agios):
        self.__agios = agios
        if self.__solde > agios:
            print("Vos agios s eleve a :", self.__agios)

    def virement(self, montant, compte_destinataire):
        if montant > self.__solde:
            print("Votre virement a ete refuse, fonds insuffisants.")
        else:
            self.__solde -= montant
            compte_destinataire.Montantverse(montant)
            print("Votre virement a ete bien realise. Nouveau solde :",)
                  

# Creation d'une instance de classe CompteBancaire exemple
compte1 = CompteBancaire("123456", "Doe", "John", 1000)

# Affichage du solde initial
compte1.afficherSolde()

# Effectuer un versement de 400
compte1.Montantverse(400)

# retrait : cette méthode prend un entier en argument (le montant à retirer) ,enlève ce montant au solde du compte et affiche le nouveau solde.
# Effectuer un retait de 2400
compte1.Montantretire(200)

#Créez une deuxième instance de la classe CompteBancaire
compte2 = CompteBancaire("123457", "Doe", "John", -3000)

# Effectuer un virement du premier compte vers le compte à découvert
montant_virement = 500
compte1.virement(montant_virement, compte2)

# Afficher les soldes après le virement
compte1.afficherSolde()
compte2.afficherSolde()