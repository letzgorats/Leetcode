# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # the list of NestedInteger elements to be flattened
        self.nestedList = nestedList

        # the flattened list of integers
        self.flattenedList = []

        # Indecx to keep track of the current position in the flattenedList
        self.currentIndex = 0

        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    # Recursively flatten nested lists
                    flatten(item.getList())
        
        flatten(self.nestedList)

    # Returns the next integer in the flattened list
    def next(self):
        """
        :rtype: int
        """
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        
        return number
        
    # Checks if therer are more integers in the flattened list
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currentIndex < len(self.flattenedList)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
