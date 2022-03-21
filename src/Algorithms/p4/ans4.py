#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np
from pennylane.templates import QuantumPhaseEstimation


dev = qml.device("default.qubit", wires=8)

def oracle_matrix(indices):
    """Return the oracle matrix for a secret combination.

    Args:
        - indices (list(int)): A list of bit indices (e.g. [0,3]) representing the elements that are map to 1.

    Returns:
        - (np.ndarray): The matrix representation of the oracle
    """

    # QHACK #
    my_array = np.zeros((2 ** 4, 2 ** 4))

    # Putting -1 only on entries x such that f(x) = 1
    for i in indices:
      my_array[i][i] = -1

    # QHACK #

    return my_array


def diffusion_matrix():

    # DO NOT MODIFY anything in this code block

    psi_piece = (1 / 2 ** 4) * np.ones(2 ** 4)
    ident_piece = np.eye(2 ** 4)
    return 2 * psi_piece - ident_piece


def grover_operator(indices):

    # DO NOT MODIFY anything in this code block

    return np.dot(diffusion_matrix(), oracle_matrix(indices))



@qml.qnode(dev)
def circuit(indices):
    """Return the probabilities of each basis state after applying QPE to the Grover operator

    Args:
        - indices (list(int)): A list of bits representing the elements that map to 1.

    Returns:
        - (np.tensor): Probabilities of measuring each computational basis state
    """

    # QHACK #

    target_wires =range(4)

    estimation_wires =range(4,8)
    

    # Build your circuit here
    qml.PauliZ(0)

    qpe = QuantumPhaseEstimation(grover_operator(indices), target_wires, estimation_wires)
    #print(qpe)
    #return qml.state()

    # QHACK #

    return qml.probs(estimation_wires)

def number_of_solutions(indices):
    """Implement the formula given in the problem statement to find the number of solutions from the output of your circuit

    Args:
        - indices (list(int)): A list of bits representing the elements that map to 1.

    Returns:
        - (float): number of elements as estimated by the quantum counting algorithm
    """

    # QHACK #
    mapping = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100',
               5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001',
               10: '1010', 11: '1011', 12: '1100', 13: '1101', 
               14: '1110', 15: '1111'}
    probs = circuit(indices)
    theta = int(bytes(mapping[np.argmax(probs)], encoding='UTF-8'))
    print(np.argmax(probs), theta)
    M = 16*np.sin(theta/2)**2 

    return M

    # QHACK #

def relative_error(indices):
    """Calculate the relative error of the quantum counting estimation

    Args:
        - indices (list(int)): A list of bits representing the elements that map to 1.

    Returns: 
        - (float): relative error
    """

    # QHACK #
    estimated = number_of_solutions(indices)
    rel_err = (estimated/len(indices) - 1)*100

    # QHACK #

    return rel_err

if __name__ == '__main__':
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    lst=[int(i) for i in inputs]
    output = relative_error(lst)
    print("the end")
    print(f"{output}")
