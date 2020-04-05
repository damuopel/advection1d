import numpy as np
import matplotlib.pyplot as plt
import FEM.FEM as FEM
import sys

def InitialConditions():
    
    return u0

def Runge_Kutta():
    
    return u

if __name__ == '__main__':
    # User input
    fileName = sys.argv[0]
    h = sys.argv[1] # size of elements
    xElms = sys.argv[2] # elements in x direction
    yElms = sys.argv[3] # elements in y direction
    time = sys.argv[4] # span of time
    incrTime = sys.argv[5] # steps in iterative temporal solver
    # Create Mesh
    Topology,XYZ = FEM.Mesh(h,xElms,yElms)
    # Initial Conditions
    u = InitialConditions()
    # Boundary Conditions
    # Get Operators
    # Temporal Integration (SOLVER)
    steps = np.arange(0,time,incrTime)
    for iStep in steps:
        uin = u
        u = Runge_Kutta(uin)
    