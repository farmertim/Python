def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
string=input()
answer=string.split(';')
final=answer[0].split('=')
final1=answer[1].split('=')
final2=answer[2].split('=')
a=[]
if is_number(final[1])==True:
    a.append(int(final[1]))
else:
    a.append(0)
if is_number(final1[1])==True:
    a.append(int(final1[1]))
else:
     a.append(0)
if is_number(final2[1])==True:
    a.append(int(final2[1]))
else:
     a.append(0)
print(str(a[0])+" "+str(a[1])+" "+str(a[2]))





