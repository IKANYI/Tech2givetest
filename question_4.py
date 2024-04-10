#Write a program that accepts a strinng as input, capitalizes the first letter of each word in the string and then returns the result string
def capitalizer(sentence):
    char = sentence.split()
    
    capitalized_words = [word.capitalize() for word in char]
    
    result = ' '.join(capitalized_words)
    
    return result

input_string = input("Enter a string: ")
capitalized_char = capitalizer(input_string)
print("Capitalized string:", capitalized_char)
