from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.datastore =  {}
        self.access_store = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.datastore.keys():
            return -1
        else:
            self.access_store[key] = 1
            self.access_store.move_to_end(key)
            print(self.access_store)
            return self.datastore[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.datastore.keys():
            if len(self.datastore) < self.capacity:
                self.access_store[key] = value
                self.datastore[key] = value
            else:
                self.datastore[key] = value
                popval = self.access_store.popitem(last=False)[0]
                print("Trying to pop",popval)
                self.datastore.pop(popval)
        else:
            self.access_store[key] = 1
            self.access_store.move_to_end(key)
            self.datastore[key] = value



# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
