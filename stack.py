class Stack:
    def __init__(self, capacity = 255): 
        self.stk = []
        for i in range(capacity):
            self.stk.append(None)
        self.capacity = capacity 
        self.size = 0
    
    def __repr__(self):
        return f"Stack({self.size}/{self.capacity}: {self.stk})"
    
    def push(self, item):
        if self.size == self.capacity:
            raise IndexError(f"Stack is at full capacity! ({self.capacity})")
        else:
            self.stk[self.size] = item
            self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError(f"Stack is empty!")
        else:
            self.size -= 1
            return self.stk[self.size]


s = Stack(5) 
s.push(1)
s.push(5)
s.push(3)
s.push(7)
s.push(2)

pass 

