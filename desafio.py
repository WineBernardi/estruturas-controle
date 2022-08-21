from random import randint


def sortear_dado():
    return randint(1, 6)  # sortear_dado = randint(1, 6)


for l in range(1, 7):
    if l % 2 == 1:  # if l % 2 == 0:
        continue

    if sortear_dado() == l:
        print("Acertou...", l)
        break
else:
    print('Não acertou o número!')
