# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class LCRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.my_dic = {}

    def get(self, key):
        if key in self.stack:
            self.stack.append(key)
            self.stack_operation()
            return self.my_dic[key]
        else:
            return -1

    def put(self, key, value):
        self.my_dic[key] = value
        self.stack.append(key)
        self.stack_operation()

    def stack_operation(self):
        if len(self.stack)>self.capacity:
            self.stack = self.stack[1:]

lcr = LCRUCache(2)
lcr.put(2,2)
lcr.put(3,3)
lcr.put(4,4)
print(lcr.get(3))
lcr.put(5,5)
print(lcr.get(4))