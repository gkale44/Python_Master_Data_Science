# Author Ganesh Kale
#Date 17/10/2022

import numpy as np
n1=np.array([10,20,30,40]) #Create Array
print("n1 array data=",n1)
n1_1=np.array([50,60,70,80])
print("value of n1_1=",n1_1)
n2=np.array([[10,20,30,40,10],[1,2,3,4,5]])# two dimensional array
print("n2 array data=",n2)
n3=np.array((3,3))#
print("n3 array data=",n3)
n4=np.full((5,5),10)# create 5*5 array with value 10
print("n4 array data=",n4)
n5=np.arange(10,51,5) #create array with specific differance or create array with 10 to 51 with differance of5
print("n5 array data =",n5)
n6=np.arange(1,105,10)
print("n6 array data (arange data)=",n6)
n7=np.random.randint(1,100,5) #create random array with 5 value between 1 to 100
print("random data n7 = ",n7)
n8=np.vstack((n1,n1_1))#vertical Stack
print("vertically stack data=",n8)
n9=np.hstack((n1,n1_1))#horizontal stack
print("horizotally statck value of n1 and n1_1=",n9)

#Numpy Intersection and Difference
n10=np.array([10,20,30,40,50,60])
print ("value of n10=",n10)
n11=np.array([50,60,70,80,90,100])
print ("value of n11=",n11)
n12=np.intersect1d(n10,n11) #intersection 
print ("n12=Intersection value of n10 and n11",n12)
n13=np.setdiff1d(n10,n11)#value present in n10 but not in n11
print("n13=differance value of n10 and n11=",n13)
n14=np.setdiff1d(n11,n10)
print("differance value of n11 and n10",n14)

n15=np.array([10,20])
print ("n15 array=",n15)
n16=np.array([30,40])
print ("n16 array=",n16)
n17=np.sum([n15,n16])
print("Sum of n15 and n16=",n17)#sum of n15 and n16 
n18=np.sum([n10,n11],axis=0) #axis=0 mean sum element to element of two array
print("sum of n10 and n11 with axis 0=",n18)
n19=np.sum([n10,n11],axis=1) #axis=1 mean sum of one array horizotally and another also
print("sum of n10 and n11 with axis 1=",n19)
n20=n10+5 #adding 1 to each element of array n10, apply same for -,*,/
print("value of n20",n20)
n21=np.mean(n10)
print("Mean value of n10",n21)
n22=np.std(n10)
print("standard deviation value of n10",n22)#checking standard deviation of values
n23=np.save('my_numpy',n10)
n24=np.load('my_numpy.npy')
print("value of saved numpy ",n24)
n25=np.array([[10,20,30],[40,50,60]])
print("n25 array=",n25)
n26=np.array([50,60])
n26.shape=(2,1) #change shape of n26 array to 2*1 shape of array 
print("n26 array=",n26)
print (np.shape(n25))
print (np.shape(n26))
n27=n25+n26
print("Addition of n25 and n26",n27)#dimension should same or according to rule of broadcasting

n28=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Multidimension matrix",n28) #multidimension array
n29=n28[0] #to access 0 index matrix or row from n28
print ("Access 0 index value",n29)
n30=n28[:,1] #access all rows of second colom
print('Access all rows of second coloum',n30)
n31=n28[0,1] #access individual value... index start from 0
print(n31)
