class Node:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None

    def size(self):
        s = 1
        if self.left:
            s += self.left.size()

        if self.right:
            s += self.right.size()

        return s



    def height(self):
        s = 1
        if self.size() == 1:
            return s
        else:
            left_height = 0
            right_height = 0
            if self.left:
                left_height = self.left.height()
            if self.right:
                right_height = self.right.height()

            s += max(left_height, right_height)

        return s

    def level(self, root):
        return (root.height() - self.height())


if __name__ == '__main__':
    root_node = Node('uggla')

    n1 = Node("hamster")
    root_node.left = n1

    n2 = Node("pingvin")
    root_node.right = n2

    n3 = Node("apa")
    n1.left = n3

    n4 = Node("häst")
    n1.right = n4

    n5 = Node("varg")
    n2.right = n5

    n6 = Node("gorilla")
    n3.right = n6

    n7 = Node("lemur")
    n4.right = n7

    print(root_node.size())
    print(root_node.height())

    print(n3.level(root_node))
    print(n6.level(root_node))
    print(n7.level(n6))
