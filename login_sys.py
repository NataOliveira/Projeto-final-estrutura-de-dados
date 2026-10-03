import bcrypt
from conexao_db import conectar_banco, encerrar_conectar_banco

def login(app, usuario, senha, label_resultado):
    # Recebe o input do usuário
    from home_sys import homeapp

    usuario_entrada = usuario.get().strip()
    senha_input = senha.get().strip()
    conexao = None
    cliente = None
    cursor = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes WHERE usuario = %s', (usuario_entrada,))
        cliente = cursor.fetchone()

        if cliente and bcrypt.checkpw(senha_input.encode('utf-8'),cliente[3].encode('utf-8')):
            label_resultado.configure(text='Logado com Sucesso',text_color='green')
            homeapp(app, cliente)

        else:
            label_resultado.configure(text='Usuário ou Senha inválios',text_color='red')

    except Exception as erro:
        label_resultado.configure(text='Sistema offline', text_color='red')
        print(erro)
        return

    finally:
        if cursor:
            cursor.close()
        if conexao:
            encerrar_conectar_banco(conexao)
