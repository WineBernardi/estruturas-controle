for x in range(1, 11):
    if x % 2 == 0:# numeros impares.
        continue #essa acao continua dentro do bloco.
    print(x)

for z in range(1, 11):
    if z == 5:
        break #essa acao sai do bloco, finaliza.
    print(z)
print('Fim')