
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def add(self, item):
        self.queue.insert(0,item)

    def remove(self):
        self.queue.pop()

    def displayQueue(self):
        print(self.queue)
