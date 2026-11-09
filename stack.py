class Stack:
    def __init__(delf): 
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack") 
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1] 

    def size(self) -> int:
        return len(self.items)
    
    def check_brackets(sequence: str) -> str:
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return "Несбалансированно"
            
            top_element = stack.pop()
            
            if pairs[char] != top_element:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"
