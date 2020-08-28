import json #importing the standard json module
from difflib import get_close_matches # allows to compare text values

data=json.load(open("data.json")) #load and read the json file data.json and save it into data varaible

def getDefinition(word):
    word = word.lower() #change to lower case to eliminate errors with mixed case input
    if word in data:
        return data[word]
    elif word.title() in data: #if user enters delhi or DELHI it will check for Delhi
        return data[word.title()]
    elif word.upper() in data: #if user enters nato it will change to NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0: # checks if there is a close match by seeing if the item returns lenght is greater than 0 ie not blank
         yn = input("Did you mean %s instead? Enter Y for Yes, Enter N for No " % get_close_matches(word,data.keys())[0]) #asks the user did they mean to type the first item returned by get_close_matches
         if yn =="Y":
            return data[get_close_matches(word,data.keys())[0]]
         elif yn == "N":
            return "The word doesnt exist"
         else: #if user doesnt enter Y or N
            return "We didnt understand your input"
    else:
        return "Word not found please check the spelling"


enteredWord = input("Please enter a word:") # ask the user to enter a word and save it in a varaible
##print(getDefinition(enteredWord))
#Makes output userfrieldly
output = getDefinition(enteredWord) # call the function getDefinition with enterWord as a parameter to find out what the word means

if type(output) == list: #checks if the output is a list
    for item in output: #loops through all the returned list items
        print(item) # prints each item on a seperate line
else:#if not a list
    print(output)

 
