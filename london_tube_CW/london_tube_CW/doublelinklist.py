class DoublyLinkList:

    class Node:
        def __init__(self, datavalue):
            self.datavalue = datavalue  # data element
            self.nextval = None
            self.prevval = None


    def __init__(self):
        self.headval = self.Node(None)
        self.tail = self.headval
        self.current = None

    def __iter__(self):
        self.current = None
        return self

    def __next__(self):
        if self.is_empty() or self.current == self.tail:
            raise StopIteration()
        elif self.current is None:
            self.current = self.headval
        self.current = self.current.get_next()
        return self.current

    def get_next(self, node):
        if node == self.tail:
            raise Exception("Cannot get the element after the trailer of this list")
        else:
            return node.get_next()

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # Adding data elements:
    def push(self, newVal):
        newNode = self.Node(newVal)
        newNode.nextval = self.headval
        if self.headval is not None:
            self.headval.prevval = newNode
        self.headval = newNode

    def insert(self, prev_node, newVal):
        if prev_node is None:
            return
        newNode = self.Node(newVal)
        newNode.nextval = prev_node.nextval
        prev_node.nextval = newNode
        newNode.prevval = prev_node
        if newNode.nextval is not None:
            newNode.nextval.prevval = newNode

    # Define the append method to add elements at the end:
    def append(self, newVal):
        newNode = self.Node(newVal)
        newNode.nextval = None
        if self.headval is None:
            newNode.prevval = None
            self.headval = newNode
            return
        last = self.headval
        while (last.nextval is not None):
            last = last.nextval
        last.nextval = newNode
        newNode.prevval = last
        return

    def listprint(self, node):
        while (node is not None):
            print(node.datavalue)
            last = node
            node = node.nextval

#dbllist = DoublyLinkList()
#dbllist.push(12)
#dbllist.push(8)
#dbllist.push(62)
#dbllist.insert(dbllist.headval.nextval, 13)
#dbllist.append(45)
#dbllist.listprint(dbllist.headval)