# method resolution order
class a:
    def __init__(self)->None:
        pass
    def f(self):
        print(f'for a is called')
class b:
    def f(self):
        print(f'b is called')
class c(a):
    pass
class d(c,b):
    pass
d=d()
d.f()
d.f()
