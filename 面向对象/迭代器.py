class Foo:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        self.n+=1
        if self.n==100:
            raise StopIteration('jiezhu')
        return self.n



f=Foo(10)
# print(f.__next__())
# print(f.__next__())
for i in f:
    print(i)