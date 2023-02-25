dic = {'SP': 67836.43,
'RJ':  36678.66,
'MG': 29229.88,
'ES': 27165.48,
'Outros': 19849.53}
total= sum(dic.values())
percentual_dic ={}
for i in dic:
    print(f'{i}: {dic[i]/total}%')