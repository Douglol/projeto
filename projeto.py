import sqlite3
import time

class usuario:
    # Novo usuário
    def new_user():
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Criar uma tabela
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            senha TEXT NOT NULL,
                            contato TEXT NOT NULL
                        )''')

        # Inserir dados na tabela
        cursor.execute("INSERT INTO usuarios (nome, senha, contato) VALUES (?, ?, ?)", (new_name, new_pass, new_cont))

        # Selecionar ID
        cursor.execute("SELECT MAX(id) FROM usuarios")
        valor = list(cursor.fetchone())
        print(f"\033[94m{valor[0]}\x1b[0m")

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

    # ----------------------------------------------------------------------------------

    # Bool para login
    boolLogin = False

    # Login ID
    def login_user(id):
        global boolLogin
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Verificar se ID de usuário existe
        cursor.execute("SELECT id FROM usuarios")
        for l in cursor.fetchall():
            l = list(l)
            id = int(id)
            if id == l[0]:
                boolLogin = True
                print("\033[92mID valido\x1b[0m")
                break
            else:
                boolLogin = False

    # ----------------------------------------------------------------------------------

    # Bool para senha
    boolSenha = False

    # Login senha
    def pass_user(senha):
        global boolSenha
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Verificar se senha esta correta
        cursor.execute('SELECT senha FROM usuarios WHERE id=?', (login_id))
        for l in cursor.fetchall():
            l = list(l)
            if senha == l[0]:
                boolSenha = True
                print("\033[92mEntrou\x1b[0m")
            else:
                boolSenha = False
                print("\033[91mSenha invalida\x1b[0m")

    # ----------------------------------------------------------------------------------

class livro:
    # Novo livro
    def new_book():
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Criar tabela de livros
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                            id_livro INTEGER PRIMARY KEY,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL,
                            data_publi INTEGER NOT NULL,
                            copias INTEGER NOT NULL
                        )''')

        # Inserir dados na tabela
        cursor.execute("INSERT INTO livros (titulo, autor, data_publi, copias) VALUES (?, ?, ?, ?)", (titulo, autor, data_publi, copias))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

    # ----------------------------------------------------------------------------------

    # Escolher livro
    def choice(escolha):
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Criar tabela de livros emprestados
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros_empr (
                            id INTEGER PRIMARY KEY,
                            id_livro INTEGER NOT NULL,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL,
                            data_publi INTEGER NOT NULL,
                            id_usuario INTEGER NOT NULL
                        )''')

        cursor.execute("SELECT * FROM livros WHERE id_livro=?", (escolha))
        for linha in cursor.fetchall():
            valor = linha[4] - 1
            print(f"\033[92mEmprestimo de {linha[1]} feito\x1b[0m")
            cursor.execute(f"UPDATE livros SET copias = {valor} WHERE id_livro = {escolha}")
            # Inserir dados na tabela de emprestimos
            cursor.execute("INSERT INTO livros_empr (id_livro, titulo, autor, data_publi, id_usuario) VALUES (?, ?, ?, ?, ?)", (escolha, linha[1], linha[2], linha[3], login_id))
            
            cursor.execute("DELETE FROM livros WHERE copias = 0")

        time.sleep(2)

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

    # ----------------------------------------------------------------------------------

    # Buscar livro
    def book_search(busca):
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros")
        print("============================================================")
        for linha in cursor.fetchall():
            linha = list(linha)
            linha[0] = str(linha[0])
            linha[3] = str(linha[3])
            linha[4] = str(linha[4])
            if busca in linha:
                print(f"\033[93mID: \033[94m{linha[0]} \033[93mTítulo: \033[94m{linha[1]} \033[93mAutor: \033[94m{linha[2]} \033[93mData de publicação: \033[94m{linha[3]} \033[93mCopias disponiveis: \033[94m{linha[4]}\x1b[0m")

    # ----------------------------------------------------------------------------------

    # Pegar informações do livro para devolução
    aux1 = None
    aux2 = None
    aux3 = None
    aux4 = None

    # Exibir livro
    def show():
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        global aux1
        global aux2
        global aux3
        global aux4

        # Mostrar emprestimos
        cursor.execute("SELECT * FROM livros_empr WHERE id_usuario=?", (login_id))
        for linha in cursor.fetchall():

            # Pegar informações do livro para devolução
            aux1 = str(linha[1])
            aux2 = str(linha[2])
            aux3 = str(linha[3])
            aux4 = str(linha[4])

            print(f"\033[93mID: \033[94m{linha[0]} \033[93mTitulo: \033[94m{linha[2]} \033[93mAutor: \033[94m{linha[3]} \033[93mData de publicação: \033[94m{linha[4]}\x1b[0m")

    # ----------------------------------------------------------------------------------

    # Acrescentar livro na devolução
    def quant():
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Verifica se o item já existe no banco de dados
        cursor.execute("SELECT copias FROM livros WHERE id_livro=?", (aux1))
        row = cursor.fetchone()

        if row is None:
            # Se o item não existe, adiciona-o ao banco de dados
            cursor.execute("INSERT INTO livros (titulo, autor, data_publi, copias) VALUES (?, ?, ?, ?)", (aux2, aux3, aux4, "1"))
        else:
            # Se o item existe, aumenta a quantidade
            row = list(row)
            nova_quant = row[0] + 1
            nova_quant = str(nova_quant)
            cursor.execute("UPDATE livros SET copias=? WHERE id_livro=?", (nova_quant, aux1))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

    # ----------------------------------------------------------------------------------

    # Devolver livro
    def give_back(devolver):
        # Conectar ao banco de dados
        conn = sqlite3.connect('projeto.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        cursor.execute("DELETE FROM livros_empr WHERE id=?", (devolver))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

# ----------------------------------------------------------------------------------

# Relatório
def report():
    print("==============================")
    print("RELATÓRIO")
    print()
    # Conectar ao banco de dados
    conn = sqlite3.connect('projeto.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    cursor.execute("SELECT * FROM livros_empr")
    cursor.execute("SELECT * FROM usuarios")

    print("\033[95mLIVROS DISPONÍVEIS\x1b[0m")
    print("==============================")
    cursor.execute("SELECT * FROM livros")
    for linha in cursor.fetchall():
        print(f"\033[93mID: \033[94m{linha[0]} \033[93mTitulo: \033[94m{linha[1]} \033[93mAutor: \033[94m{linha[2]} \033[93mData de publicação: \033[94m{linha[3]} \033[93mCópias disponíveis: \033[94m{linha[4]}\x1b[0m")
    
    print()
    print("\033[95mLIVROS EMPRESTADOS\x1b[0m")
    print("==============================")
    cursor.execute("SELECT * FROM livros_empr")
    for linha in cursor.fetchall():
        print(f"\033[93mID: \033[94m{linha[0]} \033[93mTitulo: \033[94m{linha[1]} \033[93mAutor: \033[94m{linha[2]} \033[93mData de publicação: \033[94m{linha[3]} \033[93mID de usuario: \033[94m{linha[4]}\x1b[0m")
    
    print()
    print("\033[95mUSUÁRIOS CADASTRADOS\x1b[0m")
    print("==============================")
    cursor.execute("SELECT * FROM usuarios")
    for linha in cursor.fetchall():
        print(f"\033[93mNome: \033[94m{linha[1]} \033[93mContato: \033[94m{linha[3]}\x1b[0m")

# ----------------------------------------------------------------------------------
# INICIO DO PROGRAMA
# ----------------------------------------------------------------------------------

# Variável vazia da 1° entrada 
pt = ""
while pt != "5":
    # Menu inicial
    print("==============================")
    print("Sistema Biblioteca")
    print("==============================")
    print("\033[94mNovo usuário[1]\x1b[0m")
    print("\033[92mLogin[2]\x1b[0m")
    print("\033[95mCadastrar Livros[3]\x1b[0m")
    print("\033[93mRelatório[4]\x1b[0m")
    print("\033[91mSair[5]\x1b[0m")
    print("==============================")
    pt = input("Opção: ")

    # Novo usuário
    if pt == "1":
        new_name = input("Digite um nome de usuário: ")
        new_pass = input("Nova senha: ")
        new_cont = input("Número para contato: ")
        print("\033[92mFaça login com seu ID: \x1b[0m")
        usuario.new_user()
        time.sleep(2)

    # Login
    elif pt == "2":
        try:
            login_id = input("ID: ")
            usuario.login_user(login_id)
            if boolLogin:
                login_senha = input("senha: ")
                usuario.pass_user(login_senha)
                if boolSenha:
                    print("==============================")
                    print("\033[94mBuscar livros[1]\x1b[0m")
                    print("\033[93mDevolver livros[2]\x1b[0m")
                    print("==============================")
                    menu_user = input("opção: ")

                    # Pesquisar livro
                    if menu_user == "1":
                        print("==============================")
                        busca = input("\033[95mBusque por ID, Título, Autor ou Ano de publicação: \x1b[0m")
                        livro.book_search(busca)
                        print("==============================")

                        # Escolher livro
                        esco_livro = input("Digite o ID do livro para emprestimo: ")
                        livro.choice(esco_livro)
                    elif menu_user == "2":
                        print("==============================")
                        print("EMPRÉSTIMOS FEITOS")
                        print("==============================")
                        livro.show()

                        # Selecionar qual livro devolver
                        devolver = input("Digite o ID do livro para devolver: ")
                        livro.give_back(devolver)
                        livro.quant()
                        print("\033[92mDevolução feita\x1b[0m")
            else:
                print("\033[91mID invalido\x1b[0m")
        except:
            print("\033[91mErro\x1b[0m")

    # Cadastrar livro
    elif pt == "3":
        titulo = input("Título: ")
        autor = input("Autor: ")
        data_publi = input("Ano de publicação: ")
        copias = input("Quantidade de cópias: ")
        livro.new_book()
        print("\033[92mLivro cadastrado\x1b[0m")
    
    # Relatório
    elif pt == "4":
        try:
            report()
        except:
            print("\033[91mPara ver o relatório, precisa de pelo menos um usuario e livro cadastrados, e um emprestimo feito\x1b[0m")