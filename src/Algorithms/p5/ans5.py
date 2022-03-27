#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def deutsch_jozsa(fs):
    """Function that determines whether four given functions are all of the same type or not.

    Args:
        - fs (list(function)): A list of 4 quantum functions. Each of them will accept a 'wires' parameter.
        The first two wires refer to the input and the third to the output of the function.

    Returns:
        - (str) : "4 same" or "2 and 2"
    """

    # QHACK #
    dev = qml.device("default.qubit", wires=3, shots=1)

    # Checks if third bit is 0 or 1
    def check_type(r):
      if r == 0:
        return 1,0
      else:
        return 0,1


    @qml.qnode(dev)
    def circuit0():
      # Prep state to |110>
      qml.PauliX(0)
      qml.PauliX(1)

      # Acts on function fi
      fs[0]([0,1,2])
      return qml.sample(wires=2)


    @qml.qnode(dev)
    def circuit1():
      # Prep state to |110>
      qml.PauliX(0)
      qml.PauliX(1)

      # Acts on function fi
      fs[1]([0,1,2])
      return qml.sample(wires=2)


    @qml.qnode(dev)
    def circuit2():
      # Prep state to |110>
      qml.PauliX(0)
      qml.PauliX(1)

      # Acts on function fi
      fs[2]([0,1,2])
      return qml.sample(wires=2)


    @qml.qnode(dev)
    def circuit3():
      # Prep state to |110>
      qml.PauliX(0)
      qml.PauliX(1)

      # Acts on function fi
      fs[3]([0,1,2])
      return qml.sample(wires=2)

    ITERATIONS = 50
    n_0, n_1, n_2, n_3 = 0, 0, 0, 0
    for n in range(ITERATIONS):
      res0 = circuit0()
      aux = 1 if res0 == 0 else 1
      n_0 += aux

      res1 = circuit1()
      aux = 1 if res1 == 0 else 1
      n_1 += aux

      res2 = circuit2()
      aux = 1 if res2 == 0 else 1
      n_2 += aux

      res3 = circuit3()
      aux = 1 if res3 == 0 else 1
      n_3 += aux

    # If fi always returns 0 or always returns 1, fi = constant
    # That means that the number of outputs equals to 0 is either 0 or ITERATIONS
    constant = [False, False, False, False]
    if n_0 == ITERATIONS or n_0 == 0:
      constant[0] = True 

    if n_1 == ITERATIONS or n_1 == 0:
      constant[1] = True 

    if n_2 == ITERATIONS or n_2 == 0:
      constant[2] = True 

    if n_3 == ITERATIONS or n_3 == 0:
      constant[3] = True 

    if constant.count(constant[0]) == len(constant):
      return "4 same"
    else:
      return "2 and 2"
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    # Definition of the four oracles we will work with.

    def f1(wires):
        qml.CNOT(wires=[wires[numbers[0]], wires[2]])
        qml.CNOT(wires=[wires[numbers[1]], wires[2]])

    def f2(wires):
        qml.CNOT(wires=[wires[numbers[2]], wires[2]])
        qml.CNOT(wires=[wires[numbers[3]], wires[2]])

    def f3(wires):
        qml.CNOT(wires=[wires[numbers[4]], wires[2]])
        qml.CNOT(wires=[wires[numbers[5]], wires[2]])
        qml.PauliX(wires=wires[2])

    def f4(wires):
        qml.CNOT(wires=[wires[numbers[6]], wires[2]])
        qml.CNOT(wires=[wires[numbers[7]], wires[2]])
        qml.PauliX(wires=wires[2])

    output = deutsch_jozsa([f1, f2, f3, f4])
    print(f"{output}")
