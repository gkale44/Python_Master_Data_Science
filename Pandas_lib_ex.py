import pandas as pd
l1=[1,2,3,4,5] #object
s1=pd.Series([1,2,3,4,5])
print(s1)
s2= pd.Series([1,2,3,4,5],index = ['gk','b','c','d','e']) #changing index value
print(s2)
s3=pd.Series({'a':10,'b':20,'c':30}) #create series object from dictionary
print(s3)
s4=pd.Series({'a':10,'b':20,'c':30},index=['b','c','d','a']) #changing index position
print(s4)
print(s1[:-3])

s5=pd.DataFrame({"Name":["Ganesh","Pornima","Mahesh"],"Marks":["70","80","90"]})    #create dataframe
print(s5) #Printing data frame 

s6=pd.read_csv("sample_data.csv")
print(s6.head())


s7=s6.mean()
print("Mean value from csv",s7)
s8=s6.max()
print("Maximum value from csv",s8)
def double_make(s):
    return s*2
s9=s6[["Sepal.width","Petal.width"]].apply(double_make)
print(s9)

s10=s6['Spices'].value_counts()
print("Count value of spices",s10)

s11=s6.sort_values(by='Sepal.Length')
print("Sort value ",s11)
