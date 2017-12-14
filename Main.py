
from Stack import Stack
from Queue import Queue
from DQueue import DQueue

# Stack
def testStack():
    a = Stack()

    #Testing isEmpty()
    print a.isEmpty()

    #Testing Push
    for i in range(10):
        a.push(i)
        a.displayStack()

    #Testing pop
    a.pop()
    a.displayStack()

    #Testing isEmpty()
    print a.isEmpty()

def testQueue():
    a = Queue()

    #Testing isEmpty()
    print a.isEmpty()

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
    print a.isEmpty()

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
    print a.isEmpty()

#testStack()
#testQueue()
#testDQueue()
