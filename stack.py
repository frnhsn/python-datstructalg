"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        current = self.head
        if self.head:
            while (position > 1):
                current = current.next
                position -= 1
                if current == None:
                    break
            return current
        else:
            return None
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position == 1:
            return self.head
        
        prev_node = self.get_position(position - 1)

        if prev_node != None:
            next_node = prev_node.next
            prev_node.next = new_element
            new_element.next = next_node

    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head
        previous = None

        while current.value != value:
            if current.next == None:
                break
            previous = current
            current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

        del current

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        
        new_element.next = self.ll.head
        self.ll.head = new_element

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"

        deleted = self.ll.head

        if deleted:
            self.ll.head = deleted.next
            deleted.next = None

            return deleted
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)