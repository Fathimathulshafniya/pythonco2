a=0
b=1
n=int(input("Enter the number of terms:"))
if n<=0:
    print("Number of fibonacci series:")
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)
