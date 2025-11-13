from contrat import Contrat

c = Contrat(1, "Initial")
c.modifier("Révisé")

print("\nJSON du contrat :")
print(c.to_json())

print("\nHistorique :")
c.afficher_historique()
