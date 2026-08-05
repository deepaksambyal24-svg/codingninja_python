user_activity=("clicked button 1","clicked button 2")
print(user_activity)
# tuple support indexing  and also support negative indexing
print(user_activity[::-1])
for i in range(0,len(user_activity)):
    print(user_activity[i])

for ele in user_activity:
    print(ele)

