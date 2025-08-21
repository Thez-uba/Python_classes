if 2==2:
    print("yes")
a=26
b=18
print(a+b)
#This is a comment
fruits=["Peach", "Strawberry", "Mango"]
fruits1=(("Banana", "Apple", "Orange"))
print(fruits)
print(fruits1[2])
print(len(fruits1))
#del fruits
#print(fruits)
fruits.pop()
print(fruits)
fruits.remove("Strawberry")
print(fruits)
#deleting second item of 2nd item of fruit1 above
del fruits1[1]
print(fruits1)
#Using Tuples
fruits2=("Orange", "Mango", "Banana")
fruits3=tuple(("Orange", "Mango", "Banana"))
#Using range
abc=range(0, 200)