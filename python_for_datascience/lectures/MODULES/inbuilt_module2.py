import os
print(os.getcwd())
print(os.listdir())
#print(os.mkdir('name'))
#print(os.rename('name','name2'))
#print(os.remove('name'))
#os.rmdir('name')# remove directory

# BUSINESS USE CASE ---automate a monthly report folder
folder='aug_2026_report '
if not os.path.exists(folder):
    os.mkdir(folder)
print(os.listdir())

# to check available business files

files =os.listdir()
print('available files ')
for file in files:
    print(file)

#print(os.rename('aug_2026_report','aug_2026_rep'))
print(os.listdir())