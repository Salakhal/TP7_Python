from horodatable import Horodatable
from validable import Validable
from serializable import Serializable
from historisable import Historisable

class Document(Horodatable, Validable, Serializable, Historisable):
    def __init__(self, titre, contenu):
        Historisable.__init__(self)
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        self.enregistrer_action("Document sauvegardé")
        print(f"Document '{self.titre}' sauvegardé.")
