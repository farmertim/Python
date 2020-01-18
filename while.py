number=1
total=0
Length=len([1,2,3,4,5,6,7])
while  total<10:#while 判斷是: 記得縮排 否則會出錯
    number1=int(input("input number1:"))
    number2=int(input("input number2:"))
    total=number1+number2
    print(number1+number2)
for n in range(1,Length): #range 從1跑到Length
    print(n)
for m in (9,6,8): #從9跑到8
    print(m)