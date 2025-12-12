import sqlite3

# Criar conexão com o banco
def connect():
    return sqlite3.connect("usuarios.db", check_same_thread=False)

# Criar tabela
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    conn.commit()
    conn.close()

# Inserir
def add_user(nome, email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

# Listar
def get_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()
    conn.close()
    return data

# Atualizar
def update_user(user_id, novo_nome, novo_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, user_id))
    conn.commit()
    conn.close()

# Deletar
def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
