#import da biblioteca Matplotlib
import matplotlib.pyplot as plt
#Classe
class Livro: 
  def __init__(self, titulo, autor, genero, quantidade):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.quantidade = quantidade
  #retornando o objeto de forma legível
  def __str__(self):
    return f"Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}"
#lista onde ficará armazenada os livros
biblioteca = []
#função para cadastrar o livro 
def cadastrar_livro(titulo, autor, genero, quantidade):
    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(livro)
    print(f'Livro {titulo} cadastrado com sucesso!')
#função para listar os livros
def listar_livros():
    if biblioteca:
        print('Lista de livros disponíveis:')
        for livro in biblioteca:
            print(livro)
    else:
        print('Nenhum livro cadastrado.')



#função para buscar livro pelo titulo
def buscar_livro(titulo):
  for livro in biblioteca:
    if livro.titulo.lower() == titulo.lower():
      return print(f'Livro encontrado:{livro}') 
    else:
      return print(f'o livro {titulo} não foi encontrado')

def gerar_grafico():
    if not biblioteca:
        print('Nenhum livro cadastrado para gerar gráfico.')
        return
    
    # Dicionário para contar a quantidade de livros por gênero
    generos = {}
    
    for livro in biblioteca:
      #verifica se o genero do livro atual ja existe como chave no dicionário
        if livro.genero in generos:
          #se ja existe, incrementa a quantidade
            generos[livro.genero] += livro.quantidade
        else:
          #se não, cria um chave com o nome do gênero
            generos[livro.genero] = livro.quantidade
    
    # Gerando o gráfico
    generos_lista = list(generos.keys())
    quantidades_lista = list(generos.values())
    
    plt.bar(generos_lista, quantidades_lista)
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

#cadastro dos livros        
cadastrar_livro('Código Limpo', 'Robert Cecil Martin', 'Informática', 15)
cadastrar_livro('Duna: livro 1', 'Frank Herbert','Ficção científica', 8 )
cadastrar_livro("1984", "George Orwell", "Distopia", 5),
cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 7),
cadastrar_livro("Dom Quixote", "Miguel de Cervantes", "Clássico", 3),
cadastrar_livro("Neuromancer", "William Gibson", "Ficção Científica", 4),
cadastrar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 10),
cadastrar_livro("Admirável Mundo Novo", "Aldous Huxley", "Distopia", 6),
cadastrar_livro("O Grande Gatsby", "F. Scott Fitzgerald", "Clássico", 2)

#listagem dos livros
listar_livros()

#buscar livro
buscar_livro('Código Limpo')

#gerar gráfico
gerar_grafico()