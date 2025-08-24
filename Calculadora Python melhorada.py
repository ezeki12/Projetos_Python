import tkinter as tk

# Funções principais
def clicar(botao):
    atual = visor.get()
    visor.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, 'Erro')

def limpar():
    visor.delete(0, tk.END)

# janela principal
janela = tk.Tk()
janela.title('Calculadora Moderna')
janela.geometry('320x420')
janela.config(bg='#1e1e2f') # cor de fundo escura

# visor da calculadora
visor = tk.Entry(janela, font=('Arial', 24), justify='right', bg="#2d2d3a", fg="white", bd=0, insertbackground="white")
visor.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# função para criar botões estilizados
def criar_botao(frame, texto, cor_bg, cor_fg, comando):
    return tk.Button(
     frame, text=texto, font=('Arial', 16, 'bold'),
     bg=cor_bg, fg=cor_fg, activebackground='#44475a',
     relief='flat', height=3, width=6, command=comando

    )

# layout dos botões
botoes = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame_botoes = tk.Frame(janela, bg='#1e1e2f')
frame_botoes.pack()

for linha in botoes:
    frame_linha = tk.Frame(frame_botoes, bg='#1e1e2f')
    frame_linha.pack(expand=True, fill='both')
    for botao in linha:
        if botao == '=':
            b = criar_botao(frame_linha, botao, "#50fa7b", "black", calcular)
        else:
            b = criar_botao(frame_linha, botao, "#6272a4", "white", lambda bt=botao: clicar(bt))
        b.pack(side='left', expand=True, fill='both', padx=2, pady=2)

# Botão de limpar
botao_limpar = tk.Button(
    janela, text="Limpar", font=("Arial", 16, "bold"),
    bg="#ff5555", fg="white", activebackground="#ff6e6e",
    relief="flat", height=2, command=limpar
)
botao_limpar.pack(fill='both', padx=10, pady=10)

# Rodar aplicação
janela.mainloop()

