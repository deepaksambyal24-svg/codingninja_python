# stack is one to top of another  it works on first in last out
# call stack whevever in compouter is running a program it store the function call in the memeory
#for every function call a new memory is created in stack
# and every is called is stack frame this frame is processing the memeory
#whevenever a function is call a stack is allloted
#whever the functin is executed and retrun statemnet call stack is removed
def function3():
    print("function3")
def function2():
    print("function2")
    function3()
def function1():
    print("function1")
    function2()
function1()
