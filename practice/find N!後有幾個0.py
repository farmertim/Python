total=1
count=0
number=int(input("輸入整數:"))
for num in range(1,number+1):
    total=total*num
print(total)
string=str(total)
print("string",string)
for x in string:
    if x=="0":
        count=count+1
    elif x!="0":
        count=0
print(count)

