class Queue:
    def __init__(self):
        self._qHead = None
        self._tail = None
        self._count = 0
        
    def isEmpty(self):
        return self._qHead is None
    
    def __len__(self):
        return self._count
    
    def enqueue(self, item):
        node = _QueueNode(item)
        if self._tail is None:  # if the queue is empty
            self._qHead = node
        else:
            self._tail.next = node
        self._tail = node
        self._count += 1
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qHead
        if self._qHead is self._tail:  # if there is only one item in the queue
            self._tail = None
            self._qHead = None
        else:
            self._qHead = self._qHead.next
        self._count -= 1
        return node.item

class _QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None