# Write a program that reads numbers from the user until a blank line is entered. 
# Your program should display the average of all of the values entered by the user. 
# Then the program should display all of the below average values, followed by all of the average values (if any), 
# followed by all of the above average values. 
# An appropriate label should be displayed before each list of values.

numList = [] # Contains all values entered by user
average = 0 # Will be used to calculate average
total = 0 # contains total of all values in numList
belowAverage = [] #Will be used to append below average values
averageVals = [] #Will be used to append average values
aboveAverage = [] #Will be used to append above average values

# GetNum function asks user input and only converts to int when an actual value entered
def GetNum():
    userNum = (input("Please enter a number: "))
    if userNum == "":
        return userNum # Returns blank string 
    else:
        userNum = int(userNum) 
        numList.append(userNum)
        return userNum
# While loop that calls GetNum() function and calculates total and average when broken
while GetNum() != "":
    GetNum()
total = sum(numList)  
average = total // (len(numList))

# For loop to evaluate all values in numList and append them in appropriate lists
for x in numList:
    if x == average:
        averageVals.append(x)
    elif x > average:
        aboveAverage.append(x)
    elif x < average:
        belowAverage.append(x)
print(f"Total Average: {average}") # Prints total average
print(f"Below Average Values Entered : {belowAverage}") #Prints Below Average values
print(f"Average Values Entered : {averageVals}") #prints any value that is average from list
print(f"Above Average Values Entered : {aboveAverage}") #Prints above average values



