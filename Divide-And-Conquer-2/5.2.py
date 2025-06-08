import random

class TreeNode:

    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                tempNode = TreeNode()
                tempNode.data = data
                self.left = tempNode
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                tempNode = TreeNode()
                tempNode.data = data
                self.right = tempNode
            else:
                self.right.insert(data)

    def traverseInOrder(self):
        if self is not None:
            if self.left is not None:
                self.left.traverseInOrder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.traverseInOrder()

    @staticmethod
    def createRoot():
        i = random.randint(0, 10)
        rootNode = TreeNode()
        rootNode.data = i
        return rootNode

    @classmethod
    def createTree(cls):
        rootNode = cls.createRoot()
        numNodes = random.randint(1, 10)
        currentNode = rootNode
        j = 0
        L = []

        while j < numNodes:
            newVal = random.randint(1, 20)
            if newVal not in L:
                currentNode.insert(newVal)
                L.append(newVal)
                j += 1
        rootNode.traverseInOrder()
        return rootNode

    @staticmethod
    def getSum(node):
        if node is None:
            return 0
        else:
            leftSum = TreeNode.getSum(node.left)
            rightSum = TreeNode.getSum(node.right)
            return node.data + leftSum + rightSum

rootNode = TreeNode.createTree()
print("\nSum =", TreeNode.getSum(rootNode))
