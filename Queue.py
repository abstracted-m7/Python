#Write a Python program to organize an element of QUEUE using the ENQUEUE & DEQUEUE operation
class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, value):
        if value not in self.queue:
            return self.queue.insert(0, value)
        #     return True
        # return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Queue is Empty"

    def listprint(self):
        printvalue = self.queue
        if printvalue is not None:
            print(printvalue)
            return


q = Queue()
q.enqueue("x")
q.enqueue("Y")
q.enqueue("Z")
q.listprint()
q.dequeue()
q.listprint()