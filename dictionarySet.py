#Dictionary
Student1={"name":"Josh", "age":"18 yrs", "gender":"Male", "DOB": "13-04", "Natinality":"Nigeriaan", "Email":"uba.thelmad@gmail.com", "Phone":"07082310150"}
#print Name & email
print(Student1["name"])
print(Student1["Email"])
#Add home address
Student1 ["homeAddress"]="Abuja"
#Change nationlity
Student1["Nationality"]="Canada"
#Print Student1
print(Student1)
#Delete content
Student1.clear()
print(Student1)

#Set Datatype
fruits1={"Apple","Orange"}
fruits2=frozenset(("Apple","Orange"))

print(fruits1)
for item in fruits1:
    print(item)

#Adding item(s) to set
# 1. Using the set.add() method
fruits1.add("Strawberry")
print(fruits1)
#Ading Using set.update() method
fruits1.update({"Mango","Banana","Guava"})
print(fruits1)

newItems=[23, 76, "a", "b"]
fruits1.update(newItems)
print(fruits1)

#Removing Items from set
# Using set.remove or set.discard
fruits1.remove("Orange")
print(fruits1)
fruits1.discard("Banana")
print(fruits1)

# Boolean Datatype
# True or False / 1 or 0

# Length of an obj
# Length of a String
text="This is to demonstrate string length"
print(len(text))
print(len(fruits1))

#To check variable datatype
print(type(fruits1))