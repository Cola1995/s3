#map函数
num=[1,2,3,4]
print(list(map(lambda x:str(x),num)))

#reduce 函数
from functools import reduce
print(reduce(lambda x,y:x+y,num,2))

#filter函数
name=['wang_sb','ma']
print(list(filter(lambda x:x.endswith('sb'),name)))