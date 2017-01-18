operands = []
operators = []

def Node(data, next = None, prev = None):
    def get(msg):
        nonlocal data, next, prev
        if msg == 'data': return data 
        if msg == 'next': return next 
        if msg == 'prev': return prev 

    def set_new(msg, obj):
        nonlocal data, next, prev
        if msg == 'data':
            data = obj
        if msg == 'next':
            next = obj
        if msg == 'prev':
            prev = obj

    def getitem(i):
        nonlocal data, next, prev
        if i == 0:
            return self
        return self.next[i-1]

    def str():
        nonlocal data, next, prev
        if prev: prev = prev['get']('data')
        else: prev = None
        if next: next = next['get']('data')
        else: next = None
        return '{0} <-- {1} --> {2}'.format(prev, data, next)

    dispatch = {'get' : get, 'set' : set_new, 'getitem' : getitem, 'str' : str} 
    return dispatch

class LinkedList:
    def __init__( self ):
        self.head = None
        self.tail = None

    def addHead(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node['set']('next', self.head) # node.next = self.head
            node['get']('next')['set']('prev', node) # node.next.prev = node
            self.head = node

    def addTail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node['set']('prev', self.tail) # node.prev = self.tail
            node['get']('prev')['set']('next', node) # node.prev.next = node
            self.tail = node

    def search(self, k):
        p = self.head
        if p != None:
            while p != None:
                if (p.data == k):
                    return p
                p = p.next
        return None

    def remove(self, p):
        if p.prev != None: p.prev.next = p.next
        else: self.head = p.next
        if p.next != None: p.next.prev = p.prev
        else: self.tail = p.prev

    def __str__(self):
        s = '<'
        p = self.head
        if p != None:
            while p != None:
                s += str(p['get']('data'))
                p = p['get']('next')
        return s + '>'

    def __repr__(self):
        return str(self)

    def __getitem__(self, i):
        if i == 0:
            return self.head
        return self.head.next[i-1]

    def __len__(self):
        count = 0
        p = self.head
        if p != None:
            while p != None:
                p = p.next
                count += 1
            return count
        return 0

def StrToLinkedList(str):
    l = LinkedList()
    for i in str:
        l.addTail(i)
    return l

def Plus(list1, list2):
    def Add(x, y):
        return((int(x.data) if x is not None else 0) + (int(y.data) if y is not None else 0))
    l = LinkedList()
    p1, p2 = list1.tail, list2.tail
    while(p1 or p2):
        x = Add(p1, p2)
        l.addHead(x % 10)
        if x // 10 > 0:
            if p1.prev:
                p1.prev.data = int(p1.prev.data) + x // 10
            else:
                p1.prev = Node(x // 10)
        if p1: p1 = p1.prev
        if p2: p2 = p2.prev
    return l

def Sub(list1, list2):
    pass

def Mul(list1, list2):
    pass

def Div(list1, list2):
    pass

def Apply(x):
    if(x == '+'):
        return Plus
    elif(x == '-'):
        return Sub
    elif(x == '*'):
        return Mul
    elif(x == '/'):
        return Div

def Insert_Loop():
    global operands, operators
    l = LinkedList()
    x = ''
    while True:
        x = input('Put the number> ')
        if x == 'q': return        
        if (x in ('+', '-', '*', '/')):
            operators += x
        else:
            l = StrToLinkedList(x)
            operands += [l]

def Calc():
    global operands, operators
    while(len(operators) > 0):
        x = operators.pop()
        m = Apply(x)
        l = m(operands.pop(), operands.pop())
        operands += [l]

# Insert_Loop()
# Calc()
# print(operands)
# print(operators)
l = LinkedList()
l.addHead(1)
l.addHead(2)
l.addHead(3)
print(l)
