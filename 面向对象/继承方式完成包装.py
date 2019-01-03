class lis(list):


    def append(self, object):

        print('ok')
        if type(object) is str:

            super().append(object)
        else:
            print('添加类型必须为str')
    def show_mid(self):
        mid=int(len(self)/2)
        return self[mid]




l1=lis('helloworld')
l1.append("sb")
print(l1)
print(l1.show_mid())