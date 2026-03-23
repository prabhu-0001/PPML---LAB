s=input("Enter a String : ")
print("Reverse = ",s[::-1])
v=0;c=0
for i in s:
    if i in "AEIOUaeiou":
        v+=1
    else:
        c+=1
print(f"Vowel = {v}\nConsonant={c}")
# st=input("Enter a string : ")
# rev=''.join(reversed(st))
# print(rev)
# vowel=0;consonant=0
# for i in st:
#     if i in "aeiouAEIOU":
#         vowel+=1
#     else:
#         consonant+=1
# print("Number of vowel = ",vowel,"\nNumber of consonant = ",consonant)