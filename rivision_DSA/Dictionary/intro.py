# Dictionary --- it is a data type which store the key value pair structure
from DIctionary.intro import social_impression, social_handles

print(social_impression)
print(type(social_impression))

# dictionaries are mutable ie. you can delete or update or modify on same memory location dictionary
#keys are unique and immutable ie. you can not change the key value once it is created but you can change the value of key

# to create empty dictionary
empty_dict=dict()
empty_dict2=social_impression.copy() # to create copy of dictionary
print(social_impression.keys())
print(social_impression.values())
print(len(social_impression.keys()))
print(social_impression.get())
      