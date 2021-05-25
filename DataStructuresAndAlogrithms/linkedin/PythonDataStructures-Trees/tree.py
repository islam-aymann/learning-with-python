def rotate_right(root):
    pivot = root.left
    reattach_node = pivot.right
    root.left = reattach_node
    pivot.right = root
    return pivot


def rotate_left(root):
    pivot = root.right
    reattach_node = pivot.left
    root.right = reattach_node
    pivot.left = root
    return pivot


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print('Not found!')

    def add(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
                self.left = self.left.fix_imbalance_if_exists()

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
                self.right = self.right.fix_imbalance_if_exists()

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self

    def delete(self, target):
        if self.data == target:
            if self.left and self.right:
                # RTFM: Right Tree Find Minimum
                min_value = self.right.find_min()
                self.data = min_value.data
                self.right = self.right.delete(min_value.data)
                return self

            else:
                return self.left or self.right

        if self.right and target > self.data:
            self.right = self.right.delete(target)

        if self.left and target < self.data:
            self.left = self.left.delete(target)

        return self.fix_imbalance_if_exists()

    def traverse_preorder(self):
        print(self.data, end=' ')

        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()

        print(self.data, end=' ')

        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()

        if self.right:
            self.right.traverse_postorder()

        print(self.data, end=' ')

    def height(self, h=0):
        lh = self.left.height(h + 1) if self.left else h
        rh = self.right.height(h + 1) if self.right else h

        return max(lh, rh)

    def get_nodes_at_depth(self, depth, nodes=None):
        if nodes is None:
            nodes = list()

        if depth == 0:
            nodes.append(self)
            return nodes

        if self.left:
            self.left.get_nodes_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        if self.right:
            self.right.get_nodes_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        return nodes

    def is_balanced(self):
        lh = self.left.height() + 1 if self.left else 0
        rh = self.right.height() + 1 if self.right else 0

        return abs(lh - rh) < 2

    def get_left_right_height_difference(self):
        lh = self.left.height() + 1 if self.left else 0
        rh = self.right.height() + 1 if self.right else 0
        return lh - rh

    def fix_imbalance_if_exists(self):
        if self.get_left_right_height_difference() > 1:
            if self.left.get_left_right_height_difference():
                return rotate_right(self)
            else:
                self.left = rotate_left(self.left)
                return rotate_right(self)

        elif self.get_left_right_height_difference() < -1:
            if self.right.get_left_right_height_difference():
                return rotate_left(self)
            else:
                self.right = rotate_right(self)
                return rotate_left(self)

        return self

    def re_balance(self):
        if self.left:
            self.left.re_balance()
            self.left = self.left.fix_imbalance_if_exists()
        if self.right:
            self.right.re_balance()
            self.right = self.right.fix_imbalance_if_exists()

    def to_str(self):
        return str(self.data) if self.is_balanced() else str(self.data) + '*'


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def add(self, data):
        self.root.add(data)
        self.root = self.root.fix_imbalance_if_exists()

    def delete(self, target):
        self.root = self.root.delete(target)

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_inorder(self):
        self.root.traverse_inorder()

    def traverse_postorder(self):
        self.root.traverse_postorder()

    def height(self):
        return self.root.height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)

    def re_balance(self):
        self.root.re_balance()
        self.root = self.root.fix_imbalance_if_exists()

    @staticmethod
    def _node_to_char(n, spacing):
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(n.to_str()) + 1
        return n.to_str() + (' ' * spacing)

    def print_shape(self, label=''):
        print(self.name + ' ' + label)
        height = self.root.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        # Root offset
        offset = int((width - 1) / 2)
        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(
                    ['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            row = self.root.get_nodes_at_depth(depth)
            print((' ' * offset) + ''.join(
                [self._node_to_char(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print('')


if __name__ == '__main__':
    # node = Node(10)
    # node.left = Node(5)
    # node.right = Node(15)
    #
    # node.left.left = Node(2)
    # node.left.right = Node(6)
    #
    # node.right.left = Node(13)
    # node.right.right = Node(1000)

    # print(node.right.data)
    # print(node.right.right.data)

    # tree = Tree(node, 'Ryan\'s Tree')

    # print(tree.name)
    # print(tree.root.left.data)
    # print(tree.root.right.data)

    # found = tree.root.search(1000)
    # print(found.data)
    #
    # found = tree.search(1000)
    # print(found.data)

    # node = Node(50)
    # node.left = Node(25)
    # node.right = Node(75)
    # node.left.left = Node(10)
    # node.left.right = Node(35)
    # node.left.right.left = Node(30)
    # node.left.right.right = Node(42)
    # node.left.left.right = Node(13)
    # node.left.left.left = Node(5)
    # node.left.left.left.left = Node(2)
    #
    # tree = Tree(node, 'Ryan\'s Tree')
    #
    # tree.traverse_preorder()
    # print()
    # tree.traverse_inorder()
    # print()
    # tree.traverse_postorder()
    # print()
    #
    # print(tree.height())
    # tree2 = Tree(Node(50), 'A very short tree')
    # print(tree2.height())

    # print(tree.get_nodes_at_depth(tree.height()))
    # print(tree.get_nodes_at_depth(3))

    # for i in range(tree.height()):
    #     print(' ' * (tree.height() - i ** 2), tree.get_nodes_at_depth(i))

    # tree = Tree(Node(50))
    # tree.root.left = Node(25)
    # tree.root.right = Node(75)
    #
    # tree.add(10)
    # tree.print_shape_shape()
    #
    # tree.add(76)
    # tree.print_shape_shape()
    #
    # tree.add(75)
    # tree.print_shape_shape()
    #
    # tree = Tree(Node(50))
    # tree.root.left = Node(25)
    # tree.root.right = Node(75)
    # tree.root.right.left = Node(67)
    # tree.root.right.right = Node(100)
    # tree.root.right.right.right = Node(120)
    # tree.root.right.right.left = Node(80)
    # tree.root.right.right.left.right = Node(92)
    #
    # tree.print_shape_shape()
    # print(tree.delete(75))
    # print(tree.delete(50))
    #
    # tree.print_shape_shape()

    # tree = Tree(Node(50))
    # tree.root.left = Node(25)
    # tree.root.right = Node(75)
    # tree.root.right.right = Node(100)
    # tree.root.right.right.right = Node(150)
    # print(tree.root.is_balanced())
    # print(tree.root.left.is_balanced())
    # print(tree.print_shape_shape())

    # unbalancedLeftLeft = Tree(Node(30), 'UNBALANCED LEFT LEFT')
    # unbalancedLeftLeft.root.left = Node(20)
    # unbalancedLeftLeft.root.left.right = Node(21)
    # unbalancedLeftLeft.root.left.left = Node(10)
    # unbalancedLeftLeft.root.left.left.left = Node(9)
    # unbalancedLeftLeft.root.left.left.right = Node(11)
    # unbalancedLeftLeft.print_shape()
    # unbalancedLeftLeft.root = rotate_right(unbalancedLeftLeft.root)
    # unbalancedLeftLeft.print_shape()
    #
    # unbalancedRightRight = Tree(Node(10), 'UNBALANCED RIGHT RIGHT')
    # unbalancedRightRight.root.right = Node(20)
    # unbalancedRightRight.root.right.left = Node(19)
    # unbalancedRightRight.root.right.right = Node(30)
    # unbalancedRightRight.root.right.right.left = Node(29)
    # unbalancedRightRight.root.right.right.right = Node(31)
    # unbalancedRightRight.print_shape()
    # unbalancedRightRight.root = rotate_left(unbalancedRightRight.root)
    # unbalancedRightRight.print_shape()
    #
    # unbalancedLeftRight = Tree(Node(30), 'UNBALANCED LEFT RIGHT')
    # unbalancedLeftRight.root.right = Node(31)
    # unbalancedLeftRight.root.left = Node(10)
    # unbalancedLeftRight.root.left.right = Node(20)
    # unbalancedLeftRight.root.left.left = Node(9)
    # unbalancedLeftRight.root.left.right.left = Node(19)
    # unbalancedLeftRight.root.left.right.right = Node(21)
    # unbalancedLeftRight.print_shape()
    #
    # unbalancedLeftRight.root.left = rotate_left(unbalancedLeftRight.root.left)
    # unbalancedLeftRight.root = rotate_right(unbalancedLeftRight.root)
    # unbalancedLeftRight.print_shape()
    #
    # unbalancedRightLeft = Tree(Node(30), 'UNBALANCED RIGHT LEFT')
    # unbalancedRightLeft.root.left = Node(31)
    # unbalancedRightLeft.root.right = Node(10)
    # unbalancedRightLeft.root.right.left = Node(20)
    # unbalancedRightLeft.root.right.right = Node(9)
    # unbalancedRightLeft.root.right.left.right = Node(19)
    # unbalancedRightLeft.root.right.left.left = Node(21)
    # unbalancedRightLeft.print_shape()
    #
    # unbalancedRightLeft.root.right = rotate_right(
    #     unbalancedRightLeft.root.right)
    # unbalancedRightLeft.root = rotate_left(unbalancedRightLeft.root)
    # unbalancedRightLeft.print_shape()
    #
    # tree = Tree(Node(50))
    # tree.root.left = Node(25)
    # tree.root.right = Node(75)
    # tree.root.left.left = Node(10)
    # tree.root.left.right = Node(35)
    # tree.root.left.right.left = Node(30)
    # tree.root.left.left.left = Node(5)
    # tree.root.left.left.right = Node(13)
    # tree.root.left.left.left.left = Node(2)
    # tree.root.left.left.left.left.left = Node(1)
    # tree.print_shape()
    #
    # tree.re_balance()
    # tree.print_shape()

    tree = Tree(Node(50))
    values = [25, 75, 10, 35, 30, 5, 2, 1]
    for value in values:
        tree.add(value)

    tree.print_shape()
    tree.delete(50)
    tree.delete(75)
    tree.print_shape()

