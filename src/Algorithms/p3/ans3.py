#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)
        qml.QFT(wires=wires)

        cte = 2*np.pi*m/(2**n_wires -1)


        for k in wires:
          qml.RZ(-2*cte, wires=k)
          qml.PhaseShift(cte, wires=k)

        for i in range(len(wires)-1):
          if(i%2 ==0):
            qml.CNOT(wires=[i,i+1])
          else:
            qml.CNOT(wires=[i+1,i])


        qml.QFT(wires=wires).inv()
        #return qml.state()

        return qml.sample()

    output = test_circuit()
    #print(output)
    print(*output, sep=",")
