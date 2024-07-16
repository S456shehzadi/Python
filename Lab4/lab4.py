#Question no:1 "Implement Stack using python"
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
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  
print(stack.peek())  


#Question no:2 "Implement Queue using python"


print("Printing Queue Functionality")
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
            return "Queue is empty"

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  
print(queue.size())  

#Question no:3 "Binary search or Half interval search Algorithm"


print("Binary Search Starts Here")
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
arr = [6, 12, 17, 23, 38, 45, 55, 77, 84, 90]
target = 45

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")

