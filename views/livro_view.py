'''
class LivrosView:
    def mostrar_livro(self, livro):
        print(livro)
        
    def mostrar_livros(self, livros):
        for livro in livros:
            self.mostrar_livro(livro)
'''

import tkinter as tk
from tkinter import ttk, messagebox
from controllers.livro_controller import LivroController

class LivroView:
    def __init__(self, controller):
        self.controller = controller
        self._show_livros_tela()
        
    @staticmethod # estou falando que o metodo é estatico, é um metodo da class    
    def iniciar_login_banco():
        def conectar():
            db_config = {
                "dbname": db_name_entry.get(), 
                "user": db_user_entry.get(),
                "password": db_password_entry.get(),
                "host": db_host_entry.get(),
                "port": db_port_entry.get()
            }
            try:
                controller = LivroController(db_config)
                login_win.destroy() # Destroi a tela de login
                LivroView(controller)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possivel conectar ao banco de dados:\n {e}")
        
        login_win = tk.Tk()# Intancia janela
        login_win.title("Conectar ao Banco de Dados")
        login_win.geometry("350x300")
        
        tk.Label(login_win, text="Host: ").pack(pady=2)# nome do quadradinho de escrever
        host_entry = tk.Entry(login_win)
        host_entry.pack()