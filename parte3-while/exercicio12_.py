contador = int(input("Digite um número: "))
opcao = contador

while opcao != 0:
    print(contador)
    opcao = int(input("Digite outro número (ou 0 para sair): "))
    contador = contador + opcao
    print("A soma é:", contador)
    