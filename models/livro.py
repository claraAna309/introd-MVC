class Livros:
    def __init__(self, id, titulo, autor, ano, isbn): # Construtor
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        
    def __str__(self):# str == transforma o objeto em string
        return f"Livro(ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, ISBN: {self.isbn})"
  