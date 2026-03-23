a=int(input("Enter 1st no : "))
b=int(input("Enter 2nd no : "))
print("before swap : ",a,"   ",b)
a=a^b
b=a^b
a=a^b
print("After swap : ",a,"   ",b)