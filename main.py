#import de todas as bilbiotecas necessárias
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Conectando ao banco de dados 
conexao = sqlite3.connect('dados_vendas.db')

#Criando  um cursor
cursor = conexao.cursor()

#Criando a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')
#Inserindo os dados na tabela
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
''')
conexao.commit()

#Após a criação da tabela, carregar os dados para a biblioteca Pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
print(df_vendas.head())
print(df_vendas.info())
print(df_vendas.describe())

#Total de vendas por categoria
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print(vendas_por_categoria)

#Total de vendas por mês
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes'] = df_vendas['data_venda'].dt.month
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
print(vendas_por_mes)

# Gráfico de vendas por categoria
plt.figure(figsize=(8, 6))
sns.barplot(x='categoria', y='valor_venda', data=vendas_por_categoria)
plt.title('Vendas por Categoria')
plt.ylabel('Total de Vendas (R$)')
plt.xlabel('Categoria')
plt.show()
# Gráfico de vendas por mês
plt.figure(figsize=(8, 6))
sns.lineplot(x='mes', y='valor_venda', data=vendas_por_mes, marker='o')
plt.title('Vendas Mensais')
plt.ylabel('Total de Vendas (R$)')
plt.xlabel('Mês')
plt.xticks(range(1, 13))
plt.show()