import requests
from email import header

header = {
        'Authorization':'token 1f78420bfd4d2fdc9c52851098e3419787a5dbe7'
    }
api = "https://zite.zite.io/api/v2/custom-report/report-data/1932"
resp = requests.get("{}".format(api),headers=header,)     
# print(*[api, resp.status_code, resp.json()])
test = resp.json()
a = list(test.get("data"))
# print(a)
e = test.get("next_page")
# print (e)
while e != None  :
    api2 = "https://zite.zite.io/api/v2/custom-report/report-data/1932?reportId=1932&project_id=394&page_no={}".format(e)
    resp2 = requests.get("{}".format(api2),headers=header)  
    # print(resp2.json())
    test2 = resp2.json()
    # print(test2)
    e = test2.get("next_page")
    # print(e)
    a = a + list(test2.get("data"))
# print(a)
c = len(a)
print (c)
for n in range(c):
    print(n)
    d = list(a)[n]

    if 'female' in d :
        
        print((a)[n])          

    else:
        pass