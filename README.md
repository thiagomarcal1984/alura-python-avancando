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
# Para Saber Mais: Outros recursos com a lista
Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função `.count()` das listas, veja:
```python
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))
# O código acima nos retorna 3, pois em nossa 
# lista encontramos 3 vezes o número zero nela.
```
Utilizando a função `.count()` podemos por exemplo, detectar quantas letras ainda faltam para o nosso usuário preencher:

```python
letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
```
Uma outra função que pode ser bastante útil é a função `.index()`, que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista, veja:

```python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))
# O código acima nos retorna 3, pois é o índice da 
# primeira ocorrência do elemento 'Uva' na lista frutas 
# (lembre-se nas listas começamos a contar do índice 0).
```
Só tome cuidado quando utilizar a função .index(), pois a mesma pode retornar um erro caso você tente buscar pelo índice de um elemento que não existe. Veja o caso abaixo:

```python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))
```
Ao tentar buscar pela fruta 'Melancia', obteremos o erro `"ValueError: 'Melancia' is not in list"` no console, já que é impossível buscar o índice de algo que não está na lista. Por isto, é sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter o seu índice. Um código ideal que faz uso da função `index()` é demonstrado abaixo:

```python
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
```
Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.

# O que são tuplas?
Strings, listas, ranges (sim, ranges) e tuplas são tipos sequenciais.

> Tuplas são listas imutáveis.
```python
>>> tupla = (1, 2, 3) 
>>> type(tupla) 
<class 'tuple'>
>>> tupla.append(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> tupla.pop()     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'
>>>
```

# Listas e tuplas juntas
Pontos podem ter boa representação como tuplas:
```python
>>> ponto = (2, 5)
>>> p1 = (3,5)
>>> p2 = (4,6)
>>> p3 = (5,7)
>>> line = [p1, p2, p3]
>>> line # Uma lista de tuplas que representam pontos em linha.
[(3, 5), (4, 6), (5, 7)] 
>>>
```

Strings, tuplas e range são imutáveis. Lista é um tipo sequencial mutável.

As funções `list()` e `tuple()` servem para converter tuplas para lista e vice-versa:
```python
>>> lista = ['a', 'b', 'c']
>>> tupla = tuple(lista)
>>> tupla
('a', 'b', 'c')
>>> lista = []
>>> lista = list(tupla)
>>> lista
['a', 'b', 'c']
>>>
```

# Para saber mais: Set
Listas e tuplas permitem duplicidade de dados, além de possuírem um índice (ordem de aparição na estrutura de dados).

Mas há no Python o tipo de dados chamado `set`, que não tem índice e não permite inserção de dados duplicados. Os conjuntos são declarados usando chaves ({}).

```python
>>> conj = {1} # Conjuntos vazios são declarados usando a função set({}).
>>> conj.add(2) # Tipos sequenciais usam append; sets usam add.
>>> conj.add(3) # Acrescentando o elemento 2 ao conjunto.
>>> conj.add(1) # O elemento 1 não será reinserido, porque já existe.
>>> conj
{1, 2, 3}
>>> conj[0] # Sets não tem índice.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> for i in conj:
...     print(i) # Não há garantia de que o conjunto será apresentado na ordem de inserção.
... 
1
2
3
>>> 
```

# Para saber mais: Dictionary
Dicionários em Python são a mesma coisa que arrays associativos em PHP: são conjuntos formados por pares de chave/valor. A notação para criar dicionários é quase a mesma para os sets (só que nesses últimos cada entrada é um valor único, e não um par chave/valor): 

```python
>>> idades_instrutor = {    # Mesma notação dos sets...
...     'Nico' : 39,        # Mas cada elemento é um key/value pair...
...     'Flavio' : 37,      # A chave e o valor são separados por dois pontos.
... }                       # E os pares são separados por vírgulas, assim como nos sets.
>>> idades_instrutor
{'Nico': 39, 'Flavio': 37}
>>> type(idades_instrutor)
<class 'dict'>
>>>
```

# Estipulando tentativas de erros
Mudanças no código do arquivo `forca.py`:
```python
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if (chute in palavra_secreta): # Teste de erros/acertos.
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        # Nenhum caracter em letras_acertadas dever ser um underscore.
        acertou = "_" not in letras_acertadas
        # Limitar o jogo a 6 tentativas.
        enforcou = erros == 6

        print(letras_acertadas)

    if (acertou): # Resultado do jogo.
         print("Você ganhou!!!")
    else:
         print("Você perdeu!!!")

    print("Fim do jogo")

if(__name__ == "__main__"):
        jogar()
```

# Compreensão de lista
Como converter a palavra_secreta para uma lista de mesmo tamanho composta só por underscores? Uma forma é:

```python
>>> word = "maca"
>>> lista = []
>>> for letra in word:
...     lista.append('_')
... 
>>> lista
['_', '_', '_', '_']
>>>
```
Mas existe o conceito de compreensão de lista, que abrevia códigos de loops em uma única linha:
```python
palavra = 'abacate' # Sete letras.
>>> # A sintaxe é: [ retorno_individual for elemento in sequencial ]
lista = [ '_' for letra in palavra ] 
>>> lista
['_', '_', '_', '_', '_', '_', '_']
>>> len(lista)
7
>>> # Para usar compreensão de sets, use {} ao invés de [].
>>> conj = { f'Letra {i}' for i in palavra } 
>>> palavra # Sete letras com repetição.
'abacate'
>>> conj # Cinco elementos de conjunto, sem repetição e desordenado.
{'Letra a', 'Letra t', 'Letra c', 'Letra b', 'Letra e'}
>>>
```

Outro uso de compreensões de lista é usar uma condição no fim da declaração da lista comprehension:
```python
>>> inteiros = range(10) # Elementos de zero a nove.
>>> # Repare no if depois do loop: if n % 2 == 0.
>>> lista_pares = [ n for n in inteiros if n % 2 == 0 ]
>>> lista_pares
[0, 2, 4, 6, 8]
```

# Escrevendo em um arquivo
Código Python para escrever em arquivos:
```python
# O parâmetro encoding não é obrigatório, mas é bom 
# usar para a codificação UTF-8 (com acentuação).
# O parâmetro 'w' é para apagar o arquivo e reescrevê-lo.
>>> arquivo = open('palavras.txt', 'w', encoding='UTF-8')
>>> arquivo.write('banana\n') # \n para forçar a quebra de linha.
7 # Foram escritos 7 caracteres, incluindo a quebra.
>>> arquivo.write('melancia\n')
9 # Foram escritos 9 caracteres, incluindo a quebra.
>>> arquivo.close() # Escreve tudo no arquivo, e o libera arquivo para outros programas.
# O parâmetro 'a' é para acrescentar linhas ao arquivo, sem reescrevê-lo.
>>> arquivo = open('palavras.txt', 'a', encoding='UTF-8')
>>> arquivo.write('morango\n') 
8 # Foram escritos 8 caracteres, incluindo a quebra.
>>> arquivo.write('maçã\n')    
5 # Foram escritos 5 caracteres, incluindo a quebra.
>>> arquivo.close() # Fecha/libera o arquivo.
>>> 
```
> Ainda há o modo de escrita exclusiva ('x'): se o arquivo existir, o Python lança um erro:
> ```python
> >>> arquivo = open('palavras.txt', 'x') 
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> FileExistsError: [Errno 17] File exists: 'palavras.txt'
> >>>
> ```
> Para arquivos binários, usamos a letra 'b' depois de um dos outros modificadores ('w', 'a', 'x' e 'r'). Para arquivos texto, o 'b' pode ser substituído pelo 't' ou omitido. Ainda é possível acrescentar o caracter '+' para acrescentar o modificador de leitura à escrita ('x', 'w' ou 'a') ou o modificador de escrita à leitura ('r'):
> ```python
> logo2 = open('logo.png', 'wb+') # Escreve e lê em binário.
> ```

# Lendo um arquivo
Código Python para leitura de arquivos:
```python
>>> arquivo = open('palavras.txt', 'r', encoding='UTF-8')
>>> arquivo.write('Tentei escrever') 
# Não funciona, porque usamos o modo 'r' de leitura.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not writable
>>> arquivo.read() 
# Lê o arquivo inteiro.
'banana\nmelancia\nmorango\nmaçã\n'
>>> arquivo.read() 
# Depois que se lê tudo, não há mais o que ler.
''
>>>
```

Lendo um arquivo linha a linha:
```python
>>> arquivo = open('palavras.txt', 'r', encoding='UTF-8')
>>> for linha in arquivo:
...     print(linha, end='') 
... 
# Cada linha no arquivo já tem uma quebra com /n.
# Por isso o parâmentro end='' na função print.
banana
melancia
morango
maçã
>>> arquivo.close()
```
> Uma alternativa para ler condicionalmente o arquivo é usar função `arquivo.readline()`:
> ```python
> >>> arquivo = open('palavras.txt', 'r', encoding='UTF-8')
> >>> arquivo.readline() 
> # O resultado é a leitura da primeira linha com os caracteres não imprimíveis.
> 'banana\n'
> >>> arquivo.readline().strip() 
> # Faz nova leitura, mas a função strip remove a quebra de linha '\n'.
> 'melancia'
> >>> fruta = arquivo.readline().strip() 
> # Armazena a terceira linha sem quebra na variável fruta.
> >>> fruta
> 'morango'
> >>>
> ```

# Escolhendo uma palavra
Modificações no código do arquivo `forca.py`:
```python
import random

def jogar():
    # resto do código

    arquivo = open('palavras.txt','r', encoding='UTF-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    # resto do código
```
> Um bloco com a palavra `with` garante que o arquivo será fechado, mesmo que ocorra um erro durante a execução do uso do arquivo dentro do bloco:
> ```python
> with open('palavras.txt','r', encoding='UTF-8') as arquivo:
>     for linha in arquivo:
>         linha = linha.strip()
>         palavras.append(linha)
> ```
