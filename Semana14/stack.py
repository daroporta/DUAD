
class Node:
    data: str

    def __init__(self, data):
        self.data = data
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None  

    def push(self, data):
        new_node = Node(data)  
        new_node.next = self.top  
        self.top = new_node 

    def pop(self):
        if self.top is None:
            empty="The stack does not have any data."
            return empty
        deleted_data = self.top.data 
        self.top = self.top.next 
        return deleted_data 

    def print_stack(self):
        if self.top is None:
            print("The stack does not have any data.")
            return
        current_node = self.top  
        while current_node is not None:
            print(current_node.data)  
            current_node = current_node.next  


stack = Stack()
stack.push("1️⃣")
stack.push("2️⃣")
stack.push("3️⃣")

stack.print_stack()  

print(f"Data deleted: {stack.pop(), stack.pop()}")  

print("Last data:")
stack.print_stack() 

print(f"Last element removed {stack.pop()}")  


stack.print_stack()  
