#Write a program that counts the number of vowel in a sentence.
def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    vowel_count = 0
    
    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1
    
    return vowel_count

input_sentence = input("Enter a sentence: ")
num_vowels = count_vowels(input_sentence)
print("Number of vowels in the sentence:", num_vowels)
