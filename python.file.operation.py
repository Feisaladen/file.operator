try:
    filename = input("Enter the file name: ")

    # Step 1: Write initial content
    with open(filename, "w") as file:
        file.write("hello this is the first version of the file")

    # Step 2: Read file
    with open(filename, "r") as file:
        content = file.read()
        print("Original content:", content)

    # Step 3: Modify the file
    with open(filename, "w") as file:
        file.write("this is an updated file")

    # Step 4: Read modified file
    with open(filename, "r") as file:
        content = file.read()
        print("Updated content:", content)

except FileNotFoundError:
    print("File not found")





