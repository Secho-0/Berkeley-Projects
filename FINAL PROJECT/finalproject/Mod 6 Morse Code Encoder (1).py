#module imports
import RPi.GPIO as GPIO
import time

#RPi GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

#variable and list definition
greeting = input("What phrase would you like to convert to Morse?\n>")
morse_dict = {'a':'.-', 'b':'-....', 'c':'-.-.',
              'd':'-..', 'e':'.', 'f':'..-.',
              'g':'--.', 'h':'....', 'i':'..',
              'j':'.---', 'k':'-.-', 'l':'.-..',
              'm':'--', 'n':'-.', 'o':'---',
              'p':'.--.', 'q':'--.-', 'r':'.-.',
              's':'...', 't':'-', 'u':'..-',
              'v':'...-', 'w':'.--', 'x':'-..-',
              'y':'-.--', 'z':'--..',}

#convert greeting into morse code
def encode(message):
    encoded_message = ''
    for l in message:
        if l != " ":
            encoded_message += morse_dict[l.lower()] + " "
            print(l,":",morse_dict[l.lower()])
        else:
            encoded_message += "_"
            print(" ")
    return encoded_message
        

#blink the light
def blink(encoded_message):
    d_word = ''
    for d in encoded_message:
        d_word += d         # used to display whole string as light is flashing 
        if d == ".":        #if . blink for 1s
            GPIO.output(11,True)
            time.sleep(0.5)
            print(d)        #print as close to simultaneously as I could conceive for
            GPIO.output(11,False)
            time.sleep(0.5)
        elif d == "-":      #if - blink for 2s
            GPIO.output(11,True)
            time.sleep(1)
            print(d)
            GPIO.output(11,False)
            time.sleep(0.5)
        else:               #if "  " sleep for 2s, 2s between letters, 4s between words
            GPIO.output(11,False)
            time.sleep(1)
            print("_")      # used _ to indicate spaces in console during 'typing'
            print(">>", d_word,"\n")

#main body
encoded_greeting = encode(greeting)
blink(encoded_greeting)

#error checking prints        
print('_'*15,'\n', greeting)         # print original greeting 
print(encoded_greeting) # print converted greeting

        
