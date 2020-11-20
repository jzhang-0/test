'''
1.数据类型
2.矩阵，矩阵转置
'''

'''列表'''
a = [66.25, 333, 333, 1, 1234.5]
a.count(333)#数个数

a.index(1)#位置从0开始

'''列表作为堆栈使用'''#最先进去的最后出
stack=[3,4,5]
stack.append(7)
stack
stack.pop()
stack

'''列表作为队列使用'''#最先进去的最先出
from collections import deque
queue=deque(["a","klion","zj"])
queue.popleft()

'''列表推导式'''
vec=[2,4,6]
[3**x for x in vec if x>3]

'''矩阵'''
matrix=[[1,2,3,4],
        [5,7,6,8],
        [9,10,11,12]]
matrix[0]

'''矩阵转置'''
[[row[i] for row in matrix] for i in range(4)]

'''del语句'''
a.pop(1)
a = [66.25, 333, 333, 1, 1234.5]
del a[2:4]#只有2到3

'''list,tuple,set'''
t=1,2,3#tuple元组，不可变
list=[1,2,4,3,3]
set={1,2,3,3}#数学中的集合
nulset=set()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
knights.items()
 for k, v in knights.items():
   print(k, v)

