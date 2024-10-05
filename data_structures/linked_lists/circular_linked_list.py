# Circular Linked List Implementation

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        new_node.next = self.head
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        self.head = new_node

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            if current.next == self.head:  # Only one node
                self.head = None
                return
            last = current
            while last.next != self.head:
                last = last.next
            last.next = current.next
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
            if current == self.head:  # If we reached back to head
                return
        if not current:  # Key not found
            return
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        if not current:
            return False
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def traverse(self):
        current = self.head
        if not current:
            return
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Example Usage:
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(10)
    circular_linked_list.append(20)
    circular_linked_list.prepend(5)
    circular_linked_list.traverse()  # Output: 5 -> 10 -> 20 -> (head)
    circular_linked_list.delete(10)
    circular_linked_list.traverse()  # Output: 5 -> 20 -> (head)
    print(circular_linked_list.search(20))  # Output: True
