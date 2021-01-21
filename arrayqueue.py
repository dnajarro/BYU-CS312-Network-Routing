import math


# priority queue implemented as an array
class ArrayQueue:
    # array of node IDs
    def __init__(self):
        self.queue = []
        self.length = 0

    # adds the elements from a list to the queue
    def make_queue(self, elems):
        for i in elems:
            self.insert(i)

    # adds an element to the queue
    def insert(self, item):
        self.queue.append(item)
        self.length += 1

    # removes the element with the smallest weight from the queue
    def deletemin(self, distances):
        smallest = math.inf  # smallest distance
        node_id = None  # node with smallest distance
        index = None
        for i, x in enumerate(self.queue):
            if distances[self.queue[i]] <= smallest:
                smallest = distances[self.queue[i]]
                node_id = x
                index = i
        if index is not None:
            self.queue.pop(index)
            self.length -= 1
        return node_id

    # print the elements in the queue
    def to_string(self):
        print(self.queue)

    # does nothing
    def decreasekey(self):
        pass

    # returns the length of the queue
    def get_length(self):
        return self.length
