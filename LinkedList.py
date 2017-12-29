
class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:

    def __init__(self):
        self.head = None

    def addElements(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            if current.getData() == item:
                print("Element found at position: {}".format(count))
                break
            else:
                current = current.getNext()

    def remove(self,item):

        current = self.head
        count = 0
        previous = None
        found = False
        while found == False:
            count = count + 1

            if current.getData() == item:
                found = True
                print("Removing element")

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
