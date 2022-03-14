#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    w0, w1 = cnot.wires.toarray()

    # Checks if a is neighbour of b
    def check(a,b):
      if a in graph[b] or a == b:
        return True

    # Goes until we:
    #  - Find the target
    # - Goes back (cyclic) in to other neighbour
    # - Reach a dead end (no more neighbours)
    def breadth_search(a, b, neighbours):
      # We already looked here! (cyclic graph)
      if len(neighbours) == 0:
        return 0

      # Spreads and check each neighbour
      for n in neighbours:
        res = 0

        # Found the target !
        if check(w1,n):
          res += 1
          return res
        # We circled back to an existent neighbour
        elif n in looked: 
          return 0

        # We keep moving !
        else:
          res += 1
          looked.append(n)
          neigh_of_n = graph[n]

          # Neighbours we didn't check
          for l in looked:
            if l in neigh_of_n:
              neigh_of_n.remove(l)

          # We go again
          res += breadth_search(n, b, neigh_of_n)

      return res


    # They are neighbours
    if check(w0, w1):
      return 0

    looked = [w0]
    n_swaps = breadth_search(w0, w1, graph[w0])

    # Multiply by 2 for swapping everything back
    return 2*n_swaps 

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
