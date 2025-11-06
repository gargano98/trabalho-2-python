import tkinter as tk
from tkinter import filedialog, messagebox

def escolher_pdf():
    # Abre o seletor de arquivos
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    
    if caminho_arquivo:
        messagebox.showinfo("Arquivo Selecionado", f"Você escolheu:\n{caminho_arquivo}")
    else:
        messagebox.showwarning("Nenhum arquivo", "Nenhum arquivo PDF foi selecionado.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Selecionar PDF")
janela.geometry("300x150")

# Botão para selecionar o arquivo
botao = tk.Button(janela, text="Escolher PDF", command=escolher_pdf)
botao.pack(pady=40)

# Inicia a interface
janela.mainloop()
