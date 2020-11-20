import sqlite3

def titulo (n,s):
    print("=" * n)
    print (f"{s}".center(n))
    print("=" * n)

path = r"C:\xampp\htdocs\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

cursor.execute("SELECT nome FROM Perfumes ORDER BY nome asc")
tabela_nome = cursor.fetchall()
print(tabela_nome)


cursor.execute("SELECT Perfumes.nome, Marcas.nome, Essencias.nome FROM Perfumes, Marcas, Essencias")
tabela_perfumes = cursor.fetchall()
print(tabela_perfumes)
