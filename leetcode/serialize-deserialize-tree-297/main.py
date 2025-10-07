# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []
        q = deque([root])

        while q:
            qlen = len(q)

            for _ in range(qlen):
                node = q.popleft()
               
                if node:
                    res.append(f"{node.val}")
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("null")
        
        while res and res[-1] == "null":
            res.pop()

        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # print(data)
        # 1,2,3,null,null,4,5
        #     p           c c
        # p=2 => c1=5, c2=6
        # c1=2p-1, c2=2p
        # p=0 => c1=1, c2=2
        # 

        if data == "" or data is None:
            return None

        vals = data.split(',')
        root = TreeNode(int(vals[0])) # 0-index is always parent node
        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft()
            if vals[i] != "null":
                left_node = TreeNode(int(vals[i]))
                q.append(left_node)
                node.left = left_node
            i += 1

            if i < len(vals) and vals[i] != "null":
                right_node = TreeNode(int(vals[i]))
                q.append(right_node)
                node.right = right_node
            i += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
