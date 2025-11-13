from abc import ABC, abstractmethod

class ValidableABC(ABC):
    @abstractmethod
    def valider(self):
        """Méthode obligatoire pour valider l'objet"""
        pass

class Validable(ValidableABC):
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        print("Validation OK")
