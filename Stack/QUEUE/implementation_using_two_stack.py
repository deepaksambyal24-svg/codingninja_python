class Queue:
    def __init__(self):
        self.__st=[]
    def is_empty(self):         # it returns true for empty stack
        return len(self.__st) == 0
    def enqueue(self,data):
        #o(1) time complexity
        self.__st.append(data)
    def dequeue(self):
        secondary = []
        #bring all elements of primary stack st to secondary stack
def front(self):
    secondary = []

        while not (len(self.__st)==0):
            top_of_stack = self.__st[len(self.__st)-1]
            secondary.append(top_of_stack)
            self.__st.pop()

        #once the primary stack is empty ,elements are present in reverse order in the secondary stack
        #front of queue is on top of secondary
        result=None
        if len(secondary)!=0:
            result=secondary[len(secondary)-1]  # put top of sencondary in result
        # bring back all the elements from secondary to primary
        while not (len(secondary)==0):
            top_of_stack = secondary[len(secondary)-1]
            self.__st.append(top_of_stack)
            secondary.pop()


        return result