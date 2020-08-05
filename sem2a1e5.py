palavra=input('Informe sua palavra: ')
b=(palavra[::-1])  #inverte a string
if palavra == b:
    print('É palíndroma')
else:
    print('NÃO é palíndroma')