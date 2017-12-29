
from Stack import Stack
from Queue import Queue
from DQueue import DQueue
from LinkedList import Node
from LinkedList import UnorderedList

# Stack
def testStack():
    a = Stack()

    #Testing isEmpty()
    print(a.isEmpty())

    #Testing Push
    for i in range(10):
        a.push(i)
        a.displayStack()

    #Testing pop
    a.pop()
    a.displayStack()

    #Testing isEmpty()
    print(a.isEmpty())

def testQueue():
    a = Queue()

    #Testing isEmpty()
    print(a.isEmpty())

    #Testing adding
    for i in range(10):
        a.add(i)
        a.displayQueue()

    #Testing removing
    a.remove()
    a.displayQueue()

def testDQueue():
    a = DQueue()

    #Testing isEmpty()
    print(a.isEmpty())

    a.addBegin(0)
    a.displayDQueue()
    a.addBegin(1)
    a.displayDQueue()
    a.addEnd(2)
    a.displayDQueue()
    a.remBegin()
    a.displayDQueue()
    a.remEnd()
    a.displayDQueue()

    #Testing isEmpty()
    print(a.isEmpty())

def testLinkedList():
    node1 = Node(None)
    print(node1.next)
    print(node1.data)

    node2 = Node(None)
    node1.setNext(node2)

    print(node2)
    print(node1.getNext())

    if node2 == node1.getNext():
        print("Linked List successfully created")
    else:
        print("An error in the node creation")

    mylist = UnorderedList()
    mylist.addElements(31)
    mylist.addElements(77)
    mylist.addElements(17)
    mylist.addElements(93)
    mylist.addElements(26)
    mylist.addElements(54)

    mylist.search(31)
    mylist.search(54)

    mylist.remove(54)




#testStack()
#testQueue()
#testDQueue()
testLinkedList()
