# Dynamic Array (List) Implementation using Python's Built-in List

class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, element):
        self.array.append(element)
    
    def insert(self, index, element):
        self.array.insert(index, element)
    
    def delete(self, element):
        if element in self.array:
            self.array.remove(element)
        else:
            raise ValueError("Element not found in the array")

    def search(self, element):
        if element in self.array:
            return self.array.index(element)
        return -1
    
    def traverse(self):
        for elem in self.array:
            print(elem, end=" ")
        print()

# Example Usage:
if __name__ == "__main__":
    dyn_arr = DynamicArray()
    dyn_arr.append(10)
    dyn_arr.append(20)
    dyn_arr.append(30)
    dyn_arr.traverse()  # Output: 10 20 30
    
    dyn_arr.insert(1, 15)
    dyn_arr.traverse()  # Output: 10 15 20 30
    
    dyn_arr.delete(20)
    dyn_arr.traverse()  # Output: 10 15 30
    
    print(f"Search for 30: {dyn_arr.search(30)}")  # Output: Search for 30: 2
    print(f"Search for 100: {dyn_arr.search(100)}")  # Output: Search for 100: -1
