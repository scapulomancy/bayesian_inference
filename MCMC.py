import numpy as np
import scipy.linalg as lin

def iterate_markov(M, state):
    elements = list(range(len(M)))
    transitions = M[state]
    return np.random.choice(elements, 1, p=transitions)[0]


def n_iterate_markov(M, initial_state, n):
    state = initial_state
    states = [initial_state]
    for i in range(n):
        state = iterate_markov(M, state)
        states += [state]
    return states


M = np.array([[1/2,0,0,0,1/2],[0,1/2,0,1/2,0],[0,0,1,0,0],[0,1/4,1/4,1/4,1/4],[1/2,0,0,0,1/2]])
