from tkinter import *
from funcoes import *
from tkinter import messagebox


def abrir_novo_sistema():
    nome = entry_nome.get()
    valor = entry_senha.get()

    try:
        with open('login.json', 'r', encoding='utf-8') as arquivo:
            dados_login = json.load(arquivo)
            for i in dados_login:
                if nome == i['Usuario'] and valor == i['Senha']:
                    login.destroy()
                    janela_principal()
                    break
            else:
                messagebox.showerror("Erro", "Usúario ou Senha incorreta!")  # Janela de erro
    except FileExistsError:
        print('Arquivo não encontrado!')

def mostrando_senha(): 
    if marcado.get() == 1:
        entry_senha.config(show='')
    else:
        entry_senha.config(show='*')

login = Tk()
login.title("")
login.geometry("275x110+570+340")
login.resizable(False, False)

login.iconbitmap('Cadastro de Ativos/arqs/download.ico')

label_nome = Label(login, text="Nome:", font=('Roboto', 12))
label_nome.grid(row=0, column=0, sticky="w", padx=5, pady=(1, 0)) 

label_senha = Label(login, text="Senha:", font=('Roboto', 12))
label_senha.grid(row=1, column=0, sticky='w', padx=5, pady=(1, 0))

# Digite 1
entry_nome = Entry(login, width=23, bg='#f0f0f0', font=('Roboto', 10))
entry_nome.place(x=100, y=5)

# Digite 2
entry_senha = Entry(login, width=23, show='*', font=('Roboto', 10))
entry_senha.place(x=100, y=30)

btn_login = Button(login, text="Login", bg="#2196F3", fg="white", width=15, command=abrir_novo_sistema)
btn_login.place(x=7, y=80)

btn_creds = Button(login, text='Créditos', width=15, bg="#DBDBDB", fg='black', command=creditos)
btn_creds.place(x=150, y=80)

# 0 = desmarcado, 1 = marcado
marcado = IntVar()

mostrar_senha = Checkbutton(login, variable=marcado, width=10, text='Mostrar Senha', anchor='n',command=mostrando_senha, relief="flat")
mostrar_senha.place(x=170, y=50)

login.mainloop()