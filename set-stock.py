import mysql.connector
from tkinter import *

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="boutique"
)
mycursor = mydb.cursor()

# Fonction pour afficher la liste des produits


def get_produits():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM produit")
    produits = mycursor.fetchall()
    return produits


def get_categorie_by_id(id):
    mycursor.execute("SELECT nom FROM categorie WHERE id=%s", (id,))
    categorie = mycursor.fetchone()
    return categorie[0] if categorie else ""


# Fonction pour ajouter un produit


def ajouter_produit():
    nom = nom_entry.get()
    description = description_entry.get()
    prix = prix_entry.get()
    quantite = quantite_entry.get()
    id_categorie = id_categorie_entry.get()

    sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s )"
    val = (nom, description, prix, quantite, id_categorie)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "produit ajouté")

# Fonction pour supprimer un produit


def supprimer_produit(id):
    sql = "DELETE FROM produit WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "produit supprimé")


# Interface graphique avec Tkinter
root = Tk()
root.title("Gestion de stock")
root.geometry("500x500")

# Liste des produits
liste_frame = Frame(root)
liste_frame.pack()
Label(liste_frame, text="Liste des produits").grid(row=0, column=0)
liste_box = Listbox(liste_frame, width=50)
liste_box.grid(row=1, column=0)


def afficher_produits():
    # Récupérer la liste des produits depuis la base de données
    produits = get_produits()
    # Ajouter chaque produit dans la liste
    for produit in produits:
        # Récupérer le nom de la catégorie correspondante
        categorie = get_categorie_by_id(produit[5])
        liste_box.insert(
            END, f"{produit[0]} - {produit[1]} - {produit[2]} - {produit[3]}€ - {produit[4]} - {categorie[1]}")


afficher_produits()

# Créer les widgets pour l'interface utilisateur
nom_label = Label(root, text="Nom du produit")
nom_entry = Entry(root)
description_label = Label(root, text="Description")
description_entry = Entry(root)
prix_label = Label(root, text="Prix")
prix_entry = Entry(root)
quantite_label = Label(root, text="Quantité")
quantite_entry = Entry(root)
id_categorie_label = Label(root, text="ID de catégorie")
id_categorie_entry = Entry(root)
ajouter_bouton = Button(root, text="Ajouter produit", command=ajouter_produit)

# Afficher les widgets à l'écran
nom_label.pack()
nom_entry.pack()
description_label.pack()
description_entry.pack()
prix_label.pack()
prix_entry.pack()
quantite_label.pack()
quantite_entry.pack()
id_categorie_label.pack()
id_categorie_entry.pack()
ajouter_bouton.pack()

# Création de la fonction appelée lors du clic sur le bouton de suppression de produit


def clic_supprimer():
    id_produit = id_produit_entry.get()
    supprimer_produit(id_produit)
    # Mettre à jour l'affichage de la liste des produits (non inclus dans cet exemple)

# Création de l'interface Tkinter avec un champ d'entrée pour l'ID du produit à supprimer et un bouton de suppression


id_produit_label = Label(root, text="ID du produit à supprimer :")
id_produit_label.pack()

id_produit_entry = Entry(root)
id_produit_entry.pack()

supprimer_bouton = Button(root, text="Supprimer", command=clic_supprimer)
supprimer_bouton.pack()


root.mainloop()
