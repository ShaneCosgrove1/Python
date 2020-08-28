import mysql.connector # import sql connector

con = mysql.connector.connect( ##connecting to database
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor() ##needed to search the database
word = input("Enter a word: ")#ask user for input
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word) #writing and calling sql query
results = cursor.fetchall() #getting the results

if results: #if query comes back with a result
    for results in results: #puts each def on a new line
        print(results[1]) #the one will print out the defination and not the expression(entered word)
else:
    print("No Word Found")