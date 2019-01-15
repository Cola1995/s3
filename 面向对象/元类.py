
def __init__(self):
    pass




test=type('foo',(object,),{'x':1,'__init__':__init__,})
print(test.__dict__)