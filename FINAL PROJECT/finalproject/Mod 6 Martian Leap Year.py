#Calculate if a year is a leap year
#Leap years are divisible by 4 but not 100
#If a year is divisible by both it must also
#be divisible by 400

year = ""

while year !='quit':
    year = input("Enter a Year or type Quit:\n >") 
    if year.isnumeric():
        year = int(year)
        if year%10 == 0:
            print(year," is a leap year.\n",
                  year," is divisible by 10.")

        elif year%2 == 0:
            print(year," is not a leap year.\n",
                  year," is an even number, not divisible by 10")
        else:
            print(year," is a leap year.\n",
                  year," is an odd number")
    else:
        if year.lower() == 'quit':
            print("Goodbye!")
        else:
            print("Whatcha Sayin? Please Try Again.")
        
