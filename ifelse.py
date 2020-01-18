#number2=input() 輸入語法 input() 都是字串要轉資料型態
#不支援 switch


number=int(input("enter number"))
number1=int(input("enter number2"))
op=input("input  +,-,*,/:")
if op=="+":
    print(number+number1)
elif op=="-":
    print(number-number1)
elif op=="*":
    print( number*number1)
elif op=="/":
    print(number/number1)
else:
    print("輸入錯誤")
#number2=int(number2)
#number=int(number)*5
#print(number)
#if number<=50: #if 判斷是: 
#    print("this number less than 50")
#elif number>100: #elif 判斷是:
 #   print("this nubmer OX")
#else:
 #   print("byby")