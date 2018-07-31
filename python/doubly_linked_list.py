# Example of a doubly linked list
# Will expand upon this and clean it up eventually
# Could probably make something similar with a list of lists? Maybe more performant?
# Seems silly to have a class that's just a pretty simple data container.


class DoublyLinkedNode(object):
    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyLinkedNode(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def show(self):
        print("Show list data:")
        current_node = self.head
        while current_node is not None:
            print("Previous: ", current_node.prev.data) if hasattr(current_node.prev, "data") else None,
            print("Current: ", current_node.data),
            print("Next: ", current_node.next.data) if hasattr(current_node.next, "data") else None

            current_node = current_node.next


d = DoublyLinkedList()

d.append(5)
d.append(6)
d.append(50)
d.append(30)

d.show()

d.remove(50)
d.remove(5)

d.show()
