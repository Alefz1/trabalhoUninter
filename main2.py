print("Bem-vindo a Loja de Gelados do Alef Emanoel") #inicio do programa

#exibição do cardápio
print("-"*20,"Cardápio","-"*20)
print("-"*50)
print("---| Tamanho |  Cupuaçu (CP)   |   Açaí (AC)  |---")
print("---|    P    |     R$ 9.00     |   R$ 11.00   |---")
print("---|    M    |     R$ 14.00    |   R$ 16.00   |---")
print("---|    G    |     R$ 18.00    |   R$ 20.00   |---")
print("-"*50)

valor_total = 0 #variavel acumuladora fora do loop

#estrutura usada para coletar informações do pedido(sabor/tamanho)
def pedido():
    global valor_total #indica que a variavel sera global
    while True: #laço de repetição que vai criar um loop
        #coleta do sabor desejado
        sabor = input("Entre com o sabor desejado (CP/AC): ").upper()#recebe sabor desejado
        while sabor != "CP" and sabor != "AC": 
            print("Sabor inválido. Tente novamente", end="\n\n") #sída em casos de opção inválida
            sabor = input("Entre com o sabor desejado (CP/AC):").upper() #pergunta novamente o sabor
            continue #retorna ao inicio do loop

        #coleta do tamanho desejado
        tamanho = input("Entre com o tamanho desejado (P/M/G):").upper()#recebe tamanho desejado
        while tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente", end="\n\n") #saída em casos de opção inválida
            tamanho = input("Entre com o tamanho desejado (P/M/G):").upper() #pergunta novamente o tamanho
            continue #retorna ao inicio do loop
        break #quebra do loop

    #estrutura que vai verificar o tamanho e o sabor para determinar o valor
    if tamanho == "P" and sabor == "CP":
        valor = 9.00
    elif tamanho == "M" and sabor == "CP":
        valor = 14.00
    elif tamanho == "G" and sabor == "CP":
        valor = 18.00
    elif tamanho == "P" and sabor == "AC":
        valor = 11.00
    elif tamanho == "M" and sabor == "AC":
        valor = 16.00
    else:
        valor = 20.00

    valor_total += valor #variavel acumuladora para somar os valores de dois ou mais pedidos
    
    #variaveis para exibir as escolhas do usuario 
    if sabor == "CP":
        sabor = "Cupuaçu"
    else:
        sabor == "Ac"
        sabor = "Açaí"
    print(f"Você pediu um {sabor} tamanho {tamanho}: R${valor}", end="\n\n") #saída que mostra os itens e o valor do pedido

pedido() #chamada da função para efetuar o pedido

#coleta de informação de pedido adicional ou finalização do pedido
while True: #laço de repetição
    resposta = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if resposta == "S": 
        pedido() #repete a estrutura para adicionar um novo pedido
        print(f"O Valor total a ser pago: R${valor_total}") #saída com o valor total a ser pago
    else: #encerra o programa e exibe o valor total a ser pago
        print(" ")#quebra de linha
        print(f"O Valor total a ser pago: R${valor_total}")
        break #quebra do loop
        
        