'''
Created on Dec 17, 2017

@author: rajjanwa
'''
from operator import pos

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    '''
    Linked List is a linear data structure. Unlike arrays, 
    linked list elements are not stored at contiguous location; 
    the elements are linked using pointers.
    '''
    def __init__(self):
        self.head=None       

    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            curr=self.head
            new_node=Node(data)
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node    
                  
    def printList(self):
        curr=self.head
        if curr is None:
            print "The list is empty" 
        
        while( curr != None ):
            print str(curr.data)
            curr=curr.next
        
    def addAtStart(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def exists(self,key):
        curr=self.head
        pos=1
        while(curr != None):
            if key == curr.data:
                print "Key present at: "+str(pos)
                return True
                break
            curr=curr.next
            pos +=1
        return False      

    def addAfterKey(self,key,data):
        curr=self.head
        while(curr != None) :
            if curr.data == key :
                new_node=Node(data)
                new_node.next=curr.next
                curr.next=new_node
                break
            curr=curr.next  
    def getPosition(self,key):
        curr=self.head
        pos=1
        while curr != None :
            if curr.data == key:
                return pos
            pos += 1
            curr=curr.next
        return -1
                
    def remove(self,key):
        preNodePosition=self.getPosition(key)-1
        posCounter=1
        curr=self.head
        while curr != None :
            if posCounter == preNodePosition :
                temp=curr.next.next
                curr.next=temp
            curr=curr.next
            posCounter += 1       
                
                
if __name__ == '__main__':
    lst=LinkedList()
    lst.append(4)
    lst.append(412)
    lst.append(6)
    lst.append(41)
    print"_________________________________________________"
    
    lst.printList()
    lst.addAtStart(100)
    print str(lst.exists(101))
    print str(lst.exists(41))
    
    print"_________________________________________________"
    
    lst.printList()    
    
    print"_________________________________________________"
    lst.addAfterKey(5,60)
    lst.printList()
    
    print"_________________________________________________"
    lst.addAfterKey(6,60)
    lst.printList()
    
    print"_________________________________________________"
    
    print str(lst.getPosition(6))
    print str(lst.getPosition(8))
    print"_________________________________________________"
    print str(lst.remove(100))
    lst.printList()
    
    print"_________________________________________________"
    