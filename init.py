import sqlite3

path = r"C:\xampp\htdocs\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE Perfumes (id integer, nome  varchar (50), quantidade integer, id_volume_FK integer, id_marca_FK integer, id_fixacao_FK integer)")
cursor.execute("CREATE TABLE Marcas (id integer, nome  varchar (50))")
cursor.execute("CREATE TABLE Fixacoes (id integer, nome  varchar (50))")
cursor.execute("CREATE TABLE Volumes (id integer, nome  varchar (50))")
cursor.execute("CREATE TABLE Essencia_Perfume (id_essencia_FK integer, id_perfume_FK integer)")
cursor.execute("CREATE TABLE Essencias (id integer, nome  varchar (50))")
