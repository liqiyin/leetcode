class node:
    def __init__(self, data, node):
        self.data = data
        self.next = node

def solution(node):
    cur = node
    last = None
    while cur:
        temp = cur
        cur = cur.next
        temp.next = last
        last = temp
    return last

node1 = node(1, None)
node2 = node(2, node1)
node3 = node(3, node2)
node4 = node(4, node3)
node5 = node(5, node4)

test = solution(node5)
while test:
    print test.data
    test = test.next
