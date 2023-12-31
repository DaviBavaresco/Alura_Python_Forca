import random




def jogar():

    mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagme_perdedor()





    print("Fim do jogo")

def imprime_mensagem_ganhador():
    print("Voce ganhou")


def imprime_mensagme_perdedor():
    print("Voce perdeu")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):  # transformo tudo em letra maiuscula
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual a letra: ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
   return ["_" for letra in palavra]


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")




if(__name__ == "__main__"):
    jogar()