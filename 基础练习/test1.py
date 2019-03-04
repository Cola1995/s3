
l=['ma','wang','zhang','sb','eb']

while True:
    if 'sb' in l:
        l.remove('sb')
    elif 'eb' in l:
        l.remove('eb')
    else:
        break

    print(l)
