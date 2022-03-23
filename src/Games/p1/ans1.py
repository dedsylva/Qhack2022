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
    def density_no_tardigrade():
      qml.Hadamard(0)
      qml.CNOT(wires=[0,1])
      return qml.density_matrix([1]) 


    @qml.qnode(dev)
    def density_with_tardigrade():
      qml.Hadamard(0)

      qml.CRY(theta, wires=[0,2])
      qml.Toffoli(wires=[0,2,1])
      qml.CNOT(wires=[0,1])

      qml.PauliX(0)

      return qml.density_matrix([1]) 


    # | > AB

    ent_no_tardigrade = density_no_tardigrade()
    ent_nt = second_renyi_entropy(ent_no_tardigrade) #should give 0.693

    # | > ABT
    ent_with_tardigrade = density_with_tardigrade()
    ent_t = second_renyi_entropy(ent_with_tardigrade)

    return [ent_nt, ent_t]


    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    theta = np.array(sys.stdin.read(), dtype=float)

    S2_without_tardigrade, S2_with_tardigrade = compute_entanglement(theta)
    print(*[S2_without_tardigrade, S2_with_tardigrade], sep=",")
