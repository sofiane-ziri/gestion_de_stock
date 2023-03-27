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

# Insérer plusieurs categories
mycursor = mydb.cursor()
sql = "INSERT INTO categorie (nom , id) VALUES (%s , %s)"
val = [
    ('Jordan', 1),
    ('Nike', 2),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "categories insérés.")


# Afficher les catégories
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM categorie")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Insérer plusieurs produits
mycursor = mydb.cursor()
sql = "INSERT INTO produit ( nom ,description ,prix ,quantite ,id_categorie ) VALUES (%s , %s , %s , %s , %s)"
val = [
    ('Jordan 1', 'Jordan 1 hight lost and found', 170, 400, 1),
    ('Jordan 1 ', 'Jordan 1 Maison Chateaux Rouge', 150, 600, 1),
    ('Nike Air Force 1', 'Clasical', 100, 1000,  2),
    ('Jordan 4', 'Guava Ice', 200, 350, 1),
    ('Air max 90', 'Air max day', 130, 700, 2),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "produits insérés.")


# Afficher les catégories
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM produit")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)