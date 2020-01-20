import urllib.request as request #網路連線的東溪
import json
#臺北市水質監測資訊網站 
src="	https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=190796c8-7c56-42e0-8068-39242b8ec927"
with request.urlopen(src)as response:
   
    #data=response.read().decode("utf-8")#取得網站上的原始碼
    data=json.load(response)#利用json 模組處理json資料格式
print(data)
alist=data["result"]["results"]#字典
print(alist)
print("--------------------------------------")

with open("webpractice.txt",mode="w",encoding="utf-8")as TXT:#把資料寫入webpractice.txt中
    for acticity in alist:
        print(acticity["code_name"]+"\n")
        TXT.write(acticity["code_name"]+"\n")