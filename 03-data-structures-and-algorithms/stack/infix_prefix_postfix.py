def isoperator(char):
    return char == "+" or char == "-" or char == "*" or char == "/"


def prefix_to_infix(s):
    i = len(s) - 1
    st = []

    while i >= 0:
        if isoperator(s[i]):
            expr1 = st.pop()
            expr2 = st.pop()

            st.append("(" + expr1 + s[i] + expr2 + ")")
        else:
            st.append(s[i])

        i -= 1

    return st.pop()


ans = prefix_to_infix("*67")
print(ans)