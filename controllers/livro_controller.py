'''
padrão MVC(tambem existem outros padroes como o MVT ou MVP)
'''
from database.db import Database # Estou buscanco da pasta database o codigo db
from views.livro_view import LivroView
#from pasta.arquivo import class == da pasta tal e tal arquivo import tal class


class LivroController:
    def __init__(self, db_config):
        self.db = Database(
            db_config["dbname"],
            db_config["user"],
            db_config["password"],
            db_config["host"],
            db_config["port"]
        )
        
        self.criar_tabela_se_nao_existir()
        self.view = LivroView()
        
    def criar_tabela_se_nao_existir(self):
        conn = self.db.connect()
        if conn: # se a tabela criada não existe entao
            cur = conn.cursor() # 
            cur.execute("""
                CREATE TABLE IF NOT EXISTS livros(
                   id SERIAL PRIMARY KEY,
                   titulo VARCHAR(255) NOT NULL,
                   autor VARCHAR(255) NOT NULL,
                   ano INTEGER NOT NULL,
                   isbn VARCHAR(13) 
                );
                
            """)
            
            conn.commit()
            cur.close()
            conn.close()
            
    def adicionar_livro(self, id, titulo, autor, ano, isbn):
        conn = self.bd.connect()
        if conn: # Se essa conexão for verdadeira
            cur = conn.cursor() # cur é um objeto criado a partir de uma conexão com o banco de dados
            # execute(): Método do cursor que executa uma consulta SQL passada por argumento
            cur.execute(
                # %s é um placeholder que será substraido pelos valores da tupla a seguir.
                # O psycopg2 substitui esse %s por valores reais de forma segura, evitando injeção de SQL
                "Isert INTO livros(id, titulo, autor, ano, isbn) VALUES(%s, %s, %s, %s, %s) ON CONFLICT(id) DO NOTHING", #on conflict == se eu tiver um conflito nesse campo em com esse parametro que eu vom encontrar
                (id, titulo, autor, ano, isbn)
            )# s% == evita problema com dados
            
            conn.commit() # Confirma a transação, salvando as mudanças do banco de dados
            cur.close()
            conn.close()
            
            print("Livro adicionado com sucesso!")
            
        else:
            print("Erro ao conectar ao banco de dados.")
            
    def listar_livros(self, livros):
        self.view.mostrar_livros(livros)