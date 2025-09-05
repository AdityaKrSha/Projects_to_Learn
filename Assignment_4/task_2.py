try:
    data = input("Enter some text to write to the file: ")
    file = open("output.txt", "w")
    file.write(data + "\n")
    file.close()

    more_data = input("Enter additional text to append: ")
    file = open("output.txt", "a")
    file.write(more_data + "\n")
    file.close()

    file = open("output.txt", "r")
    read_file = file.read()
    print("\nFinal content of output.txt:")
    print(read_file)
    file.close()

except FileNotFoundError:
    print("The file 'output.txt' was not found.")
