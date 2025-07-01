num=[5,4,2,3,6,8]
sorted_num=sorted(num)
print(sorted_num)
for i in range(0,len(sorted_num)-1,2):
    sorted_num[i],sorted_num[i+1]=sorted_num[i+1],sorted_num[i]
print(sorted_num)