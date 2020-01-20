

def Add(*number):#加法
    total=0
    for num in number:
        total+=num
    return total
def Subtraction(*number):#減法
    total=0
    for num in number:
        total-=num
    return total
def multiplication(*number):#乘法
    total=1
    for num in number:
        total*=num
    return total
def division(*number):
    total=number[0]
    count=0
    for num in number:
        if count!=0:
            total/=num
        count+=1
    return total

