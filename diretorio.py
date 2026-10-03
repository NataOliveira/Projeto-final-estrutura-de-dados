import os, sys

#pega o diretória atual da pasta atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(diretorio_atual, "logo.png")
ico = os.path.join(diretorio_atual, "logo.ico")

# Adiciona a pasta ao caminho do banco de dados
caminho_mydb = os.path.join(diretorio_atual, "MyDB")
sys.path.append(caminho_mydb)