#Program to validate username by A00206086
#input username
username = input("Enter a username: ")

#check length is not  between 4-8
if not 4 <= len(username) <= 8:
    print("Username must be between 4-8 characters") 
#check if first letter is not lower
elif not username[0].islower():
    print("Username must start with a lower case letter")
#check if username is not alnum
elif not username.isalnum():
    print("Username must only contain  alphanumeric characters")
else:
    print(username," is valid")
    
    

    