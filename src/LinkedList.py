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