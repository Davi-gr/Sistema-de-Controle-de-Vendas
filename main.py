class Produto:
    
    def __init__ (self, nome, preco_compra, preco_venda, estoque, numid):
            self.numid = numid
            
            nome = nome.strip()
            if not nome:
                raise ValueError("O nome do produto não pode ficar vazio.")
            self.nome = nome

            if preco_compra < 0:
                raise ValueError("O valor de compra não pode ser negativo")
            self.preco_compra = preco_compra

            if preco_venda < preco_compra:
                raise ValueError("O Preço de venda não pode ser menor que o Preço de compra")
            self.preco_venda = preco_venda

            if estoque < 0:
                raise ValueError("Estoque não pode ser negativo")
            self.estoque = estoque
            

def cadastrar_produtos():
      print("------------Cadastro de Produtos------------")

      try:
        numid = int(input("ID do produto: "))
        nome = input("Nome do produto: ")
        preco_compra = float(input("Preço de Compra: "))
        preco_venda = float(input("Preço de Venda: "))
        estoque= int(input("Quantidade: "))
        produto = Produto(
        numid = numid,    
        nome=nome,
        preco_compra=preco_compra,
        preco_venda=preco_venda,
        estoque=estoque
    )
        return produto
      except ValueError as erro:
        print(f"Erro: {erro}")
        return None

produtos = []

while(True):
    produto = cadastrar_produtos()
    if produto is not None:
        produtos.append(produto)
    continuar = input("Deseja cadastrar outro produto? [s/n]")

    if continuar != "s":
        break

def listar_produtos():
    for produto in produtos:
        print("------------------")
        print("ID:", produto.numid)
        print("Produto:", produto.nome)
        print("Preço de venda:", produto.preco_venda)
        print("Estoque:", produto.estoque)

def registrar_venda():
    