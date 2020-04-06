import math
#28,30,31,34,39,48,63,70,82,91,107,112,127,146,171,198,258,334,403,497,571,657,730,883,1024,1139,1329,1635,2059
#ay=[2,4,8,16,32,64,128,256,512,1024,2048,4096]
y=[]
for i in range(15):
#    print("timepsa  ",ay[i])
 #   y.append(math.log2(ay[i])-math.log2(ay[0]))
    y.append(i)
m=len(y)
print (m)
xtx=(m-1)*(m)*(2*m-1)/6
b=0
j=0
for i in range(m):
    b+=(i*y[i]/xtx)
for i in range(m):
    print((y[i]),' ',(i*b),' ')
    j=j+(y[i]-b*i)**2
j=j/m
j=j**0.5
print(15*b,' +- ',round(j))
