class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Deque:
    def __init__(self):
        self.first = None
        self.last = None

    def push_left(self, data):
        new_node = Node(data)
        if self.first is None:  
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first.previous = new_node
            self.first = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.last is None:  
            self.first = self.tail = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node

    def pop_left(self):
        if self.first is None:  
            return None
        data = self.first.data
        if self.first == self.last:  
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.previous = None
        return data

    def pop_right(self):
        if self.last is None: 
            return None
        data = self.last.data
        if self.first == self.last:  
            self.first = self.last = None
        else:
            self.last = self.last.previous
            self.last.next = None
        return data

    def print_deque(self):
        current = self.first
        while current is not None:
            print(f" {current.data} ", end=" ")
            current = current.next
        print()

Double_ended_queue = Deque()

Double_ended_queue.push_left("O")
Double_ended_queue.push_right("L")
Double_ended_queue.push_left("H")
Double_ended_queue.push_right("A")

Double_ended_queue.push_right(" ")
Double_ended_queue.push_right("A")
Double_ended_queue.push_right("M")
Double_ended_queue.push_right("I")
Double_ended_queue.push_right("G")
Double_ended_queue.push_right("O")

Double_ended_queue.print_deque() 

print(Double_ended_queue.pop_left())  
print(Double_ended_queue.pop_right()) 
print(Double_ended_queue.pop_left())
print(Double_ended_queue.pop_right())


Double_ended_queue.print_deque() 
