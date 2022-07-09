#pip install binarytree

from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print('Binary tree :', root)

# Getting list of nodes
print('List of nodes :', list(root))

# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)

# Checking tree properties
print('Size of tree :', root.size)
print('Height of tree :', root.height)

# Get all properties at once
print('Properties of tree : \n', root.properties)

"""
Binary tree : 
  3
 / \
6   8

List of nodes : [Node(3), Node(6), Node(8)]
Inorder of nodes : [Node(6), Node(3), Node(8)]
Size of tree : 3
Height of tree : 1
Properties of tree : 
 {'height': 1, 'size': 3, 'is_max_heap': False, 'is_min_heap': True, 'is_perfect': True, 'is_strict': True, 'is_complete': True, 'leaf_count': 2, 'min_node_value': 3, 'max_node_value': 8, 'min_leaf_depth': 1, 'max_leaf_depth': 1, 'is_balanced': True, 'is_bst': False, 'is_symmetric': False}

"""

# Creating binary tree
# from given list
from binarytree import build

# List of nodes
nodes = [3, 6, 8, 2, 11, None, 13]

# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree)

# Getting list of nodes from
# binarytree
print('\nList from binary tree :',
      binary_tree.values)

"""
Binary tree from list :
 
    ___3
   /    \
  6      8
 / \      \
2   11     13


List from binary tree : [3, 6, 8, 2, 11, None, 13]
"""

"""
Hash functions 
In computer programming hash functions map text (or other data) to integer numbers.
Python:
import hashlib, binascii
sha3_256hash = hashlib.sha3_256(b'hello').digest()
print("SHA3-256('hello') =", binascii.hexlify(sha3_256hash))

Example 1:
# Python hash() function example  
# Calling function  
result = hash(21) # integer value  
result2 = hash(22.2) # decimal value  
# Displaying result  
print(result)  
print(result2)
Output:
21
461168601842737174

Example 2:
text = 'Python Programming'

# compute the hash value of text
hash_value = hash(text)
print(hash_value)

# Output: -966697084172663693

Example 3:
# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))
Hash for 181 is: 181
Hash for 181.23 is: 530343892119126197
Hash for Python is: 2230730083538390373

"""

# Time Complexity
# https://wiki.python.org/moin/TimeComplexity
# https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
"""

The comment was referring to the Big-O Notation.
Briefly:
    1. O(1) means in constant time - independent of the number of items.
    2. O(N) means in proportion to the number of items.
    3. O(log N) means a time proportional to log(N)
Basically any 'O' notation means an operation will take time up to a maximum of k*f(N)
where:
k is a constant multiplier
f() is a function that depends on N

"""
# https://www.youtube.com/watch?v=8jafWpXPMBs

