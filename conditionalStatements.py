# If Statement
day=2
if day==3:
    print("Welcome to Wednesday!")

    # If else Statement
day=2
if day==3:
    print("Welcome to Wednesday!")
else:
    print("Today is not Wednesdsy! Come another day!")

    # If elif Statement
day=2
if day==0:
    print("Welcome to Sunday!")
elif day ==1:
    print("Happy Monday!")
elif day ==2:
    print("Make a positive Tuesday!")
elif day ==3:
    print("Yes! It's Wednesday!")
elif day ==4:
    print("Almost there, It's Thursday!")
elif day ==5:
    print("We are heading to the weekend!")
else:
    print("It's the weekend!!")

# Match Statement
day=2
match day:
    case 0:
        print("Welcome to Sunday!")
    case 1:
        print("Welcome to Monday!")
    case 2:
        print("Welcome to Tuesday!")
    case 3:
        print("Welcome to Wednesday!")
    case 4:
        print("Welcome to Thursday!")
    case 5:
        print("Welcome to Friday!")
    case _:
        print("Welcome to Saturday!")

# Using multiple inputs in case
day=2
match day:
    case 0| 2| 3| 4:
        print("Weekday Greetings!")
    case 5:
        print("Heding to the Weekends!")
    case 6| 0:
        print("It's the Weekends!")
    case _:
        print("Happy Weekends!")

# Input Function
day=int(input("Enter a number between 0 and 6:")) # Use of int to read the int.
match day:
    case 0| 2| 3| 4:
        print("Weekday Greetings!")
    case 5:
        print("Heding to the Weekends!")
    case 6| 0:
        print("It's the Weekends!")
    case _:
        print("Happy Weekends!")


