ist=list(map(str,input().split()))
str=""
for i in range(len(ist)-2,len(ist)+1):
     print(ist[i:len(ist)][::-1],end="")
