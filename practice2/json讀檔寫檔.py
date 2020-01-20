import json
with open("practice.json",mode="r",encoding="utf-8")as file:
    data=json.load(file)
    print(data)#data是一個字典資料
    name=data["name"]
    grade=data["grade"]
print(grade)
number=int(input("輸入一個數字:"))
sex=input("輸入性別:")
name=input("輸入name")
data["grade"]=number
data["name"]=name
data["sex"]=sex
print(name)
with open("practice.json",mode="w",encoding="utf-8")as file:
    json.dump(data,file)#複寫資料

    