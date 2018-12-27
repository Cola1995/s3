import re
suan='1+(9+3*1-4+(1+4+(2+1*2+4/2)+(1+1))+(2*4))'


f=re.search('\([^()]*\)',suan).group()

print(f)


s='(2+1*2+1*3+3*3+9/3)'
s_t=''

if  '*'or '/' in s:


    for i in s:

        if i=='*':
            jie=int(s[s.index(i)-1])*int(s[s.index(i)+1])
            s=s.replace(s[s.index(i)-1:s.index(i)+2],str(jie))
            print(s)
        elif i=='/':
            jie1=int(s[s.index(i)-1])/int(s[s.index(i)+1])
            s=s.replace(s[s.index(i)-1:s.index(i)+2],str(jie1))
            print('体替换后的字符串是%s'%s)

    else:
        print("ssssss%s"%s)
        index=s.count('+')+s.count('-')
        for jj in range(index+1):
            for i in s:
                if i=='+':
                    sd=int(s[s.index(i)-1])+int(s[s.index(i)+1])
                    s=s.replace(s[s.index(i)-1:s.index(i)+2],str(sd))
                    print(s)


# else:
#     for i in s_t:
#         if i== '+':
#             int_jg=int(s_t[s_t.index(i)-1])+int(s_t[s_t.index(i)+1])
#             t_jia=s_t.replace(s_t[s_t.index(i)-1:s_t.index(i)+2],str(int_jg))
#             print(t_jia)







