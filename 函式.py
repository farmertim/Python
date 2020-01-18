apple=[0]
def odd(number1,number2):
    return number1+number2  #直接寫return 不用像C要有回傳型態
    #print("Answer is:",number1+number2)
def less(number1,number2):
    print("Answer is:",number1-number2)
def multiplication(number1,number2):
    print("Answer is :",number1*number2)
def division(number1,number2):
    print("Answer is :",number1/number2)
def check(name,name1):
    print(name)
    print(name1)
def private1(p=2):#可以預設數字
    print(p)
def more(*NAME):
    print(NAME)
    print("ONE:",NAME[6])
    apple[0]=NAME

more(5,9,10,5,6,8,9,9,9,9)
check(name1=5,name=3) #對應相同的參數名稱 
private1()
print("apple:",apple)
while True:
    n1=int(input("輸入數字1:"))
    n2=int(input("輸入數字2:"))
    op=input("輸入+,-,*,/:")
    if op=="+":
        print(odd(n1,n2))
    elif op=="-":
        less(n1,n2)
    elif op=="*":
        multiplication(n1,n2)
    elif op=="/":
        division(n1,n2)
    else:
        print("False")

