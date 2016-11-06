#   2016-11-5
L = list(range(1,12))
print(L)

L1=[x*x for x in range(1,100)]
print(L1)

L2=[1,'StringS','汉字字符串',';23432;',100.1]

# 生成器
g = (x.lower() for x in L2 if isinstance(x,str))

##  只能用循环调用一次
for i in g:
    print('g:',i)

##  只能用循环调用一次
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as identifier:
    print('Generator stop iteration error')

# 列表生成式
L3 = [x.lower() for x in L2 if isinstance(x,str)]
print(L3)

# 斐波拉契数列    1,1,2,3,5,8,13....
def fib(max):
    a,b,n=0,1,0
    result=[]
    while max > n:
        result.append(b)
        a,b,n=b,a+b,n+1
    print(result)

print('~~~~fib(0)~~~~~~')
fib(0)
print('~~~~fib(1)~~~~~~')
fib(1)
print('~~~~fib(2)~~~~~~')
fib(2)
print('~~~~fib(3)~~~~~~')
fib(3)
print('~~~~fib(6)~~~~~~')
fib(6)
print('~~~~fib(10)~~~~~~')
fib(10)
print('~~~~fib(20)~~~~~~')
fib(20)
print('~~~~fib(100)~~~~~~')
fib(100)

print('~~~~~~~~~~')


# 杨辉三角
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1

def yhsj(max):
    a,b,n=[],[1],1
    while max>=n:
        if n>1:
            a,b=b,[]
            for x in range(0,n):
                if x==0 or x==a.__len__():
                    b.append(1)
                else:
                    b.append(a[x-1]+a[x])
        print(b)
        n=n+1

print('~~~~yhsj(0)~~~~~~')
yhsj(0)
print('~~~~yhsj(1)~~~~~~')
yhsj(1)
print('~~~~yhsj(2)~~~~~~')
yhsj(2)
print('~~~~yhsj(3)~~~~~~')
yhsj(3)
print('~~~~yhsj(5)~~~~~~')
yhsj(5)
print('~~~~yhsj(10)~~~~~~')
yhsj(10)
print('~~~~yhsj(20)~~~~~~')
yhsj(20)

print('~~~~~~~~~~')
