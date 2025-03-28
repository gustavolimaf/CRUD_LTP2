import sqlite3

def create_connection():
    return sqlite3.connect('estoque.db')

def create_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    );
    """
    conn.execute(sql)
    conn.commit()

def inserir_produto(conn, nome, quantidade, preco):
    sql = "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)"
    try:
        conn.execute(sql, (nome, quantidade, preco))
        conn.commit()
        print("Produto inserido com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Produto com esse nome já existe.")

def listar_produtos(conn):
    sql = "SELECT * FROM produtos"
    cursor = conn.execute(sql)
    produtos = cursor.fetchall()
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Nenhum produto cadastrado.")

def atualizar_produto(conn, produto_id, nova_quantidade, novo_preco):
    sql = "UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?"
    cursor = conn.execute(sql, (nova_quantidade, novo_preco, produto_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def deletar_produto(conn, produto_id):
    sql = "DELETE FROM produtos WHERE id = ?"
    cursor = conn.execute(sql, (produto_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrado.")

def buscar_produto_por_nome(conn, nome):
    sql = "SELECT * FROM produtos WHERE nome LIKE ?"
    cursor = conn.execute(sql, ('%' + nome + '%',))
    resultados = cursor.fetchall()
    if resultados:
        print("Resultado da busca:")
        for row in resultados:
            print(row)
    else:
        print("Nenhum produto encontrado com esse nome.")

def filtrar_produtos_por_preco(conn, preco_min, preco_max):
    sql = "SELECT * FROM produtos WHERE preco BETWEEN ? AND ?"
    cursor = conn.execute(sql, (preco_min, preco_max))
    resultados = cursor.fetchall()
    if resultados:
        print(f"Produtos com preço entre {preco_min} e {preco_max}:")
        for row in resultados:
            print(row)
    else:
        print("Nenhum produto encontrado nesse intervalo de preço.")

def filtrar_produtos_por_quantidade(conn, quant_min, quant_max):
    sql = "SELECT * FROM produtos WHERE quantidade BETWEEN ? AND ?"
    cursor = conn.execute(sql, (quant_min, quant_max))
    resultados = cursor.fetchall()
    if resultados:
        print(f"Produtos com quantidade entre {quant_min} e {quant_max}:")
        for row in resultados:
            print(row)
    else:
        print("Nenhum produto encontrado nesse intervalo de quantidade.")
