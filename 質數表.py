answer=[]
count=0
for i in range(2,101):
    for j in range(2,i+1):
        if i%j==0:
            count+=1
    if count==1:
        answer+=[i]
    count=0
#for i in range(0,len(answer)):
print(answer)
