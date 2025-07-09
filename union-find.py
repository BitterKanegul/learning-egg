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

import numpy as np
import scipy as sc


# Inputs are (id, data)
# We need the ids to be partially ordered so that we can choose the 'better' one as our canonical representative.
# We can either take human input id or generate from data. For this purpose we take human input.
# An implementation of the Disjoint Set is present in https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.DisjointSet.html
#
