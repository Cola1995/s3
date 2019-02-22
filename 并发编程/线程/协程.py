from greenlet import greenlet

def eat():
    print("Star eating")
    g2.switch()
    print("end eating")
    g2.switch()
def play():
    print("start play")
    g1.switch()
    print("end play")



g1=greenlet(eat)
g2=greenlet(play)
g1.switch()
