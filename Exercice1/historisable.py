from datetime import datetime

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_action(self, action):
        timestamp = datetime.now()
        self.historique.append(f"{timestamp} : {action}")
    
    def afficher_historique(self):
        print("Historique des actions :")
        for entry in self.historique:
            print(entry)
