'''
Created on Dec 17, 2017

@author: rajjanwa
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None       

    def append(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            curr=self.head
            new_node=Node(data)
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node    
                  
    def printList(self):
        curr=self.head
        while(curr.next != None):
            print str(curr.data)
            curr=curr.next
        print str(curr.data)
        
    def addAtStart(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def exists(self,key):
        curr=self.head
        while(curr.next != None):
            if key == curr.data:
                return True
            curr=curr.next  
    



if __name__ == '__main__':
    lst=LinkedList()
    lst.append(4)
    lst.append(412)
    lst.append(6)
    lst.append(41)
    lst.printList()
    lst.addAtStart(100)
    print str(lst.exists(101))
    print str(lst.exists(41))
    lst.printList()    