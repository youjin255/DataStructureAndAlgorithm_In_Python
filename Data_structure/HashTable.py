class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)//size

    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nexthash=self.rehash(key,len(self.slots))
                while self.slots[nexthash] !=None and self.slots[nexthash] != key:
                    nexthash=self.rehash(nexthash,len(self.slots))

                if self.slots[nexthash] == None:
                    self.slots[nexthash] = key
                    self.data[nexthash] = data

                else:
                    self.data[nexthash]=data
    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        stop=False
        found = False
        position=startslot
        data=None

        while self.slots[position] !=None and not stop and not found:

            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position==startslot:
                    stop=True
        return data

    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        self.put(key,data)

H=HashTable()
H.put(1,'fuck')
H.put(2,'shit')
print(H[1])