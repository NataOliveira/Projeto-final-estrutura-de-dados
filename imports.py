# Importações de bibliotecas
import sys
import customtkinter as ctk
import bcrypt
import os
from datetime import datetime
from PIL import Image
from tkinter import messagebox

# Importa as funções da conexão
from conexao_db import conectar_banco,encerrar_conectar_banco

# Importações para criação do app 
from login_sys import login
from menuLogin import menulogin
from cadastro import cadastro
from login_sys import login
from menuLogin import menulogin