import sqlite3

path = r"C:\xampp\htdocs\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES (1, 'Malbec', '100', '0001', '001', '01')")
cursor.execute("INSERT INTO Perfumes VALUES (2, 'Kaiak', '100', '0002', '002', '02')")
cursor.execute("INSERT INTO Perfumes VALUES (3, 'Una', '200', '0003', '003', '03')")

#Volumes
cursor.execute("INSERT INTO Volumes VALUES(1, 'ml')")

#Essencia_Perfume
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1, 001)")


#Essencias
cursor.execute("INSERT INTO Essencias VALUES(1, 'Malbec Colônia')")
cursor.execute("INSERT INTO Essencias VALUES(2, 'Kaiak Colônia')")
cursor.execute("INSERT INTO Essencias VALUES(3, 'Una Colônia')")

#Marcas
cursor.execute("INSERT INTO Marcas VALUES(1, 'Natura')")
cursor.execute("INSERT INTO Marcas VALUES(2, 'Avon')")
cursor.execute("INSERT INTO Marcas VALUES(3, 'Jequiti')")

#Fixacoes
cursor.execute("INSERT INTO Fixacoes VALUES(1, 'Parfum')")
cursor.execute("INSERT INTO Fixacoes VALUES(2, 'Eau de Toilette')")
cursor.execute("INSERT INTO Fixacoes VALUES(3, 'Água de Colônia')")
banco.commit()
