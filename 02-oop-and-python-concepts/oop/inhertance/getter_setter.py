class person:
    def __init__(self,name)->None:
        self.name = name
    def print_info(self):
        print(f"person's name is {self.name}")
class Student(person):
    def __init__(self,rank,name)->None:
        self.rank = rank
        super().__init__(name)
    def print_info(self):
        super().print_info()                # this super () function call the print_info from base class
        print(f"student rank is {self.rank}")

student = Student(1,"ram")
student.print_info()


# getter
  class Account:
      def __init__(self,balance):
          self.balance = balance
  account1 = Account(100)
  print(account1.balance)
  account1.balance = 200
  print(account1.balance)       # account balance get updated


# how to create a getter
 class account:
     def __init__(self,balance)->None:
         self._balance = balance    # variable name should be different
     @property
     def balance(self):
         return self._balance
     # setter
     @balance.setter
     def balance(self,new_balance):
         if new_balance >=0:
            self._balance = new_balance

