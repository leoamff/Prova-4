listaDeCarros = [   #Criando a lista com os nomes de carros
        "ONIX","CAMARO", "CELTA","KICKS","POLO","JETTA","GOLF","HILUX","S10","UNO","PALIO"
        ,"VECTRA","CRUZE","VELAR","AMAROK","GOL","CORVETTE","COMPASS","SW4","COROLLA"]   

def procurar_carro(carro): #criando a funçao "procurar_carr"o e adiconando o parametro "carro"
      for carro in listaDeCarros: #Percorrendo a listaDeCarros
        if nomeDoCarro in (carro): #Criando uma condiçao, se o usuario digitar algum carro que esteja dentro da lista
            return "Carro encontrado!"     #Irá retornar essa mensagem

def avaliacao_carro(preco): #Criando a funçao "avaliacao_carro" e adicionando o parametro "preco"
            if valorDoCarro < 10000:   #Criando condiçoes dependendo do vque o usuario inseriu,                                             
                return "Mal estado."   #irá retornar uma mensagem em especifico

            elif valorDoCarro < 30000:
                return "Conservado."

            elif valorDoCarro < 60000:
                return "Seminovo."

            else:
                return("Novo.")

  
while True:  #Criando um loop para receberr infinitos nomes e valores de carro
    
    nomeDoCarro = (input("Digite o nome do carro que você deseja comprar: ").upper()) #Recebendo o nome do carro(convertendo para maiscula)
    valorDoCarro = float(input("Digite o valor que você gostaria de pagar:")) #Recebendo o valor do carro
    print(f"O usuário gostaria de saber se o carro {nomeDoCarro} está disponível e gostaria de pagar {valorDoCarro} reais nesse carro.") #printando msg

    resultado_busca = procurar_carro(nomeDoCarro)  #criando uma variavel para chamara funçao procurar_carro e atribuindo o parametro nome do carro
    print(resultado_busca)  

    if resultado_busca == "Carro encontrado!": #Criando condiçao, que se o carro for encontrado, aprensenta a avaliaçao
        print(f"O carro {nomeDoCarro} está disponivel, e está avaliado como {avaliacao_carro(valorDoCarro)}")  


    continuar = input("Digite 'sim' para continuar ou qualquer outra coisa para sair: ") #Pergunta se deseja continuar o loop
    if continuar.lower() != "sim": #Criando condição para encerra o programa
        break
    

    

