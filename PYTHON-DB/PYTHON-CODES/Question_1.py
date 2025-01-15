# Question 1: Read a text file line by line and display each word separated by a #.


# Initialize the file name in a variable
file_name = 'Document.txt' 

#open the file and process line by line
with open(file_name, 'r') as file:
    for line in file:
        result = ' # '.join(line.split())
        print(result)



'''
describe the code:
1. Specify File Name: Assign the file name to file_name. Replace 'sample.txt' with your file's name.
2. Open File: Use 'with open()' to open the file in 'read mode'-> ('r').
3. Read Each Line: Loop through each line in the file using 'for line in file'.
4. Split and Join Words: Split the line into words with 'split()' and join them with '#' using 'join()'.
5. Print Result: Output the processed line with words separated by #.
'''