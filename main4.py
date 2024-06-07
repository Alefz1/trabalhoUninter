print("Bem-vindo a Livraria do Alef Emanoel") #inicio do programa

lista_livro = [] #criação da lista no código principal
id_global = 0 #variavel acumuladora para os ID dos livros

#função menu de cadastro para coletar as informações de cadastro de livros
def cadastrar_livro(id_global): 
    linhas()#linhas de interface
    while True: #laço de repetição
        print("-"*12,"MENU CADASTRO","-"*13) #interface
        print(f"ID do livro: {id_global}") #mostra o ID do livro a ser adicionado
        nome = input("Entre com o nome: ") #recebe nome do livro
        autor = input("Entre com o autor: ") #recebe autor do livro
        editora = input("Entre com a editora: ") #recebe editora do livro
        livro = {"id": id_global, "nome": nome, "autor": autor, "editora": editora} #diciónario com chaves e valores de cada item
        lista_livro.append(livro) #copia o diciónario para a lista
        break #quebra do loop

#funções para interface para o usuário       
def chamar_livro():
    print("ID:",livro["id"])
    print("Nome:",livro["nome"])
    print("Autor:",livro["autor"])
    print("Editora:",livro["editora"])
    linhas()
def resposta_inválida():
    print("Opção inválida, tente novamente.")
def menu_livro(): #função para gerar um print para interface no console
    print("-"*10,"LIVROS CADASTRADOS","-"*10)
def linhas(): #função para gerar linhas 
    print("-"*40)
#-----------------------------------------------------

def consultar_livro(): #menu de consulta
        global livro #indica variável global
        while True: #laço de repetição
            #interface para o usuário
            print("-"*40)
            print("-"*12,"MENU CONSULTA","-"*13)
            print("Entre com a opção que deseja:")
            print("1 - Consultar Todos")
            print("2 - Consultar por ID")
            print("3 - Consultar por Autor")
            print("4 - Retornar ao Menu Principal")
            try: #verifica se a opção é um numero
                opcao = int(input(">>"))
                linhas()
                if lista_livro: #verifica se existe algum livro na lista
                    if opcao == 1:
                        menu_livro() 
                        for livro in lista_livro:
                            chamar_livro() #chamada da função para mostrar todos os livros cadastrados
                    elif opcao == 2:
                        id_consulta = int(input("Entre com o ID: ")) #consulta de livro pela id 
                        menu_livro()
                        livro_achado = False #variável booleana para definir se o livro foi achado ou não
                        for livro in lista_livro:
                            if livro["id"] == id_consulta: #verifica se a id fornecida é igual a id de algum livro
                                chamar_livro() #se for igual, será exibido o livro específico
                                livro_achado = True #livro achado
                        if not livro_achado:  
                            print(f"Nenhum livro cadastrado com a ID: {id_consulta}")  #sáida em caso de não achar um livro com a id fornecida
                    elif opcao == 3:
                        autor_consulta = input("Entre com o autor: ") #consulta de livro do autor desejado
                        menu_livro() 
                        livro_achado = False #variável booleana que indica se o livro foi achado ou não  
                        for livro in lista_livro:
                            if livro["autor"] == autor_consulta: #verifica se existe algum livro com
                                chamar_livro()
                                livro_achado = True #livro achado
                        if not livro_achado:
                            print(f"Nenhum livro cadastrado com esse autor: {autor_consulta}") #sáida em caso de não achar um livro com o autor fornecida
                    elif opcao == 4:
                        break #quebra do loop para retornar ao menu principal
                else:
                    print("Não há livros cadastrados.") #sáida caso não tenha livros cadastrados
                    break #quebra do loop
            except ValueError:
                resposta_inválida() #saída caso a opção seja inválida
                continue #retorna ao inicio do loop

#função que remove livros
def remover_livro():
    global livro #indica variável global
    linhas()
    print("-"*12,"MENU REMOVER","-"*13) #interface
    try: #verifica se a reposta é um numero
        while True: #laço de repetiçao
            if lista_livro: #verifica se existe algum livro cadastrado
                id_remove = int(input("Entre com o ID do livro a ser removido: "))
                livro_achado = False #variável booleana que indica se o livro foi achado ou não 
                for livro in lista_livro:
                    if livro["id"] == id_remove: #verifica se há algum livro que tenha a id igual a id fornecida
                        lista_livro.remove(livro) #comando para remover livro com a id fornecida
                        print("Livro removido com sucesso.") 
                        livro_achado = True #livro achado
                if not livro_achado:        
                    print("Não existe um livro com essa ID")            
                    continue #retornar ao inicio do loop
                break #quebra o loop
            else:
                print("Nenhum livro cadastrado.") #sáida caso não exista livros cadastrados
                break #quebra do loop
    except ValueError:
        resposta_inválida() #caso a resposta seja inválida será chamada a função de interface para respostas inválidas
        
while True: #laço de repetição
    #interface para o usuário   
    linhas()   
    print("-"*12,"MENU PRINCIPAL","-"*12)
    print("Escolha a opção desejada:")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Remover")
    print("4 - Sair")
    try: #verifica se a resposta é um numero
        menu = int(input(">>")) #recebe opção com o valor do serviço desejado
        if menu == 1:
            id_global += 1  #acumula valor das ID's dos livros
            cadastrar_livro(id_global) #chama a função para efetuar o cadastro de um livro
        elif menu == 2:
            consultar_livro()#chama a função para consultar livro
        elif menu == 3:
            remover_livro()#chama a função para remover livro
        elif menu == 4:
            print("Encerrando o programa...")
            break #quebra do loop para encerrar o programa
        else:
            resposta_inválida() #caso a opção do usuário seja diferente das opções disponiveis
    except ValueError:
        resposta_inválida() #caso a resposta seja inválida sera chamada essa função com interface de resposta inválida
     
                    

