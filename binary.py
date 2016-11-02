"""Class implementing binary search algorithm"""

class BinarySearch(object):
    #  constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alist = [x for x in range(b, (a*b)+1, b)]  # generate list here
        self.length = len(self.alist)

    # Method to ensure class object is accessed through indexing

    def __getitem__(self, item):
        return self.alist[item]

    def __setitem__(self, item, value):
        return self.alist[item] == value

    """Search method to find if the value is in the list"""

    def search(self, value):
        self.value = value
        first = 0
        last = len(self.alist) - 1
        count = 0

        # check if value is == to first or last elements first
        if self.alist[first] == value:
            return {'count': 0, 'index': first}

        if self.alist[last] == value:
            return {'count': 0, 'index': last}

        # if not loop through the list while updating the count
        while first <= last:
            mid = (first + last) // 2
            count += 1
            if self.alist[mid] == value:

                return {'count': count, 'index': mid}

            elif value > self.alist[mid]:
                first = mid + 1

            elif value < self.alist[mid]:
                last = mid - 1

        # for value > last item. value out of range
        if first > last:

            return {'count': 0, 'index': -1}

    """Try searching recursively """
    def search_r(self, element, first=0, last=None, count=0):

        if not first:
            last = self.length - 1
        if element == self[first]:
            return {'index': first, 'count': count}
        elif element == self[last]:
            return {'index': last, 'count': count}
        mid = (first + last) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            first = mid + 1
        elif element < self[mid]:
            last = mid - 1
        if first >= last:
            return {'index': -1, 'count': count}
        count += 1
        return self.search(element, first, last, count)


"""do some test here simple test here first"""
"""
    bsearch = BinarySearch(20, 1)
    csearch = BinarySearch(100,10)
    #print(csearch.alist)
    print(csearch.search(10000))

"""






