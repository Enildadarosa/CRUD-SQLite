import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS devs ( 
               id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR(60),
               area_atuacao varchar(200),
               telefone varchar(14)
) """)

# cursor.execute("""INSERT INTO devs (nome, area_atuacao,telefone) VALUES ('Joaozinho', 'Analista de Dados', '678425741')""")

nomeDev = input("Digite o nome do Desenvolvedor\n")
area = input("Digite a área de atuação do Desenvolvdor\n")
tel = input("Digite o número do telefone do Desenvolvedor\n")

cursor.execute("""INSERT INTO devs (nome, area_atuacao, telefone) VALUES (?,?,?)""", (nomeDev,area, tel))

cursor.execute("""SELECT * FROM devs""")
dados = cursor.fetchall()

for desenvolvedores in dados:
    print(desenvolvedores)



conexao.commit()