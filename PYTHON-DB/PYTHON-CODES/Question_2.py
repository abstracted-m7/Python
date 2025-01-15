# Question 2: Read a text file and display the number of vowels/constants/uppercase/lowercase characters in the file.


file_name = 'Document.txt'

#intialize all variable = 0
vowels = consonants = uppercase = lowercase = spacial_char = 0

#create a set for vowels and consonants
vowel_set = set("AEIOUaeiou")
consonant_set = set("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")

#open the file and process it
with open(file_name, 'r') as file:
    for line in file:
        print(line)
        for char in line:
                if char in vowel_set:
                    vowels += 1
                elif char in consonant_set:
                    consonants += 1
                elif char not in vowel_set and consonant_set:
                     spacial_char += 1

                if char.isupper():
                    uppercase += 1
                elif char.islower():
                    lowercase += 1

#display the results
print(f"\n\nTotal Vowels: {vowels}")
print(f"Total Consonants: {consonants}")
print(f"Total uppercase characters: {uppercase}")
print(f"Total lowercase characters: {lowercase}")
print(f"Total spacial characters: {spacial_char}")




'''
Describe the code:

1. File Name: Assign file name `Document.txt`.  
2. Initialize Counters: Set all counters (`vowels`, `consonants`, etc.) to 0.  
3. Define Sets: Use sets for vowels and consonants.  
4. Open File: Open the file in read mode.  
5. Process Characters: Check if each character is a vowel, consonant, special, uppercase, or lowercase and increment respective counters.  
6. Display Results: Print total counts of vowels, consonants, uppercase, lowercase, and special characters.  
'''