numero = int(input("Digite um número: "))

if numero < 0:
    print("Número inválido. Digite um valor maior ou igual a 0.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")
