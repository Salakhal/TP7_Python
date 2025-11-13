class ValidationMixin:
    def valider_titre(self):
        if not getattr(self, "titre", None) or not self.titre.strip():
            raise ValueError("Le titre doit être renseigné et non vide.")
        # Validation OK
