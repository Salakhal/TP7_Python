from serializable import Serializable
from historisable import Historisable
from journalisable import Journalisable
from horodatable import Horodatable

class Contrat(Serializable, Historisable, Journalisable, Horodatable):
    def __init__(self, id, description):
        Historisable.__init__(self)  # Init du mixin Historisable
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.horodatage()
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc
