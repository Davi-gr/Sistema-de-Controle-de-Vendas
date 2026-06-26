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

#Função que registra vendas retorna um dicionário
def registrar_venda():
    id_produto_vendido = int(input("Digite o ID do produto:"))

    for produto in produtos:
        if produto.numid == id_produto_vendido:
            
            #Verificando Estoque -----------------------------
            quantidade_vendida = int(input("Quantidade vendida: "))
            if quantidade_vendida <= 0:
                print("Quantidade inválida.")
                return None
            if quantidade_vendida > produto.estoque:
                print("Quantidade de estoque ficará negativa!")
                continuar = input("Deseja continuar a venda? [s/n]")
                if continuar != "s":
                    return None
           

            #Desconto-----------------------------------------
            desconto = float(input("Desconto: "))
            if desconto < 0:
                print("Desconto inválido.")
                return None
            if desconto > produto.preco_venda - produto.preco_compra:
                print ("Você está tendo prejuízo!")
                continuar = input("Deseja continuar a venda? [s/n]")
                if continuar != "s":
                    return None
            
            produto.estoque -= quantidade_vendida
            preco_final_unitario = produto.preco_venda - desconto
            total = preco_final_unitario * quantidade_vendida
            lucro = (preco_final_unitario - produto.preco_compra) *quantidade_vendida

            return {
            "produto": produto.nome,
            "quantidade": quantidade_vendida,
            "total": total,
            "lucro": lucro
            }
    return None        

print("---- Venda Iniciada ----")
venda = registrar_venda()
if venda is not None:
    print("Total da venda:", venda["total"])
