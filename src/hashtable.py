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
        '''Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.'''
        if self.retrieve(key) is None : #== KeyError:
            my_integer = self._hash_mod(key)
            new_linked_pair = LinkedPair(key,value)
            if self.storage[my_integer] is None:
                self.storage[my_integer] = new_linked_pair
            else:
                placeholder = self.storage[my_integer]
                while placeholder.next is not None:
                    placeholder = placeholder.next
                placeholder.next = new_linked_pair
        else:
            self.remove(key)
            self.insert(key,value)



    def remove(self, key):
        '''Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.'''
        integer_find = self._hash_mod(key)
        if self.storage[integer_find] is not None:
            previous_node = None
            current_node = self.storage[integer_find]
            #check if key in first linked list
            while current_node is not None:
                if current_node.key == key:
                    if previous_node is None:
                        self.storage[integer_find] = None
                    else:
                        self.storage[integer_find] = current_node.next
                    return #print("value deleted")
                previous_node = current_node
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    #print("value could not be found")
                    return KeyError
        else:
            return KeyError





    def retrieve(self, key):
        '''Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.'''
        integer_find = self._hash_mod(key)
        if self.storage[integer_find] is not None:
            current_node = self.storage[integer_find]
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
        return None #KeyError


    def resize(self):
        '''Doubles the capacity of the hash table and
        rehash all key/value pairs.Fill this in.'''
        self.capacity = self.capacity*2
        new_storage = [None] * self.capacity
        for item in self.storage:
            while item is not None:
                my_new_hash = self._hash_mod(item.key)
                if new_storage[my_new_hash] is None:
                    new_storage[my_new_hash] = LinkedPair(item.key,item.value)
                else:
                    placeholder = new_storage[my_new_hash]
                    while placeholder.next is not None:
                        placeholder = placeholder.next
                    placeholder.next = LinkedPair(item.key,item.value)
                item = item.next
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

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
