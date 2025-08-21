#Lists Tuples and Range
cars1=["Toyota", "Camery", "Volvo", "Venza", "Lexus"]
cars2=("Toyota", "Camery", "Volvo", "Venza", "Lexus")
range1=range(10, 89)

print(type(cars1))
print(type(cars2))
print(type(range1))

#Index
print(cars1[0:3])
print(cars2[-1])
print(range1[1])
print(range1[-1:-3])

#Adding new Items usinl list.append
cars1.append("Benz")
print(cars1)
#Inserting at specific position using isert
cars1.insert(0, "Volkwagon")
print(cars1)
cars1.insert(6, "BMW_second to last")
print(cars1)
#removing list items using pop, remove, clear
cars1.pop()
print(cars1)
cars1.remove("Toyota")
print(cars1)
del cars1[1]
print(cars1)
#Editing using index...
cars1[2]="Porche"
print(cars1)
#Working with Tuple
cars2[0]
#casting or converting a tuple to a list
editTuple=list(cars2)
print(editTuple)
#cars1.clear()
#print(cars1)
#Mapping Python Dictionary
person={"name":"Josh", "age":"18 yrs", "Sex":"Male"}
print(type(person))
person["name"]
print(person["name"])
