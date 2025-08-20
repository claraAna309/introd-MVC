import psycopg2
from psycopg2 import sql

class Databese:
    '''
    Classe Data Base é responsavel em verificar
    se o banco ja existe, se não existe irá
    criar
    '''
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
    def criar_database_se_nao_existir(self): 
        try:
            # conecta ao Banco de Dados
            conn = psycopg2.connect(
                dbname = self.dbname,
                user = self.dbname,
                password = self.password,
                host = self.host,
                port = self.port
            ) # Esta passando os parametros do construtor
            
            conn.autocommit = True
            cur = conn.cursor() # cur == cursor
            # Verifica se o Banco ja existe
            cur.execute("SELECT 1 FROM 'pg_database WHERE datname = %s", (self.dbname))
            exists = cur.fetchone() # Aqui ele esta percorrendo a lista de bancos e vendo se ja existe um banco igual ao que o usuario esta criando
            # 'exists' recebe o nome do banco ja existente que tem o nome igual ao que esta sendo criado
            
            if not exists: # Se ele não existe, vai ser criado aqui
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname))) # Cria DB
                cur.close()
                conn.closse() # Quebrando a conexão com o postgre aqui
                
        except Exception as e: # Caso haja uma exceção, ira printar uma mensagem de erro, com 'e' sendo o erro ocorrido
            print(f"Erro ao criar o banco de dados: {e}") # 'e' == apelido para 'exection'
            
    def connect(self):
        self.criar_database_se_nao_existir()
        try: 
            '''
            Aqui dentro esta o fluxo de execução de um codigo,
            se não acontecer nenhum erro o try vai ser executado 
            tranquilamente
            Se ocorrer algum erro o que vai ser executado vai ser o 'except'
            '''
            conn = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )
            return conn
        except Exception as e:
            print(f"Erro ao cenectar ao banco de dados: {e}")
            return None