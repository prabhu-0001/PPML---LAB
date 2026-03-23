def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(f"Factorial = {fact(int(input("Enter a number to find the factorial : ")))}")