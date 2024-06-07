# Prova 4 - Augusto
Construindo um sistema simulador de concessionária em Python.

Simulador de concessionária, onde o usuário informa o tipo de carro e a faixa de preço que pode pagar. O sistema retorna se o carro está disponível e a classificação do carro com base no preço.

## Ferramentas
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc) 
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)
![Python](https://img.shields.io/badge/python-000?style=for-the-badge&logo=python&logoColor=ffdd54)


# Explicando o código
###        Criando a lista com os nomes de carros.
```
listaDeCarros = [ "ONIX","CAMARO", "CELTA","KICKS","POLO","JETTA","GOLF","HILUX","S10","UNO","PALIO"
        ,"VECTRA","CRUZE","VELAR","AMAROK","GOL","CORVETTE","COMPASS","SW4","COROLLA"]  
```

###        Definindo a função "procurarCarro" e adicionando o parâmetro "carro".
```
def procurarCarro(carro):
```

###        Percorrendo a listaDeCarros.
```
        for carro in listaDeCarros:  
```
###        Verificando se o carro digitado pelo usuário está na lista.
```
                if nomeDoCarro in (carro):
                    return "Carro encontrado!"

        return "Carro não encontrado" 
```


###        Definindo a função "avaliacaoCarro" e adicionando o parâmetro "preco".
###        Criando condições dependendo do valor que o usuário inseriu, para retornar uma mensagem específica.
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

###     Criando um loop para receber infinitos nomes e valores de carros.
 ```
while True:
``` 
###     Recebendo o nome do carro (convertendo para maiúsculo).
```
    nomeDoCarro = (input("Digite o nome do carro que voce deseja comprar: ").upper())
```
###     Recebendo o valor do carro.
```
    valorDoCarro = float(input("Digite o valor que você gostaria de pagar:"))
    print(f"O usuário gostaria de saber se o carro {nomeDoCarro} está disponível e gostaria de pagar {valorDoCarro} reais nesse carro.") 
```

###     Atribuindo o resultado da busca ao chamar a função procurarCarro com o nomeDoCarro.
```
        resultadoBusca = procurarCarro(nomeDoCarro)
        print(resultadoBusca)
```

###        Se o carro for encontrado, apresenta a avaliação.
```
        if resultadoBusca == "Carro encontrado!":
            print(f"O carro {nomeDoCarro} está disponivel, e está avaliado como {avaliacaoCarro(valorDoCarro)}")
```

###        Pergunta se deseja continuar o loop, criando condição para encerrar o programa.
```
        continuar = input("Digite 'sim' para continuar ou qualquer outra coisa para sair: ")

        if continuar.lower() != "sim":  
            break
```

# Contribuidores
<a href="https://github.com/leoamff/Prova-4/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=leoamff/Prova-4"/>
</a>


