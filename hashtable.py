class HashTable:
    def __init__(self):
        self.collection={}
    def hash(self,string):
        summ=0
        for i in string:
            summ+=ord(i)
        return summ
    def add(self,key,value):
        k=self.hash(key)
        if k not in self.collection:
            self.collection[k]={key:value}
        else:
            self.collection[k][key]=value
    def remove(self,key):
        k=self.hash(key)
        if k not in self.collection or key not in self.collection[k]:
            return
        del self.collection[k][key]
    def lookup(self,key):
        k=self.hash(key)
        if k not in self.collection or key not in self.collection[k]:
            return None
        return self.collection[k][key]
# Create hash table
ht = HashTable()

# Add key-value pairs
ht.add("apple", 10)
ht.add("banana", 20)

# Force a collision ("ab" and "ba" have same ASCII sum)
ht.add("ab", 1)
ht.add("ba", 2)

# Lookups
print(ht.lookup("apple"))    # Expected: 10
print(ht.lookup("banana"))   # Expected: 20
print(ht.lookup("ab"))       # Expected: 1
print(ht.lookup("ba"))       # Expected: 2

# Lookup non-existing key
print(ht.lookup("orange"))  # Expected: None

# Remove a key
ht.remove("ab")
print(ht.lookup("ab"))      # Expected: None
print(ht.lookup("ba"))      # Expected: 2 (should still exist)

# Remove non-existing key (should not crash)
ht.remove("xyz")

# Inspect internal structure (optional, for understanding)
print(ht.collection)
