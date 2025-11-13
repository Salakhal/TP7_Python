from tache import Tache

t = Tache("Écrire rapport", "Rédiger le rapport annuel.")

t.mettre_a_jour("Rédiger et corriger le rapport annuel.")
t.mettre_a_jour("Rédiger, corriger et valider le rapport annuel.")

print("\nHistorique :")
t.afficher_historique()
