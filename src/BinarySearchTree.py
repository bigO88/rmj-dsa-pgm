'''
Created on Nov 16, 2017

@author: rajjanwa
'''

class Node:

    def __init__(self,data):
        self.left_child=None
        self.right_child=None
        self.data=data
        
class BinarySearchTree:
    '''
    Binary Search Tree, is a node-based binary tree data structure which has the following properties:
    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.
    '''
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        if self.root == None :
            self.root=Node(data)
        else:
            self._insert(data,self.root)    
    def _insert(self,data,currNode):
        if data <currNode.data :
            if currNode.left_child == None:
                currNode.left_child=Node(data)
            else:
                self._insert(data, currNode.left_child)
        elif data > currNode.data:
            if currNode.right_child == None:
                currNode.right_child=Node(data)
            else:
                self._insert(data, currNode.right_child)
        else:
            print"value already in Tree"          
                            
                        
    def printTree(self):
        if self.root != None:
            self._printTree(self.root)                    
                        
    def _printTree(self,currNode):
        if currNode != None :
            self._printTree(currNode.left_child)
            print str(currNode.data) 
            self._printTree(currNode.right_child)                   
    def height(self):
        if self.root != None :
            return self._height(self.root,0)
        else:
            return 0
    def _height(self,currNode,currHeight):
        if currNode == None : return currHeight
        left_height=self._height(currNode.left_child, currHeight+1)
        right_height=self._height(currNode.right_child, currHeight+1)
        return max(left_height,right_height)
    
    def find(self,key):
        if self.root != None:
            return self._find(self.root,key)
        else:
            return False
        
    def _find(self,currNode,key):
        if key == currNode.data: 
            return True
        if key < currNode.data and currNode.left_child != None :
            return self._find(currNode.left_child, key)
        elif key > currNode.data and currNode.right_child != None:
            return self._find(currNode.right_child, key)    
        
        return False        
                        
    
if __name__ == '__main__':         
    bst=BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(5)
    bst.insert(8)
    bst.insert(34)
    bst.insert(51)
    bst.insert(15)
    bst.insert(36)
    bst.insert(136)
    bst.insert(1126)
    bst.insert(1126)
    bst.printTree()
    print "Height of binary search tree: "+ str(bst.height())
    print "Height of binary search a key: "+ str(bst.find(34))
    print "Height of binary search a key: "+ str(bst.find(35))
    
    