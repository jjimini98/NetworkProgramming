from urllib import request

rsp = request.urlopen("https://labs.sch.ac.kr/department/iot/m")
print("HTTP Response : ", rsp)
print("URL : ", rsp.geturl())
print("Status : ", rsp.getcode())

headers = rsp.info()
print("Date : ", headers['date'])
print("Headers")
print("=================================")
print(headers)



data = rsp.read().decode()
print("Length : " , len(data))
print("Data")
print("==================================")
print(data)