s = cont = 0
while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'A soma de todos os {cont} é {s}')
