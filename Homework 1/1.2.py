class Node:
    """Node constructor for our Signle-Linked List of integeres. // Input: Integer number // Output: Node with integer data and pointer to NIL"""
    def __init__(self, integerData):
        """Initialize self. (See help(type(self)) for accurate signature) and integerData (should be integer)."""
        if type(integerData) is int:
            self.integerData = integerData
            self.next = None
        else:
            print("Insert Data Should Be Integer")
            exit(1)
      
class SinglyLinkedList:
    """Singly Linked List consctructor for our Signle-Linked List of integeres."""
    def __init__(self):
        """Initialize self. See help(type(self)) for accurate signature)"""
        self.head = None
    
    def int_list_insert(self, integerData):
        """Method .int_list_insert(i) of the class SinglyLinkedList, where i is the integer number, is a method for adding a new nodes at the beginning of our Signle-Linked List. // Input: Integer number // Output: Updated Signle-Linked List with the new node at the beginning whose data is the inputed integer number."""
        newNode = Node(integerData)
        newNode.next = self.head
        self.head = newNode
        
    def int_list_delete(self, nodePosition):
        """Method .int_list_delete(x) of the class SinglyLinkedList, where x is the node to delete, is a method for deleting a node x (1, 2, 3, ...) from ourSignle-Linked List. // Input: Positive integer number // Output: Updated Signle-Linked List after deleting the required node."""
        if type(nodePosition) is not int or nodePosition != abs(nodePosition) or nodePosition == 0:
            print("Node Position In The Delete Method Should Be Positive Integer")
            exit(2)
        else:
            if self.head is None:
                return
        
            if nodePosition == 1:
                self.head = self.head.next
                return 
        
            stepCounter = 1
            pointer = self.head
            newPointer = self.head
            oldPointer = self.head
            flag = 0
            while pointer is not None:
                if stepCounter == nodePosition:
                    newPointer = pointer.next
                    flag = 1
                    break
                else:
                    stepCounter = stepCounter + 1
                    oldPointer = pointer
                    pointer = pointer.next
            if flag == 1: 
                oldPointer.next = newPointer
            
                    
    def printSLLContent(self):
        """Method .printListContent() of the class SinglyLinkedList that's handles printing of the content of our Signle-Linked List. // Input: Nothing // Output: Content of Signle-Linked List."""
        outputText = ""
        if self.head is None:
            outputText = "Head --> NIL"
        else:
            pointer = self.head
            outputText = "Head --> "
            while pointer is not None:
                outputText = outputText + f"{pointer.integerData} --> "
                pointer = pointer.next
            outputText = outputText + "NIL"
        return outputText
            
            
def Enqueue(Q, x):
    """Free function Enqueue(Q, x) for inserting a node with integer data "x" (from left to right) to a queue "Q", where in our case Q is a singly-linked list object. // Input: Singly-linked list object and integer number // Output: Updated singly-linked list."""
    newNode = Node(x)
    newNode.next = Q.head
    Q.head = newNode
    
def Dequeue(Q):
    """Free function Dequeue(Q) for removing a node (with a rule FIFO) from a queue "Q", where in our case Q is a singly-linked list object. // Input: Singly-linked list object // Output: Updated singly-linked list and a message about the content of the singly-linked list."""
    if Q.head is None:
        Q.head = None
    else:
        pointer = Q.head
        oldPointer = Q.head
        while pointer.next is not None:
            oldPointer = pointer
            pointer = pointer.next
        if Q.head.next is not None:
            oldPointer.next = None
        else:
            Q.head = None
    return Q.printSLLContent()
    
def main():
    Q = SinglyLinkedList()
    for i in range(1, 6):
        Enqueue(Q, i)
    print(Dequeue(Q))
    print(Dequeue(Q))
    for i in range(6, 14):
        Enqueue(Q, i)
    print(Dequeue(Q))
    print(Dequeue(Q))
    Enqueue(Q, 14)
    for j in range(1, 11):
        print(Dequeue(Q))
    
if __name__ == "__main__":
    main()