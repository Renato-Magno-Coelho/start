vendedor = str(input('Nome vendedor: '))
codigo_peca = int(input('Codigo da peça: '))
preco_unitario = float(input('Digite o valor da peça: '))
qtd_vendida = int(input('Quantas peças foram vendidas: '))

comissao = (preco_unitario * qtd_vendida) / 20
print('O vendedor {} vai receber {} de comissão esse mês'.format(vendedor, comissao))