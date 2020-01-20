#file=open("writedata.txt",mode="w",encoding="utf-8")
#file.write("測試\ntext")
#file.close()
with open("writedata.txt",mode="w",encoding="utf-8")as file:
    file.write("5\n9\n10")
with open("writedata.txt",mode="r",encoding="utf-8")as file:
    data=file.read() #讀取全部文字
print(data)
sum=0
print("-------------------------------------------------")
with open("writedata.txt",mode="r",encoding="utf-8")as file:
    for number in file: #一行一行讀取文字
        sum+=int(number) 
print("sum:",sum)
        