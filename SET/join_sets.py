p1= {"chips", "bottle","milk"}
p2={"apples","bananas"}
p3={"milk","mangos","bananas"}
combined = p1.union(p2)
print(combined)

combined =p1|p2|p3

print(combined)

# for above we also have a function called as union
combined_list_union=p1.union(p2)
print(combined_list_union)
combined_list2= p1.union(p2,p3)
print(combined_list2)