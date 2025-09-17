
'''
2. Open a file in different modes (r, w, a, r+) and print file attributes like:
    a. name, mode, closed, readable(), writable().
'''


file_name = 'opr.txt'


modes = ['r', 'w', 'a', 'r+']

for mode in modes:
    print(f"\nOpening file in mode '{mode}':")
    file = open(file_name, mode)

    print(f"Name: {file.name}")
    print(f"Mode: {file.mode}")
    print(f"Closed: {file.closed}")
    print(f"Readable: {file.readable()}")
    print(f"Writable: {file.writable()}")

    file.close()
    print(f"Closed after closing: {file.closed}")
