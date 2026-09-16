
while True:
    try:
        numero = float(input("Escreva um número inteiro: "))

        if numero > 7:
            print("O número é maior que 7")

        elif numero < 7:
            print("O número é menor que 7")

        else:
            print("O número é igual a 7")

        break

    except ValueError:
        print("Por favor, digite um número inteiro")
