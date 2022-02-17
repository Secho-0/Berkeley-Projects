#Question 1

text = "this is an arbitrary text string"

def str_to_int(text):
    try:
        text = int(text)
    except ValueError as msg:
        print("Sorry Can't convert this string :( \n",msg)
        text = input("Enter a new String:  ")
        text = str_to_int(text)
    return text

text = str_to_int(text)
print(text)
#text = str_to_int(text)
#print(text)
print("-"*15)

#Question 2
user_lines = []
try:
    while True:
        user_input = input("Enter a line:  ")

        print(user_input)
        user_lines.append(user_input)

except KeyboardInterrupt:
    print("\n" + "-"*15 +"\nUser Entries:")
    for line in user_lines:
        print(line.title())
    print("-"*15 + "\nSession ended by user, have a great day :)")
