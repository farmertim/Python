print(pow(2,32))
number=int(input())
a=[]
count=0
count1=0
for i in range(number):
    a.append(int(input()))
for i in range(number):
    for j in range(int(a[i])):
        b=str(j)
        for k in range(len(str(j))):
            if b[k]=='7':
                count1=1
                break
        if count1==1:
            count+=1
        count1=0
    print(int(a[i])-count)
    count=0
    

