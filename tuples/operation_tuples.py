from tuples.sample_tuple import user_activity


mutable_tuple=list(user_activity)
print(mutable_tuple)
mutable_tuple[0]="ddepak"
print(mutable_tuple)
user_activity= tuple(mutable_tuple)
print(user_activity)

act1,act2,act3=user_activity
print(act1)