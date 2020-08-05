#variaveis de entrada
frase=input('Digite a frase: ').upper()
l1=input('Informe o caractere/letra a ser substituido(a): ').upper()[0]
l2=input('Informe o caractere/letra para substituição: ').upper()[0]

#alteerações
trocas=frase.count(l1)
frase=frase.replace(l1,l2)
print("frase alterada:",frase)
print('Foram realizadas',trocas,'substituições')