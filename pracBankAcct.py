# Bannk Account Operations
# 1. User Registration
# Customer Requirement - First and last name, email, phone, NIN, home_address, gender, occupation, LGA, DOB
# Staff Requirement - firstname, lastname, email, phone, gender...
# 2. Deposits
# 3. Withdrawal
# 4. Checking Balance
# 5. Transfer Operation
# 6. Update User Account Details
# 7. View User Details
# 8. Restrict User Bank Account
# 9. Delete User Acocunt

"System Users"
"a. Customer"
"b. Staff"
"c. Manager"

customers = []
staff = []
manager = {"username" : "manager", "password" : "123456"}

# define the user class
class User:
    def __init__(self, firstname, lastname, email, phone, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.gender = gender

# Customer Class
class Customer(User):
    def __init__(self):
        pass
        # super().__init__(firstname, lastname, email, phone, gender)
        # self.nin = nin
        # self.home_address = home_address
        # self.occupation = occupation
        # self.state_of_origin = state_of_origin
        # self.lga = lga
        # self.dob = dob
    
    def registerCustomer(self, firstname, lastname, email, phone, gender, nin, home_address, occupation, state_of_origin, lga, dob, account_number):
        new_customer = {
            "firstname" : firstname,
            "lastname" : lastname,
            "email" : email,
            "phone_number": phone,
            "gender" : gender,
            "nin" : nin,
            "home_address" : home_address,
            "occupation" : occupation,
            "state_of_origin" : state_of_origin,
            "dob" : dob,
            "lga" : lga,
            "account_number" : account_number,
            "balance" : 0.00,
            "restricted" : False
        }
        customers.append(new_customer)
        print(f"Registration was successful, Your account number is: {account_number}")

    # Method to handle deposit
    def depositMoney(self, account_number, amount):
        for customer in customers:
            if customer["account_number"] == account_number:
                new_bal = customer["balance"] + amount
                customer["balance"] = new_bal
                print("Deposit was successful.")
            else:
                pass
    
    # Method to handle withdrawal
    def withdrawMoney(self, account_number, amount):
        for customer in customers:
            if customer["account_number"] == account_number:
                if customer["balance"] > amount:
                    new_bal = customer["balance"] - amount
                    print(f"{amount} withdrawn from {customer["firstname"]}")
                    customer["balance"] = new_bal
                else:
                    print("Insufficient fund!")
            else:
                pass

    # Method to check balance
    def checkBalance(self, account_number):
        for customer in customers:
            if customer["account_number"] == account_number:
                print(f"{customer["firstname"]} {customer["lastname"]} balance is: {customer["balance"]}")
            else:
                print("Access Denied , contact customer care")
        else:
            print("Account Number does not exists") 

    # Method to handle trnsfer operation
    def transferMoney(self, sender_account, receiver_account, amount):
        for customer in customers:
            if customer["account_number"] == sender_account:
                if customer["restricted"] != True:
                    if customer["balance"] <= amount:
                        print("Inssuficient funds")
                        return
                    else: 
                        for reciever_customer in customers:
                            if reciever_customer["account_number"] == receiver_account:
                                reciever_customer["balance"] += amount
                                customer["balance"] -= amount
                                print(f"{amount} has been successfully transfered to {reciever_customer["firstname"]}")
                else:
                    print("Access Denied , contact customer care") 

    #method to handle customers detail update
    def updateDetails(self, *details):
        for customer in customers:
            if customer["account_number"] == item["account_number"]:
                for item in details:
                    if item["email"] and item["phone"]:
                        customer["email"] = item["email"]
                        customer["phone_number"] = item["phone"]
                        print("customer Details Submitted")
                    elif item["email"] == None and item["phone"] != None: 
                        customer["phone_number"] = item["phone"]
                        print("New phonenumber submitted for changes")
                    elif item["email"] != None and item["phone"] == None:
                        customer["email"] = item["email"]   
                        print("New email address has been submitted for changes") 

    #method to handle view user details operation 

    def viewUserDetail(self, account_number):
        for customer in customers:
            if customer["account_number"] == account_number:
                print(f"Name: {customer["firstname"]} {customer["lastname"]}, Account Number: {customer["account_number"]}, Email Address: {customer["email"]}, Phone Number: {customer["phone_number"]}, State Of Origin: {customer["state_of_origin"]}, LGA: {customer["lga"]}, Date of Birth: {customer["dob"]}, Account Number: {customer["balance"]}, NIN: {customer["nin"]}, Occupation: {customer["occupation"]}, Gender: {customer["gender"]}, Home Address: {customer["home_address"]} " )
 
            elif customer["account_number"]!= account_number and customer == customer[-1]:
                 print("invalid account number ")  

    # return print(Invalid accont number....)

    # Metjod to handle account restriction

    def accountRestriction(self, account_number):
        for customer in customers:
            if customer["account_number"] == account_number:
                customer["restricted"] = True
                return print(f"{customer["firstname"]} account has been restricted.")
            elif customer["account_number"] != account_number and customer == customers[-1]:
                return print("No account found. Kindly check the number provided.")
            else:
                pass

    # Method to handle delete acount operation

    def deleteCustomer(self, account_number):
        for customer in customers:
            if customer["account_number"] == account_number:
                customers.remove(customer)
                return print(f"{customer["firstname"]} account has been deleted from the list.")
            elif customer["account_number"] != account_number and customer == customers[-1]:
                return print("No account found. Kindly check the number provided.")
            else:
                pass


# Staff class
class Staff(User):
    def __init__(self):
        # self.staffList = []
        pass
    # Method to handle Rigisering Staff
    def addStaff(self, staff_name, staff_id, email, phone, home_address, password):
        new_staff = {
            "name" : staff_name,
            "id" : staff_id,
            "email" : email,
            "phone_number" : phone,
            "home_address" : home_address,
            "password" : password
        }
        staff.append(new_staff)
        return print(f"{staff_name} added succesfully,\n Email: {email}, Password: {password}")
    
    # Deposit money for cusotmer
    def depositForCustomer(self, staff_id, password):
         for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                customer_account = input("Enter customer account number: ")
                amount = input("Enter amount: ")
                customer = Customer()
                customer.depositMoney(customer_account, amount)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")
    
    # Create account for customer
    def createAccountForCustomer(self, staff_id, password):
        for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                customer = Customer()
                firstname = input("Enter customer firstame: ")
                lastname = input("Enter customer lastname: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phone number: ")
                nin = input("Enter customer NIN: ")
                home = input("Enter customer home address: ")
                gender = input("Enter customer gender: ")
                dob = input("Enter customer DOB: ")
                state = input("Enter customer state of origin: ")
                lga = input("Enter customer LGA: ")
                occupation = input("Enter customer occupuation: ")
                account_number = input("Enter 10 digit account number: ")
                customer.registerCustomer(firstname, lastname, email, phone, nin, home, gender, dob, state, lga, occupation, account_number)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")

    # Method for staff to handle transfer
    def transfer(self, staff_id, password):
        for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                sender_account = input("Enter sender account number: ")
                receiver_account = input("Enter receiver account number: ")
                amount = input("Enter amount: ")
                customer = Customer()
                customer.transferMoney(sender_account, receiver_account, amount)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")

    # Preview customer details as a staff
    def previewDetails(self, staff_id, password):
        for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                customer_account = input("Enter customer account number: ")
                customer = Customer()
                customer.viewUserDetail(customer_account)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")

    def withdrawal(self, staff_id, password):
        for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                customer_account = input("Enter customer account number: ")
                amount = float(input("Enter amount to be withdrawn: "))
                customer = Customer()
                customer.withdrawMoney(customer_account, amount)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")

    # Retrict customer account access as a staff
    def restrict_account_access(self, staff_id, password):
        for staff_user in staff:
            if staff_user["id"] == staff_id and staff_user["password"] == password:
                customer_account = input("Enter customer account number: ")
                customer = Customer()
                customer.accountRestriction(customer_account)
            elif staff_user["id"] != staff_id and staff_user["password"] != password and staff [-1] == staff_user:
                print("Incorrect login credentials")

class Manager:
    # Create staff as a manager
    def createStaff(self, username, password):
        if username == manager["username"] and password == manager["password"]:
            new_staff = Staff()
            staff_name = input("Enter staff name: ")
            staff_id = input("Enter staff id: ")
            email = input("Enter staff email address: ")
            phone = input("Enter staff phone number: ")
            home_address = input("Enter staff home address: ")
            password = input("Enter staff password: ")
            new_staff.addStaff(staff_name, staff_id, email, phone, home_address, password)
        else:
            print("Incorrect login credentials")

    # Method for manager to restrict customer account
    def restrict_customer_access(self, username, password):
        if username == manager["username"] and password == manager["password"]:
            customer = Customer()
            account_number = input("Enter the customer account to be restrcted: ")
            customer.accountRestriction(account_number)
        else:
            print("Incorrect login credentials")
            
    # Method for manager to delete customers account
    def delete_customer_account(self, username, password):
        if username == manager["username"] and password == manager["password"]:
            customer = Customer()
            account_number = input("Enter the customer account to be deleted: ")
            customer.deleteCustomer(account_number)
        else:
            print("Incorrect login credentials")

    # Method for manager to view customers details
    def view_customers(self, username, password):
        if username == manager["username"] and password == manager["password"]:
            customer = Customer()
            account_number = input("Enter the customer account to be deleted: ")
            customer.viewUserDetail(account_number)
        else:
            print("Incorrect login credentials.")

# Main App
class MainApp:
    def __init__(self):
        pass
    def appMenu(self):
        print("Wellcome to Memic Bank App")
        print("What do you want to perform?")
        print("1. Create Account for Customer as a staff.")
        print("2. Deposit Money as a Staff.")
        print("3. Withdraw Money as a Staff.")
        print("4. Transer Money as a Customer.")
        print("5. Transer Money as a Staff.")
        print("6. Update Account Details.")
        print("7. View Customer Details as a Staff.")
        print("8. View Customer Details as a Bank Manager.")
        print("9. Restrict Account Access as a Staff.")
        print("10. Restrict Account Access as a Bank Manager.")
        print("11. Delete Customer Account as a Bank Manager.")
        print("12. Add staff as a Manager.")

    def startApp(self):
        self.appMenu()
        staffObj = Staff()
        customerObj = Customer()
        managerObj = Manager()
        while True:
            choice = input("Enter a number between 1 and 12: ")
            match choice:
                case "1":
                    staffId = input("Enter your Staff ID: ")
                    staffPassword = input("Enter your Password: ")
                    staffObj.createAccountForCustomer(staffId, staffPassword)
                case "2":
                    staff_id = input("Enter your Staff ID: ")
                    password = input("Enter your Password: ")
                    staffObj.depositForCustomer(staff_id, password)
                case "3":
                    staffId = input("Enter your Staff ID: ")
                    staffPassword = input("Enter your Log in Password: ")
                    staffObj.withdrawal(staffId, staffPassword)
                case "4":
                    sender = input("Enter sender account: ")
                    reciever = input("Enter receiver account: ")
                    amount = input("Enter amount to be transfered: ")
                    customerObj.transferMoney(sender, reciever, amount)
                case "5":
                    staffId = input("Enter your Staff ID: ")
                    staffPassword = input("Enter your Log in Password: ")
                    staffObj.transfer(staffId, staffPassword)
                case "6":
                    print("What do you want to update?")
                    print("1. Email Address")
                    print("2. Phone Number")
                    print("3. Both")
                    updateChoice = input("Enter 1 for Email, 2 for Phone Number, 3 for both.")
                    match updateChoice:
                        case "1":
                            email = input("Enter your new Email: ")
                            customerObj.updateDetails({"email" : email})
                        case "2":
                            phone = input("Enter your new Phone Number: ")
                            customerObj.updateDetails({"phone_number" : phone})
                        case "3":
                            email = input("Enter your new Email: ")
                            phone = input("Enter your  new Phone Number: ")
                            customerObj.updateDetails({"email" : email}, {"phone_number" : phone})
                case "7":
                    staffId = input("Enter your Staff ID: ")
                    staffPassword = input("Enter your Log in Password: ")
                    staffObj.previewDetails(staffId, staffPassword)
                case "8":
                    username = input("Enter login username: ")
                    password = input("Enter your Log in Password: ")
                    managerObj.view_customers(username, password)
                case "9":
                    staffId = input("Enter your Staff ID: ")
                    staffPassword = input("Enter your Log in Password: ")
                    staffObj.restrict_account_access(staffId, staffPassword)
                case "10":
                    username = input("Enter login username: ")
                    password = input("Enter your Log in Password: ")
                    managerObj.restrict_customer_access(username, password)
                case "11":
                    username = input("Enter login username: ")
                    password = input("Enter your Log in Password: ")
                    managerObj.delete_customer_account(username, password)
                case "12":
                    username = input("Enter login username: ")
                    password = input("Enter your Log in Password: ")
                    managerObj.createStaff(username, password)

# To start the application
# 1. craete instance of MainApp class:
App = MainApp()

# 2. Invoke the startApp method to begin
App.startApp()