import json
from abc import ABC, abstractmethod

class SerializableABC(ABC):
    @abstractmethod
    def to_json(self):
        """Méthode obligatoire pour sérialiser l'objet en JSON"""
        pass

class Serializable(SerializableABC):
    def to_json(self):
        return json.dumps(self.__dict__, default=str, indent=2)
