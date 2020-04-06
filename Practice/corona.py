from matplotlib import pyplot as plt
import math
#28,30,31,34,39,48,63,70,82,91,107,112,127,146,171,198,258,334,403,497,571,657,730,883,1024,1139,1329,1635,2059,2545,3105,3684,4289
ay=[112,127,146,171,198,258,334,403,497,571,657,730,883,1024,1139,1329,1635,2059,2545,3105,3684,4289]
y=[]
x=[]
for i in range(len(ay)):
    x.append(i+1)
    y.append(math.log2(ay[i])-math.log2(ay[0]))
m=len(y)
xtx=m*(m-1)*(2*m-1)/6
b=0
j=0
e=0
for i in range(m):
    b+=(i*y[i]/xtx)
c=[]
for i in range(m):
    c.append(round(2**(i*b+math.log2(ay[0]))))
    print((ay[i]),' ',round(2**(i*b+math.log2(ay[0]))),' ')
    j=j+(y[i]-i*b)**2
    e=e+abs(ay[i]-2**(i*b+math.log2(ay[0])))
j=j/m
j=j**0.5
e=e/m
plt.plot(x,c,linewidth=2,label='Calculated')
plt.plot(x,ay,linewidth=2,label='Actual')
f=[]
fh=[]
fl=[]
x2=[]
j/=2
for i in range(m,m+20):
    f.append(round((2**((i)*b))*(ay[0])))
    fl.append(round(ay[0]*2**(b*(m))*2**((i-m)*(b-j))))
    fh.append(round(ay[0]*2**(b*(m))*2**((i-m)*(b+j))))
    x2.append(i+1)
plt.plot(x2,f,linewidth=1,label='future')
plt.plot(x2,fl,linewidth=1,label='better future')
plt.plot(x2,fh,linewidth=1,label='worse future')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.legend()
plt.show()
