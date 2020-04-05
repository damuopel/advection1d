import numpy as np
import matplotlib.pyplot as plt
import FEM.FEM as FEM

if __name__ == '__main__':
    # Input User
    eSize = 1
    xElms = 20
    yElms = 5
    E = 2.1e11
    nu = 0.3
    thickness = 0.1
	# Create Mesh
    Topology,XY = FEM.Mesh(eSize,xElms,yElms)
    D = FEM.D_Matrix(E,nu)
    K = FEM.K_Matrix(Topology,XY,D,thickness)
    F = FEM.F_Array(Topology,XY)
    u = FEM.Solver(K,F,Topology,XY)
    # Post Process Data
    # Stresses
    # Plot Results
    dofs = int(XY.size/2)*2
    xDofs = np.arange(0,dofs,2)
    yDofs = np.arange(1,dofs,2)
    xDisp = u[xDofs]
    yDisp = u[yDofs]
    disp = (xDisp**2+yDisp**2)**(0.5)
    x = XY[0,:].reshape(yElms+1,xElms+1)
    y = XY[1,:].reshape(yElms+1,xElms+1)
    plt.pcolor(x,y,disp.reshape(yElms+1,xElms+1))
    plt.colorbar()
    plt.xlim(0,xElms*eSize)
    plt.ylim(0,yElms*eSize)
    plt.axis('equal')
    plt.axis('off')
    plt.show() 