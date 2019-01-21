import sys
import time

a=1
# if a==1:
#
#     print(a)
#
#     #sys.exit(0)
# print('ok')
index=0
for i in range(100):
    index+=1
    #print(index)
    s='#'*index
    sys.stdout.write('\r%s'%s)
    # sys.stdout.write(' ')

    # sys.stdout.write("\r# Process: %0.1f%%" % (float(index) / float(100) * 100))

    time.sleep(0.1)
    sys.stdout.flush()  #刷新缓存

# print("\n"+sys.version)  #版本信息
# print(sys.path)
# print(sys.platform)