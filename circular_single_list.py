class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next
    
    def createSingular(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "the circular single list has been created."

    def insertCll(self,value,location):
        if self.head is None:
            return "the list doesn't exist."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return " completed"

    def traversalCLL(self):
        if self.head is None:
            return " no elemnt in list"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCLL(self,nodeValue):
        if self.head is None:
            return " no elemnt in list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return " the node doesn't exist in this list."
    
    def deletionCLL(self,location):
        if self.head is None:
            return " no elemnt in list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next 
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntire(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circular_single_list = CircularList()
circular_single_list.createSingular(1)
circular_single_list.insertCll(1,0)
circular_single_list.insertCll(2,0)
circular_single_list.insertCll(3,0)
circular_single_list.insertCll(2,1)
circular_single_list.insertCll(2,1)
circular_single_list.insertCll(5,3)

print([node.value for node in circular_single_list])
# circular_single_list.traversalCLL()

# print(circular_single_list.searchCLL(2))
# print(circular_single_list.searchCLL(9))

# circular_single_list.deletionCLL(0)
# print([node.value for node in circular_single_list])

# circular_single_list.deletionCLL(4)
# print([node.value for node in circular_single_list])

# circular_single_list.deletionCLL(1)
# print([node.value for node in circular_single_list])