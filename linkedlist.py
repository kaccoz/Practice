class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def from_list(lst):
        if lst == []: 
            return None
        else:
            sentinel_head = ptr = LinkedListNode(None)
            for item in lst:
                ptr.next = LinkedListNode(item)
                ptr = ptr.next

            return sentinel_head.next

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
    def _get_node(self, i): #user still can call this method 
        ptr = self 
        for i in range(i): 
            if ptr.next is None:
                raise IndexError(f"_get_node(): index {i} does not exist")
            else:
                ptr = ptr.next
        return ptr
    
    # get(i) : return the item at index if i 
    def get(self, i):
        if i == 0:
            return self.value

        ptr = self._get_node(i)
        return ptr.value

    # set(i, value) : mutates the item at index 
    def set(self, i, value):
        self._get_node(i).value = value
    
    # delete(i) : deletes the i-th node, returns the new head of the list 
    def delete(self, i):
        if i == 0:
            return self.next 

        ptr = self._get_node(i - 1)

        if ptr.next is None:
            raise IndexError(f"delete(): index {i} does not exist")
        
        ptr.next = ptr.next.next
        return self

    # remove(value) : remove the first occurence of value in the linked list, and returns the new head of the list 
    def remove(self, value):
        find_result = self._find_node(lambda x: x == value)

        if find_result is None:
            return self
        else:
            (i, ptr) = find_result
            return self.delete(i)

    def _find_node(self, pred): # return index and the node itself 
        ptr = self 
        i = 0
        while ptr is not None:
            if pred(ptr.value): 
                return (i, ptr)
            else:
                ptr = ptr.next 
                i += 1
        else:
            return None 

    # find(p) : return the index of the first occurence  of value satisfying pred, or 'None' if no values satisfies pred
    def find(self, pred):
        find_result = self._find_node(pred)

        if find_result is None:
            return None
        else:
            (i, ptr) = find_result
            return i

    def equals(self, other_list):
        ptr1, ptr2 = self, other_list
        while not (ptr1 is None and ptr2 is None):
            if ptr1 is None or ptr2 is None: 
                return False
            elif ptr1.value != ptr2.value:
                return False
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

        else:
            return True 
    
    # map(f) : create a new linked list with f applied to each value. returns the new linked list. 
    #          does not mutate the old list
    def map(self, f):
        head = copy_ptr = LinkedListNode(f(self.value), None)
        ptr = self

        while ptr.next is not None:
            copy_ptr.next = LinkedListNode(f(ptr.next.value), None)
            copy_ptr = copy_ptr.next
            ptr = ptr.next

        return head

    # filter(p) : creates a new linked list with only the values that satisfy the predicate p
    def filter(self, pred):
        head = ptr_filter = LinkedListNode(None, None) # sentinel node, not part of the linked list 
        ptr = self  

        while ptr is not None:
            if pred(ptr.value):
                ptr_filter.next =  LinkedListNode(ptr.value, None)
                ptr_filter = ptr_filter.next
            ptr = ptr.next
        
        if head.next is not None:
            return head.next
        else:
            return LinkedListNode(None, None)

    # fold(f, acc) : returns left-associative fold. Repeats acc = f(acc, value) for each in the linked list, 
    #                returns the final acc.x
    def fold(self, f, acc):
        ptr = self

        while ptr is not None:
            acc = f(acc, ptr.value)
            ptr = ptr.next
        
        return acc

    # middle, simple version 
    def middle(self):
        # i wld just find length and // 2 to find the middle index but technically that will be 2 loops
        return self._get_node(self.length_I() // 2)

    # middle() : returns the middle node --> 1 loop
    # ptr2 moves twice as fast as ptr1
    def middle2(self):
        ptr1 = ptr2 = self
        while True:
            if ptr2.next is None or ptr2.next.next is None:
                return ptr1
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next


if __name__ == '__main__':

    reference = LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5, 2]) # remains unchanged 
    head = LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5, 2])
    pass

    print("Testing map...")
    assert head.map(lambda x: x * 2).equals(LinkedListNode.from_list([10, 14, 2, -8, 12, -6, 10 ,4]))
    assert head.map(lambda x: x).equals(reference)
    assert head.map(lambda x: x * x).equals(LinkedListNode.from_list([25, 49, 1, 16, 36, 9, 25, 4]))
    pass

    print("Testing filter...")
    assert head.filter(lambda x: x % 2 == 0).equals(LinkedListNode.from_list([-4, 6, 2]))
    assert head.filter(lambda x: x == 0).equals(LinkedListNode(None, None))
    assert head.filter(lambda x: x != 100).equals(reference)
    pass

    print("Testing fold...")
    assert head.fold(lambda x, y: x + y, 0) == 19
    assert head.fold(lambda x, y: x * y, 1) == 25200
    assert head.fold(lambda x, y: str(x) + str(y), '') == "571-46-352"
    pass

    print("Testing delete...")
    head = LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5, 2])
    assert head.delete(0).equals(LinkedListNode.from_list([7, 1, -4, 6, -3, 5 ,2]))

    head = LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5, 2])
    assert head.delete(2).equals(LinkedListNode.from_list([5, 7, -4, 6, -3, 5, 2]))

    head = LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5, 2])
    assert head.delete(7).equals(LinkedListNode.from_list([5, 7, 1, -4, 6, -3, 5]))

    try: head.delete(8)
    except IndexError: pass
    head = LinkedListNode(5, LinkedListNode(7, LinkedListNode(1, LinkedListNode(-4))))
    try: head.delete(4)
    except IndexError: pass


pass


        



