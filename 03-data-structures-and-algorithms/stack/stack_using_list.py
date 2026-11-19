class Stack:
        def __init__(self):
            self.__arr=[]
            self.__top= None

        def push(self,data):
            self.__arr.append(data)
            self.__top = len(self.__arr)-1
        def pop(self):
            if self.__top== None:
                print("Stack is empty")
                return
            # to remove the last added element , we can remove our list's last element
            self.__arr.pop()
            # update the value of top to point to the last index
            self.__top=len(self.__arr)-1
            if self.__top==-1:
                self.__top=None
        def peek(self):
           if self.__top==None:
               return ("stack is empty")
           value = self.__arr[self.__top]
           return value



st=Stack()
st.push(22)
st.push(19)



v=st.peek()
print(v)