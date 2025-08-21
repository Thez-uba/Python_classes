a=10
b=9
if a<=b:
    pass
# List of cars
cars=["Honda","Camery","Lexus","Jeep","Jett"]
# cars[0]
for variable in cars:
    if variable=="Camery":
        print(variable)
    else:
        pass

# dict of car
car={
    "name":"Volkswagon",
    "prodYear":"1978",
    "model":"v20",
    "driver":"Morris"
}
for prop in car: # prop represents the keys loopin' through 'dict'
    print(prop, car[prop])
    #print(car[prop])

a=0
while a<len(cars):
    print(cars[a])
    a+=1

c=1
text=" "
for c in range(1, 500):
    text+=str(c)+" "
print(text)

