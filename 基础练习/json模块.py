import json
dic={'name':"mahong"}
# f=open('ma.txt','w')
# # f.write(str(dic))
data=json.dumps(dic)
print(data,type(data))

l_data=json.loads(data)
print(l_data,type(l_data))
print(l_data['name'])