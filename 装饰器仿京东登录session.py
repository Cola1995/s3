user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

curren_user={'user':None,'login':False}
# str1="{'name':'alex'}"
# a='1+2'
# print(eval(str1))
# print(eval(a))

# f=open('user_list.txt','r',encoding='utf-8')  #处理TXT文件
# data=f.readlines()
# for i in data:
#     dict_i=eval(i)
    #print(dict_i['name'],dict_i['passwd'])


def fi(type='a'):
    def check_login(fuc):
        def wap(*args,**kwargs):
            #print(curren_user['user'] and curren_user['login'])
            print(type)
            if type=='a':
                if curren_user['user'] and curren_user['login']:
                    res = fuc(*args, **kwargs)
                    return res
                username=input('请输入用户名：')
                passwd=input('请输入密码：')
                for item in user_list:
                    if username==item['name'] and passwd==item['passwd']:
                        print('密码输入正确')
                        curren_user['user']=username
                        curren_user['login']=True
                        res = fuc(*args, **kwargs)

                        return res
                    else:
                        print('用户名或密码输入错误')
                        break
            else:
                print('第二种验证法师')

                if curren_user['user'] and curren_user['login']:
                    res = fuc(*args, **kwargs)
                    return res
                username=input('请输入用户名：')
                passwd=input('请输入密码：')
                # for item in user_list:
                #     if username==item['name'] and passwd==item['passwd']:
                #         print('密码输入正确')
                f = open('user_list.txt', 'r', encoding='utf-8')  # 处理TXT文件
                data = f.readlines()
                for i in data:
                    dict_i = eval(i)
                    if username==dict_i['name'] and passwd==dict_i['passwd']:
                        print('succes')

                        curren_user['user']=username
                        curren_user['login']=True
                        res = fuc(*args, **kwargs)

                        return res
                    else:
                        print('用户名或密码输入错误')
                        break


        return wap
    return check_login



@fi(type='a')
def index():
    print('欢迎光临')


@fi(type='b')
def shopping():
    print('shopping')


index()

shopping()