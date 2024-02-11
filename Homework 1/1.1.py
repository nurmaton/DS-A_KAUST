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
        if self.head is None:
            print("Singly Linked List is Empty: Head --> NIL")
        else:
            pointer = self.head
            outputText = "Head --> "
            while pointer is not None:
                outputText = outputText + f"{pointer.integerData} --> "
                pointer = pointer.next
            outputText = outputText + "NIL"
            print(outputText)
            
            
def main():
    SLL = SinglyLinkedList()
    SLL.printSLLContent()
    SLL.int_list_delete(20)
    SLL.printSLLContent()
    SLL.int_list_insert(1)
    SLL.int_list_insert(3)
    SLL.int_list_insert(4)
    SLL.int_list_insert(2)
    SLL.printSLLContent()
    SLL.int_list_delete(3)
    SLL.printSLLContent()

if __name__ == "__main__":
    main()