from linkedlist import Node, LinkedList

class Stack(LinkedList):
    
    def push(self, value):
        self.prepend(value)
    
    def pop(self):
        value = self.lookup(0)
        self.remove(0)
        return value

    def peek(self):
        return self.lookup(0)


class Queue(Stack):
    def push(self, value):
        self.append(value)




if __name__ == '__main__':
    print('Stack'.center(100, '*')) 
    a = Stack(5)
    print(a)
    a.push(3)
    print(a)
    print(a.peek())
    a.pop()
    print(a)

    print('Queue'.center(100, '*')) 
    b = Queue(5)
    print(b)
    b.push(3)
    print(b)
    print(b.peek())
    b.pop()
    print(b)
