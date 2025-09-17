
'''
4. Demonstrate:5
    a. Use of tell() to get the current file pointer.
    b. Use of seek() to move the pointer and read data from a specific position.
'''


def demonstrate_tell_and_seek():
    """
    Demonstrates the use of tell() and seek() in a single function.
    """
    file_name = "example.txt"
    sample_text = "Hello, this is a sample text for demonstration."

    # Step 1: Create and write to a new file
    with open(file_name, "w") as file:
        file.write(sample_text)
    print(f"File '{file_name}' created with content: '{sample_text}'")
    print("-" * 30)

    # Step 2: Open the file for reading and demonstrate tell() and seek()
    with open(file_name, "r") as file:
        # a. Use of tell()
        initial_position = file.tell()
        print(f"Initial file pointer position: {initial_position} bytes")

        # Read the first 7 characters
        content_read = file.read(7)
        print(f"Read 7 characters: '{content_read}'")

        # Get the new position using tell()
        current_position = file.tell()
        print(f"Current file pointer position after reading: {current_position} bytes")
        print("-" * 30)

        # b. Use of seek()
        # Move the pointer to a specific position (e.g., 10th byte)
        file.seek(10)
        print(f"Moved file pointer to byte 10.")

        # Read from the new position
        content_after_seek = file.read(5)
        print(f"Read 5 characters from the new position: '{content_after_seek}'")

        # Move the pointer back to the beginning (0th byte)
        file.seek(0)
        print("Moved file pointer back to the beginning.")

        # Read the entire file from the start
        full_content = file.read()
        print(f"Read the entire content from the beginning: '{full_content}'")
        print("-" * 30)

    print("Demonstration complete.")

demonstrate_tell_and_seek()