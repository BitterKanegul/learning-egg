# An implementation of union find data structure and different test cases.
# 1. Using Python Classes to represent nodes.
# 2. Looking at existing implementations.
# 3. Large number of testcases
#       - Randomly generate input array and sequence of unions among them. Upto a million
#       - Correctness testcases, idempotence, reflexivity, disjointness
#           - exhaustive
#           - randomized

# What must a union-find data structure do?
# A Map from elements to representatives
#   - Each element maps to one representative.
#   - Every element is unique i.e. there are no two elements with the same id.
#   - Every element maps to one representative of the disjoint set it is a part of.
#   We have the following operations on a Disjoint Set structure:
#       - Find: Given an input element, find the canonical representative of the set it is a part of
#       - Merge: Given two elements, merge the sets that they are a part of.
#       - Add: Add a new element to the Map(by default it maps to itself)

# The Scipy implementation has the below API:
#   add (x) -> add to disjoint set
#   merge(x,y) -> merge the subsets of x and y
#   connected(x,y) -> test if x and y are in same subset
#   subset(x) -> get subset containing x
#   subsets() -> get all subsets in disjoint set
#  __getitem__(x) -> find the root element of x
#
import numpy as np
import scipy as sc
from operator import length_hint



# Inputs are (id, data)
# We need the ids to be partially ordered so that we can choose the 'better' one as our canonical representative.
# We can either take human input id or generate from data. For this purpose we take human input.
# An implementation of the Disjoint Set is present in https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.DisjointSet.html
# These guys do it in a general way, any Python object can be part of it (probably ones that can be hashed)


#Using the backing store as a Hashmap:
#  key is the item, value is the parent
#  add(x) is almost O(1)
#  merge(x,y) is : x.parent == y.parent == max(x.parent, y.parent)
#  one must also store the cardinality of the subset if we are using maximize cardinality as our criterion
# __getitem__(x) + path halving should be O(1) with a hash map + getting the parent + swapping parent
# connected(x,y) will be __getitem(x)__ ?= __getitem(y)__
# subset(x): -> we hit each item in the hashmap and check __getitem(i)__== __getitem(x)__
# subsets(): -> we hit each item, and add each parent to a hashset
#  scipy does the connected thing with the help of linked lists.


class MyDisjointSet:

    def __init__(self):
        self.__HM__ = dict()
        self.__size__=dict()

    def __getitem__(self, x):
        if x not in self.__HM__:
            raise KeyError(x)
        parent = x
        while parent != self.__HM__[parent]:
            self.__HM__[parent] = self.__HM__[ self.__HM__[parent]]
            parent = self.__HM__[parent]
        return parent

    def add(self, x):
        if x in self.__HM__:
            return
        self.__HM__[x] = x
        self.__size__[x] = 1;
        return self.__HM__[x]

    def merge(self, x, y):
        parent_x = self.__getitem__(x)
        parent_y = self.__getitem__(y)
        #we ensure that the size of the subset is stored as __size__[parent] = subset_size
        size_x = self.__size__[parent_x]
        size_y = self.__size__[parent_y]
        if size_x > size_y:
            self.__HM__[parent_y] = parent_x
            self.__size__[parent_x] = size_x + size_y
        else:
            self.__HM__[parent_x] = parent_y
            self.__size__[parent_y] = size_x + size_y

    def connected(self, x, y):
        return self.__getitem__(x) == self.__getitem__(y)

    def subset(self, x):
        #Here i am a little lazy and don't store a linked list among the different subsets, instead going over the entire Disjoint set
        subset_list = []
        parent_x = self.__getitem__(x)
        for e in self.__HM__:
            parent_e = self.__getitem__(e)
            if parent_e == parent_x:
                subset_list.append(e)
        return subset_list

    def subsets(self):
        #Create a hashmap with the parent as key, and a list containing the subset
        subset_dict ={}
        for e in self.__HM__:
            parent_e = self.__getitem__(e)
            if parent_e not in subset_dict:
                 subset_dict[parent_e] = []
            subset_dict[parent_e].append(e)

        return subset_dict




# Some of the implementation techniques I see from other places:
# Scipy uses the path halving variant for find (__getitem__)
#   Merge by Size is used in the merge method.
#

test = MyDisjointSet()
test.add('a')
test.add('b')
print(test.__getitem__('a'))
print(test.__getitem__('b'))
test.merge('a', 'b')
print(test.__getitem__('a'))
print(test.__getitem__('b'))
test.add('c')
print(test.subsets())


# =====================================================================
# TEST HARNESS
# =====================================================================
#       - Randomly generate input array and sequence of unions among them. Upto a million
#       - Correctness testcases, idempotence, reflexivity, disjointness
#           - exhaustive
#           - randomized

# idempotence disjoint.add(x) 1M times,  disjoint.merge(x,x) 1M times.
# disjointness test,  given random merges, test that the subsets don't contain any dupes
# compare with scipy too.


# Gonna have to do some profiling as well : https://docs.python.org/3/library/profile.html
# Pretty dang slow

def test_idempotence ():
    test = MyDisjointSet()
    for i in range(1000000):
        test.add('x')
    for i in range(1000000):
        test.merge('x','x')
    # print(f"subsets: {test.subsets()}")
    assert(len(test.subsets()) == 1)
    assert(test.subsets()['x'][0]=='x')
def test_single_set ():
    test = MyDisjointSet()
    for i in range(1000):
        test.add(i)
    for i in range(1000-1):
        test.merge(i,i+1)
    # print(f"subsets: {test.subsets()}")
    assert(len(test.subsets()) == 1)
def test_modulo_set (modulus):
    test = MyDisjointSet()
    for i in range(1000):
        test.add(i)
    for i in range(1000):
        test.merge(i, i% modulus)
    # print(f"subsets: {test.subsets()}")
    assert(len(test.subsets()) == modulus)
def test_modulo_set2 (modulus):
    test = MyDisjointSet()
    for i in range(1000):
        test.add(i)
    for i in range(1000):
        if i - modulus >= 0:
            test.merge(i, i-modulus)
    print(f"subsets: {test.subsets()}")
    assert(len(test.subsets()) == modulus)

test_idempotence()
test_single_set()
test_modulo_set(7)
test_modulo_set(42)
test_modulo_set2(7)
test_modulo_set2(42)
