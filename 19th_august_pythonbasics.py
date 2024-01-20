# question 1
x=12
y=13
x,y=y,x
print(x,y)

# question 2
l=int(input("enter the length of rectangle:"))
w=int(input("enter the width of rectangle:"))
area=l*w
print("the area of rectangle is",area)

# question 3
cel=int(input("enter the temparature in celcius:"))
f=1.8*cel+32
print("the temparature in farenheit is",f)

# STRING BASED QUESTION
# question 1
s=input("enter any statement here to get the length of statement:")
print("the length of statement is",len(s))

# question 2
s=input("ënter the statement to count the numbers of vowels:")
c=0
v='a','e','i','o','u','A','E','I','O','U'
for i in s:
    if i in v:
        c+=1
print("the number of vowel in the statement is",c)

# question 3
x=input("string:")
print("the reversed string is",x[ : :-1])

# question 4
x=input("enter any word to check palandrome:")
if x==x[ : :-1]:
    print("yes it is palandrone")
else:
    print("no, it is not palindrone")


# question 5
x=input("enter any statement here:")
print('we are deleting all the spaces from statement:',x.replace(" ",''))




