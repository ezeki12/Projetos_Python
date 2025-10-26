import tkinter as tk
from datetime import datetime
import locale

# configurar a data em português
try:
     locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
     pass

 # Criação da janela prncipal
janela = tk.Tk()
janela.title('Relógio Digital')
janela.geometry('400x200')
janela.resizable(False, False)
janela.configure(bg='#1e1e2e') # Fundo escuro elegante

# Estilos
fonte_hora = ('Helvetica', 48, 'bold')
fonte_data = ('Helvetica', 16)

# Widgets
lbl_hora = tk.Label(janela, font=fonte_hora, fg='#00ffcc', bg='#1e1e2e')
lbl_hora.pack(pady=(30, 0))

lbl_data = tk.Label(janela, font=fonte_data, fg='#ffffff', bg='#1e1e2e')
lbl_data.pack(pady=(10, 0))
 # Função para atualizar o relógio
def atualizar():
    agora = datetime.now()
    hora = agora.strftime('%H:%M:%S')
    data = agora.strftime('%A, %d de %B de %Y').capitalize()

    lbl_hora.config(text=hora)
    lbl_data.config(text=data)

    janela.after(1000, atualizar) #atualiza a cada 1 segundo

# inicia o relógio
atualizar()

# Executa o loop da interface
janela.mainloop()