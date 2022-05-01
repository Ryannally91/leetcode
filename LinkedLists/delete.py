class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.head = None
    
    def addNode(self, val):
        if self.head == None:
            self.head = Node(val)
            return self.head
        runner = self.head
        while runner != None:
            if runner.next == None:
                runner.next = Node(val)
                return runner.next
    
    def delterNode(self, val):
        if self.head == None:
            return False
        runner = self.head
        while runner!= None:
            if runner.next == val:
                runner.next== runner.next.next
                

