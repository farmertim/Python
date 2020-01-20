#載入模組
import pandas as pd
#建立Series 單維度的資料
# data=pd.Series([20,10,35])
# print("Max:",data.max())
# print("median:",data.median())
# print("min:",data.min())
# print(data*2)
# data=data==10
# print(data)

#DataFrame雙維度的資料 ex table
data=pd.DataFrame({
    "name":["Tim","Andy"],
    "salary":[30000,20000],
    "phone":[921333,987777]
    })
print(data)
print("--------------")
print(data["name"]) #取得所有的name
print("-------------")
print(data.iloc[1])#iloc 取得第0列
