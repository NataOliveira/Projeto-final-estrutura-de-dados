from imports import *
from diretorio import *

app = None
usuario = None
senha = None
label_resultado = None
conexao = None

# Definindo App
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
imagem_pil = Image.open(caminho_imagem)
app.iconbitmap(ico)
app.title('Dreyfus Bank')

menulogin(app, login, cadastro)
app.mainloop()
