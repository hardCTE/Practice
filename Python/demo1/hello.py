#   2016-11-5
L = list(range(1,12))
print(L)

L1=[x*x for x in range(1,100)]
print(L1)

L2=[1,'StringS','汉字字符串',';23432;',100.1]
L3 = [x.lower() for x in L2 if isinstance(x,str)]
print(L3)

    

