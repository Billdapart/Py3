# Write a Python program that accepts a word from the user and reverse it.

num=input("Please enter a word: ")

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = num

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))

  
