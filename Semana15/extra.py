class node():
    def __init__(self, data=None):
        self.data=data
        self.next=None


class Linked_list():
    def __init__(self):
        self.head=None


    def add_data(self, data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node


    def print_structure(self):
        current= self.head
        while current:
            print(current.data, end=" ")
            current =  current.next
        print("\n")


    def bubble_sort_list(self):
        sorted=True
        while sorted:
            current=self.head
            sorted=False
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    sorted=True
                current=current.next


linked_list = Linked_list()
list=[2,5,6,8,2,9,11,-78,23.6, 3, 12.5]
for data in list:
    linked_list.add_data(data)

linked_list.print_structure()

linked_list.bubble_sort_list()

linked_list.print_structure()
