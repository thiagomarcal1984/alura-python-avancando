import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = pede_chute()
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

        print(letras_acertadas)

    if (acertou):
         imprime_mensagem_vencedor()
    else:
         imprime_mensagem_perdedor()

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open('palavras.txt','r', encoding='UTF-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return [ "_" for letra in palavra_secreta ]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute 

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você ganhou!!!")

def imprime_mensagem_perdedor():
    print("Você perdeu!!!")

if(__name__ == "__main__"):
        jogar()
