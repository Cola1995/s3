class Room:

    def __init__(self,width,length,name):
        self.__width=width
        self.__length=length
        self.name=name


    def area(self):
        return self.__length*self.__width



r1=Room(10,20,'ce')
print(r1.area())
