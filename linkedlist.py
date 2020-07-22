# from math import abs

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class DoubleNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


# class DoubleLinkedList:
#     def __init__(self, val):
#         node = DoubleNode(val)
#         self.head = node
#         self.tail = node
#         self.length = 1

#     def traverse(self, index):
#         diff_start = abs(index - 0)
#         diff_end = abs(index - self.length-1)
#         ltor = diff_start <= diff_end

#         if index == 0:
#             return self.head
#         elif index == self.length - 1:
#             return self.tail
#         else:
#             if ltor:
#                 i = 0
#                 node = self.head
#                 while i < self.length:
#                     if i == index:
#                         return node
#                     i += 1
#                     node = node.next
#             else:
#                 i = self.length - 1
#                 node = self.tail
#                 while i >= 0:
#                     if i == index:
#                         return node
#                     i = i - 1
#                     node = node.prev

#     def append(self, val):
#         node = DoubleNode(val)
#         self.tail.next = node
#         node.prev = self.tail
#         self.tail = node
#         self.length += 1

#     def prepend(self, val):
#         node = DoubleNode(val)
#         node.next = self.head
#         self.head.prev = node
#         self.head = node
#         self.length += 1

#     def lookup(self, index):   
#         node = self.traverse(index)
#         return node.value

#     def insert(self, index, value):
#         node = DoubleNode(value)
#         prev = self.traverse()

    
class LinkedList:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        self.length = 1
    
    def append(self, val):
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def lookup(self, index):
        if index == 0:
            return self.head.value
        elif index == self.length - 1:
            return self.tail.value
        else:
            i = 0
            node = self.head
            while i < self.length:
                if i == index:
                    return node.value
                i += 1
                node = node.next

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            i = 0
            node = self.head
            newnode = Node(value)
            while i < self.length:
                if i == index - 1:
                    newnode.next = node.next
                    node.next = newnode
                    self.length += 1
                    break
                i = i + 1
                node = node.next

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index >= self.length:
            raise ValueError('index out of bounds')
        else:
            i = 0
            node = self.head
            while i < self.length:
                if i == index - 1:
                    node.next = node.next.next
                    self.length -= 1
                    break
                i += 1
                node = node.next

    def __str__(self):
        s = 'Length: ' + str(self.length)
        node = self.head
        s += '\n[' 
        while node is not None:
            s = s +  str(node.value)
            if node.next is not None:
                s += ' '
            node = node.next
        s += ']'
        return s

if __name__ == '__main__':
    a = LinkedList(10)
    print(a)
    a.append(5)
    print(a)
    a.prepend(3)
    print(a)
    a.insert(1, 2)
    print(a)
    a.remove(2)
    print(a)
