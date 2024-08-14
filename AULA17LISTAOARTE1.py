lanche = ['hamburguer', 'suco', 'pizza', 'picole']
valores = list(range(4, 11))
valor = [5,4,8,3,7,6]
#se eu quiser adicionar outra variavel na lista no final
lanche.append('pudim')
#se quizer adicionar um item em alguma posiçao
lanche.insert(0, 'hot-dog')
# se quiser eliminar masi basico
del lanche[3]
#se quizer eliminar o ultimo item mas tbm pode eliminar outras posiçao
lanche.pop(4)
#eliminar pelo nome do item
lanche.remove('suco')
for c in range(0, len(lanche)):
    print(f'eu vou comer {lanche[c]} na posição {c}.')
for num in range(0, len(valores)):
    print(valores[num], end=' -> ')
print(f'\nos valores são',end=' ')
for n in range(0, len(valor)):
    #para colocar em ondem numerica
    valor.sort()
    print(valor[n], end=' ')
print(f'\nos valores na posiçao ', end=' ')
for m in range(0, len(valor)):
    #para colocar em ordem numeria ao contrario
    valor.sort(reverse=True)
    print(valor[m], end=' ')

