def function3():
    print('this is function3')
def function2():
    function3()
    print('this is function2')

def function1():
    function2()
    print('this is function1')


function1()

# default parameter are the arguments value when dont pass anything # amually passed argument take presedence
# default argument should always written by manual parameter
def fun(nondefault= 'avc',fun="ride"):# DEFAULT PARAMETER ALWAYS IN LEFT 
    print(fun)
fun()   #   it automatically take ride as arugument and is assignd by equal to ===