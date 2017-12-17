'''
Created on Dec 17, 2017

@author: rajjanwa
'''


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Queue:
    '''
    Like Stack, Queue is a linear structure which follows a particular order 
    in which the operations are performed. The order is First In First Out (FIFO). 
    '''
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        if self.head is None :
            return True
        else:
            return False
        
    def addInQueue(self,data):
        new_node=Node(data)
        if self.head == None :
            self.head=new_node
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next    
            curr.next=new_node    
    def display(self):
        curr=self.head
        index=0
        while curr != None :
            print "The queue value at index: "+str(index)+": "+str(curr.data)
            curr=curr.next
            index += 1
            
    def remove(self):
        if self.isEmpty() :
            print "Queue is emppty"
        else:
            temp=self.head.next
            self.head=temp   
            

if __name__ == '__main__':
    queue=Queue()
    queue.addInQueue(23)
    queue.addInQueue(3)
    queue.addInQueue(2)
    queue.addInQueue(13)
    queue.addInQueue(233)
    queue.addInQueue(234)
    queue.addInQueue(236)
    queue.addInQueue(2223)
    queue.display()
    queue.remove()
    print "Queue after one remove"
    queue.display()