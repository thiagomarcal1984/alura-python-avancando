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
