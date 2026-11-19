sample_tuple=(1,2,3,4,"string")
print(sample_tuple[3])  ## tuples are immutabe so tuples used only for this purpose
#user activity cannot not change
user_activity= ("clicked button 1", "clicked button 2", "clicked button 3")
print(user_activity[-1])
    #also slicing also can done on this
print(user_activity[0:2])


for elementi in user_activity:
    print(elementi)


    
for i in range(0,len(user_activity)):
    print(user_activity[i])