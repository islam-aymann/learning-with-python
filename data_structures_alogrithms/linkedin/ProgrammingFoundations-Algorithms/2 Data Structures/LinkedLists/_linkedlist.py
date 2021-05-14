class Node(object):
    def __init__(self, val):
        self._val = val
        self._next = None

    @property
    def data(self):
        return self._val

    @data.setter
    def data(self, value):
        self._val = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class LinkedList(object):
    def __init__(self, head: Node = None):
        self._head = head
        self._count = 0

    @property
    def count(self):
        return self._count

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def find(self, val):
        item = self._head
        while item:
            if item.data == val:
                return item
            item = item.next
        return None

    def delete_at(self, idx):
        if idx > self._count - 1:
            return
        elif idx == 0:
            self._head = self._head.next

        temp_idx = 0
        node = self._head

        while temp_idx < idx - 1:
            node = node.next
            temp_idx += 1

        node.next = node.next.next

        self._count -= 1

    def dump_list(self):
        temp_node = self._head
        while temp_node:
            print("Node:", temp_node.data)
            temp_node = temp_node.next


if __name__ == '__main__':
    item_list = LinkedList()
    item_list.insert(38)
    item_list.insert(49)
    item_list.insert(13)
    item_list.insert(15)
    item_list.dump_list()

    print("Item count:", item_list.count)
    print("Finding Item:", item_list.find(13))
    print("Finding Item:", item_list.find(78))
    print("=======================================")
    item_list.delete_at(3)
    print("Item count:", item_list.count)
    print("Finding item:", item_list.find(38))
    item_list.dump_list()
