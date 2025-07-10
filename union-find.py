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


    def merge(self, x, y):

    def connected(self, x, y):

    def subset(self, x):

    def subsets(self):



# Some of the implementation techniques I see from other places:
# Scipy uses the path halving variant for find (__getitem__)
#   Merge by Size is used in the merge method.
#
