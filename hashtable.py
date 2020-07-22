class HashTable:
    def __init__(self, length):
        self.length = length
        self.lut = [[] for _ in range(length)]
    
    def _hash(self, key):
        return sum([ord(c) for c in key]) % self.length
    
    def set(self, key, value):
        hashval = self._hash(key)
        self.lut[hashval].append((key, value))
        print(self.lut)

    def get(self, key):
        hashval = self._hash(key)
        for x in self.lut[hashval]:
            if x[0] == key:
                found = True
                return x[1]
        
        raise ValueError('Key not found')


ht = HashTable(50)
ht.set('guru', 36)
ht.set('urug', 63)
print(ht.get('guru'))
print(ht.get('anu'))


