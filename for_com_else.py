PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e de política',
    'A praia foi divertida',
]

for texto in textos:
    # found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            # found = True
            break

    else:
        print('Texto Autorizado:', texto)
