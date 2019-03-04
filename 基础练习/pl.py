import re
suan='1+(9+3*1-4+4+(2+1)+(1+1))+(2*4)'
suan1='1+0.2/3+78*6+9/3'
suan2='1*0.2/3*78*6*9/3'
#print(1+2*3+7*6+9/3)  #52.0
#list_suan1=re.findall('(\d\.)+|+|-|*|/|*',suan1)
list_suan2=re.findall('([\d\.]+|/|-|\+|\*)',suan2)

f=re.search('\([^()]*\)',suan).group()
def first_cal(l,x):
    a=l.index(x)
    if x=="*":
        k=float(l[a-1])*float(l[a+1])
    else:
        k=float(l[a - 1]) / float(l[a + 1])
    print(l,a,k)
    # if x=='*'and l[a+1]=='-':
    #     k = -float(l[a - 1]) * float(l[a + 2])
    # elif x=='/' and l[a+1]=='-':
    #     k = -float(l[a - 1]) / float(l[a + 2])
    # elif x=='*' and l[a+1]!='-':
    #     k = float(l[a - 1]) * float(l[a + 1])
    # elif x=='/' and l[a+1]!='-':
    #     k = float(l[a - 1]) / float(l[a + 1])



    del l[a-1]
    del l[a-1]
    del l[a-1]
    l.insert(a-1,str(k))
    print("替换完的字符串是%s"%l)
    return l




# print(first_cal(list_suan1,"/"))
def all(s):
    print(s)
    sum=0

    while True:
        if "*" in s and '/' not in s:
            first_cal(s,'*')
            #print('全部是*%s'%(first_cal(s,'*')))
        elif "*" not in s and '/' in s:
            first_cal(s,'/')
        elif '*' in s and '/' in s:
            a=s.index('*')
            b=s.index('/')
            print('a=%d,b=%d'%(a,b))
            if a>b:
                first_cal(s,'*')
                print(first_cal(s,'*'))
            else:
                first_cal(s,'/')
                print(first_cal(s, '/'))

        else:
            if s[0]=='-':
                s[0]=s[0]+s[1]
                del s[1]
            sum+=float(s[0])
            for i in range(1,len(s),2):
                if s[i]=='+' and s[i+1]=='-':
                    sum-=float(s[i+2])
                elif s[i]=='+' and s[i+1]!='-':
                    sum+=float(s[i + 1])
                elif s[i]=='-' and s[i+1]=="-":
                    sum+=float(s[i+2])
                elif s[i]=="-" and s[i+1]!='-':
                    sum-=float(s[i+1])


            break

    print(sum)
    return sum




# print(kk(suan))
# print(all(['2', '+', '1', '*', '2', '+', '4', '/', '2']))



# def calculate(expression):
#     ex=[]
#     ans=0
#     if '(' not in expression:
#         ans=all(expression)
#         return ans
#     for i in range(len(expression)):
#         if expression[i]=='(':
#             ex.append(i) #ex=[6,7]
#         elif expression[i]==')': #14
#             temp=0
#             sub=expression[ex[len(ex)-1]+1:i]
#             temp=all(sub)
#             expression=expression[0:ex[len(ex)-1]]+str(temp)+expression[i+1:len(expression)+1]
#             ex.pop()
#             return calculate(expression)

# print(calculate(suan))
# print(all(list_suan2))
# print(1*0.2/3*78*6*9/3)