class MyQueue(object):

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.output_stack.pop() if self.output_stack else None

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.output_stack[-1] if self.output_stack else None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.input_stack and not self.output_stack

    def move(self):
        """
        Moves elements from input stack to output stack if output stack is empty.
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
