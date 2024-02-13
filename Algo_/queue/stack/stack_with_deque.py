from collections import deque

"""
Deque is preferred over the list in the cases where we need quicker append and pop operations 

#####from both the ends#### of the container
"""

stack1 = deque()
stack1.append('x')
stack1.append('y')
stack1.append('z')

print(stack1)
print(stack1.pop())
print(stack1.popleft())
