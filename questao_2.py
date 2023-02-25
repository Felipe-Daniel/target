entrada = input('número escolhido: ')
try:
    entrada = int(entrada)
except:
    print('insira número')

i=1
while True:
    if (i==entrada):
        print('Número pertence')
        break
    elif(i>entrada):
        print('Número não pertence')
        break
    i+=i