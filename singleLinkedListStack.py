import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self):
        x = int(input("enter an element to insert\n"))
        n = Node(x)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while (temp.link) != None:
                temp = temp.link
            temp.link = n
            
    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end = " ")
                temp = temp.link
            print()
    
    def pop(self):
        if self.head == None:
            print("empty")
        else:
            temp = self.head
            if temp.link != None:
                while (temp.link).link != None:
                    temp = temp.link
                print("the popped element is", (temp.link).data)
                temp.link = None
            else:
                self.head = None
                print("the popped element is", temp.data)

li = LinkedList()
while True:
    print("1:push, 2:pop, 3:display, 4:exit")
    x = int(input())
    if x is 1:
        li.push()
    elif x is 2:
        li.pop()
    elif x is 3:
        li.display()
    elif x is 4:
        sys.exit()
    
