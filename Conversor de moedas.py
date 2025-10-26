import tkinter as tk
import requests

def converter():
    valor = float(entrada_valor.get())
    de = entrada_de.get().upper()
    para = entrada_para.get().upper()

    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{de}"
        resposta = requests.get(url)
        dados = resposta.json()
        taxa = dados["rates"].get(para)

        if taxa:
            convertido = valor * taxa
            resultado_label.config(text=f"{valor:.2f} {de} = {convertido:.2f} {para}")
        else:
            resultado_label.config(text="Moeda inválida.")
    except Exception as e:
        resultado_label.config(text="Erro na conversão.")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("400x250")
janela.configure(bg="#1e1e2e")

# Widgets
tk.Label(janela, text="💱 Conversor de Moedas 💱", font=("Helvetica", 16, "bold"),
         fg="#00ffcc", bg="#1e1e2e").pack(pady=10)

frame = tk.Frame(janela, bg="#1e1e2e")
frame.pack(pady=10)

tk.Label(frame, text="Valor:", fg="white", bg="#1e1e2e").grid(row=0, column=0, padx=5, pady=5)
entrada_valor = tk.Entry(frame)
entrada_valor.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="De (ex: USD):", fg="white", bg="#1e1e2e").grid(row=1, column=0, padx=5, pady=5)
entrada_de = tk.Entry(frame)
entrada_de.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Para (ex: BRL):", fg="white", bg="#1e1e2e").grid(row=2, column=0, padx=5, pady=5)
entrada_para = tk.Entry(frame)
entrada_para.grid(row=2, column=1, padx=5, pady=5)

tk.Button(janela, text="Converter", font=("Helvetica", 12, "bold"),
          bg="#00ffcc", fg="#1e1e2e", relief="flat", command=converter).pack(pady=10)

resultado_label = tk.Label(janela, text="", font=("Helvetica", 14), fg="white", bg="#1e1e2e")
resultado_label.pack(pady=10)

janela.mainloop()
