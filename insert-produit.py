import mysql.connector

# Se connecter à la base de données "boutique"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="boutique"
)

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
