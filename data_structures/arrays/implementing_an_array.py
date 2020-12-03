

class MyArray:

    def __init__(self):

        self.length = 0 
        self.data = {}

    def get(self, index):

        return self.data[index]

    def push(self, item):

        self.data[self.length] = item

        self.length += 1

        return self.length

    def delete(self, index):

        delete_item = self.data[index]

        for i in range(index, (self.length - 1)):

            self.data[i] = self.data[i+1]


        del self.data[self.length-1]
        self.length -= 1

        return delete_item

if __name__ == "__main__":

     new_array = MyArray()

     new_array.push("John")
     new_array.push("Robert")
     new_array.push("Hi")

     new_array.delete(1)

     print(new_array.__dict__) 