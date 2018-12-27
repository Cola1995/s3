name='马'

def ma():
    print(name)
    def wang():

        global name
        name='王'
    wang()
    print(name)

ma()

