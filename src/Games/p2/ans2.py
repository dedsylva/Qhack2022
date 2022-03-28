#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


dev = qml.device("default.qubit", wires=2)


def prepare_entangled(alpha, beta):
    """Construct a circuit that prepares the (not necessarily maximally) entangled state in terms of alpha and beta
    Do not forget to normalize.

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>
    """

    # QHACK #
    # We need to multiply by sqrt(2) because of Hadamard
    a = np.sqrt(2)*alpha/(np.sqrt(alpha**2 + beta**2))
    b = np.sqrt(2)*beta/(np.sqrt(alpha**2 + beta**2))

    # Our custom CNOT with the apropriate constants
    U = np.array([[a, 0., 0., 0.],
                  [0., a, 0., 0.],
                  [0., 0., 0., -b],
                  [0., 0., -b, 0.]])

    # Transforming |0> into 1/sqrt(2) * (|0> + |1>)
    qml.Hadamard(0)

    qml.QubitUnitary(U, wires=[0,1])
    # QHACK #

@qml.qnode(dev)
def chsh_circuit(theta_A0, theta_A1, theta_B0, theta_B1, x, y, alpha, beta):
    """Construct a circuit that implements Alice's and Bob's measurements in the rotated bases

    Args:
        - theta_A0 (float): angle that Alice chooses when she receives x=0
        - theta_A1 (float): angle that Alice chooses when she receives x=1
        - theta_B0 (float): angle that Bob chooses when he receives x=0
        - theta_B1 (float): angle that Bob chooses when he receives x=1
        - x (int): bit received by Alice
        - y (int): bit received by Bob
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (np.tensor): Probabilities of each basis state
    """

    prepare_entangled(alpha, beta)

    # QHACK #
    if x == 0:
      thetaA = theta_A0
    else:
      thetaA = theta_A1
             
    if y == 0:
      thetaB = theta_B0
    else:
      thetaB = theta_B1
             

    # Rotation basis for Alice's qubit
    Ua = np.array([[np.cos(thetaA), np.sin(thetaA)],
                  [-np.sin(thetaA), np.cos(thetaA)]])

    qml.QubitUnitary(Ua, wires=0)


    # Rotation basis for Bob's qubit
    Ub = np.array([[np.cos(thetaB), np.sin(thetaB)],
                  [-np.sin(thetaB), np.cos(thetaB)]])

    qml.QubitUnitary(Ub, wires=1)

    # QHACK #

    return qml.probs(wires=[0, 1])
    

def winning_prob(params, alpha, beta):
    """Define a function that returns the probability of Alice and Bob winning the game.

    Args:
        - params (list(float)): List containing [theta_A0,theta_A1,theta_B0,theta_B1]
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning the game
    """

    # QHACK #
    res = [0.]*4
    x,y = 0,0
    # a=b=0, a=b=1, i.e., |00> , |11>
    probs = chsh_circuit(params[0], params[1], params[2], params[3],
                         x, y, alpha, beta)
    res[0] = probs[0] + probs[3]

    x,y = 0,1
    # a=b=0, a=b=1, i.e., |00> , |11>
    probs = chsh_circuit(params[0], params[1], params[2], params[3],
                         x, y, alpha, beta)
    res[1] = probs[0] + probs[3]

    x,y = 1,0
    # a=b=0, a=b=1, i.e., |00> , |11>
    probs = chsh_circuit(params[0], params[1], params[2], params[3],
                         x, y, alpha, beta)
    res[2] = probs[0] + probs[3]

    x,y = 1,1
    # a=1, b=0, a=0, b=1, i.e., |01> , |01>
    probs = chsh_circuit(params[0], params[1], params[2], params[3],
                         x, y, alpha, beta)
    res[3] = probs[1] + probs[2] 

    return sum(res)/4



    # QHACK #
    

def optimize(alpha, beta):
    """Define a function that optimizes theta_A0, theta_A1, theta_B0, theta_B1 to maximize the probability of winning the game

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning
    """

    def cost(params):
        """Define a cost function that only depends on params, given alpha and beta fixed"""
        

        # We want to make loss small, aka making prob of losing small
        res = winning_prob(params, alpha, beta)
        return 1 - res 


    # QHACK #

    #Initialize parameters, choose an optimization method and number of steps
    # We need that tensoooorrr with the gradd
    init_params = np.ones(4, requires_grad=True) 
    opt = qml.GradientDescentOptimizer(0.6)
    steps = 100

    # QHACK #
    
    # set the initial parameter values
    params = init_params

    for i in range(steps):
        # update the circuit parameters 
        # QHACK #

        params = opt.step(cost, params)

        # Thetas between - 2pi and 2pi
        params = np.clip(opt.step(cost,params), -2 * np.pi, 2*np.pi)

        # QHACK #

    return winning_prob(params, alpha, beta)


if __name__ == '__main__':
    inputs = sys.stdin.read().split(",")
    output = optimize(float(inputs[0]), float(inputs[1]))
    print(f"{output}")
