-- Trabalho M3: Bancos De Dados I
-- Implementação De Crud
-- Kaio Saldanha, Davi Rangel e Marco Antônio Da Conceinção

-- Criando o banco de dados sistema_varejo
CREATE DATABASE sistema_varejo;

-- Usando o banco de dados sistema_varejo
USE sistema_varejo;

-- Criando a tabela Produtos
CREATE TABLE Produtos (
    IDProduto INT PRIMARY KEY,
    Nome VARCHAR(100),
    Preço DECIMAL(10,2)
);

-- Criando a tabela Fornecedores
CREATE TABLE Fornecedores (
    ID_Fornecedor INT PRIMARY KEY,
    Nome VARCHAR(100),
    Endereço VARCHAR(200),
    Telefone VARCHAR(20)
);

-- Criando a tabela Clientes
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Endereço VARCHAR(200),
    Telefone VARCHAR(20)
);

-- Criando a tabela Pedidos
CREATE TABLE Pedidos (
    ID_Pedido INT PRIMARY KEY,
    DataPedido DATE,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

-- Criando a tabela ItensPedido
CREATE TABLE ItensPedido (
    ID_Item INT PRIMARY KEY,
    ID_Pedido INT,
    IDProduto INT,
    Quantidade INT,
    PrecoUnitário DECIMAL(10,2),
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),
    FOREIGN KEY (IDProduto) REFERENCES Produtos(IDProduto)
);