# 杨辉三角
#1            1
#2          1   1
#3        1   2   1
#4      1   3   3   1
#5    1   4   6   4   1
#6  1   5   10  10  5   1

def yhsj():
    L=[1]
    while True:
        yield print(L)
        L.append(0)     #### 此问题的关键！！！！列表[-1]是最后一个元素
        L=[L[x-1]+L[x] for x in range(len(L))]

n=0
for t in yhsj():
    print(t)
    n=n+1
    if n==10:
        break

##########
def yhsj2():        # 不如yhsj()巧妙
    a,b=[],[1]
    while True:
        if a!=[]:
            b=[]
            for x in range(0,len(a)+1):
                if x==0 or x==len(a):
                    b.append(1)
                else:
                    b.append(a[x-1]+a[x])
        a=b
        yield b

n2=0
for t in yhsj2():
    print(t)
    n2=n2+1
    if n2==10:
        break