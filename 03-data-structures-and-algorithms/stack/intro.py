# stack is data structure , it has storage,mechanisms to prepare restriction that people can access only top of
## of data structure
# push - toadd data
#pop operation - delete the data
## apppend function is use fto push the element

class Stack:
        def __init__(self):
            self.__arr=[]       # by using two underscore arr make it private
            self.__top= None        # so it can not be accessed   it is called private variable
    ## by private vairalbe we cannot access it direnctly we have to create the funtion to access
        def push(self,data):
           # dump the date in the array
            self.__arr.append(data)   # add the element to the very last of the array


          # update the top to point to the last index
            self.__top = len(self.__arr)-1

        def peek(self):

           if self.__top==None:
               return ("stack is empty")
           value = self.__arr[self.__top]
           return value

    # st = Stack()
    # print(st.arr)


st=Stack()
st.push(22)
st.push(19)

    # 11->19->5(top)

v=st.peek()
print(v)