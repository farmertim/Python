class Point:
    number=5
    def __init__(self,n1,n2):
        self.firstname=n1
        self.lastname=n2
name1=input("輸入姓:")
name2=input("輸入名")
name=Point(name1,name2)
print(name.firstname,name.lastname)
