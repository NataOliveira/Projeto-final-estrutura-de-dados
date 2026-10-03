# Dreyfus Bank - Sistema Bancario Desktop

Aplicacao desktop desenvolvida em Python com CustomTkinter, que simula um sistema bancario com autenticacao segura, cadastro de clientes e funcionalidade de transferencias via Pix, com persistencia em banco de dados PostgreSQL.

## Sobre o Projeto

O sistema permite que um usuario se cadastre com dados pessoais e de endereco, realize login com validacao segura de senha (via bcrypt) e gerencie sua conta. A aplicacao conta com uma interface moderna, suporte a modo claro/escuro e um sistema de sugestoes de contatos para transferencias Pix baseado em frequencia de uso.

## Funcionalidades

- Autenticacao Segura:
  - Tela de Login com validacao de usuario e senha.
  - Senhas armazenadas utilizando hash bcrypt para maxima seguranca.
- Cadastro Detalhado:
  - Coleta de dados pessoais: Nome, CPF, E-mail, Telefone e Data de Nascimento.
  - Endereco completo: Logradouro, Numero, Bairro, Cidade, Estado (via ComboBox) e CEP.
  - Validacao de preenchimento de campos obrigatorios.
- Area do Cliente (Home):
  - Visualizacao de todas as informacoes cadastrais do usuario logado.
- Sistema de Pix:
  - Interface para envio de transferencias via chave Pix.
  - Inteligencia de Contatos: Sugere automaticamente os contatos com os quais o usuario mais interage.
  - Registro de transferencias para alimentar o historico de frequencia.
- Infraestrutura:
  - Persistencia de dados em PostgreSQL.
  - Tratamento de erros de conexao com o banco ("Sistema offline").
  - Interface responsiva construida com CustomTkinter.

## Tecnologias Utilizadas

- Python 3
- CustomTkinter - Interface Grafica
- bcrypt - Criptografia de senhas
- Pillow (PIL) - Processamento de imagens
- PostgreSQL - Banco de dados relacional
- psycopg - Driver de conexao Python -> PostgreSQL
- python-dotenv - Gestao de variaveis de ambiente

## Estrutura do Projeto

```
projeto/
├── main.py              # Ponto de entrada da aplicacao
├── imports.py           # Centralizacao de bibliotecas e dependencias
├── diretorio.py         # Gestao de caminhos de arquivos (Imagens/Icones)
├── conexao_db.py        # Logica de conexao com PostgreSQL
├── login_sys.py         # Logica de autenticacao
├── menuLogin.py         # Interface de login
├── cadastro.py          # Interface e logica de cadastro
├── home_sys.py          # Interface da area do cliente
├── telaPix.py           # Interface da area de transferencias Pix
├── pixSys.py            # Logica do grafo e sugestoes de Pix
├── .env                 # Credenciais do banco (NAO versionar)
└── assets/              # Imagens e icones (ex: 2.png, 2.ico)
```

## Estrutura da Tabela clientes

A aplicacao utiliza a seguinte estrutura de colunas no banco de dados:

| Indice | Campo             | Descricao               |
|--------|-------------------|-------------------------|
| 0      | id                | Identificador unico     |
| 1      | nome              | Nome completo           |
| 2      | cpf               | CPF do cliente          |
| 3      | senha             | Hash da senha (bcrypt)   |
| 4      | email             | Endereco de e-mail      |
| 5      | data_nascimento   | Data de Nascimento      |
| 6      | logradouro        | Rua/Av                  |
| 7      | numero            | Numero da residencia    |
| 8      | bairro            | Bairro                  |
| 9      | cidade            | Cidade                  |
| 10     | estado            | UF                      |
| 11     | cep               | CEP                     |
| 12     | telefone          | Telefone de contato     |

## Como Executar

1. Clone o repositorio:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

2. Instale as dependencias:
   ```bash
   pip install customtkinter bcrypt pillow psycopg python-dotenv
   ```

3. Configure o Ambiente:
   Crie um arquivo .env na raiz do projeto:
   ```env
   DB_HOST=localhost
   DB_NAME=nome_do_banco
   DB_USER=usuario
   DB_PASSWORD=senha
   ```

4. Execute a aplicacao:
   ```bash
   python main.py
   ```

## Licenca

Projeto desenvolvido para fins de estudo e portfolio.
