n=int(input("Enter a number : "))
x=n;p=0
while(x!=0):
    p=p*10+x%10
    x//=10
print("Palindrome ") if p==n else print("Not palindrome")