tup1 = ('1', '2', '3', '4', '5')
tup2 = ('apple', 'bat', 'car', 'dog')
dict_tup={}
min_len=min(len(tup1),len(tup2))
for i in range(min_len):
    dict_tup[tup1[i]]=tup2[i]
print(dict_tup)