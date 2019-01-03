import time
class Open:

    def __init__(self,filename,mode="r",encoding='utf-8'):
        self.filename=filename
        self.mode=mode
        self.encoding=encoding
        self.file=open(filename,mode,encoding=encoding)
    def write(self,line):
        t=time.strftime("%Y-%m-%d %X")
        self.file.write("%s %s"%(t,line))
    def __getattr__(self, item):
        return getattr(self.file,item)

f=Open('a.txt','w+')
f.write('111111\n')
f.write('cpu使用率过高\n')
f.write('内存过高\n')
f.seek(0)
print(f.read())
