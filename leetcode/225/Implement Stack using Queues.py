from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque([])        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        q = self.queue
        q.append(x)
        for _ in range(len(q)-1):
            q.append(q.popleft())

    def pop(self):
        """
        :rtype: int
        """
        
        return self.queue.popleft() if self.queue else None
        

    def top(self):
        """
        :rtype: int
        """

        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.queue) == 0 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
