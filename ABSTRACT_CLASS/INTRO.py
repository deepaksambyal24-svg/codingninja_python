#Abstract class and methods in this base class direct the derived classt to define some methods
#so it dont not throw an error
from abc import ABC, abstractmethod
class bird(ABC):
    @abstractmethod
    def fly(self):
        pass
    ## derived class throw an eror your don overwirete the abstract method
    # it is mendotory to enforce the abstract method
class sparrow(bird):
    def fly(self):
        pass
