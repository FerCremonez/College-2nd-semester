'''frase=input('Digite uma frase: ').upper()
cont=0
for i in range(len(frase)):
    if frase[i]=='A' or frase[i]=='E' or frase[i]=='I' or frase[i]=='O' or frase[i]=='U':
        cont+=1
print(f'Existem {cont} vogais na frase')'''


frase = input('Digite uma frase = ').lower()
lista = ['a','e','i','o','u']
cont = 0
for i in range(len(frase)):
    if frase[i] in lista:
        cont += 1
print(f'Existem {cont} vogais na frase')