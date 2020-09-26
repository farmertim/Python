
number=int(input())
a=[]
for i in range(number):
    a.append(int(input()))
count=0
result=0
k=0
for i in range(number):
    count=0
    result=0
    while a[i]>0:
        k=a[i]%10
        if k>7:
            result+=(k*pow(9,count)-pow(9,count))
        else:
            result+=(k*pow(9,count))
        a[i]=int(a[i]/10)
        count+=1
    print(result)