# Write your code here
def char_ext(s,positions):
    print(type(s))
    print(type(positions))

s="abcdefgh"
positions="0 2 4 6"
ans=""
positions =input().split()
for ind in positions:
    ind_n=int(ind)
    ans+=(s[ind_n])
print(ans)