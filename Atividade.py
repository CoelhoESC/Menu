def Preco_total(lista):
    total = sum([float(valor[1]) for valor in lista])
    return total


Carrinho = []
print(""" Produtos da loja:
[1] = Brinquedo R$ 300.00
[2] = Ferramenta R$ 150.00
[3] = Camisa R$ 50.00
[4] = Bota R$ 100.00
[5] = Ver seu Carrinho
[6] = Preço total a pagar
[0] = Sair da loja""")

while True:
    Pedidos = input('O que deseja comprar?')

    match int(Pedidos):

        case 0:
            break
        case 1:
            Carrinho.append(('Brinquedo', 300.00))
            print('Adicionado ao seu Carrinho')
        case 2:
            Carrinho.append(('Ferramenta', 150.00))
            print('Adicionado ao seu Carrinho')
        case 3:
            Carrinho.append(('Camisa', 50.00))
            print('Adicionado ao seu Carrinho')
        case 4:
            Carrinho.append(('Bota', 100.00))
            print('Adicionado ao seu Carrinho')
        case 5:
            print('Seus pedidos:')
            for pedidos in Carrinho:
                print(f'{pedidos[0]} R$ {pedidos[1]}')
        case 6:
            Valor_total = Preco_total(Carrinho)
            print(f'Total a pagar das suas comprar: {Valor_total:.2f}')
        case _:
            print('Digite o que gostaria de comprar:')
            continue
