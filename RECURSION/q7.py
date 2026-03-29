def palindrome(n):
    if len(n)==1 or len(n)==0:
        return True
    if n[0]!=n[-1]:
        return False
    return palindrome(n[1:len(n)-1])
print(palindrome(input("Enter a string : ")))
