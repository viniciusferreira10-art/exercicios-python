numeros = [12, 25, 37, 48, 59]

maior = numeros[0]
for numero in numeros[1:]:
    if numero > maior:
        maior = numero

print(maior)
