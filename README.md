# Game Loop
Em Python, o tipo de dados booleano é `bool`:

```python
>>> type(True) 
<class 'bool'>
>>> type(False) 
<class 'bool'>
>>>
```

Vamos fazer com que o jogo se repita enquanto o jogador não enforcar e não acertar a palavra. Veja o código do arquivo `forca.py`:

```python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
        jogar()
```

> Da mesma forma como há funções built-in para converter dados para float e int (`float(valor)` e `int(valor)`), temos a função `bool(valor)`:
```python
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(-100)
True
>>> bool(13.5)
True
>>> bool("teste")
True
>>> bool(True)
True
```
# Encontrando letras
Temos a função `find()` nas strings do Python para localizar a posição de uma letra nessa string:

```python
>>> palavra = "zoo"
>>> palavra.find("o")
1 
    # "o" foi encontrada na segunda posição. 
    # Mas não mostra que tem a letra "o" também na 3a posição.
>>> palavra.find("z") 
0 
    # "z" foi encontrada na primeira posição.
>>> palavra.find("x") 
-1 
    # Não encontrou a letra "x".
>>>
```
A solução neste caso será iterar a palavra e checar a letra procurada em cada posição:

```python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        
        index = 0
        for letra in palavra_secreta:
            if (letra == chute):
                print(f"Achou a letra {letra} na posição {index}!")
            index += 1
        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
        jogar()
```
# Funções importantes da String
```python
>>> "banana".startswith('ba') # Retorna True se palavra começa com 'ba'.
>>> True
>>> "banana".endswith('na') # Retorna True se palavra termina com 'na'.
>>> True
>>> 'banana'.endswith('XP') # Retorna False se a palavra não termina com 'XP'.
>>> False
>>> 'banana'.capitalize() # Retorna string com inicial maiúscula.
'Banana'
>>> 'banana'.upper() # Retorna string toda em maiúscula.
'BANANA'
>>> 'BANANA'.lower() # Retorna string toda em minúscula.
'banana'
>>> '   abc   '.strip() # Retorna string sem espaços nos extremos.
'abc'
>>>
```

Aplicações das funções no código `forca.py`:
```python
# Resto do código...
while (not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip() # Remove espaços dos extremos com strip().
    
    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()): # Coloca as letras em maiúsculas.
            print(f"Achou a letra {letra} na posição {index}!")
        index += 1
    print("Jogando...")
# Resto do código...
```

# Estrutura de dados: List
```python
>>> valores = [0,1,2,3,5] # Declaração de uma lista de números.
>>> type(valores) # O tipo de dados da lista é 'list'.
<class 'list'>
>>> 3 in valores
True
>>> 9 in valores
False
>>> valores[0] # O elemento na posição zero é 0.
0
>>> valores[4] # O elemento na quarta posição é 5.
5
>>> min(valores) # Menor elemento da lista.
0
>>> max(valores) # Maior elemento da lista.
5
>>> len(valores) # Length, número de elementos da lista.
5
>>> valores.append(7) # Acrescenta um elemento à lista.
>>> valores
[0, 1, 2, 3, 5, 7]
>>> valores.pop() # Remove e retorna o último elemento da lista
7
>>> valores
[0, 1, 2, 3, 5]

>>> "n" in "banana" # Strings são tipos sequenciais.
True
>>> "x" in "banana" # O operador "in" testa a existência de um elemento em uma sequência.
False

```

# Guardando as letras acertadas
Adaptação do código `forca.py` para incluir os recursos de lista mostrados na aula anterior:
```python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas) # Imprime a lista.

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if (letra.upper() == chute.upper()):
                # print(f"Achou a letra {letra} na posição {index}!")
                letras_acertadas[index] = letra # Troca a letra na posição atual.
            index += 1
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
        jogar()
```
