class TreeNode:
    def __init__(self, key, val ):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root:
            # find the place to insert
            curr = self.root

            while curr:
                if curr.key == key:
                    curr.val = val
                    return
                elif curr.key < key:
                    if not curr.right:
                        curr.right = TreeNode(key, val)
                        return
                    curr = curr.right
                else:
                    if not curr.left:
                        curr.left = TreeNode(key, val)
                        return
                    curr = curr.left                        
        else:
            self.root = TreeNode(key, val)


    def get(self, key: int) -> int:

        node = self._get_node(key)

        if node:
            return node.val
        return -1

    def _get_node(self, key):
        curr = self.root

        while curr:
            if curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        
        return None

    def getMin(self) -> int:

        min_node = self._get_min_node(self.root)
        if min_node:
            return min_node.val
        return -1
        
    def _get_min_node(self, node):
        
        if not node:
            return None

        curr = node

        while curr and curr.left:
            curr = curr.left
        
        return curr


    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root

        while curr and curr.right:
            curr = curr.right
        
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self._remove_node(self.root, key)


    def _remove_node(self, node, key):

        if not node:
            return None
        
        if node.key > key:
            node.left = self._remove_node(node.left, key)
        elif node.key < key:
            node.right = self._remove_node(node.right, key)
        else:
            # node to remove is found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._get_min_node(node.right)
                node.key = min_node.key
                node.val = min_node.val
                node.right = self._remove_node(node.right, min_node.key)
        return node

    def getInorderKeys(self) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.key)
            inorder(node.right)

        inorder(self.root)

        return res
