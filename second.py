data=[[1,2,3],[4,5,6]]
data[0][0:2]=[3,3,3,3,3]
print(data[1])
print(data[0])
#data=(3,5) ()不可電動 data[0]=5 錯誤
#data=[1,2,3] []可變動
#有順序，可以移動的列表
[1,5,6]
#有順序，不可以移動的列表
(12,2)
#集合 Set 無順序姓
{"df","df"}
print(3 in data[0]) #3有在列表中
print(1 not in data[0][1:2])

s1={1,5,6,9}
s2={5,9,10,13}
s3=s1&s2 #取S1與S2的交集
s4=s1|s2 #取S1與S2的聯集
s5=s1-s2 #取S1與S2的差集
s6=s1^s2 #取S1與S2的反交集
print(s3)
print(s4)
print(s5)
print(s6)