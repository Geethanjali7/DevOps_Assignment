def fact(n):
    if n<0:
        return -1
    elif n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter an integer:"))
res=fact(num)
if res==-1:
    print("Oops!!!! enter a positive integer !!!!!")
else:
    print(f"factorial of {num} = ",res) 
