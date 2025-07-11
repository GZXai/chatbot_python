"""a_list = [3.5,6,[1,2],"abs"]
a_list[3] = list(range(0,5,2))
a_list[:2] =["a","b"]
a_list.extend([5,3,1])
print(len(a_list))
for elem in a_list:
    print(str(elem)+":"+str(type(elem)))
del(a_list[3:5])
a_list.remove("a")
print(a_list)

list = [1,2,3]
alist = list#与list指向同一个列表(同一内存)，类比同名
blist=list.copy()#不同"""
"""def get_digits(num):
    res=[]
    while num!=0:
        tem=num%10
        res.insert(0,tem)
        num=int((num-tem)/10)

    return res
print(get_digits(334567))"""

