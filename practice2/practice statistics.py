import statistics as st #把statistics 縮短成 st
number=[1,2,3,4,5,6]
average=st.mean(number)#算平均
print(average)
center=st.median(number)#中位數
print(center)
n=st.stdev(number)#標準差
print(n)
