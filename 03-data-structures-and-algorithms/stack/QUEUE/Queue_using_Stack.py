class Queue:
    def __init__(self):
        self.__st=[]

    def enqueue(self,data):
        sec=[]
    #empty the elements of primary stack to secondary

        while not (len(self.__st)==0):
            topelement=self.__st[len(self.__st)-1]
            self.__st.pop()
            sec.append(topelement)

        #now the primary stack is empty,lets put data insideit
        self.__st.append(data)

        # bring back all elements from sec to primary
        while not (len(sec)==0):
            topelement=sec [len(sec)-1]
            sec.pop()
            self.__st.append(topelement)
    def isEmpty(self):
        return len(self.__st)==0
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        self.__st.pop()
    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.__st[len(self.__st)-1]

