# import hashlib
#
# obj=hashlib.md5('wsdeewwewewew'.encode('utf8'))  #md5加密
#
# obj.update('ma'.encode('utf8'))
# #obj.update("ma",encode('utf-8'))
# print(obj.hexdigest())
# import re
# ste='(1+2)'
# print(re.sub('[\()]+','',ste))
#
# print(ste[1:-1])
import re
import pl
suan='1+(9+3*1-4+(4+(2+1))+(1-2))+(2*4)'
suan1='1+2'
f = re.search('\([^()]*\)', suan).group()


# ff=f[1:-1]
# sum='3'
# tt=suan.replace(f,sum)
# print(tt)
# fff=re.findall('([\d\.]+|/|-|\+|\*)',ff)
def kk(ss):

    f = re.findall('\([^()]*\)', ss)
    while True:
        for i in range(len(f)):
            rr=re.findall('([\d\.]+|/|-|\+|\*)', f[i])
            sum=pl.all(rr)
            ss=ss.replace(f[i],str(sum))

        if '(' in ss:
            f=re.findall('\([^()]*\)', ss)
            for i in range(len(f)):
                rr = re.findall('([\d\.]+|/|-|\+|\*)', f[i])
                sum = pl.all(rr)
                ss = ss.replace(f[i], str(sum))
        else:
            break


    print(ss)
    sss = re.findall('([\d\.]+|/|-|\+|\*)', ss)
    return sss









print(pl.all(kk(suan)))
print(1+(9+3*1-4+(4+(2+1))+(1-2))+(2*4))