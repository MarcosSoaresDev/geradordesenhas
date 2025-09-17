import string
import random
import customtkinter as ctk
from tkinter import messagebox


 
def update_label():
    try:
        tamanho_senha = int(tamanho_entry.get())

        if tamanho_senha <=0:
           messagebox.askokcancel("ERRO!","Por favor insira um tamanho inteiro válido")

        letras = string.ascii_letters   
        numeros = string.digits      
        simbolos = string.punctuation 


        todos_caracteres = letras + numeros + simbolos


        senha_gerada = "".join(random.choice(todos_caracteres) for _ in range(tamanho_senha))
        label.configure(text=f"A senha é: {senha_gerada}")  
    except ValueError:
     messagebox.askokcancel("ERRO!", "Por favor insira um número inteiro válido")
    except Exception as e:
        messagebox.askokcancel("ERRO!", f"Ocorreu um erro:{e}")



app = ctk.CTk()
app.geometry("400x200")
app.title("GERADOR DE SENHAS")
app.configure(fg_color="#53C3E9")



input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20)

frame2 = ctk.CTkFrame(app)
frame2.pack(pady=10)

tamanho_label = ctk.CTkLabel(input_frame, text="Tamanho da Senha:")
tamanho_label.pack(side="left", padx=10)

tamanho_entry = ctk.CTkEntry(input_frame, width=50)
tamanho_entry.insert(0, "10") 
tamanho_entry.pack(side="left", padx=10)

button = ctk.CTkButton(app, text="Gerar Senha",command=update_label)
button.pack(padx=20, pady=10)

label = ctk.CTkLabel(frame2, text="Aguardando texto...")
label.pack(pady=10)

app.mainloop()