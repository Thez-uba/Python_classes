#Python Operators
#Arithmetic Operstors, Assignment, Comparison, Logical, Bitwise....

# Logical Operators
# and, or, not
# Logical and
a=10
b=12
c=13
print((a<b) and (b<c))
print((a<b) and (b>c))

# Logical or
print((a<b) or (b>c))

# Logical not
d= True
print(not d)

# Bitwise Operator
# Bitwise AND-&, OR-, XOR-^(caret), NOT-~
x=7 #111
y=5 #101
print(x & y)
print(x | y)
print(x ^ y)
e= 1 #001
print(~e)

# Identity Operator
#is and is not operator
person={"name": "Thelma",
        "Gender": "Female",
        "DOB": "13-04"}
student={"name": "Thelma",
        "Gender": "Female",
        "DOB": "13-04"}

# Identity Operator...is / is not
staff=person
print(person==student)
print(person is student)
print(person is not student)

# Membership Operator... in / not in
str1="Thelma"
print("Y" in str1)
print("Y" not in str1)
print("Tlma" not in str1) # Checks in sequence so true
students=[
    {"name":"Thelma", "school":"UNIZIK"},
    {"name":"Patricia", "school":"Nile"},
    {"name":"Mandy", "school":"Unijos"}
]
students1= {"name":"Thelma", "school":"UNIZIK"}
print(students1 in students)
    
   


