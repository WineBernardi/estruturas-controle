palavra = 'paralelepípedo'
for letra in palavra:
    # print(letra) uma letra debaixo da outra.
    # print(letra, end=',') uma letra do lado da outra porém com vírgula separando.
    print(letra, end=' ') #uma letra do lado da outra porém com espaços entre elas.
print('Fim')
aprovados = ['Wellington', 'Wine', 'Jiraya', 'Minerva', 'Zoro']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    # print(posicao + 1, nome) enumera os nomes contidos na lista.
    # print(f'posicao +1', nome) antes dos nomes acrescenta a frase entre ''.
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça', 
               'Quarta','Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('muito legal'):
    print(letra)

for numero in {1, 2, 3, 4, 5}:
    print(numero)