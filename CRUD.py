import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS devs ( 
               id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR(60),
               area_atuacao varchar(200),
               telefone varchar(14)
) """)

conexao.commit()

def cadastrar():
    nomeDev = input("Digite o nome do Desenvolvedor\n")
    area = input("Digite a área de atuação do Desenvolvdor\n")
    tel = input("Digite o número do telefone do Desenvolvedor\n")

    cursor.execute("""INSERT INTO devs (nome, area_atuacao, telefone) VALUES (?,?,?)""", (nomeDev,area, tel))

    conexao.commit()

    print("Cadastro realizado com sucesso!")

def listar():
    cursor.execute("""SELECT * FROM devs""")
    dados = cursor.fetchall()

    if not dados:
        print("Nenhum dev cadastrado.")
        return

    print("\n LISTA DE DEVS")
    for desenvolvedores in dados:
        print(f"ID: {desenvolvedores[0]} | Nome: {desenvolvedores[1]} | Área de Atuação: {desenvolvedores[2]} | Telefone: {desenvolvedores[3]}")

def atualizar():
    listar()
    id_dev = int(input("\nDigite o ID do dev que deseja atualizar: "))

    nomeDev = input("Novo nome: ")
    atuacao = input("Nova área de atuação: ")
    tel = input('Novo Telefone: ')

    cursor.execute("""UPDATE devs SET nome = ?, area_atuacao = ?, telefone = ? WHERE id_dev = ?""", (nomeDev, atuacao, tel, id_dev))

    conexao.commit()

    print("Dados atualizados com sucesso!")

def deletar():
    listar()
    id = int(input("\nDigite o ID do usuário que deseja deletar: "))

    cursor.execute("""DELETE FROM devs WHERE id_dev = ?""", (id,))
    conexao.commit()

    print("\nUsuário deletado com sucesso!")

def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Cadastrar DEV")
        print("2 - Listar DEV")
        print("3 - Atualizar DEV")
        print("4 - Deletar DEV")
        print("5 - Sair")

        op = int(input("Digite sua escolha: "))

        match op:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                atualizar()
            case 4:
                deletar()
            case 5:
                print("Tchau.... O bar está aberto....")
                break
            case _:
                print("ERROR 404")
    
menu()

conexao.close()
            
