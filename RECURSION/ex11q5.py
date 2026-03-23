def mini(n):
    if len(n)==1:
        return n[0]
    elif n[0]<n[1]:
        n.remove(n[1])
    else :
        n.remove(n[0])
    return mini(n)
print(mini(list(eval(input("Enter list ")))))