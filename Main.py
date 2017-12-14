
from Stack import Stack

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


testStack()
