import customtkinter as ctk
from tkinter import messagebox
from pixSys import grafo_pix

def tela_pix(app, cliente, voltar):
    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("500x500")

    titulo = ctk.CTkLabel(app, text="Área Pix", font=('Arial', 24, "bold"))
    titulo.pack(pady=20)

    cpf_logado = cliente[2]
    contatos_frequentes = grafo_pix.sugerir_contatos(cpf_logado, limite=3)

    frame_sugestoes = ctk.CTkFrame(app)
    frame_sugestoes.pack(pady=10, padx=20, fill="x")

    lbl_sugestoes = ctk.CTkLabel(frame_sugestoes, text="Contatos Frequentes:", font=('Arial', 16, "bold"))
    lbl_sugestoes.pack(pady=5)

    # Cria o formulário ANTES dos botões de sugestão 
    frame_novo_pix = ctk.CTkFrame(app, fg_color="transparent")
    frame_novo_pix.pack(pady=20)

    lbl_chave = ctk.CTkLabel(frame_novo_pix, text="Chave Pix (CPF/Email/Cel):")
    lbl_chave.pack()
    entry_chave_pix = ctk.CTkEntry(frame_novo_pix, width=250)
    entry_chave_pix.pack(pady=5)

    lbl_valor = ctk.CTkLabel(frame_novo_pix, text="Valor (R$):")
    lbl_valor.pack()
    entry_valor = ctk.CTkEntry(frame_novo_pix, width=150)
    entry_valor.pack(pady=5)

    def preencher_chave(c):
        entry_chave_pix.delete(0, "end")
        entry_chave_pix.insert(0, c)

    if contatos_frequentes:
        for contato in contatos_frequentes:
            ctk.CTkButton(
                frame_sugestoes,
                text=f"Pix para: {contato}",
                fg_color="#2c3e50",
                command=lambda c=contato: preencher_chave(c)
            ).pack(pady=5)
    else:
        ctk.CTkLabel(frame_sugestoes, text="Nenhum contato recente.").pack(pady=5)

    def efetuar_pix():
        chave_destino = entry_chave_pix.get().strip()
        valor = entry_valor.get().strip()

        if chave_destino and valor:
            grafo_pix.adicionar_transferencia(cpf_logado, chave_destino)
            messagebox.showinfo("Sucesso", f"Pix de R$ {valor} enviado para {chave_destino}!")
            tela_pix(app, cliente, voltar)
        else:
            messagebox.showwarning("Erro", "Preencha chave e valor.")

    ctk.CTkButton(frame_novo_pix, text="Enviar Pix", command=efetuar_pix, fg_color="green").pack(pady=15)
    ctk.CTkButton(app, text="Voltar", command=lambda: voltar(app, cliente)).pack(pady=10)