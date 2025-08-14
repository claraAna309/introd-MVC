from controllers.livro_controller import LivroController

def main():
    db_config = {
        "dbname" : "intro_mvc",
        "user" : "postgres",
        "password" : "wcc@2023",
        "host" : "127.0.0.1",
        "port" : "5433"
    }
    
    livro_controller = LivroController(db_config)
    
    # Exemplo de uso
    livro_controller.adicionar_livro(1, "Percy Jackson: O Ultimo Olimpiano", "Ana Clara", 2001, "3284hr823hhe8")
    
if __name__ == "__main__":
    main()