def func(p, q, r):
    global s
    p = 10
    q = 20
    r = 30
    s = 40


p, q, r, s = 1, 2, 3, 4
func(5, 10, 15)
print(p, q, r, s)