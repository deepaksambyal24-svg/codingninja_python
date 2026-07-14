# simple or single inheritance
#multiple ineheritance
# multilevel inheritance
from OOP.inhertance.inheritance_constructors import employee


# single
class person:
    def __init__(self,name,age)->None:
        self._name = name
        self._age = age
    class employee:
        def __init__(self,name,empcode)->None:
            super().__init__(name)
            self._empcode = empcode

# multiple inheritance
class father:
    def __init__(self,name,age)->None:
        self.fathername = name
class mother:
    def __init__(self,name)->None:
        self.mothername = name
class son(father,mother):
    def __init__(self,fathername,mothername,name)->None:
        father.__init__(self,fathername)
        mother.__init__(self,mothername)
        self.name = name

son=son("a","b","c")
print(son.name,son.fathername,son.mothername)


# multilevel inheritance
 class person:
     def __init__(self,name)->None:
         self.name = name
class crickter(person):
    def __init__(self,name,matchesplayed)->None:
        super().__init__(name)
        self.matchesplayed = matchesplayed

class batsman(crickter):
    def __init__(self,name,matchesplayed,totalruns)->None:
        super().__init__(name,matchesplayed)
        self.totalruns = totalruns
batsman=batsman("batman",1000,2000)
print(f'{batsman.name}has played {batsman.matchesplayed}and scored {batsman.totalruns}')
