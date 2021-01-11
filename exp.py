import numpy as np       #for mathematical calculations
import matplotlib.pyplot as plt #for plotting
import pandas as pd      #for data frame creation 
import array as arr
df=pd.read_csv("/home/dilna/Documents/kalman filter/simple-master/dt/mp1.txt",sep="\t")
df1=np.array(df)
x=df1[:,5]
y=df1[:,7]
z=df1[:,6]
#plt.plot(x,z)
#plt.xlabel('posx(mm)')
#plt.ylabel('posz(mm)')
#plt.show()
#plt.plot(y,z)
#plt.xlabel('posy(mm)')
#plt.ylabel('posz(mm)')
#plt.show()
#print (x [150])
#x_e = np.array(x[0]+(((x[1]-x[0])/(z[1]-z[0]))*.001))
# print(x_e)
n=(len(x))
x_e = []
y_e = []
x_e.insert(0,x[0]+(((x[1]-x[0])/(z[1]-z[0]))*.001))
y_e.insert(0,y[0]+(((y[1]-y[0])/(z[1]-z[0]))*.001))
for i in range  (1,n) :
    dx = ((x[i])-np.array(x_e[i-1]))



#print (np.array(x_e[0]))

    dy = (y[i]-y_e[i-1])
    dz = (z[i]-z[i-1])
    tx = dx/dz
    ty = dy/dz
    x_e .append  ((x[i])+(tx*.001))
    y_e  . append ((y[i])+(ty*.001))
#print (x_e[2])



#scatter plot
#xval=plt.scatter(y,z,color='blue',marker='*',label='posx (mm)')
#labelling axis
plt.xlabel('pos(mm)')
plt.ylabel('posz(mm)')

yval=plt.scatter(y_e,z,color='yellow',marker='.',label='posy (mm)')


#naming the data sets,getting label on plot
#plt.legend(handles=[xval,yval])
#getting plot
plt.show()
print(np.sqrt(36))