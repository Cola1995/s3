

def person(name,age,sex):
    def init(name,age,sex):
        p={
            "name":name,
            "age":age,
            "sex":sex,
            "spe":spreak,
            'eat':'eat'
        }
        return p
    def spreak():
        print('%s正在讲话'%name)

    def eat():
        print('正在吃饭')


    return init(name,age,sex)

p1=person('wang','20','nv')
p1['spe']()

