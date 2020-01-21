import pandas as pd
#資料索引

#可自訂index
data=pd.Series([5,4,3],index=["a","b","c"])
# print(data)
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)

#取得資料
print(data[2])#根據順序取得資料
print(data["a"])#根據索引取得資料

print(data.max())
print(data.sum())
print(data.median())
print("標準差",data.std())
print("最大的三位數:\n",data.nlargest(2))

data=pd.Series(["您好","Python","Pandas"])
print(data.str.lower())#轉成小寫
print(data.str.len())#計算每個字串的長度
print(data.str.cat(sep=","))#把字串串起來 可自訂串接的符號cat(sep=",")
print(data.str.contains("P"))#判斷 每個字串是否包含P
print(data.str.replace("您好","Hello"))#把您好換成Hello

print(data)