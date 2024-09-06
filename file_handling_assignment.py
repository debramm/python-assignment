

# Task 1: File Creation and Writing
try:
    # Create a new file in write mode and write some content
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is line 1.\n")
        file.write("The number is: 1234\n")
        file.write("Goodbye, this is line 3.\n")
    print("File created and initial content written successfully.")
    
    # Task 2: File Reading and Display
    with open("my_file.txt", 'r') as file:
        print("\nReading contents of 'my_file.txt':")
        content = file.read()
        print(content)

    # Task 3: File Appending
    with open("my_file.txt", 'a') as file:
        file.write("This is an appended line 4.\n")
        file.write("Another number: 5678\n")
        file.write("Final goodbye, this is line 6.\n")
    print("Additional lines appended successfully.")

    # Reading the file again after appending
    with open("my_file.txt", 'r') as file:
        print("\nContents of 'my_file.txt' after appending:")
        content = file.read()
        print(content)

# Task 4: Error Handling
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
