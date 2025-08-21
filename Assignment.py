# Assignment 1
def count_character(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    print(count)
count_character("This is to count string occurance", "i") 


# Assignment 2
def second_highest(numbers):
    if len(numbers) < 2: # If the list has fewer than 2 elements, there can’t be a second highest number.
        print("List must have at least two unique numbers.")
        return

    uni_numbers = list(set(numbers)) # Set(numbers) to remove duplicates... Then list to convert it back to a list to sort it.
    uni_numbers.sort(reverse=True) # Sort the list from highest to lowest.

    if len(uni_numbers) < 2:
        print("All numbers are the same...")
    else:
        print(uni_numbers[1]) # Prints second highest number...
second_highest([3]) # Output: List must have at least two unnique number.
second_highest([5, 3, 9, 7, 9])  # Output: 7
second_highest([4, 4, 4])        # Output: All numbers are the same...
