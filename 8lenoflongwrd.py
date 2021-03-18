list=[]
n=int(input("enter the limit"))
for i in range(n) :
 x=input("enter the words")
 list.append(x)
print(list)
length=len(list[0])
temp=list[0]
for i in list :
 if len(i)>length :
   length=len(i)
   temp=i
print("longest word is of length",length)