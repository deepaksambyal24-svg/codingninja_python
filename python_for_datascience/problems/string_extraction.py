# Write your code here
input = "C:/Users/JohnDoe/Documents/Report.txt"
file_name_index = input.rfind("/")
file_name = input[file_name_index + 1:]

file_ext_index = file_name.find(".")
file_ext = file_name[file_ext_index:]

reverse = file_name[file_ext_index - 1::-1]
print(f"File Name: {file_name}\n File Extension: {file_ext}\n Reversed Base Name: {reverse}")
