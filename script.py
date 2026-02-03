
def get_data(f):
    # Sets local variables to look through the given file and then returns the values found.
    # When called must have three areas to store values in!
    # Pass in the file as parameter.
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0

    for x in f:
        number_of_lines += 1
        number_of_characters += len(x)
        words = x.split()
        number_of_words += len(words)

    return number_of_lines, number_of_words, number_of_characters


File_not_read = True # Flag for failure to read file

while File_not_read:
    try:
        with open(input("Enter in a file name here:")) as f:
            number_of_lines, number_of_words, number_of_characters = get_data(f)
    except:
        print("Error: The file either doesn't exist or cannot be read :(, please try again")
    else:
        print(f"Hello User!")
        print(f"After opening your file we found that you have,")
        print(f"{number_of_lines} lines of data in your file.")
        print(f"You also have {number_of_words} words in your file,")
        print(f"That is {number_of_characters} characters!")
        break

f.close()
