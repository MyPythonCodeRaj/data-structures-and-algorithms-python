# Basic Array Implementation in Python

class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def insert(self, index, element):
        if self.size == self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        
        # Shift elements to the right to make space for the new element
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        
        self.array[index] = element
        self.size += 1
    
    def delete(self, index):
        if self.size == 0:
            raise Exception("Array is empty")
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        
        # Shift elements to the left to fill the gap of the removed element
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = None
        self.size -= 1

    def search(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                return i
        return -1

    def traverse(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()

# Example usage:
if __name__ == "__main__":
    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.traverse()  # Output: 10 20 30
    arr.insert(1, 15)
    arr.traverse()  # Output: 10 15 20 30
    arr.delete(2)
    arr.traverse()  # Output: 10 15 30
    print(f"Search 30: {arr.search(30)}")  # Output: Search 30: 2
    print(f"Search 40: {arr.search(40)}")  # Output: Search 40: -1
