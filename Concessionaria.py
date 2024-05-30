# Criei uma variavel e atribui ela a funçao input para que o usuario possa digitar o nome do carro
# OBS: Adicionei a função .upper, pa
nomeDoCarro = (input("Digite o nome do carro que você deseja comprar: ").upper())

# Criei uma variavel (float) para que o usuario possa digitar o valor do carro que ele gostaria de conhecer
valorDoCarro = float(input("Digite o valor do carro que você gostaria de conhecer: "))

# Utilizando a função print para aparecer no terminal o nome e o valor do carro que o usuario esta interessado
print(f"O usuário gostaria de saber se o carro {nomeDoCarro} está disponível e gostaria de pagar {valorDoCarro} reais nesse carro.")

#Criando uma lista com os nomes dos carros disponiveis na concessionaria
listaDeCarros = [
    "ONIX","CAMARO", "CELTA","KICKS","POLO","JETTA","GOLF","HILUX","S10","UNO","PALIO"
    ,"VECTRA","CRUZE","VELAR","AMAROK","GOL","CORVETTE","COMPASS","SW4","COROLLA"]


# Usando a função for para percorrer a lista. Adicionando dentro do for uma função que verifica se
# o carro que ususario quer tem dentro da lista
for carro in listaDeCarros:
    if nomeDoCarro in (carro.upper()):
        print("Carro encontrado!")
        if valorDoCarro < 10000:
            print("Mal estado.")

        elif valorDoCarro < 30000:
            print("Conservado.")

        elif valorDoCarro < 60000:
            print("Seminovo.")

        else:
            print("Novo.")
            break
    else:
        print("Carro não encontrado!")
        break

        

# Criando uma função
def procurar_carro(nome_carro):
    for carro in listaDeCarros:
        if nomeDoCarro in (carro.upper()):
            return nome_carro
        else:
            break
procurandoCarro = procurar_carro() # criando uma variavel para atribuir a funçao
print(procurandoCarro)
            
        