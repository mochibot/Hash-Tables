# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.retrieve(key) is None:
            newNode = LinkedPair(key, value)
            if self.storage[index] is None:
                self.storage[index] = newNode
            else:
                node = self.storage[index]
                while node.next is not None:
                    node = node.next
                node.next = newNode
            return
        else:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
                    

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if self.retrieve(key) is None:
            print(f'key {key} is not found')
            return
        index = self._hash_mod(key)
        if self.storage[index].key == key:
            self.storage[index] = None
            return
        prev_node = self.storage[index]
        curr_node = self.storage[index].next
        while curr_node is not None:
            if curr_node.key == key:
                next_node = curr_node.next
                prev_node.next = next_node
                break
            prev_node = curr_node
            curr_node = curr_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        
        for i in range(len(old_storage)):
            node = old_storage[i]
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

if __name__ == "__main__":
    # ht = HashTable(8)

    # ht.insert("key-0", "val-0")
    # ht.insert("key-1", "val-1")
    # ht.insert("key-2", "val-2")
    # ht.insert("key-3", "val-3")
    # ht.insert("key-4", "val-4")
    # ht.insert("key-5", "val-5")
    # ht.insert("key-6", "val-6")
    # ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    # ht.insert("key-0", "new-val-0")
    # ht.insert("key-1", "new-val-1")
    # ht.insert("key-2", "new-val-2")
    # ht.insert("key-3", "new-val-3")
    # ht.insert("key-4", "new-val-4")
    # ht.insert("key-5", "new-val-5")
    # ht.insert("key-6", "new-val-6")
    # ht.insert("key-7", "new-val-7")
    # ht.insert("key-8", "new-val-8")
    # ht.insert("key-9", "new-val-9")

    # print(ht.retrieve("key-0"))
    # print(ht.retrieve("key-1"))
    # print(ht.retrieve("key-2"))
    # print(ht.retrieve("key-3"))

    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # ht.remove('line_2')
    # ht.insert("line_3", "Testing")
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
