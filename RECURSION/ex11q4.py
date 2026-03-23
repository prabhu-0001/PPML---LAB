def rev(n):
    if len(n)==0:
        return n
    return rev(n[1:])+n[0]
print(rev(input("Enter a string : ")))