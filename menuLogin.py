from imports import *
from diretorio import *

def menulogin(app,login,cadastro):
    
    global usuario, senha, label_resultado, lbl_image

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("350x450")
    imagem_pil = Image.open(caminho_imagem)
    labelimg = ctk.CTkImage(light_image=imagem_pil, size=(150,150))
    lbl_image = ctk.CTkLabel(master=app, image=labelimg,text='')
    lbl_image.pack(pady=(20,0))

    label_usuario = ctk.CTkLabel(app,text="Usuário: ", font=('Arial', 16))
    label_usuario.pack(pady=(10,0))
    usuario = ctk.CTkEntry(app,placeholder_text='Usuário')
    usuario.pack(pady=(0,0))

    label_senha = ctk.CTkLabel(app, text="Senha: ", font=('Arial', 16))
    label_senha.pack(pady=(0,0))
    senha = ctk.CTkEntry(app,placeholder_text='password', show ="*")
    senha.pack(pady=(0,0))

    botao_entrar = ctk.CTkButton(app, text="Entrar", command=lambda: login(app, usuario, senha, label_resultado))

    botao_entrar.pack(pady=20)

    botao_cadastro = ctk.CTkButton(app, text="Cadastrar-se",command=lambda: cadastro(app))

    botao_cadastro.pack(pady=0)

    label_resultado = ctk.CTkLabel(app,text='',font=('Arial', 16,"bold"))
    label_resultado.pack(pady=20)