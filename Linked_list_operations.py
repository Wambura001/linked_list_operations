# create node class 
class Node:
    def __init__(self, value = None, next = None) :
        self.item = value 
        self.link = next 
        
# create list
class linked_list: 
    def __init__(self):
        self.head = None
        
# Linked list operations 
# inserting item at head
def add_first(self, value):
    new_node = Node(value)
    new_node.link = self.head
    self.head = new_node
    
# inserting item at end 
def add_last(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        return 
    x = self.head
    while x.link is not None:
        x = x.link
    x.link = new_node 

# Travesing list
# display list
def display_list(self):
    node = self.head 
    while node is not None:
        print(" ", node.item)
        node = node.link 

# removing from list 
def remove_front(self):
    if self.head is None:
        print("list is empty, nothing to delete")
        return 
    self.head = self.head.link 
    
def remove_last(self):
    if self.head is None:
        print("List is empty, nothing to delete actually")
        return 
    x = self.head 
    while x.link.link is not None:
        x = x.link
    x.link = None

