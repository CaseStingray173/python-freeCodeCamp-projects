class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print("None")

        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        print(ll_string)

    def insert_before(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_after(self, data):
        if self.head is None:
            self.insert_before(data)

        self.last.next_node = Node(data, None)
        self.last = self.last.next_node


