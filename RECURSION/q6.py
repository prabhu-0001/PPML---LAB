def power(x,y):
    if y==1:
        return x
    return x*power(x,y-1)
print("Power =",power(int(input("Enter base : ")),int(input("Enter power : "))))
