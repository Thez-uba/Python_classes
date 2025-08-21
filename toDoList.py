toDoList = [{"name" : "Reading",
              "due_date":"29/07/2025", 
              "status" : "Pending"
              }
           ]

def viewListItem():
    index = 1
    print("To Do Items: ")
    for item in toDoList:
        print(f"{index} - {item["name"]} - {item["due_date"]} - {item["status"]}")
        index += 1

def addNewItem(itemName, dueDate, status):
    toDoList.append({"name": itemName, "due_date": dueDate, "status": status})
    print("New item has been added!")
    viewListItem()

# addNewItem("Meeting", "28/07/2025: 4pm", "pending")



def deleteItem(index):
    del toDoList[index]
    print("ONE ITEM HAS BEEN DELETED FROM THE LIST !")
    viewListItem()

# deleteItem(0)

def editItem(index):
    item = toDoList[index]
    print("What do you want to modify ?")
    option = int(input("Enter 1 for edit item name, 2 to edit item due date, 3 to edit item status "))
    if option > 3 or option < 1:
        print("Wrong option inputted. Try again")
        option = int(input("Enter 1 for edit item name, 2 to edit item due date, 3 to edit item status "))

    match option:
        case 1:
            newName = input("Enter new item name: ")
            toDoList[index]["name"] = newName
            print("Item updated !")
            print(f"{toDoList[index]["name"]} - { toDoList[index]["due_date"]} - {toDoList[index]["status"]}")
        case 2:
            newDueDate = input("Enter new item due date: ")
            toDoList[index]["due_date"] = newDueDate
            print("Item updated !")
            print(f"{toDoList[index]["name"]} - { toDoList[index]["due_date"]} - {toDoList[index]["status"]}")
        case 3:
            newStatus = input("Enter new item Status: ")
            toDoList[index]["status"] = newStatus
            print("Item updated !")
            print(f"{toDoList[index]["name"]} - { toDoList[index]["due_date"]} - {toDoList[index]["status"]}")    

# editItem(0)

def appMenu():
    print("Welcome To My First Terminal To Do App")
    print("What do you want to perform ?")
    print("1. View List Items")
    print("2. Add New Item")
    print("3. Delete an Item")
    print("4. Edit an Item")

def startApp():
    appMenu()
    while True:
        choice= int(input("Enter a number between 1 and 4: "))
        if choice == 1:
            viewListItem()
            appMenu()
        elif choice == 2:
            itemName = input("Enter item name: ")
            itemDueDate = input("Enter due date: ")
            itemStatus = "pending"
            addNewItem(itemName, itemDueDate, itemStatus)
            appMenu()
        elif choice == 3:
            viewListItem()
            itemNumber = int(input("Enter item number to be deleted: ")) - 1
            deleteItem(itemNumber)
        elif choice == 4:
            viewListItem()
            itemNumber = int(input("Enter item number to be Edited: ")) - 1
            editItem(itemNumber)
        else:
            print("Goodbye, you entered out of range!")
            exit()

# run the app
startApp()