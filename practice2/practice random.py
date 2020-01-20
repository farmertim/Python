import random
number=[5,9,9,3]
print(random.choice(number))#從number中隨機選取1個
print(random.sample(number,2))#從number中隨機選取2個
random.shuffle(number)#將number的 資料就地調換順序
print(number)
data=int(random.uniform(10,60))#從10~60間取亂數 ，機率都相同(uniform)
print(data)
answer=random.normalvariate(100,10)#常態分布的亂數 100平均數 10標準差
print(answer)
