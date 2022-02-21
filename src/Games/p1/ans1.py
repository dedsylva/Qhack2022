#!/usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


def second_renyi_entropy(rho):
    """Computes the second Renyi entropy of a given density matrix."""
    # DO NOT MODIFY anything in this code block
    rho_diag_2 = np.diagonal(rho) ** 2.0
    return -np.real(np.log(np.sum(rho_diag_2)))


def compute_entanglement(theta):
    """Computes the second Renyi entropy of circuits with and without a tardigrade present.

    Args:
        - theta (float): the angle that defines the state psi_ABT

    Returns:
        - (float): The entanglement entropy of qubit B with no tardigrade
        initially present
        - (float): The entanglement entropy of qubit B where the tardigrade
        was initially present
    """

    dev = qml.device("default.qubit", wires=3)

    # QHACK #
  
    @qml.qnode(dev)
    def get_density(w):
      return qml.density_matrix([w]) 

    # | > AB
    qml.Hadamard(0)
    #qml.CNOT(wires=[0,1])

    ent_no_tardigrade = get_density(1)
    ent_nt = second_renyi_entropy(ent_no_tardigrade) #should give 0.693
    print('**** Without tardigrade ****')
    print(ent_no_tardigrade)
    print(ent_nt)


    # | > ABT
    qml.PhaseShift(theta, wires=0)
    qml.PhaseShift(theta, wires=1)
    qml.CNOT(wires=[0,2])

    ent_with_tardigrade = get_density(1)
    ent_t = second_renyi_entropy(ent_with_tardigrade)
    print('**** With tardigrade ****')
    print(ent_with_tardigrade)
    print(ent_t)

    exit(0)

    return [ent_nt, ent_t]


    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    theta = np.array(sys.stdin.read(), dtype=float)

    S2_without_tardigrade, S2_with_tardigrade = compute_entanglement(theta)
    print(*[S2_without_tardigrade, S2_with_tardigrade], sep=",")
