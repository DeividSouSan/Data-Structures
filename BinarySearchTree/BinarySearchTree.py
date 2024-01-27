from .Node import Node
class BinarySearchTree:
    def __init__(self):
        self.root: Node = None
        self.left: Node = None
        self.right: Node = None

    def add(self, value) -> None:
        # A arvore está vazia
        if self.root is None:
            self.root = Node(value, None, None)

        else:
            currentNode: Node = self.root

            while currentNode.value is not value:
                if value < currentNode.value:
                    if currentNode.left is None:
                        print(f"O valor {value} foi adicionado à esquerda de {currentNode.value}")
                        currentNode.left = Node(value, None, None)
                        currentNode = currentNode.left
                    else:
                        currentNode = currentNode.left

                elif value > currentNode.value:
                    if currentNode.right is None:
                        print(f"O valor {value} foi adicionado à direita de {currentNode.value}")
                        currentNode.right = Node(value, None, None)
                        currentNode = currentNode.right
                    else:
                        currentNode = currentNode.right