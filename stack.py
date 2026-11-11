class Stack:
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
    
    def check_brackets(self, sequence: str) -> str:
        pairs = {')': '(', '}': '{', ']': '['}
        
        self.items = [] 

        for char in sequence:
            if char in "({[":
                self.push(char)
            elif char in ")}]":
                if self.is_empty():
                    return "Несбалансированно"
                
                top_element = self.pop()
                
                if pairs[char] != top_element:
                    return "Несбалансированно"

        if self.is_empty():
            return "Сбалансированно"
        else:
            return "Несбалансированно"
        
if __name__ == '__main__':
    user_input = input("Введите строку со скобками: ")
    stack = Stack()
    result = stack.check_brackets(user_input)
    print(result)