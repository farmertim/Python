def odd(number1,number2):
    return number1+number2  #直接寫return 不用像C要有回傳型態
    #print("Answer is:",number1+number2)
def less(number1,number2):
    print("Answer is:",number1-number2)
def multiplication(number1,number2):
    print("Answer is :",number1*number2)
def division(number1,number2):
    print("Answer is :",number1/number2)
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
