print("Bem-vindo a Loja do Alef Emanoel") #inicio do programa

valor_unitario = float(input("Entre com o valor do produto: ")) #recebe valor do produto
quantidade = int(input("Entre com a quantidade do produto: ") )#recebe quantidade do produto

valor_quantidade = valor_unitario*quantidade #variavel que recebe o valor unitário multiplicado pela quantidade

#estrutura para aplicar o desconto em diferentes valores ou quantidades
if valor_quantidade < 2500:
    valor_desconto = 0 #nenhum desconto
elif valor_quantidade >= 2500 and valor_quantidade < 6000:
    valor_desconto = valor_quantidade * 0.04 #4% de desconto 
elif valor_quantidade >= 6000 and valor_quantidade < 10000:
    valor_desconto = valor_quantidade * 0.07 #7% de desconto
else: 
    valor_desconto = valor_quantidade * 0.11 #11% de desconto

#saida que informa os valores sem e com desconto
print(f"Valor SEM desconto: R${valor_quantidade}")
print(f"Valor COM desconto: R${valor_quantidade - valor_desconto}")