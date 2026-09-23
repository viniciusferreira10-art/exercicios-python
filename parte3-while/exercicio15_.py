number = float(input("digite um número: "))
while number != 0:
    
    if number < 0:
        print ("Número negativo")
        number = float(input("digite um número: "))
    elif number > 0:
        print ("Número positivo")
        number = float(input("digite um número: "))
    else:
        print ("fim do programa")


       