from queue import Queue
def reversek(queue, k):

    if k<=0:
        return queue
    if k > queue.qsize():
        return queue
    if queue.empty():
        return queue




    stack = []
    #bring k elemetns from queue to stack
    for i in range (k):
        stack.append(queue.get())
    # bring all elements of stack back to queue
        while not (len(stack ) ==0):
            top =stack[len(stack)-1]
            queue.put(top)
            stack.pop()

        for i in range (queue.qsize()-k):
            queue.put(queue.get())

    return queue
