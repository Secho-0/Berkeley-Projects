#####
#Farenheit to Celsius Converter
#####
x = True
def c_to_f(tempc):
  f = float(tempc)*1.8+32 #convert C to F
  return f
def f_to_c(tempf):
  c = (float(tempf)-32)/1.8
  return c
while x == True:
  choice = input("Would you like to convert (F)ahrenheit or (C)elsius? ")
  if choice.lower() == 'c':
    temp = input("Input Degrees Celsius: ")
    fahrenheit = c_to_f(temp)
    print(temp,"C is %.2fF" % fahrenheit)
  elif choice.lower() == 'f':
    temp = input("Input Degrees Fahrenheit: ")
    celsius = f_to_c(temp)
    print(temp,"F is %.2fC" % celsius)
  elif choice.lower() == 'exit':
    print("Goodbye!")
    x = False
  else:
    print("I don't understand!")
