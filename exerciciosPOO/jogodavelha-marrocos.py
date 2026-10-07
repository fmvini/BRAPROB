import random

def venceu(jogador):
    for linha in jogador:
        if linha.count(1) == 3:
            return True
    for coluna in range(3):
        if (jogador[0][coluna] == 1 and
            jogador[1][coluna] == 1 and
            jogador[2][coluna] == 1):
            return True
    if (jogador[0][0] == 1 and
        jogador[1][1] == 1 and
        jogador[2][2] == 1):
        return True
    if (jogador[0][2] == 1 and
        jogador[1][1] == 1 and
        jogador[2][0] == 1):
        return True
    return False

def empate(tabuleiro):
    for linha in tabuleiro:
        for posicao in linha:
            if isinstance(posicao, int):
                return False
    print('Empatou!!')
    return True


def mostrar_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end='    ')
        print('\n')
def velha(tabuleiro, jogador, simbolo):
    jogada_valida = False
    while not jogada_valida:
        mostrar_tabuleiro(tabuleiro)
        try:
            escolha = int(input(f'Jogador {simbolo} - Digite Sua escolha: '))
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == escolha:
                        tabuleiro[i][j] = simbolo
                        jogador [i][j] = 1
                        jogada_valida = True
            if not jogada_valida:
                print('Jogada inválida, tente outra posição! ')
        except ValueError: 
            print('Erro! Valor inválido')

def jogada_maquina(tabuleiro, maquina, simbolo):
    posicoes_livres = []
    for i in range(3):
        for j in range(3):
            if isinstance(tabuleiro[i][j], int):
                posicoes_livres.append(tabuleiro[i][j])
    if posicoes_livres:
        escolha_maquina = random.choice(posicoes_livres)
        for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == escolha_maquina:
                        tabuleiro[i][j] = simbolo
                        maquina [i][j] = 1
                     
                     
tabuleiro = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

jogador1 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

jogador2 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


print("Bem vindo ao Jogo da velha!")
print('===========================')
print('Você quer jogar contra um humano ou contra a maquina?')
print('1 - Jogar contra humano')
print('2 - Jogar contra maquina')
try: 
    escolha = int(input(''))
    while escolha not in (1, 2):
        print("Escolha inválida!!!!")
        escolha = int(input(''))
    if escolha == 1:
        while(not venceu(jogador1) and not venceu(jogador2)):
            velha(tabuleiro, jogador1, '\U0001F607')
            if venceu(jogador1) or empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                break
            velha(tabuleiro, jogador2, '\U0001F608')
            if venceu(jogador2) or empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                break

        if venceu(jogador1):
            print('O Jogador \U0001F607 Venceu!')
        if venceu(jogador2):
            print('O Jogador \U0001F608 Venceu!')

    else:
        maquina = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        while(not venceu(jogador1) and not venceu(maquina)):
            velha(tabuleiro, jogador1, '\U0001F607')
            if venceu(jogador1):
                mostrar_tabuleiro(tabuleiro)
                print("Você venceu do Robo!")
                break
            if empate(tabuleiro):
                break;
            jogada_maquina(tabuleiro, maquina, '\U0001F916')
            if venceu(maquina):
                print("Você perdeu para o Robo! kkkkkkkkkkk")
                break
            if empate(tabuleiro):
                break
except ValueError:
    print('Erro! Valor não compativel, digite um numero inteiro!')