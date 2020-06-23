# Pig Latin is a language constructed by transforming English words. 
# While the origins of the language are unknown, it is mentioned in at least two documents 
# from the nineteenth century, suggesting that it has existed for more than 100 years. 
# The following rules are used to translate English into Pig Latin:
# If the word begins with a consonant (including y), then all letters at the beginning of the word, 
# up to the 
# first vowel (excluding y), are removed and then added to the end of the word, followed by ay. 
# For example, computer becomes omputercay and think becomes inkthay.

# If the word begins with a vowel (not including y), then way is added to the end of the word. 
# For example, algorithm becomes algorithmway and office becomes officeway.

# Write a program that reads a line of text from the user. 
# Then your program should translate the line into Pig Latin and display the result. 
# You may assume that the string entered by the user only contains lowercase letters and spaces.

# Initialize two lists: one containing consonants and one containing vowels
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
#######################
ay = "ay" # For concatenation
way = "way"# For concatenation
piglatin = [] # list to hold the converted values of input string

words = input("Please enter a word or phrase: ") #ask user for string to convert 
wordsList = words.split() # Split the string input from user into parts in a list

for word in wordsList: # Iterate through the words from User string and apply Pig Latin Rules
    if word[:1] in consonants:
        wordLength = len(word)
        removeLetters = word[1:wordLength]
        pigword = removeLetters + word[:1] + ay
        piglatin.append(pigword)
    elif word[:1] in vowels:
        wordLength = len(word)
        pigword = word + way
        piglatin.append(pigword)

format_list = ["{} " for item in piglatin] # Initial formatting to contain all values from piglatin

pigLatinString = " ".join(format_list).format(*piglatin) # join all values in piglatin as a string

print(pigLatinString) # print the result

