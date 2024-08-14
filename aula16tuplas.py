lanche = ('hamburguer', 'suco', 'pudim','pizza')
for c in lanche:
    print(f'quero comer {c}')

for comida in range(0, len(lanche)):
    print(f'eu vou comer {lanche[comida]} na posiçao {comida+1}')
print('comi pra caramba')

a = (1, 2, 3, 6, 8)
b = (4, 5, 6)
c = a + b
#pra ficar em ondem numericas
print(sorted(c))
#pra ler quantas numero tem ao todos
print(len(c))
#pra contar quantas vezes aparece no (6) indicado
print(c.count(6))
#em que posiçao esta o numero informado (8)
print(c)
print(c.index(8))
# se tiver mais de um numero no index ele vai contar sempre a primeira aparecer se quiser o outro que tirar ate aonde o primeiro ta ()
#ex
print(c)
print(c.index(6, 3))
print(c.index(6, 4))

pessoa = 'camila', 30, 'F', 90
#se eu quiser apagar da memoria
for p in pessoa:
    print(p,end='.....................R$')

    lanche = 'hambúrguer', 'suco', 'pizza', 'pudim', 'batata-frita'
    # PRA COLOCAR EM ORDEM ALFABETICA
    print(sorted(lanche))
    print(lanche)
    # se eu nao precisar da posiçao
    for comida in lanche:
        print(f'Eu vou comer {comida}')
    print('==' * 30)
    # seu eu precisar da posiçao
    for cont in range(0, len(lanche)):
        print(f'eu vou comer {lanche[cont]} na posição {cont}')
    print('=-' * 30)
    for pos, comida in enumerate(lanche):
        print(F'Eu vou comer {comida} na posição {pos}')
    print('=-' * 30)
    print('Comi pra caramba')