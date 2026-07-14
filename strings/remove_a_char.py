def remove_all_occurance(input_string, char_to_remove):
    result = ""

    for char in input_string:
        if char != char_to_remove:
            result += char

    return result



input_string = input()
char_to_remove = input()  


print(remove_all_occurance(input_string, char_to_remove))