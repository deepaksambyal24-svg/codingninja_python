# hybrid inhertance
class person:
    def __init__(self)->None:
        print("person constructor is called")
class crickter(person):
    def __init__(self)->None:
        super().__init__()
        print("crickter constructor is called")
class batman(crickter):
    def __init__(self)->None:
        super().__init__()
        print("batman constructor is called")