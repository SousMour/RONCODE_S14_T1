#Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.
a=[]
b=[]
for i in range(20):
    valor_a=int(input())
    a.append(valor_a)

for i in range(20):
    valor_b=int(input())
    b.append(valor_b)

c = []

for i in range(len(a)):
    soma = a[i] + b[i]
    c.append(soma)


print(a)
print(b)
print(c)