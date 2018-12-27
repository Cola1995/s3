# tag=True
# while tag:
#     print('第一层')
#     k=input('1--->:')
#     if k=='quit': break
#     if k=="qa" : tag=False
#     while tag:
#         print("第二层")
#         k= input('2--->:')
#         if k == 'quit': break
#         if k == "qa": tag = False
#         while tag:
#             print("第三层")
#             k= input('3--->:')
#             if k == 'quit': break
#             if k == "qa": tag = False


for i in range(10):
    if i==2:

        break
    print(i)
