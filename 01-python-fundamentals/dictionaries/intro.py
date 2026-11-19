# it has {} bracket with both key and values and these are imutabel
social_impression = {"linkedin":2000,"fb":5000,"x":7000,"instgram":4000}
print(social_impression)
print(type(social_impression))



#dictionary are mutable  but the keys are immutable
#to create an empty dictionary
dic={}          # or dict()
social_handles={}
social_handles["x"]=5000
social_handles["linkedin"]=6000
print(social_handles.keys())
print(social_handles.items())
print(len(social_handles.items()))
print(social_handles.get("linkedin"))