import sqlite3

conexao = sqlite3.connect('DBTHAIS')

cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100) NOT NULL, idade INT NOT NULL, curso VARCHAR(100) NOT NULL)')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(nome, idade , curso) VALUES ("Flavia", 18, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(nome, idade , curso) VALUES ("Maria", 19, "Engenharia")')
cursor.execute('INSERT INTO alunos(nome, idade , curso) VALUES ("Ana", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(nome, idade , curso) VALUES ("José", 20, "Medicina")')
cursor.execute('INSERT INTO alunos(nome, idade , curso) VALUES ("João", 21, "Psicologia")')

# 3 - a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos')

# 3 - b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

# 3- c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética

dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')


# 3 d) Contar o número total de alunos na tabela

dados = cursor.execute('SELECT count(nome) FROM alunos')


# 4 - a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade = 19 WHERE nome = "Flavia"')

# 4 - b) Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id = 4')


# 5- Crie uma tabela chamada "clientes" com os campos: id (chaveprimária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela

cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100) NOT NULL, idade INT NOT NULL, saldo float)')

cursor.execute('INSERT INTO clientes(nome, idade , saldo) VALUES ("Flavia", 25, 1000)')
cursor.execute('INSERT INTO clientes(nome, idade , saldo) VALUES ("Maria", 31, 1500)')
cursor.execute('INSERT INTO clientes(nome, idade , saldo) VALUES ("Ana", 32, 1001)')
cursor.execute('INSERT INTO clientes(nome, idade , saldo) VALUES ("José", 26, 5000)')
cursor.execute('INSERT INTO clientes(nome, idade , saldo) VALUES ("João", 19, 500)')


# 6 - a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')


# 6- b) Calcule o saldo médio dos clientes.

dados = cursor.execute('SELECT AVG(saldo) FROM clientes')


# 6- c) Encontre o cliente com o saldo máximo.

dados = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')

# d) Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT count(nome) FROM clientes WHERE saldo > 1000')


# 7 = a) Atualize o saldo de um cliente específico

cursor.execute('UPDATE clientes SET saldo = 5200 WHERE id = 4')


#7 - b) Remova um cliente pelo seu ID.


cursor.execute('DELETE FROM clientes  WHERE id = 4')


# 8 - Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra


cursor.execute('CREATE TABLE compras(id_compras  INTEGER PRIMARY KEY AUTOINCREMENT,  produto VARCHAR(100), valor REAL, cliente_id INTEGER, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')


cursor.execute('INSERT INTO compras(produto, valor , cliente_id) VALUES ("Fone", 250,1)')
cursor.execute('INSERT INTO compras(produto, valor , cliente_id) VALUES ("Caixa de Som", 200,2)')
cursor.execute('INSERT INTO compras(produto, valor , cliente_id) VALUES ("Smartphone", 2500,3)')
cursor.execute('INSERT INTO compras(produto, valor , cliente_id) VALUES ("Geladeira", 2500,5)')


dados = cursor.execute('SELECT a.nome, b.produto, b.valor FROM clientes as a INNER JOIN compras as b on a.id = b.cliente_id')



for i in dados:
    print(i)


conexao.commit()
conexao.close()