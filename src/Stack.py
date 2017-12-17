'''
Created on Dec 17, 2017

@author: rajjanwa
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    '''
    Stack is a linear data structure which follows a particular order 
    in which the operations are performed. 
    The order may be LIFO(Last In First Out) or FILO(First In Last Out).
    '''
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        if self.head is None :
            return True
        else:
            return False
            
    def push(self,key):
        new_node=Node(key)
        if self.isEmpty():
            self.head=new_node
        else:
            temp=self.head
            self.head=new_node
            new_node.next=temp
            
    def pop(self):
        if self.isEmpty():
            print" No values in stack"
        else:
            temp=self.head.next
            self.head=temp    
    def top(self):
        if self.isEmpty() :
            print "Stack is empty"
        else:
            return self.head.data
    def display(self):
        if self.isEmpty():
            print " Stack is empty"
        else:
            curr=self.head
            while curr != None:
                print str(curr.data)
                curr=curr.next
                                                    
if __name__ == '__main__':
    
    stack = Stack()
    stack.push(4)
    stack.push(14)
    stack.push(423)
    stack.push(422)
    stack.push(1124)
    stack.push(1322134)
    stack.display()
    print "______________________________________________________"
    print "Top "+str(stack.top())
    stack.pop()
    print "______________________________________________________"   
    
    print "Top: "+str(stack.top())
    stack.display()
   
   
   
   