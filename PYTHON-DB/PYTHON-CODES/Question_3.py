'''
Question 3: Remove all the lines that contain the character 'a' in a file and write it to another file.

require 2 files 1 for input and 1 for output
'''

input_file  , output_file = 'Document.txt', 'emptyTextFile.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        if 'a' not in line and 'A' not in line:
            outfile.write(line)

print(f"Line without 'a' are written to {output_file}")

with open(output_file, 'r') as file:
    for line in file:
        print(f"\nOpen output file : {line}\n")





'''

Description : 

1. File Names:  
   - input_file = 'Document.txt', output_file = 'emptyTextFile.txt': Assign input and output file names.

2. Open Files:  
   - with open(input_file, 'r') as infile, open(output_file, 'w') as outfile: Open input file for reading and output file for writing.

3. Filter Lines:  
   - if 'a' not in line and 'A' not in line: Check if line does not contain `'a'` or 'A'.
   - Write valid lines (without `'a'`) to the output file.

4. Confirmation Message:  
   - print(f"Line without 'a' are written to {output_file}"): Print message after writing to the output file.

5. Read and Print Output:  
   - with open(output_file, 'r') as file: Open the output file for reading.
   - print(f"\nOpen output file : {line}\n"): Print each line from the output file.

'''