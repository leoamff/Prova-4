# Prova 4 - Augusto
# Construindo um sistema simulador de concessionária em Python.

###       # Criando a lista com os nomes de carros.
```
listaDeCarros = [ "ONIX","CAMARO", "CELTA","KICKS","POLO","JETTA","GOLF","HILUX","S10","UNO","PALIO"
        ,"VECTRA","CRUZE","VELAR","AMAROK","GOL","CORVETTE","COMPASS","SW4","COROLLA"]  
```

###       # Criando a funçao "procurarCarro" e adiconando o parametro "carro".
```
def procurarCarro(carro):
```

# Percorrendo a listaDeCarros
```
for carro in listaDeCarros:  
```
###       # Criando uma condiçao, se o usuario digitar algum carro que esteja dentro da lista.
```
if nomeDoCarro in (carro):
    return "Carro encontrado!"

return "Carro não encontrado" 
```


###       # Criando a funçao "avaliacaoCarro" e adicionando o parametro "preco".
###       # Criando condiçoes dependendo do valor que o usuario inseriu, irá retornar uma mensagem em especifico.
```
def avaliacaoCarro(preco):
    if valorDoCarro < 10000:  
        return "Mal estado."  

    elif valorDoCarro < 30000:
        return "Conservado."

    elif valorDoCarro < 60000:
        return "Seminovo."

    else:
        return ("Novo.")
```

 # Criando um loop para receber infinitos nomes e valores de carro.
 ```
while True:
``` 
###    # Recebendo o nome do carro(convertendo para maiscula).
```
    nomeDoCarro = (input("Digite o nome do carro que voce deseja comprar: ").upper())
```
###    # Recebendo o valor do carro.
```
    valorDoCarro = float(input("Digite o valor que você gostaria de pagar:"))
    print(f"O usuário gostaria de saber se o carro {nomeDoCarro} está disponível e gostaria de pagar {
    valorDoCarro} reais nesse carro.") 
```

###    # criando uma variavel para chamara funçao procurar_carro e atribuindo o parametro nome do carro.
```
resultadoBusca = procurarCarro(nomeDoCarro)
print(resultadoBusca)
```

###       # Criando condiçao, que se o carro for encontrado, aprensenta a avaliaçao.
```
if resultadoBusca == "Carro encontrado!":
    print(f"O carro {nomeDoCarro} está disponivel, e está avaliado como {
        avaliacaoCarro(valorDoCarro)}")
```

###       # Pergunta se deseja continuar o loop, criando condição para encerrar o programa.
```
continuar = input("Digite 'sim' para continuar ou qualquer outra coisa para sair: ")

if continuar.lower() != "sim":  
    break
```


