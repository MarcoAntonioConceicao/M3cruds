#M3 - Bancos De Dados I 
#Implementação De CRUD
#Kaio Saldanha, Davi Rangel e Marco Antônio Da Conceição

import mysql.connector

# Configurações de conexão
config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'sistema_varejo',
    'raise_on_warnings': True
}

# Função para criar conexão
def create_connection():
    return mysql.connector.connect(**config)

# Funções CRUD para a tabela Produtos

def create_produto(nome, preco):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produtos (Nome, Preço) VALUES (%s, %s)", (nome, preco))
    conn.commit()
    cursor.close()
    conn.close()

def read_produtos():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos")
    for (IDProduto, Nome, Preço) in cursor:
        print(f"IDProduto: {IDProduto}, Nome: {Nome}, Preço: {Preço}")
    cursor.close()
    conn.close()

def update_produto(id_produto, nome, preco):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Produtos SET Nome=%s, Preço=%s WHERE IDProduto=%s", (nome, preco, id_produto))
    conn.commit()
    cursor.close()
    conn.close()

def delete_produto(id_produto):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produtos WHERE IDProduto=%s", (id_produto,))
    conn.commit()
    cursor.close()
    conn.close()

# Funções CRUD para a tabela Fornecedores

def create_fornecedor(nome, endereco, telefone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Fornecedores (Nome, Endereço, Telefone) VALUES (%s, %s, %s)", (nome, endereco, telefone))
    conn.commit()
    cursor.close()
    conn.close()

def read_fornecedores():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Fornecedores")
    for (ID_Fornecedor, Nome, Endereço, Telefone) in cursor:
        print(f"ID_Fornecedor: {ID_Fornecedor}, Nome: {Nome}, Endereço: {Endereço}, Telefone: {Telefone}")
    cursor.close()
    conn.close()

def update_fornecedor(id_fornecedor, nome, endereco, telefone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Fornecedores SET Nome=%s, Endereço=%s, Telefone=%s WHERE ID_Fornecedor=%s", (nome, endereco, telefone, id_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def delete_fornecedor(id_fornecedor):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Fornecedores WHERE ID_Fornecedor=%s", (id_fornecedor,))
    conn.commit()
    cursor.close()
    conn.close()

# Funções CRUD para a tabela Clientes

def create_cliente(nome, endereco, telefone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (Nome, Endereço, Telefone) VALUES (%s, %s, %s)", (nome, endereco, telefone))
    conn.commit()
    cursor.close()
    conn.close()

def read_clientes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    for (ID_Cliente, Nome, Endereço, Telefone) in cursor:
        print(f"ID_Cliente: {ID_Cliente}, Nome: {Nome}, Endereço: {Endereço}, Telefone: {Telefone}")
    cursor.close()
    conn.close()

def update_cliente(id_cliente, nome, endereco, telefone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Clientes SET Nome=%s, Endereço=%s, Telefone=%s WHERE ID_Cliente=%s", (nome, endereco, telefone, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente(id_cliente):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE ID_Cliente=%s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

# Funções CRUD para a tabela Pedidos

def create_pedido(data_pedido, id_cliente):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pedidos (DataPedido, ID_Cliente) VALUES (%s, %s)", (data_pedido, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()

def read_pedidos():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedidos")
    for (ID_Pedido, DataPedido, ID_Cliente) in cursor:
        print(f"ID_Pedido: {ID_Pedido}, DataPedido: {DataPedido}, ID_Cliente: {ID_Cliente}")
    cursor.close()
    conn.close()

def update_pedido(id_pedido, data_pedido, id_cliente):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Pedidos SET DataPedido=%s, ID_Cliente=%s WHERE ID_Pedido=%s", (data_pedido, id_cliente, id_pedido))
    conn.commit()
    cursor.close()
    conn.close()

def delete_pedido(id_pedido):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pedidos WHERE ID_Pedido=%s", (id_pedido,))
    conn.commit()
    cursor.close()
    conn.close()

# Funções CRUD para a tabela ItensPedido

def create_item_pedido(id_pedido, id_produto, quantidade, preco_unitario):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ItensPedido (ID_Pedido, IDProduto, Quantidade, PrecoUnitário) VALUES (%s, %s, %s, %s)",
                   (id_pedido, id_produto, quantidade, preco_unitario))
    conn.commit()
    cursor.close()
    conn.close()

def read_itens_pedido():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ItensPedido")
    for (ID_Item, ID_Pedido, IDProduto, Quantidade, PrecoUnitário) in cursor:
        print(f"ID_Item: {ID_Item}, ID_Pedido: {ID_Pedido}, IDProduto: {IDProduto}, Quantidade: {Quantidade}, PrecoUnitário: {PrecoUnitário}")
    cursor.close()
    conn.close()

def update_item_pedido(id_item, id_pedido, id_produto, quantidade, preco_unitario):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ItensPedido SET ID_Pedido=%s, IDProduto=%s, Quantidade=%s, PrecoUnitário=%s WHERE ID_Item=%s",
                   (id_pedido, id_produto, quantidade, preco_unitario, id_item))
    conn.commit()
    cursor.close()
    conn.close()

def delete_item_pedido(id_item):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ItensPedido WHERE ID_Item=%s", (id_item,))
    conn.commit()
    cursor.close()
    conn.close()

# Exemplo de uso

if __name__ == "__main__":
    # Exemplos de operações CRUD para Produtos
    create_produto("Camiseta", 19.99)
    print("Produtos:")
    read_produtos()
    update_produto(1, "Camiseta atualizada", 29.99)
    delete_produto(1)  # Chamada de exemplo de função de delete

    # Exemplos de operações CRUD para Fornecedores
    create_fornecedor("Fábrica Daora", "Rua Bonita", "123456789")
    print("Fornecedores:")
    read_fornecedores()
    update_fornecedor(1, "Fábrica Daora Atualizada", "Rua Bonita Atualizado", "987654321")
    delete_fornecedor(1)  # Chamada de exemplo de função de delete

    # Exemplos de operações CRUD para Clientes
    create_cliente("Joãozin Estiloso", "Avenida Do Fluxo", "123456789")
    print("Clientes:")
    read_clientes()
    update_cliente(1, "Joãozin Estiloso Atualizado", "Avenida Do Fluxo Atualizada", "987654321")
    delete_cliente(1)  # Chamada de exemplo de função de delete

    # Exemplos de operações CRUD para Pedidos
    create_pedido("2024-06-16", 1)
    print("Pedidos:")
    read_pedidos()
    update_pedido(1, "2024-06-17", 2)
    delete_pedido(1)  # Chamada de exemplo de função de delete

    # Exemplos de operações CRUD para ItensPedido
    create_item_pedido(1, 1, 2, 19.99)
    print("Itens de Pedido:")
    read_itens_pedido()
    update_item_pedido(1, 1, 2, 3, 29.99)
    delete_item_pedido(1)  # Chamada de exemplo de função de delete
