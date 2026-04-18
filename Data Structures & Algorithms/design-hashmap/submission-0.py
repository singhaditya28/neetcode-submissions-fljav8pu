class MyHashMap:

    def __init__(self):
        self.arr=[]

    def put(self, key: int, value: int) -> None:
        # if 
        for i in self.arr:
            if key==i[0]:
                i[1]=value
                # print(self.arr)
                return
        self.arr.append([key,value])

    def get(self, key: int) -> int:
        for i in self.arr:
            if i[0]==key:
                return i[1]
            # print(self.arr)
        return -1

    def remove(self, key: int) -> None:
        for i in self.arr:
            if i[0]==key:
                self.arr.remove(i)
                return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)