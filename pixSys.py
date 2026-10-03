class GrafoPix:
    def __init__(self):
# Dicionário {cpf_origem: {cpf_destino: quantidade_de_pix}}
        self.conexoes = {}

    def adicionar_transferencia(self, cpf_origem, cpf_destino):
# Se o cliente origem ainda não fez nenhum Pix, cria o nó dele
        if cpf_origem not in self.conexoes:
            self.conexoes[cpf_origem] = {}
            
# Se ele nunca fez pix para esse destino, a aresta começa em 0
        if cpf_destino not in self.conexoes[cpf_origem]:
            self.conexoes[cpf_origem][cpf_destino] = 0
            
# Aumenta o peso da aresta de acordo com frequência de transferências
        self.conexoes[cpf_origem][cpf_destino] += 1

    def sugerir_contatos(self, cpf_origem, limite=3):
# Se não tem conexões, retorna lista vazia
        if cpf_origem not in self.conexoes:
            return []
            
# Pega as conexões e ordena pelo peso maior para o menor
        contatos = self.conexoes[cpf_origem].items()
        contatos_ordenados = sorted(contatos, key=lambda x: x[1], reverse=True)
        
# Retorna apenas os CPFs dos top contatos
        return [contato[0] for contato in contatos_ordenados[:limite]]

# Instanciando o Grafo
grafo_pix = GrafoPix()

