import sqlite3
import time

# Novo livro
def new_book():
    # Conectar ao banco de dados
    conn = sqlite3.connect('projeto.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Criar uma tabela
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id_livro INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        data_publi INTEGER NOT NULL
                    )''')

    # Inserir dados na tabela
    cursor.execute("INSERT INTO livros (titulo, autor, data_publi) VALUES (?, ?, ?)", (titulo, autor, data_publi))

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()

# ----------------------------------------------------------------------------------

# Emprestimo de Livro
def book_loan():
    # Conectar ao banco de dados
    conn = sqlite3.connect('projeto.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Criar uma tabela
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros_empr (
                        id_emp INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        data_publi INTEGER NOT NULL,
                        FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
                    )''')

    # Inserir dados na tabela
    cursor.execute("INSERT INTO livros_empr (titulo, autor, data_publi) WHERE id_livro=?", (esco_livro))

    # Commit para salvar as alterações
    conn.commit()

    # Exibir os dados
    cursor.execute("SELECT * FROM livros")
    print("Dados na tabela:")
    for linha in cursor.fetchall():
        print(linha)

    # Fechar a conexão com o banco de dados
    conn.close()

# ----------------------------------------------------------------------------------

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
                        senha TEXT NOT NULL
                    )''')

    # Inserir dados na tabela
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (new_name, new_pass))

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
        if busca in linha:
            print(f"\033[93mID: \033[94m{linha[0]} \033[93mTítulo: \033[94m{linha[1]} \033[93mAutor: \033[94m{linha[2]} \033[93mData de publicação: \033[94m{linha[3]}\x1b[0m")

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
        print("\033[92mFaça login com seu ID: \x1b[0m")
        new_user()
        time.sleep(2)

    # Login
    if pt == "2":
        login_id = input("ID: ")
        login_user(login_id)
        if boolLogin:
            login_senha = input("senha: ")
            pass_user(login_senha)
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
                    book_search(busca)
                    print("==============================")

                    # Escolher livro
                    esco_livro = input("Digite o ID do livro para emprestimo: ")
                    book_loan()
        else:
            print("\033[91mID invalido\x1b[0m")

    # Cadastrar livro
    if pt == "3":
        titulo = input("Título: ")
        autor = input("Autor: ")
        data_publi = input("Ano de publicação: ")
        new_book()
        print("\033[92mLivro cadastrado\x1b[0m")