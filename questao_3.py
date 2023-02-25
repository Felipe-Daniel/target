import json
dic = json.load(open('dados (1).json'))
menor_valor = dic[0]['valor']
maior_valor = dic[0]['valor']
dias_maior_que_a_media = 0
media=0
for i in dic:
    media+=i['valor']
media=media/len(dic)
for i in dic:
    if i['valor'] == 0:
        continue
    if i['valor'] < menor_valor:
        menor_valor=i['valor']
    if i['valor'] > maior_valor:
        maior_valor=i['valor']
    if i['valor'] > media:
        dias_maior_que_a_media += 1
print(f'Menor valor: {menor_valor}')
print(f'Maior valor: {maior_valor}')
print(f'Dias maior que à média: {dias_maior_que_a_media}')