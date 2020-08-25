import json #importing the standard json module
import difflib # allows to compare text values

data=json.load(open("data.json")) #load and read the json file data.json and save it into data varaible

def getDefinition(word):
    word = word.lower() #change to lower case to eliminate errors with mixed case input
    if word in data:
        return data[word]
    else:
        return "Word not found please check the spelling"


enteredWord = input("Please enter a word:") # ask the user to enter a word and save it in a varaible


print(getDefinition(enteredWord)) # call the function getDefinition with enterWord as a parameter to find out what the word means
