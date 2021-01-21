import math


# priority queue implemented as a min heap
class HeapQueue:
    def __init__(self):
        self.length = 0
        self.tree = []  # tree of node IDs

    # takes an elem in the queue based off of the index and moves it upward in the min heap if it has a smaller distance
    # than its parent
    def bubble_up(self, index, distances):
        if len(self.tree) > 1:
            child = self.tree[index]
            parent = self.get_parent(index)
            if parent is not None and child is not None:
                parent_weight = distances[parent]
                child_weight = distances[child]
                while parent_weight > child_weight:
                    child = self.tree[index]
                    parent = self.get_parent(index)
                    if parent is not None and child is not None:
                        child_weight = distances[child]
                        parent_weight = distances[parent]
                        self.tree[self.get_parent_index(index)] = child
                        self.tree[index] = parent
                        index = self.get_parent_index(index)
                    else:
                        break

    # takes an element in the queue based off of the index and moves it down by comparing it with its children
    # the parent is compared with the smallest weight of its children and switched if the smallest child is smaller
    def bubble_down(self, index, distances):
        # recursively moves down the heap
        while True:
            parent = self.tree[index]
            left_child = self.get_left_child(index)
            right_child = self.get_right_child(index)
            # gets the weights of the parent and its children
            left_child_weight = 0
            right_child_weight = 0
            if left_child is not None:
                left_child_weight = distances[left_child]
            if right_child is not None:
                right_child_weight = distances[right_child]
            parent_weight = distances[parent]
            if left_child is not None:
                if right_child is not None:
                    # compare left and right child to get smallest weight
                    if left_child_weight <= right_child_weight:
                        if left_child_weight < parent_weight:
                            self.tree[index] = left_child
                            self.tree[(index * 2) + 1] = parent
                            index = (index * 2) + 1
                        elif right_child_weight < parent_weight:
                            self.tree[index] = right_child
                            self.tree[(index * 2) + 2] = parent
                            index = (index * 2) + 2
                        else:
                            break
                    # if left child isn't less than or equal to right, right is smaller, so switch with parent
                    elif right_child_weight < parent_weight:
                        self.tree[index] = right_child
                        self.tree[(index * 2) + 2] = parent
                        index = (index * 2) + 2
                    else:
                        break
                # no right child, so compare left child
                elif left_child_weight < parent_weight:
                    self.tree[index] = left_child
                    self.tree[(index * 2) + 1] = parent
                    index = (index * 2) + 1
                else:
                    break
            elif right_child is not None:
                # only right child, so compare it with parent
                if right_child_weight < parent_weight:
                    self.tree[index] = right_child
                    self.tree[(index * 2) + 2] = parent
                    index = (index * 2) + 2
                else:
                    break
            else:
                break

    # add element to bottom of queue and bubble up
    def insert(self, item, distances):
        self.tree.append(item)
        self.length = len(self.tree)
        self.bubble_up(self.length - 1, distances)

    # add the elements of a list to the queue
    def make_queue(self, elems, distances):
        for i in elems:
            self.insert(i, distances)

    # pop the top element in the queue and bubble down
    def deletemin(self, distances):
        x = self.tree.pop(0)
        self.length = len(self.tree)
        if len(self.tree) > 0:
            self.tree.insert(0, self.tree[-1])
            self.tree.pop()
            self.bubble_down(0, distances)
        return x

    # print the contents of the queue
    def to_string(self):
        print(self.tree)

    # reorder the elements in the queue by bubbling down based off of an element whose weight just changed
    def decreasekey(self, node_id, distances):
        if len(self.tree) > 0:
            try:
                index = self.tree.index(node_id)
                self.bubble_up(index, distances)
            except ValueError:
                pass

    # get the parent node of a given node in the min heap
    def get_parent(self, index):
        if index != 0:
            return self.tree[math.floor((index - 1) / 2)]
        else:
            return None

    # get the left child of the given node in the min heap
    def get_left_child(self, index):
        if ((index * 2) + 1) < len(self.tree):
            return self.tree[(index * 2) + 1]
        else:
            return None

    # get the right child of the given node in the min heap
    def get_right_child(self, index):
        if ((index * 2) + 2) < len(self.tree):
            return self.tree[(index * 2) + 2]
        else:
            return None

    # get the index of the parent of a given node
    def get_parent_index(self, index):
        if index != 0:
            return math.floor((index - 1) / 2)
        else:
            return None
