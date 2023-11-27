#As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
#a) len(), que recebe uma lista e retorna número de itens; 
# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida; 
# c) min(),que recebe uma lista e retorna o menor valor 
# d) max(), que recebe uma lista retorna o maior valor 
# e) sum(), que recebe uma lista retorna a soma dos valores
# Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a leitura dos elementos da lista. 
# Para cada uma das opções, imprima a lista que foi lida e o resultado encontrado.
# Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().

def comprimento(lista):
    contador = 0
    for item in lista:
        contador += 1
    return contador

def inverter(lista):
    inverso = []
    for i in lista:
        inverso = [i] + inverso
    return inverso

def minimo(lista):
    if not lista:
        return None
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def maximo(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

lista = []
while True:
    valor = int(input())
    if valor == 0:
        break
    lista.append(valor)

print(lista)
a= comprimento(lista)
b=inverter(lista)
c=minimo(lista)
d=maximo(lista)
e=soma(lista)
print(a)
print(b)
print(c)
print(d)
print(e)
