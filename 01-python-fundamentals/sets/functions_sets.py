#add
#remove
#UNION GIVE all the elements from both sets
p1={"chips","bottle","milk"}
p2={"bottle","butter","bottle","apples"}
print(p1.intersection(p2))
# to find only the unique element
print(p1.difference(p2))
print(p2.difference(p1))
s ={1,2,3,4}
s.clear()
s.discard(3)
print(s)