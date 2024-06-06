# Prova 4
## Construindo um sistema simulador de concessionária em Python.


### listaDeCarros = [  # Criando a lista com os nomes de carros


### def procurarCarro(carro):  # criando a funçao "procurarCarro" e adiconando o parametro "carro"
###    for carro in listaDeCarros:  # Percorrendo a listaDeCarros
###        # Criando uma condiçao, se o usuario digitar algum carro que esteja dentro da lista
###        if nomeDoCarro in (carro):
###            return "Carro encontrado!"

###    return "Carro não encontrado"  # Irá retornar essa mensagem


### Criando a funçao "avaliacaoCarro" e adicionando o parametro "preco"
### def avaliacaoCarro(preco):
###    if valorDoCarro < 10000:  # Criando condiçoes dependendo do vque o usuario inseriu,
###        return "Mal estado."  # irá retornar uma mensagem em especifico

###    elif valorDoCarro < 30000:
###        return "Conservado."

###    elif valorDoCarro < 60000:
###        return "Seminovo."

###    else:
###        return ("Novo.")


### while True:  # Criando um loop para receberr infinitos nomes e valores de carro

###    # Recebendo o nome do carro(convertendo para maiscula)
###    nomeDoCarro = (
###        input("Digite o nome do carro que voce deseja comprar: ").upper())
###    # Recebendo o valor do carro
###    valorDoCarro = float(input("Digite o valor que você gostaria de pagar:"))
###    print(f"O usuário gostaria de saber se o carro {nomeDoCarro} está disponível e gostaria de pagar {
###          valorDoCarro} reais nesse carro.")  # printando msg

###    # criando uma variavel para chamara funçao procurar_carro e atribuindo o parametro nome do carro
###    resultadoBusca = procurarCarro(nomeDoCarro)
###    print(resultadoBusca)

###    # Criando condiçao, que se o carro for encontrado, aprensenta a avaliaçao
###    if resultadoBusca == "Carro encontrado!":
###        print(f"O carro {nomeDoCarro} está disponivel, e está avaliado como {
###              avaliacaoCarro(valorDoCarro)}")

###   # Pergunta se deseja continuar o loop
###    continuar = input(
###        "Digite 'sim' para continuar ou qualquer outra coisa para sair: ")
###    if continuar.lower() != "sim":  # Criando condição para encerra o programa
###        break

    ///
