class Foo:
    def __setitem__(self, key, value):
        print('setitem')
        self.__dict__[key]=value

    def __getitem__(self, item):   #item系列只跟操作底层dict有关系
        print('getitem')
        return self.__dict__[item]

    def __delitem__(self, key):
        print("delitem")
        self.__dict__.pop(key)

f=Foo()

f['name']="ma"
# print(f.__dict__)
print(f['name'])
del f['name']
print(f.__dict__)