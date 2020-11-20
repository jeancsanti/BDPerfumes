import sqlite3

def titulo (n,s):
    print("=" * n)
    print (f"{s}".center(n))
    print("=" * n)

path = r"C:\xampp\htdocs\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#cursor.execute("DELETE FROM Perfumes")
#deletar = cursor.fetchall()
#print(deletar)

cursor.execute("SELECT nome FROM Perfumes ORDER BY nome asc")
tabela_nome = cursor.fetchall()
print(tabela_nome)
print("\n============================================================================\n")

cursor.execute("SELECT nome FROM Marcas ORDER BY nome asc")
tabela_marca = cursor.fetchall()

cursor.execute("SELECT nome FROM Essencias")
tabela_essencia = cursor.fetchall()
print(tabela_essencia)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

cursor.execute("SELECT Perfumes.nome, Volumes.nome FROM Perfumes, Volumes")
tabela_perfumes = cursor.fetchall()
print("O perfume", tabela_nome[0], " tem 100ml")
print("O perfume", tabela_nome[1], " tem 100ml")
print("O perfume", tabela_nome[2], " tem 100ml")

print("\n=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>\n")

cursor.execute("SELECT Perfumes.nome, Marcas.nome, Essencias.nome FROM Perfumes, Marcas, Essencias")
tabela_essencia1 = cursor.fetchall()
print("O perfume", tabela_nome[1], "de Marca", tabela_marca[0], "de essencia", tabela_essencia[0])
print("O perfume", tabela_nome[0], "de Marca", tabela_marca[2], "de essencia", tabela_essencia[1])
print("O perfume", tabela_nome[2], "de Marca", tabela_marca[1], "de essencia", tabela_essencia[2])
