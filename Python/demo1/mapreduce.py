from functools import reduce

def str2int(raws):
    def char2int(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:x*10+y,map(char2int,raws))


i1 = str2int('0123456')
i2 = str2int('123456')
i3 = str2int('123456789')
print(i1)
print(i2)
print(i3)
print(i1==i2)
print(i1>i3) 


#*首字母大写*#
def normalize(names):
    l = map(lambda x:x[0].upper()+x[1:].lower(),names)
    return list(l) 

L = normalize(['sdlfSDFsd','AABdsfk','aslfBXX'])
print(L)    