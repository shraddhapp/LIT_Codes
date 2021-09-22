class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # if key not in self.hash:
        self.hash[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hash:
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hash:
            del self.hash[key]
