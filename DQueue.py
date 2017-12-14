
class DQueue:
    def __init__(self):
        self.dequeue = []

    def isEmpty(self):
        return self.dequeue == []

    def addBegin(self, item):
        self.dequeue.insert(0,item)

    def addEnd(self, item):
        self.dequeue.append(item)

    def remBegin(self):
        self.dequeue.pop(0)

    def remEnd(self):
        self.dequeue.pop()

    def displayDQueue(self):
        print self.dequeue
