#finding the largest element in the list
marks =[34,65,89,12,45,98,56,57]
max=marks[1]
for elem in marks:
    if elem > max:
        max=elem
    elem+=1
print(max)