'''valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('fim do progranma')
'''
a = [2, 3, 4, 6]
#pra fazer uma copia da lista
b = a[:]
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista A: {b}')
