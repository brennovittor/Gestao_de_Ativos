from tkinter import *
import json
import os
from tkinter import messagebox

janela_cadastro = False
janela_status = False
janela_relatorio = False

def creditos():
    janela = Toplevel()
    janela.geometry('300x150')
    janela.resizable(False, False)
    janela.iconbitmap('Cadastro de Ativos/arqs/1d664e5f-4d58-4780-8939-908a8753db0a.ico')

    janela.title('Créditos')

    texto = Label(janela, text='Aprendizado: @Dev Jhonathan\n Desenvolvedor: @Brenno\n PIM(UNIP): Samantha, Eduardo, Thiago e Peterson.')
    direitos = Label(janela, text='© 2025 Tuckersoft. Todos os direitos reservados.')
    texto.place(x=10, y=10)
    direitos.place(x=30, y=100)
def apagar_dados(campos):
    for campo in campos:
        campo.delete(0, END)

def salvar_arquivo(ID, descricao, quantidade, valor, notafiscal, janela):
    ID_valor = ID.get()
    descricao_valor = descricao.get()
    quantidade_valor = quantidade.get()
    valor_valor = valor.get()
    nota_fiscal = notafiscal.get()

    if not ID_valor or not descricao_valor or not quantidade_valor or not valor_valor or not nota_fiscal:
        messagebox.showwarning('Atenção', 'Preencha todos os dados por favor!')
        return
    
    dados = {
        'ID': ID_valor,
        'DESCRIÇÃO': descricao_valor,
        'QUANTIDADE': quantidade_valor,
        'VALOR': valor_valor,
        'NOTA FISCAL': nota_fiscal,
        'STATUS': 'Ativo'
    }

    caminho = 'data/dados.json'
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            try:
                dados_antigos = json.load(arquivo)
            except (json.JSONDecodeError, FileNotFoundError):
                dados_antigos = []
        dados_antigos.append(dados)
    else:
        dados_antigos = [dados]
        
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_antigos, arquivo, indent=4, ensure_ascii=False)
    apagar_dados([ID, descricao, quantidade, valor, notafiscal])
    messagebox.showinfo('Sucesso', 'Ativo salvo com sucesso!')
    if procurar:
        procurar.delete(0, END)
        listar_ativos()

def cadastro():
    global janela_cadastro
    if janela_cadastro:
        return
    
    janela_cadastro = True
    Janela = Tk()
    Janela.geometry('350x200+400+400')
    Janela.resizable(False, False)
    Janela.iconbitmap('Cadastro de Ativos/arqs/download.ico')
    Janela.title('Cadastro')


    todos_os_bg = '#f2efeb'
    todas_as_fontes = ('Arial', 14)
    Janela.config(background=todos_os_bg)

    id_cadastro = Label(Janela, text='ID: ', background=todos_os_bg, font=todas_as_fontes, fg='black')
    id_cadastro.grid(column=0)
    id = Entry(Janela, width=50, font=(15))
    id.grid(column=1, row=0)

    descricao_cadastro = Label(Janela, text='Descrição: ', background=todos_os_bg, font=todas_as_fontes, fg='black')
    descricao_cadastro.grid(column=0, row=1)
    descricao = Entry(Janela, width=50, font=(15))
    descricao.grid(column=1, row=1)

    quantidade_cadastro = Label(Janela, text='Quantidade: ', background=todos_os_bg, font=todas_as_fontes, fg='black')
    quantidade_cadastro.grid(column=0)
    quantidade = Entry(Janela, width=50, font=(15))
    quantidade.grid(column=1, row=2)

    valor_cadastro = Label(Janela, text='Valor: ', background=todos_os_bg, font=todas_as_fontes, fg='black')
    valor_cadastro.grid(column=0)
    valor = Entry(Janela, width=50, font=(15))
    valor.grid(column=1, row=3)

    nota_fiscal_cadastro = Label(Janela, text='Nota Fiscal: ', background=todos_os_bg, font=todas_as_fontes, fg='black')
    nota_fiscal_cadastro.grid(column=0)
    nota_fiscal = Entry(Janela, width=50, font=(15))
    nota_fiscal.grid(column=1, row=4)

    salvar_cadastro = Button(
        Janela,
        text='Cadastrar',
        command=lambda: salvar_arquivo(id, descricao, quantidade, valor, nota_fiscal, Janela),
        width=40, 
        height=1,
        fg='white',
        background='green',
        font=('Arial', 10),
        cursor='hand2'
    )
    salvar_cadastro.place(x=175, y=175, anchor='center')

    def ao_fechar():
        global janela_cadastro
        janela_cadastro = False
        Janela.destroy()

    Janela.protocol("WM_DELETE_WINDOW", ao_fechar)
    Janela.mainloop()

procurar = None

def listar_ativos():
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for index, item in enumerate(dados):
                procurar.insert(END, f'{index +1}: {item['DESCRIÇÃO']}, Status: {item['STATUS']}')
    except:
        print('Arquivo não existe')


def detalhes():
    try:
        selecao = procurar.get(procurar.curselection())
    
        sem_numero = selecao.split(":", 1)[1].strip()
        nome = sem_numero.split(", Status:")[0].strip()
        global janela_relatorio
        if janela_relatorio:
            return
        
        janela_relatorio = True
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for dado in dados:
                if dado['DESCRIÇÃO'] == nome:
                    janela = Toplevel()
                    janela.geometry('400x200')
                    janela.iconbitmap('Cadastro de Ativos/arqs/download.ico')
                    janela.resizable(False, False)
                    janela.title('Relatório')
                    

                    fontes = 'Roboto'
                    # ID
                    id1 = f'ID: {dado['ID']}'
                    desc1 = Label(janela, text=id1, font=fontes)
                    desc1.place(x=10, y=10)

                    # Descrição
                    desc2 = Label(janela, text=f'NOME: {nome}', font=fontes)
                    desc2.place(x=10, y=30)

                    # Quantidade
                    quantidade = f'QUANTIDADE: {dado['QUANTIDADE']}'
                    desc3 = Label(janela, text=quantidade, font=fontes)
                    desc3.place(x=10, y=50)
                    # Valor
                    valor = f'VALOR: R${dado['VALOR']}'
                    desc4 = Label(janela, text=valor, font=fontes)
                    desc4.place(x=10, y=70)
                    # Nota Fiscal
                    nota_fiscal = f'NOTA FISCAL: {dado['NOTA FISCAL']}'
                    desc5 = Label(janela, text=nota_fiscal, font=fontes)
                    desc5.place(x=10, y=90)
                    # Status
                    status = f'STATUS: {dado['STATUS']}'
                    desc6 = Label(janela, text=status, font=fontes)
                    desc6.place(x=10, y=110)
    except:
        messagebox.showerror('Erro', 'Selecione um item da lista primeiro!')
        return
    
    def ao_fechar():
        global janela_relatorio
        janela_relatorio = False
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", ao_fechar)
    janela.mainloop()
                
def janela_principal():
    janela = Tk()
    janela.geometry('781x354+570+340')
    janela.resizable(False, False)
    janela.title('')
    janela.iconbitmap('Cadastro de Ativos/arqs/download.ico')

    cores_background = '#1c2120'
    cores_fontes = 'white'
    background_clicou = '#2a2f2e'
    texto_clicou = 'white'

    cadastrar_ativo = Button(
        janela,
        fg=cores_fontes,
        text='Cadastrar Ativo',
        font=('Arial'),
        background=cores_background,
        activebackground=background_clicou,
        activeforeground=texto_clicou,
        relief='flat',
        bd=0,
        command=cadastro
    )
    cadastrar_ativo.place(x=75, y=250, width=142, height=34, anchor='center')

    global procurar
    procurar = Listbox(janela, background='#1c2120', fg='white', font=('Roboto', 11))
    procurar.place(width=450, height=330, x=325, y=10)

    def gerar_relatorio():
        janela = Toplevel()
        janela.title("Relatório de Ativos")
        janela.geometry("500x400")
        janela.resizable(False, False)
        janela.iconbitmap('Cadastro de Ativos/arqs/download.ico')

        try:
            with open('dados.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

                total_ativos = len(dados)
                ativos_ativos = sum(1 for item in dados if item["STATUS"].lower() == "ativo")
                ativos_inativos = total_ativos - ativos_ativos
                valores = [float(item["VALOR"]) for item in dados]
                soma_total = sum(valores)

                texto_relatorio = f"===== RELATÓRIO DE ATIVOS =====\n\n"
                texto_relatorio += f"Total de ativos cadastrados: {total_ativos}\n"
                texto_relatorio += f"Ativos ativos: {ativos_ativos}\n"
                texto_relatorio += f"Ativos inativos: {ativos_inativos}\n"
                texto_relatorio += f"Valor total dos ativos: R$ {soma_total:.2f}\n\n"

                for item in dados:
                    texto_relatorio += (
                        f"ID: {item['ID']}\n"
                        f"Descrição: {item['DESCRIÇÃO']}\n"
                        f"Valor: R$ {item['VALOR']}\n"
                        f"Quantidade: {item['QUANTIDADE']}\n"
                        f"Nota Fiscal: {item['NOTA FISCAL']}\n"
                        f"Status: {item['STATUS']}\n\n"
                    )

        except FileNotFoundError:
            texto_relatorio = "Arquivo 'dados.json' não encontrado."
        except json.JSONDecodeError:
            texto_relatorio = "Erro ao ler o arquivo JSON."

        # Exibe o relatório em um widget Text (multi-linha)
        caixa_texto = Text(janela, wrap=WORD)
        caixa_texto.insert(END, texto_relatorio)
        caixa_texto.pack(expand=True, fill=BOTH)

    def selecionar():
        try:
            confirmar = messagebox.askyesno('Confirmação', 'Deseja mesmo apagar esse ativo?')
            if not confirmar:
                return
            
            item = procurar.get(procurar.curselection())
            descricao = item.split(': ', 1)[1]
            descricao1 = descricao.split(',')[0]

            with open('dados.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            for i, d in enumerate(dados):
                if d['DESCRIÇÃO'] == descricao1:
                    del dados[i]
                    break

            with open('dados.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            procurar.delete(0, END)
            listar_ativos()
            messagebox.showinfo("", f"'{descricao}' apagado com sucesso!")
        
        except:
            messagebox.showwarning("Erro", "Selecione um item para apagar.")

    def alterar_status():
        global janela_status
        if janela_status:
            return
        
        # Criando a janelinha para escolher o novo status
        janela = Toplevel()
        janela.title("Alterar Status")
        janela.geometry('300x130')
        janela.config(bg='lightgray')
        janela.resizable(False, False)
        janela.iconbitmap('Cadastro de Ativos/arqs/download.ico')

        janela_status = True
        try:
            with open('dados.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            def salvar_status(novo_status):
                selecoes = procurar.curselection()
                if not selecoes:
                    messagebox.showerror('Atenção', 'Selecione um item da lista primeiro!')
                    return
                selecionando = procurar.get(selecoes[0])
                numero = int(selecionando.split()[0].replace(":", "")) - 1

                if dados[numero]['STATUS'] == novo_status:
                    return messagebox.showerror('Erro', f'O STATUS desse ativo já está definido como: {novo_status}')
                
                dados[numero]['STATUS'] = novo_status
                with open('dados.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                procurar.delete(0, END)

                listar_ativos()
                messagebox.showinfo("Sucesso", f"Status alterado para {novo_status}")

            Label(janela, text="Escolha o novo status:", bg='lightgray', font=('Arial', 12)).pack(pady=10)

            Button(janela, text='Ativo', width=15, bg='green', fg='white',
                    command=lambda: salvar_status('Ativo')).pack(pady=5)

            Button(janela, text='Inativo', width=15, bg='red', fg='white',
                    command=lambda: salvar_status('Inativo')).pack(pady=5)
            def ao_fechar():
                global janela_status
                janela_status = False
                janela.destroy()

            janela.protocol("WM_DELETE_WINDOW", ao_fechar)
            janela.mainloop()

        except:
            janela_status = False
            messagebox.showwarning('Atenção', 'Erro.')


    apagar_ativo = Button(
        janela,
        fg=cores_fontes,
        text='Apagar Ativo',
        font=('Arial'),
        background=cores_background,
        activebackground=background_clicou,
        activeforeground=texto_clicou,
        relief='flat',
        bd=0,
        command=selecionar
        
    )
    apagar_ativo.place(x=75, y=293, width=142, height=34, anchor='center')

    alterar_status = Button(
        janela,
        fg=cores_fontes,
        text='Alterar Status',
        font=('Arial'),
        background=cores_background,
        activebackground=background_clicou,
        activeforeground=texto_clicou,
        relief='flat',
        bd=0,
        command=alterar_status
    )
    alterar_status.place(x=250, y=250, width=142, height=34, anchor='center')

    Relatorio = Button(
        janela,
        text='Detalhes',
        fg=cores_fontes,
        font=('Arial'),
        background=cores_background,
        activebackground=background_clicou,
        activeforeground=texto_clicou,
        relief='flat',
        bd=0,
        command=detalhes
    )
    Relatorio.place(x=250, y=293, width=142, height=34, anchor='center')
    
    selecionar = Button(
        janela,
        text='Gerar Relatório',
        fg=cores_fontes,
        font=('Arial'),
        background=cores_background,
        activebackground=background_clicou,
        activeforeground=texto_clicou,
        relief='flat',
        bd=0,
        command=gerar_relatorio

    )

    selecionar.place(x=97, y=315, width=142, height=34)
    listar_ativos()
    janela.mainloop()


if __name__ == '__main__':
    janela_principal()