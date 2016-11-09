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

egList = ['sdlfSDFsd','AABdsfk','aslfBXX']
L = normalize(egList)
print(L)

#*利用函数 capitalize，将字符串第一个字母变成大写，其他小写 *#
def normalize2(names):
    l = map(lambda x:x.capitalize(),names)
    return list(l)

print(normalize2(egList))

#*利用reduce求积*#
from functools import reduce
def prod(l):
    return reduce(lambda x,y:x*y,l)

print('3*5*8*9 =',prod([3,5,8,9]))

#*字符串转为浮点数*#
from functools import reduce

def str2float(s):
    def char2int(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':0}[c]

    i = s.index('.')
    l1 = list(map(char2int,s[0:i]))
    l2 = list(map(char2int,s[i:]))
    l2.reverse()

    return reduce(lambda x,y:x*10+y, l1) + reduce(lambda x,y:x*0.1+y, l2)

print('0123.456 =',str2float('0123.456'))
print('123.456 =',str2float('123.456'))

#*先去除点号，转成int，后除以小数的位数*#
from functools import reduce

def str2float2(s):
    def char2int(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]

    try:
        #*不含有.时，会报错（为整数时）*#
        di = s.index('.');
    except Exception:
        di = len(s);        
    
    l = s[0:di]+s[di+1:];
    i = reduce(lambda x,y:x*10+y, map(char2int,l));

    if di > 0:
        f = i/(10**len(s[di+1:]));
    else:
        f = i;
    
    return f;

print('0123.456 =',str2float2('0123.456'))
print('123.456 =',str2float2('123.456'))
print('0.456 =',str2float2('0.456'))
print('123. =',str2float2('123.'))
print('1234 =',str2float2('1234'))
