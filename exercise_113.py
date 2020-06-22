# When writing out a list of items in English, one normally separates the items with commas. 
# In addition, the word “and” is normally included before the last item, 
# unless the list only contains one item. Consider the following four lists:

# apples

# apples and oranges

# apples, oranges and bananas

# apples, oranges, bananas and lemons

# Write a function that takes a list of strings as its only parameter. 
# Your function should return a string that contains all of the items in the list formatted in the manner 
# described previously as its only result. 
# While the examples shown previously only include lists containing four elements or less, 
# your function should behave correctly for lists of any length. 
# Include a main program that reads several items from the user, formats them by calling your function, 
# and then displays the result returned by the function.
run = ["Apples", "Oranges", "Bananas", "Pineapple", "Turtle", "Chocolate"] # List with more than two strings
double = ["apples", "oranges"] # List with only two strings
single = ["Apple"] #single item list
def formatString(stringList):
    count = len(stringList) # Declare variable to see how many items in list
    if count > 2: # Determine wheter there are more than two strings in list
        format_list = ["{}, " for item in stringList[:count-1]] # Initial formatting for all values before last value in list
        lastval = ["and {}" for val in stringList[count-1:count]] # Collects and formats last value
        blankString = "".join(format_list + lastval).format(*stringList) # Combine and join formatted strings
        
    elif count == 2: # Checks to see if there are two values in list
        blankString = " and ".join(stringList) # simple join with minimal formatting
    elif count <= 1: # Check to see if list has only one value or is empty
        blankString = "".join(stringList) #simple formatting
    return blankString #returns concatenated and formatted string when function is called

print(formatString(single))
print(formatString(double))
print(formatString(run))

