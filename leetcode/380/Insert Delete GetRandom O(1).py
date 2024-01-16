# O(1)

import random
class RandomizedSet(object):

    def __init__(self):
        self.data_map = {}
        self.data = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data_map:
            return False

        last_element_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_element_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_element_in_list

        self.data[-1] = val
        self.data.pop()

        self.data_map.pop(val)
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
  

# O(n)
import random
class RandomizedSet(object):

    def __init__(self):
        self.sets = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            return False
        
        self.sets.add(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            self.sets.remove(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.sets) == 0:
            return False
        return random.choice(list(self.sets))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
