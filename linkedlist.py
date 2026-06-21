class LinkedListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        builder = [str(self.value)]
        ptr = self
        while ptr.next is not None:
            ptr = ptr.next
            builder.append(f" -> {ptr.value}")
        return f"LinkedListNode({''.join(builder)})"

    # def length_R(self):
    #     if self.next is None:
    #         return 1
    #     else:
    #         return 1 + self.next.length_R()
        
    def length_I(self):
        ptr = self
        result = 1
        while ptr.next is not None:
            result += 1
            ptr = ptr.next
        return result
    
    def insert(self, index, value): 
        """
        Returns the new head of the linked list
        """
        if index == 0:
            return LinkedListNode(value, self)
        
        ptr = self 
        for i in range(index - 1): # to set ptr to the correct node 
            if ptr.next is None:
                raise IndexError("LinkedList is too short")
            else:
                ptr = ptr.next
        
        new_node = LinkedListNode(value, ptr.next)
        ptr.next = new_node
        return self
    
    # helper shifts the pointer to the respective index
    def helper(self, i):
        ptr = self 
        for i in range(i): 
            if ptr.next is None:
                raise IndexError("LinkedList is too short")
            else:
                ptr = ptr.next
        return ptr
    
    # get(i) : return the item at index if i 
    def get(self, i):
        if i == 0:
            return self.value

        ptr = self.helper(i)
        return ptr.value

    # set(i, value) : mutates the item at index 
    def set(self, i, value):
        ptr = self.helper(i)
        ptr.value = value 
    
    # delete(i) : deletes the i-th node, returns the new head of the list 
    def delete(self, i):
        if i == 0:
            new = self.next
            return new

        ptr = self.helper(i - 1)
        new_node = ptr.next.next
        ptr.next = new_node
        return self

    # remove(value) : remove the first occurence of value in the linked list, and returns the new head of the list 
    def remove(self, value):
        ptr = self
        if ptr.value == value:
            return ptr.next

        length = ptr.length_I()
        for i in range(length - 1):
            if ptr.next.value == value:
                ptr.next = ptr.next.next
                return self
            else:
                ptr = ptr.next
            

    # map(f) : create a new linked list with f applied to each value. returns the new linked list. 
    #          does not mutate the old list
    def map(self, f):
        copy_ptr = LinkedListNode(f(self.value), None)
        result = copy_ptr
        ptr = self

        while ptr.next is not None:
            new_node = LinkedListNode(f(ptr.next.value), None)
            copy_ptr.next = new_node
            copy_ptr = copy_ptr.next
            ptr = ptr.next

        return result

    # filter(p) : creates a new linked list with only the values that satisfy the predicate p
    def filter(self, pred):
        temp = LinkedListNode(None, None)
        result = temp
        ptr = self  

        while ptr is not None:
            if pred(ptr.value):
                new_node =  LinkedListNode(ptr.value, None)
                temp.next = new_node
                temp = temp.next
            
            ptr = ptr.next
        
        return result.next

    # fold(f, acc) : returns left-associative fold. Repeats acc = f(acc, value) for each in the linked list, 
    #                returns the final acc.x
    def fold(self, f, acc):
        ptr = self
        result = acc 

        while ptr is not None:
            result = f(result, ptr.value)
            ptr = ptr.next
        
        return result

    # middle() : returns the middle node --> 1 loop
    def middle(self):
        # i wld just find length and // 2 to find the middle index but technically that will be 2 loops
        length = self.length_I()
        mid_index = length // 2

        ptr = self
        target = ptr
        for i in range(mid_index):
            target = ptr.value
            ptr = ptr.next

        return target



head = LinkedListNode(5, LinkedListNode(7, LinkedListNode(1, LinkedListNode(-4))))
head = head.insert(0, 6)
head = head.insert(5, 8)

f = lambda x: x * 2
p = lambda x: x % 2 == 0

head = self 

print(head)
pass





        



