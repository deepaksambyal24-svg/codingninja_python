p1={'chips','bottle '}
p2={'apple','banana'}
combined=p1|p2
print(combined)

print(type(combined))
p3={'milk'}
combined=p1|p2|p3
print(combined)
print(type(combined))
# pipe and union are all same


# UNION FUNCTION ---- give all the unique element combined from both sets  combines all set give unique element
# from all set


combined_list1=p1.union(p2)
print(combined_list1)

mul_combine_union=p1.union(p2,p3    )
print(mul_combine_union)

