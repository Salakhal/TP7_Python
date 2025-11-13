# TP 7 – Mixins

## Objectif général
Découvrir et approfondir l’utilisation des **mixins en Python** pour composer des comportements transversaux (validation, journalisation, historisation, sérialisation) dans des classes métiers, sans recourir à l’héritage hiérarchique traditionnel.  

Les objectifs pédagogiques incluent :  

- Séparation claire des responsabilités.  
- Réutilisation et modularité du code.  
- Traçabilité et validation métier via des mixins.  

---

# Exercice 1 : Utilisation des Mixins en Python

## Objectif pédagogique
Découvrir l’utilisation des **classes Mixins** pour enrichir des classes principales avec des comportements réutilisables, sans recourir à l’héritage hiérarchique traditionnel.

---

## Contexte
On souhaite modéliser des entités métiers pouvant bénéficier de fonctionnalités transversales comme :

- Horodatage automatique des actions.
- Validation de certains attributs avant traitement.

L’approche **Mixin** permet d’injecter ces capacités à la demande, en gardant une organisation claire et modulaire.

---

## Classes et Mixins

### 1. **Horodatable**
- Méthode : `horodatage()`
- Fonction : affiche un log avec la date et l’heure de l’action.

### 2. **Validable**
- Méthode : `valider()`
- Fonction : vérifie que le titre de l’objet est présent et non vide.
- Lève une exception `ValueError` si le titre est manquant.

### 3. **Serializable (extension)**
- Méthodes : `to_json()` et `from_json()`
- Fonction : permet de convertir l’objet en JSON et de reconstruire un objet à partir d’un JSON.

### 4. **Historisable (extension)**
- Attribut : `historique` (liste des états)
- Méthodes :
  - `enregistrer_action(action)` : enregistre l’action avec timestamp.
  - `afficher_historique()` : affiche toutes les actions effectuées.

### 5. **Document**
- Hérite des mixins `Horodatable` et `Validable` (et éventuellement `Serializable` et `Historisable` pour les extensions).
- Attributs : `titre`, `contenu`.
- Méthodes :
  - `sauvegarder()` : horodate, valide et affiche un message de sauvegarde.


##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="975" height="507" alt="image" src="https://github.com/user-attachments/assets/f108b497-b1a4-472f-9f4c-2624dab6d385" />


#  Exercice 2 : Mixins pour objets métiers

## Objectif pédagogique
Approfondir l’usage des **mixins en Python** pour structurer des comportements transversaux tels que :  

- la journalisation,  
- l’historique des modifications,  
- la sérialisation JSON.  

Le but est de favoriser la **réutilisabilité** et la **séparation des responsabilités** dans des classes métiers.

---

## Contexte
Une entreprise souhaite modéliser des objets métiers (ex. `Contrat`, `Tâche`) dotés de comportements optionnels comme :  

- traçabilité des modifications,  
- transformation en JSON,  
- journalisation des actions.  

L’approche **mixin** permet de composer dynamiquement ces capacités sans alourdir la hiérarchie principale.

---

## Classes et Mixins

### 1. **Serializable**
- Méthodes : `to_json()` et `from_json()`  
- Fonction : convertir un objet en JSON et reconstruire un objet depuis un JSON.  
- Remarque : ignore certains attributs problématiques pour éviter les références circulaires (ex. `historique`).

### 2. **Historisable**
- Attribut : `historique` (liste des états)  
- Méthodes :
  - `enregistrer_etat()` : sauvegarde l’état actuel avec timestamp.  
  - `afficher_historique()` : affiche toutes les versions précédentes des attributs.

### 3. **Journalisable**
- Méthode : `journaliser(message)`  
- Fonction : affiche un message de journal avec la date et l’heure.

### 4. **Horodatable** (extension)
- Méthode : `horodatage()`  
- Fonction : log du moment où une action est effectuée.

### 5. **Contrat**
- Hérite des mixins : `Serializable`, `Historisable`, `Journalisable`, `Horodatable`  
- Attributs : `id`, `description`  
- Méthodes :
  - `modifier(nouvelle_desc)` : met à jour la description, enregistre l’état précédent, journalise l’action et horodate.

---

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="1309" height="295" alt="image" src="https://github.com/user-attachments/assets/dd19a118-5f78-4612-8706-94c4a9c34b32" />


#  Exercice 3 : Gestion de tâches avec mixins

## Objectif pédagogique
Mettre en pratique la **composition via mixins** en Python pour :  

- valider des attributs métier,  
- conserver un historique des modifications,  
- journaliser les actions sur des objets métiers.  

L’exercice illustre la **séparation des responsabilités** et la **réutilisabilité** du code.

---

## Contexte
On souhaite modéliser un système de gestion de **tâches professionnelles**.  

Chaque tâche doit :  

1. Avoir un **titre obligatoire** validé automatiquement.  
2. Enregistrer un **historique** à chaque modification de sa description.  
3. Afficher un **journal** pour chaque action réalisée (création, mise à jour).

L’approche mixin permet de composer ces comportements de manière modulaire sans recourir à l’héritage hiérarchique complexe.

---

## Classes et Mixins

### 1. **ValidationMixin**
- Méthode : `valider_titre()`  
- Fonction : vérifie que le titre est renseigné et non vide.  
- Lève `ValueError` si la validation échoue.

### 2. **HistoriqueMixin**
- Attribut : `historique` (liste des descriptions précédentes avec timestamp)  
- Méthodes :
  - `enregistrer_etat()` : sauvegarde la description avant modification.  
  - `afficher_historique()` : affiche toutes les versions antérieures de la description.  
- Utilisation du module `copy` pour cloner l’état.

### 3. **JournalisationMixin**
- Méthode : `journaliser(message)`  
- Fonction : affiche un message dans la console avec la date et l’heure de l’action.

### 4. **Tache**
- Hérite des mixins : `ValidationMixin`, `HistoriqueMixin`, `JournalisationMixin`  
- Attributs : `titre`, `description`, `date_creation`  
- Méthodes :
  - `mettre_a_jour(description)` : met à jour la description, conserve l’historique et journalise l’action.  
  - `afficher_historique()` : permet de consulter les anciennes versions.

---

##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :


<img width="1232" height="257" alt="image" src="https://github.com/user-attachments/assets/b3cdee17-2779-4960-84d3-ef14b39642fa" />


































