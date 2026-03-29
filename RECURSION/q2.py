def fibonacci(n):
    if n<=1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)
print("fibonacci=",fibonacci(int(input("Enter a no :"))))
def fibon(n,a=0,b=1):
    if n==0:
        return 
    print(a,end=" ")
    fibon(n-1,b,a+b)
fibon(5)
