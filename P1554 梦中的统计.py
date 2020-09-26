number,number1=list(map(int,input().split()))
a=[0,0,0,0,0,0,0,0,0,0]
for i in range(number,number1+1):
    b=str(i)
    for j in range(len(b)):
        if b[j]=='0':a[0]+=1
        elif b[j]=='1':a[1]+=1
        elif b[j]=='2':a[2]+=1
        elif b[j]=='3':a[3]+=1
        elif b[j]=='4':a[4]+=1
        elif b[j]=='5':a[5]+=1
        elif b[j]=='6':a[6]+=1
        elif b[j]=='7':a[7]+=1
        elif b[j]=='8':a[8]+=1
        elif b[j]=='9':a[9]+=1
string=""
for i in range(10):
    if i!=10:
        string+=str(a[i])+" "
    else:
        string+=str(a[i])
print(string)