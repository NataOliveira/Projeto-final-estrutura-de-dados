import customtkinter as ctk
from PIL import Image
from diretorio import *
from menuLogin import menulogin
from cadastro import cadastro
from telaPix import tela_pix

def homeapp(app, cliente):
    # O app agora é passado como argumento para evitar importação circular
    from login_sys import login
    from cadastro import cadastro

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("600x650")

    imagem_pil = Image.open(caminho_imagem)
    labelimg = ctk.CTkImage(light_image=imagem_pil, size=(150,150))
    lbl_image = ctk.CTkLabel(master=app, image=labelimg,text='')
    lbl_image.pack(pady=(20,0))

    frame_grid = ctk.CTkFrame(app, fg_color='transparent')
    frame_grid.pack(pady=20)

    # Linha 3 - Nome
    label_nome = ctk.CTkLabel(frame_grid, text="Nome: ", font=('Arial', 16))
    label_nome.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    result_nome = ctk.CTkLabel(frame_grid, text=f"{cliente[1]} ", font=('Arial', 16))
    result_nome.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    # Linha 4 - CPF
    label_cpf = ctk.CTkLabel(frame_grid, text="CPF: ", font=('Arial', 16))
    label_cpf.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    result_cpf = ctk.CTkLabel(frame_grid, text=f"{cliente[2]} ", font=('Arial', 16))
    result_cpf.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Linha 5 - Email
    label_email = ctk.CTkLabel(frame_grid, text="Email: ", font=('Arial', 16))
    label_email.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    result_email = ctk.CTkLabel(frame_grid, text=f"{cliente[4]} ", font=('Arial', 16))
    result_email.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # Linha 6 - Data de Nascimento
    label_data_de_nascimento = ctk.CTkLabel(frame_grid, text="Data de Nascimento: ", font=('Arial', 16))
    label_data_de_nascimento.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    result_data_nascimento = ctk.CTkLabel(frame_grid, text=f"{cliente[5].strftime('%d/%m/%Y')} ", font=('Arial', 16))
    result_data_nascimento.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    # Linha 7 - Endreço
    label_endereço = ctk.CTkLabel(frame_grid, text="Endereço: ", font=('Arial', 16))
    label_endereço.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    result_endereço = ctk.CTkLabel(frame_grid, text=f"{cliente[6]}, {cliente[7]}, {cliente[8]}, {cliente[9]}, {cliente[10]} ", font=('Arial', 16))
    result_endereço.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    # Linha 12 - CEP
    label_cep = ctk.CTkLabel(frame_grid, text="CEP: ", font=('Arial', 16))
    label_cep.grid(row=12, column=0, padx=5, pady=5, sticky="w")
    result_cep = ctk.CTkLabel(frame_grid, text=f"{cliente[11]} ", font=('Arial', 16))
    result_cep.grid(row=12, column=1, padx=5, pady=5, sticky="w")

    # Linha 13 - Telefone
    label_telefone = ctk.CTkLabel(frame_grid, text="Telefone: ", font=('Arial', 16))
    label_telefone.grid(row=13, column=0, padx=5, pady=5, sticky="w")
    result_telefone = ctk.CTkLabel(frame_grid, text=f"{cliente[12]} ", font=('Arial', 16))
    result_telefone.grid(row=13, column=1, padx=5, pady=5, sticky="w")

    botao_voltar = ctk.CTkButton(frame_grid, text="Voltar", command=lambda: menulogin(app, login, cadastro))
    botao_voltar.grid(row=15, column=0, padx=5, pady=15, sticky="w")

    botao_pix = ctk.CTkButton(
        frame_grid, text="Pix",
        command=lambda: tela_pix(app, cliente, homeapp))
    botao_pix.grid(row=15, column=1, padx=5, pady=15, sticky="e")
