print("Bem-vindo a Copiadora do Alef Emanoel") #inicio do programa
print("-"*40)

#função para coletar o tipo de serviço e retornar seu valor
def escolha_servico():
    global valor_servico #indica que a variavel será global
    while True: #laço de repetição que cria um loop
        #interface para o usuario
        print("Entre com o tipo de serviço desejado: ")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(">> ").upper() #recebe a resposta do usuario com o serviço desejado
        print("-"*40)

        #atribuição do valor para cada serviço
        if servico == "DIG":
            valor_servico = 1.10
            return valor_servico
        elif servico == "ICO":
            valor_servico = 1
            return valor_servico
        elif servico == "IPB":
            valor_servico = 0.40
            return valor_servico
        elif servico == "FOT":
             valor_servico = 0.20
             return valor_servico
        else:
            print("Escolha inválida, entre com o serviço novamente.", end="\n\n")  #saída em casos de resposta inválida
            continue #retorna ao inicio do loop
        
escolha_servico() #chamada da função para coletar o tipo de serviço e retornar seu valor

#função que coleta a quantidade de páginas e atribui o desconto
def num_paginas():
    global numero_paginas #indica que a variavel será global
    while True: #laço de repetição   
        try: #verifica se a resposta vai ser um numero
            numero_paginas = int(input("Entre com o numero de paginas: ")) #recebe o numero de páginas desejado
            #aplicação do desconto de acordo com a quantidade de páginas
            if numero_paginas < 20:
                return numero_paginas
            elif numero_paginas >= 20 and numero_paginas < 200:
                numero_paginas = numero_paginas - numero_paginas * 0.15
                return numero_paginas
            elif numero_paginas >= 200 and numero_paginas < 2000:
                numero_paginas = numero_paginas - numero_paginas * 0.20
                return numero_paginas
            elif numero_paginas >= 2000 and numero_paginas < 20000:
                numero_paginas = numero_paginas - numero_paginas * 0.25                
                return numero_paginas
            else: 
                #interface exibida caso o usuário digite um número de páginas além do limite
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente. ", end="\n\n")
            continue
        except ValueError: #em caso da resposta não ser um numero, será exibido uma mensagem de aviso
            print("Algo deu errado. Por favor entre com o numero de paginas: ")
            continue #retorna ao inicio do loop

num_paginas() #chamada da função que coleta a quantidade de páginas e atribui o desconto

#função que pergunta se o usuário deseja algum serviço adicional
def servico_extra():
    global extra #indica que a variavel será global
    while True: #lanço de repetição
        print(" ") #quebra de linha
        #interface para o usuário
        print("Deseja adicionar algum serviço? ")
        print("1 - Encadernação Simples - R$15.00")
        print("2 - Encadernação Capa Dura - R$40.00")
        print("0 - Não desejo mais nada")

        try: #verifica se a reposta é um numero
            extra = int(input(">>")) #recebe a opção de serviço adicional
            if extra != 1 and extra != 2 and extra != 0: #caso a reposta seja diferente das opções disponiveis o programa perguntará novamente
                print("Valor inválido, tente novamente.", end="\n\n")
                continue #retorna ao inicio do loop
            #adição de valor do tipo de serviço referente a escolha do usuario
            if extra == 1:
                extra = 15
                return extra
            elif extra == 2:
                extra = 40
                return extra
            else:
                extra == 0
                extra = 0
                return extra
        except ValueError: #em caso de não ser um numero o programa exibe uma mensagem de aviso
                print("Entrada inválida. tente novamente. ")
                continue #retorna ao inicio do loop
        
servico_extra() #chamada da função que pergunta se o usuario deseja algum serviço adicional

total = (valor_servico * numero_paginas) + extra #calculo do valor total do pedido
print(f"Total: R${total}") #saida que mostra o valor total para o usuario
