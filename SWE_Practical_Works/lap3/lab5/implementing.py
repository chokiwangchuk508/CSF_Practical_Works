class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2


def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test
print(is_balanced("((()))"))  # True
print(is_balanced("(()"))  # False


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test
print(reverse_string("Hello, World!"))  # "!dlroW ,olleH"


def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()  # Remove the person who is "out"
    
    return queue.dequeue()  # Return the winner's name

# Test
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name


def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
    return stack.pop()

# Test
postfix_expr = "231*+9-"
print(evaluate_postfix(postfix_expr))  # Should print 2


class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

# Test
queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.dequeue())  # Should print 2


class TaskScheduler:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.enqueue(task)

    def process_task(self):
        if not self.queue.is_empty():
            print(f"Processing task: {self.queue.dequeue()}")
        else:
            print("No tasks to process")

# Test
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

scheduler.process_task()  # Should print "Processing task: Task 1"
scheduler.process_task()  # Should print "Processing task: Task 2"
scheduler.process_task()  # Should print "Processing task: Task 3"
scheduler.process_task()  # Should print "No tasks to process"


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""
    for char in expression:
        if char.isalnum():  # Supports alphanumeric (letters and digits)
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Discard the '('
        else:
            while (not stack.is_empty() and precedence(char) <= precedence(stack.peek())):
                postfix += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

# Test
infix_expr = "A+B*(C^D-E)"
print(infix_to_postfix(infix_expr))  # Should print "ABCD^E-*+"
