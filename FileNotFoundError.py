try:
    file = open("asap_file.txt","r")
    data = file.read()
    file.close()
    print(data)
except FileNotFoundError:
    print("Error: The file 'asap_file.txt' does not exist!")