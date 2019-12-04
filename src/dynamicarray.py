class DynamicArray:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity

    def insert(self, index, value):
        if index > self.capacity:
            print('Error: index out of range')
            return

        if self.count >= self.capacity:
            self.double_size()
            
        end = self.count
        while end > index:
            self.storage[end] = self.storage[end - 1]
            end -= 1
        self.storage[index] = value
        self.count += 1 
        
    def append(self, value):
        self.insert(self.count, value)

    def prepend(self, value):
        self.insert(0, value)

    def delete(self, index):
        if index > self.capacity:
            print('Error: index out of range')
            return
        
        start = index
        while start < self.count:
            self.storage[start] = self.storage[start + 1]
            start += 1
        self.storage[self.count] = None
        self.count -= 1

    def double_size(self):
        self.capacity = self.capacity * 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        for i in range(len(old_storage)):
            self.storage[i] = old_storage[i]

my_array = DynamicArray(3)
my_array.prepend(4)
print(my_array.storage)
my_array.insert(1, 3)
my_array.insert(2, 7)
my_array.append(5)
print(my_array.storage)
my_array.delete(0)
print(my_array.storage)
my_array.insert(1, 8)
print(my_array.storage)
my_array.delete(2)
print(my_array.storage)
my_array.insert(2, 7)
print(my_array.storage)
my_array.insert(2, 78)
print(my_array.storage)
