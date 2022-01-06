#####
#Farenheit to Celsius Converter
#####
ct = 0 #counter for examples provided in Assignment Webpage
while ct <=2: #while counter is less than or equal to 2 keep running, starting at 0
  print("\nWelcome to the Temperature Converter!\n")
  c = input("Enter Degree's Celsius: ") #Ask for Degrees C
  f = float(c)*1.8+32 #Convert C to F
  print(c," Degrees Celsius is ",f," Degrees Fahrenheit") #print message 
  ct += 1 #tick counter
  
#####
# Centimeters to Inches
#####
ct2 = 0 #counter for examples provided in Assignment Webpage
while ct2 <=1: #while counter is less than or equal to 1 keep running, starting at 0
  print("\nWelcome to the UoM Converter!")
  cm = input("Enter Centimeters: ") # Ask for Centimeters
  inch = float(cm)/2.54
  print(cm," Centimeters is %.2f Inches" % inch)
  ct2 +=1 #tick counter
  
#####
# All About Circles (and Spheres!)
## No counter provided as only one example given
#####
print("\nWelcome to All About Circles!\n")
r = input("What's your circles radius in inches ?") #ask for radius in inches
#start calculations
circ = 3.14*float(r)*2
area = 3.14*float(r)**2
sfar = 3.14*float(r)**2*4
volu = 3.14*float(r)**3*(4/3)
#print results
print("\nYour Circles Circumference is: ", circ,
    "\nYour Circles Area is: ", area,
    "\nYour Spheres Surface Area is: ", sfar,
    "\nYour Spheres Volume is: %.2f" % volu)
pause = input("Program Finished")#pause for console windows vs IDLE editor.
