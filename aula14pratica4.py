n = 1
contpar = contimp = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            contpar += 1
        else:
            contimp += 1
print(f'tem {contpar} numeros pares.')
print(f'tem {contimp} numeros impares.')
