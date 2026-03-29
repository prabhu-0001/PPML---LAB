def add(n):
    if n<=1:
        return n
    return n+add(n-1)
print("Sum=",add(int(input("Enter a no :"))))
