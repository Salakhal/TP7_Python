from datetime import datetime

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        # Copier uniquement les attributs simples
        etat = {k: v for k, v in self.__dict__.items() if k != 'historique'}
        self.historique.append((datetime.now(), etat))

    def afficher_historique(self):
        print("Historique des états :")
        for entry in self.historique:
            print(entry)
