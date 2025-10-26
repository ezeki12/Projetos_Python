import tkinter as tk
import random

# Função pra rolar o dado
def rolar_dado():
    numero = random.randint(1, 6)
    lbl_resultado.config(text=f"🎲 {numero}")

# Janela principal
janela = tk.Tk()
janela.title("Simulador de Dados")
janela.geometry("300x200")
janela.configure(bg="#1e1e2e")

# Título
lbl_titulo = tk.Label(janela, text="🎲 Simulador de Dado 🎲",
                      font=("Helvetica", 16, "bold"), fg="#00ffcc", bg="#1e1e2e")
lbl_titulo.pack(pady=10)

# Resultado
lbl_resultado = tk.Label(janela, text="Clique em Rolar!",
                         font=("Helvetica", 36, "bold"), fg="white", bg="#1e1e2e")
lbl_resultado.pack(pady=10)

# Botão
btn_rolar = tk.Button(janela, text="Rolar Dado", font=("Helvetica", 14, "bold"),
                      fg="#1e1e2e", bg="#00ffcc", activebackground="#00cc99",
                      relief="flat", command=rolar_dado)
btn_rolar.pack(pady=10)

# Executa a janela
janela.mainloop()
