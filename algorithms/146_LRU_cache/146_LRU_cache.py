"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache(object):

    """LRUCache"""

    def __init__(self, capacity):
        """LRU cache initialization

        :param capacity: TODO

        """
        self._capacity = capacity
        self.cache = {}
        self.age = {}

    def get(self, key):
        """Returns the val

        :param key: TODO
        :returns: TODO

        """
        if key not in self.cache:
            return -1
        val = self.cache[key]

        for ind, item in self.age.items():
            self.age[ind] = item + 1
        self.age[key] = 0

        # print("GET: ", key, "  Cache:", self.cache)
        # print("GET: ", key, "  Cache:", self.age)
        # print("---------------------------------")

        return val

    def put(self, key, value):
        """TODO: Docstring for put.

        :param key: TODO
        :param value: TODO
        :returns: TODO

        """
        if len(self.cache) < self._capacity:
            # Capacity is there
            self.cache[key] = value
            self.age[key] = -1
            for ind, item in self.age.items():
                self.age[ind] = item + 1
        else:
            if key in self.cache:
                self.cache[key] = value
                self.age[key] = -1
            else:
                oldest_key = max(self.age, key=self.age.get)
                self.cache.pop(oldest_key)
                self.age.pop(oldest_key)
                self.cache[key] = value
                self.age[key] = -1

            for ind, item in self.age.items():
                self.age[ind] = item + 1

        # print("PUT: ", key, "  Cache:", self.cache)
        # print("PUT: ", key, "  Cache:", self.age)
        # print("---------------------------------")


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
print(cache.get(2))
print(cache.put(2, 6))
print(cache.get(1))
print(cache.put(1, 5))
print(cache.put(1, 2))
print(cache.get(1))
print(cache.get(2))

