## Question 1
text = "this is an arbitrary text string"

def str_to_int(text):
    """Converts a string to an integer, asks for reinput if ValueError occurs"""
    try:
        text = int(text)
    except ValueError as msg:
        print("Sorry Can't convert this string :( \n",msg)
        text = input("Enter a new String:  ")
        text = str_to_int(text)
    return text

# attempt to convert the string, will return a value error to demonstrate try/except
text = str_to_int(text)
print(text)
#text = str_to_int(text)
#print(text)
print("-"*15)

## Question 2
user_lines = []

try:
    # enter an infinite loop
    while True:
        # ask and spit out a user entered line 
        user_input = input("Enter a line:  ")

        print(user_input)
        user_lines.append(user_input)

# exit loop via the Keyboard Interrupt (Ctrl+C)
except KeyboardInterrupt:
    # return each line on exit 
    print("\n" + "-"*15 +"\nUser Entries:")
    for line in user_lines:
        print(line.title())
    # say goodbye
    print("-"*15 + "\nSession ended by user, have a great day :)")
