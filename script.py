def get_data(f):
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0

    for x in f:
        number_of_lines += 1
        number_of_characters += len(x)
        words = x.split()
        number_of_words += len(words)

    return number_of_lines, number_of_words, number_of_characters


with open(input("Enter in a file name here:")) as f:
    number_of_lines, number_of_words, number_of_characters = get_data(f)


print (f"Hello User!")
print(f"After opening your file we found that you have,")
print(f"{number_of_lines} lines of data in your file.")
print(f"You also have {number_of_words} words in your file,")
print(f"That is {number_of_characters} characters!")

f.close()
