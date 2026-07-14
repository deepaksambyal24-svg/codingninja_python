from queue import Queue
# get -> front () and dequeue()
#put -> enqueue()
qu=Queue()
qu.put(10)
qu.put(11)
qu.put(12)
qu.put(13)
print(qu.get())
print(qu.get())
print(qu.get())
# removing the first element and return the value
def reverse_queue(qu):
    # prepare a stack
    st =[]
    # bring all the elements form queue to stak
    while not qu.empty():
        st.append(qu.get())# it remove tand get first elemetn and add to to the stack

    # bring all the elemeents back from stack to queue
    while not qu.empty():
        qu.put(st[len(st)-1])
        st.pop()

reverse_queue(qu)
print(qu)



