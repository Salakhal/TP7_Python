from datetime import datetime
import copy

class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        # On enregistre une copie de la description avec timestamp
        self.historique.append((datetime.now(), copy.deepcopy(self.description)))

    def afficher_historique(self):
        print("Historique des descriptions :")
        for date, desc in self.historique:
            print(f"{date} : {desc}")
