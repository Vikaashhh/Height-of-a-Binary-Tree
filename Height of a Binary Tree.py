class Solution:
    # Function to find the height of a binary tree (in terms of edges)
    def height(self, root):
        # Agar root hi None hai toh -1 return karenge kyunki edge count karna hai
        if root is None:
            return -1

        # Left subtree ki height nikaalo
        left_height = self.height(root.left)

        # Right subtree ki height nikaalo
        right_height = self.height(root.right)

        # Dono me se jo badi ho, usme 1 add karo (current edge ke liye)
        return 1 + max(left_height, right_height)
