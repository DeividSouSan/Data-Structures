from .node import Node
class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def add(self, value) -> None:
        # A arvore está vazia
        if self.root is None:
            self.root = Node(value, None, None)
        else:
            currentNode: Node = self.root

            while currentNode.value is not value:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = Node(value, None, None)
                        currentNode = currentNode.left
                    else:
                        currentNode = currentNode.left

                elif value > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = Node(value, None, None)
                        currentNode = currentNode.right
                    else:
                        currentNode = currentNode.right

    def searchIterative(self, value):
        if self.root is None:
            print("Raiz é none")
            return False

        currentNode = self.root
        while currentNode is not None:
            print(currentNode.value)
            if currentNode.value == value:
                return True
            
            else:
                if value < currentNode.value:
                    currentNode = currentNode.left

                elif value > currentNode.value:
                    currentNode = currentNode.right
        
        return False
    
    def searchRecursive(self, currentNode, value):
        if currentNode is None:
            return False

        if currentNode.value == value:
            return True
        else:
            if value < currentNode.value:
                return self.searchRecursive(currentNode.left, value)
            elif value > currentNode.value:
                return self.searchRecursive(currentNode.right, value)
        
    def remove(self, value):
        # O valor não está na lista
        # O valor está no primeiro nó
        # Valor está em um galho
        # O valor está nas folhas
        pass