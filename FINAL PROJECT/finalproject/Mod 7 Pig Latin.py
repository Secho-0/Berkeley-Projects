##
# List of Vowels
##
vowels = ('a','e','i','o','u')

##
# Convert Word
##
def word_to_pigword(word):
    pigword = ''
    if word[0].lower() in vowels:
        pigword = word + 'yay'
    else:
        while word[0].lower() not in vowels:
            word = word[1:] + word[0]
        pigword = word + 'ay'
    return pigword
##
# Split + Reform Sentence
##
def sentence_to_pigwords(sentence):
    original_words = sentence.split(' ')
    pig_sentence = ''
    for word in original_words:
        pig_sentence = pig_sentence + word_to_pigword(word)
        pig_sentence = pig_sentence + ' '
    return pig_sentence
    
print("Enter 'quit' to exit.")    
sentence = input("Enter a Sentence to Convert: ").strip()

while sentence.lower() != 'quit':
    pigsentence = sentence_to_pigwords(sentence)
    print(pigsentence)
    sentence = input('Enter a Sentence to Convert:').strip()
