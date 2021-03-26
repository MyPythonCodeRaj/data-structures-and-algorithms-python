class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while not cur is None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get_index(self, index):
        if index >= self.length():
            print("Error: Index out of rang!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

my_list = linked_list()
print("Print linked list before insertion in linked list")
my_list.display()
my_list.append(3)
my_list.append(45)
my_list.append(23)
my_list.append(46)
print("Print linked list after insertion in linked list")
my_list.display()
print("3rd node value in linked list")
print(my_list.get_index(3))
