print("-------------------")
name=set("name1")#字串切割便字元
print('m' in name)
print(name)
#字典運算 key-value配對
check={"name":"name1","car":"車子"}
check["name"]="name2" #修改
print(check["name"])
print("name" in check)#判斷key是否存在 ex name 是否存在在check裡
print("dfdfd" not in check)
print(check)
del check["name"] #刪除
print(check)

dic={x:x*2 for x in [16,2]} # 從列表中的資料產生字典

print(dic)