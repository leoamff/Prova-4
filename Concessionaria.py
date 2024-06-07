listaDeCarros = [ 
    "ONIX", "CAMARO", "CELTA", "KICKS", "POLO", "JETTA", "GOLF", "HILUX", "S10", 
    "UNO", "PALIO", "VECTRA", "CRUZE", "VELAR", "AMAROK", "GOL", "CORVETTE", "COMPASS", "SW4", "COROLLA"]

def procurarCarro(carro):  
    for carro in listaDeCarros: 
        if nomeDoCarro in (carro):
            return "Carro encontrado!"

    return "Carro nao encontrado"  


def avaliacaoCarro(preco):
    if valorDoCarro < 10000:  
        return "Mal estado." 

    elif valorDoCarro < 30000:
        return "Conservado."

    elif valorDoCarro < 60000:
        return "Seminovo."

    else:
        return ("Novo.")


while True: 

    nomeDoCarro = (input("Digite o nome do carro que voce deseja comprar: ").upper())
    
    valorDoCarro = float(input("Digite o valor que voce gostaria de pagar:"))
    print(f"O usuario gostaria de saber se o carro {nomeDoCarro} esta disponovel e gostaria de pagar {valorDoCarro} reais nesse carro.")  

    
    resultadoBusca = procurarCarro(nomeDoCarro)
    print(resultadoBusca)

    
    if resultadoBusca == "Carro encontrado!":
        print(f"O carro {nomeDoCarro} esta disponivel, e esta avaliado como {avaliacaoCarro(valorDoCarro)}")

    continuar = input("Digite 'sim' para continuar ou qualquer outra coisa para sair: ")
    if continuar.lower() != "sim": 
        break
