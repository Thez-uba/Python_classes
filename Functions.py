def myFirstFunction():
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

# Calling the abov function
myFirstFunction()

# Function to sum two number
def sumNumbers():
    a= 25
    b= 67
    print("Sum of a and b is: ", a+b)
sumNumbers()

# Using parameters & Arguements
def sumNumbers2(a, b):
    # a=int(input("Enter a first number:"))
    # b=int(input("Enter a second number:"))
    print("Sum of a and b is: ", a+b)
sumNumbers2(45, 89)
sumNumbers2(34, 12)

#  Using Keyword Argument
def sumNumbers2(a, b):
    # a=int(input("Enter a first number:"))
    # b=int(input("Enter a second number:"))
    print("Sum of a and b is: ", a+b)
sumNumbers2(b=45, a=89)
sumNumbers2(34, 12)

# Inputing the values
# def sumNumbers1():
#     a=int(input("Enter a first number:"))
#     b=int(input("Enter a second number:"))
#     print("Sum of a and b is: ", a+b)
# sumNumbers1()

# Function to find the difference of two numbers with a 'return' Statement
def diffOfNumbers(a, b):
    return a-b
    print("A - B is: ", a-b)
# Call the diffOfNumbers above
print(diffOfNumbers(56, 78))

# Arbitrary Arguments
# Function to accept names of studennts and print them
def studentsNames(*students):
    for student in students:
        if student=="Adam":
            print(student)
        else:
            pass

studentsNames("Jude", "Mike", "Rosemary", "Adam")

# Exercise
student_records=[
    {
    "name":"Student A",
    "courses":[
        {
        "title":"Intro to Programming",
        "mark": 76
    },
    {
        "title":"Data Analysis",
        "mark": 81
    }
    ],
    "totalMarks": 107
},
{
    "name":"student B",
    "courses":[{
        "title":"Intro to Programming",
        "mark": 50
    },
    {
        "title":"Data Analysis",
        "mark":81
    }
    ],
    "totalMarks":90
}
]

def findHeightScore(records):
    for student in records:
        if student["totalMarks"]>80:
            print(student["name"], student["totalMarks"])
        else:
            pass

findHeightScore(student_records)

# Assignment
# To print the total mark of each student
student_records=[
    {
    "name":"Student A",
    "courses":[
        {
        "title":"Intro to Programming",
        "mark": 100
    },
    {
        "title":"Data Analysis",
        "mark": 100
    }
    ],
},
{
    "name":"student B",
    "courses":[{
        "title":"Intro to Programming",
        "mark": 82
    },
    {
        "title":"Data Analysis",
        "mark":79
    }
    ]
},
{
    "name":"student C",
    "courses":[{
        "title":"Intro to Programming",
        "mark": 50
    },
    {
        "title":"Data Analysis",
        "mark":81
    }
    ]
},
{
    "name":"student D",
    "courses":[{
        "title":"Intro to Programming",
        "mark": 57
    },
    {
        "title":"Data Analysis",
        "mark": 54
    }
    ]
},
{
    "name":"student E",
    "courses":[{
        "title":"Intro to Programming",
        "mark": 39
    },
    {
        "title":"Data Analysis",
        "mark": 58
    }
    ]
}
]

def totalMarks(records):
    for student in records:
        total = 0
        for course in student['courses']:
            total+=course["mark"]
        if total> 80:    
            print(student["name"] +" totalMark: " + str(total))
        else:
            pass   

totalMarks(student_records)

# Assignment: 
# Determine the grade of the student according to the aggregate
# If the aggregate is > 100, the grade will be outstandin'.
# If < 100 & > 80, very good.
# If <= 80 & > 60, credit.
# If <= 60 & > 49, pass.
# If < 50 fail.
# Grade according to aggregate and not total score
# Total marks divided by the number of courses

def grade_by_aggregate(records):
    for student in records:
        total = 0
        num_courses = len(student['courses'])
        
        for course in student['courses']:
            total += course["mark"]
        
        aggregate = total / num_courses
        
        if aggregate >= 100:
            grade = "Outstanding"
        elif 80 < aggregate < 100:
            grade = "Very Good"
        elif 60 < aggregate <= 80:
            grade = "Credit"
        elif 49 < aggregate <= 60:
            grade = "Pass"
        else:
            grade = "Fail"
        
        print(student['name'] + " - Aggregate: " + str(round(aggregate, 2)) + ", Grade: " + grade)

grade_by_aggregate(student_records)

