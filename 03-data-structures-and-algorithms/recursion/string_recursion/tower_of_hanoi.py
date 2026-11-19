def tower_hanoi(n,a,b,c):
    if n==1:
        print("move ist disk from " ,a, "to",c)
        return
    tower_hanoi(n-1,a,c,b)
    print("move",n,"th disk from " ,a,"to",c)
    tower_hanoi(n-1,b,a,c)
