from document import Document

doc = Document("Rapport", "Contenu important")
doc.sauvegarder()

print("\nJSON du document :")
print(doc.to_json())

print("\nHistorique :")
doc.afficher_historique()
