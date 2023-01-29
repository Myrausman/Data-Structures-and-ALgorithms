#implements Bag ADT container using a Python list structure

class Bag:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems
    def add(self, item):
        self._theItems.append(item)
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag."
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    def __iter__(self):
        return _BagIterator(self._theItems)

class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
if __name__ == '__main__':
    B =Bag()
    B.add(49)
    B.add(7)
    B.add(20)
    B.add(2)
    for item in B:
        print(item)

    #Create a BaGIterator for B
    # iterator=B.__iter__()
    # # Repeat the while loop until break is called
    # while True:
    #     try:
    #         '''get the next item from the Bag. If there are no more items
    #         the StopIteration exception is raised'''
    #         item=iterator.__next__()
    #         #perform the body of the loop
    #         print(item)
    #         # Catch the exception and break from the loop when we are done.
    #     except StopAsyncIteration:
    #         break