import mysql.connector

# Se connecter au serveur SQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

# Créer une base de données "boutique"
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE boutique")

# Se connecter à la base de données "boutique"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="boutique"
)

# Créer la table "produit"
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE produit (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), description text, prix INT, quantite INT, id_categorie INT)")

# Créer la table "categorie"
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE categorie (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")


print("Les tables ont été créées avec succès !")        

