try:
    file = open("sample.txt", "r")

    read_file = file.read()
    print(read_file)
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
