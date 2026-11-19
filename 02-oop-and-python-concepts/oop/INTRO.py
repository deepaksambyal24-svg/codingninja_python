class Student:
    def __init__(self)->None:
        self.name=""
        self.score=[]
        self.address=""
    def setName(self,name):
        self.name=name
    def addScore(self,score):
        self.score.append(score)
    def setAddress(self,address):
        self.address=address
# these all are setters
    def calculateCGP(self):
        total=0
        for i in self.score:
             total+=i
        return total/len(self.score)
studentA=Student()
studentB=Student()
studentC=Student()
studentA.setName("deepak")
studentB.setName("soham")
studentC.setName("deep")

studentA.addScore(100)
studentB.addScore(90)
studentC.addScore(80)
print(studentA.calculateCGP())