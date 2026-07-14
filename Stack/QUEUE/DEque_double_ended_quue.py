# efficiently inserts data in the quue form both sides and also supports efficient removal fro both sides
from collections import deque
d=deque()
# insertion form the back
d.append(1)
d.append(2)
d.append(3)
# for insertion form the front
d.appendleft(4)
d.appendleft(5)
print(d)
# remove from front
d.popleft()
print(d)
#removal from the back
d.pop()
print(d)
