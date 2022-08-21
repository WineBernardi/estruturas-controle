PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e de política',
    'A praia foi divertida',
]

for texto in textos:
    interseccao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if interseccao:
        print('Texto possui pelo menos uma palavra proibida:', interseccao)
    else:
        print('Texto Autorizado:', texto)