import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import json
import os

ARQUIVO_SENHAS = "senhas.json"

# Função para gerar senha segura
def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return ""

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Função para salvar senha no arquivo JSON
def salvar_senha(servico, senha):
    dados = {}
    if os.path.exists(ARQUIVO_SENHAS):
        with open(ARQUIVO_SENHAS, "r") as f:
            dados = json.load(f)
    dados[servico] = senha
    with open(ARQUIVO_SENHAS, "w") as f:
        json.dump(dados, f, indent=4)

# Função para carregar senhas do JSON
def carregar_senhas():
    if os.path.exists(ARQUIVO_SENHAS):
        with open(ARQUIVO_SENHAS, "r") as f:
            return json.load(f)
    return {}

# Função de clique para gerar e exibir a senha
def ao_gerar():
    try:
        tamanho = int(spinbox_tamanho.get())
        senha = gerar_senha(
            tamanho,
            var_maiusculas.get(),
            var_minusculas.get(),
            var_numeros.get(),
            var_simbolos.get()
        )
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Tamanho inválido")

# Salvar serviço + senha
def ao_salvar():
    servico = entry_servico.get().strip()
    senha = entry_senha.get().strip()
    if not servico or not senha:
        messagebox.showwarning("Atenção", "Preencha o serviço e gere a senha")
        return
    salvar_senha(servico, senha)
    messagebox.showinfo("Salvo", f"Senha salva para {servico}")
    entry_servico.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    atualizar_lista()

def atualizar_lista():
    listbox_senhas.delete(0, tk.END)
    dados = carregar_senhas()
    for servico, senha in dados.items():
        listbox_senhas.insert(tk.END, f"{servico}: {senha if mostrar_senhas.get() else '*' * len(senha)}")

def alternar_mostrar():
    atualizar_lista()

# GUI
root = tk.Tk()
root.title("🔐 Gerenciador de Senhas")
root.geometry("600x500")
root.configure(bg="#1e272e")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#1e272e", foreground="#ffffff", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.configure("TCheckbutton", background="#1e272e", foreground="#ffffff", font=("Segoe UI", 10))

frame = ttk.Frame(root, padding=20)
frame.pack(pady=10)

# Campo de serviço
ttk.Label(frame, text="Serviço (ex: Google, YouTube)").grid(row=0, column=0, sticky="w")
entry_servico = ttk.Entry(frame, width=40)
entry_servico.grid(row=1, column=0, columnspan=2, pady=5)

# Tamanho
ttk.Label(frame, text="Tamanho da senha").grid(row=2, column=0, sticky="w")
spinbox_tamanho = ttk.Spinbox(frame, from_=8, to=64, width=10)
spinbox_tamanho.set(12)
spinbox_tamanho.grid(row=2, column=1, sticky="e")

# Checkboxes
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

ttk.Checkbutton(frame, text="Maiúsculas", variable=var_maiusculas).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(frame, text="Minúsculas", variable=var_minusculas).grid(row=3, column=1, sticky="w")
ttk.Checkbutton(frame, text="Números", variable=var_numeros).grid(row=4, column=0, sticky="w")
ttk.Checkbutton(frame, text="Símbolos", variable=var_simbolos).grid(row=4, column=1, sticky="w")

# Campo da senha
ttk.Label(frame, text="Senha Gerada").grid(row=5, column=0, sticky="w", pady=(10, 0))
entry_senha = ttk.Entry(frame, width=40, font=("Courier New", 10))
entry_senha.grid(row=6, column=0, columnspan=2, pady=5)

# Botões
ttk.Button(frame, text="Gerar Senha", command=ao_gerar).grid(row=7, column=0, pady=10)
ttk.Button(frame, text="Salvar Senha", command=ao_salvar).grid(row=7, column=1, pady=10)

# Mostrar/Ocultar senhas salvas
mostrar_senhas = tk.BooleanVar(value=False)
ttk.Checkbutton(root, text="Mostrar senhas salvas", variable=mostrar_senhas, command=alternar_mostrar).pack()

# Lista de senhas salvas
listbox_senhas = tk.Listbox(root, width=70, height=10, font=("Segoe UI", 10))
listbox_senhas.pack(pady=10)

atualizar_lista()
root.mainloop()
