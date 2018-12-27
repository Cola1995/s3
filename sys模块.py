import sys
import time

a=1
# if a==1:
#
#     print(a)
#
#     #sys.exit(0)
# print('ok')

for i in range(10):

    sys.stdout.write('#')
    time.sleep(0.1)
    sys.stdout.flush()  #刷新缓存

print("\n"+sys.version)  #版本信息
print(sys.path)
print(sys.platform)