import mysql.connector

# Se connecter à la base de données "boutique"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="boutique"
)

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
