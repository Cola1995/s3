import abc
class all_file(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def read(self):
        pass

    @abc.abstractclassmethod
    def write(self):
        pass

class disk(all_file):
    def read(self):
        print('disk read')
    def write(self):
        print('disk write')


class men(all_file):
    def read(self):
        print('men read')
    def write(self):
        pass

d1=disk()
d1.read()
d1.write()
