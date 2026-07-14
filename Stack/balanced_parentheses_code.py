def isBalanced(Expression):
    stack=[]
    for i in range (len(Expression)):
        if Expression[i]=='(':
            stack.append(i)
        elif Expression[i]==')':
            if len(stack)==0:
                return False
            if stack[len(stack)-1] =='(':
                stack.pop()
    return len(stack)==0
isd = isBalanced("(()))")
print(isd)