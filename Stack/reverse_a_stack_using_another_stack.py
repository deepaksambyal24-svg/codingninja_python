from traceback import extract_stack


def reverseStack(inputStack,extraStack):

    if isEmpty(inputStack): # if stack is emptu do nothnig
        return

    # we are reversing the data from s11 using s2
topElement=input.Stack.pop()  # get access to top element and remove it aslo

reverseStack(inputStack,extraStack)         #recursive assumption
# push the topelement to the bottom of inputStack


while not isEmpty(inputStack):
    element=inputStack.pop()
    extraStack.append(element)
inputStack.append(topElement)

while not isEmpty(extracStack):
    element=extraStack.pop()
    inputStack.append(element)