tup1 = ('1', '2', '3', '4', '5')
tup2 = ('apple', 'bat', 'car', 'dog')
rev_tuple=[]
for i in range(len(tup1)-1,-1,-1):
    rev_tuple.append(tup1[i])
print(rev_tuple)
dict_tuple={}
rev=tuple(rev_tuple)
min_len=min(len(rev),len(tup2))
for i in range (min_len):
    dict_tuple[rev[i]]=tup2[i]
print(dict_tuple)
value=[]
for i in dict_tuple.values():
    value.append(i)
print(value[-2])
