# capsule_3d.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # needed for 3D projection side‑effect

def plot_capsule_3d(radius=1.0, length=4.0, n_theta=40, n_z=80):
    """
    Simple axisymmetric capsule: cylinder + two hemispheres.
    """
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, projection='3d')

    # Cylinder
    z_cyl = np.linspace(-length/2, length/2, n_z)
    theta = np.linspace(0, 2*np.pi, n_theta)
    Zc, Th = np.meshgrid(z_cyl, theta)
    Xc = radius * np.cos(Th)
    Yc = radius * np.sin(Th)

    # Hemispheres
    phi = np.linspace(0, np.pi, n_z)
    Th_s, Ph_s = np.meshgrid(theta, phi)
    Xs_left  = radius * np.sin(Ph_s) * np.cos(Th_s)
    Ys_left  = radius * np.sin(Ph_s) * np.sin(Th_s)
    Zs_left  = -length/2 - radius * np.cos(Ph_s)
    Xs_right = radius * np.sin(Ph_s) * np.cos(Th_s)
    Ys_right = radius * np.sin(Ph_s) * np.sin(Th_s)
    Zs_right =  length/2 + radius * np.cos(Ph_s)

    # Draw
    ax.plot_surface(Xc, Yc, Zc, color='steelblue', alpha=0.9, linewidth=0)
    ax.plot_surface(Xs_left,  Ys_left,  Zs_left,  color='steelblue', alpha=0.9, linewidth=0)
    ax.plot_surface(Xs_right, Ys_right, Zs_right, color='steelblue', alpha=0.9, linewidth=0)

    ax.set_box_aspect([1, 1, (length+2*radius)/(2*radius)])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3‑D Capsule Concept')
    plt.tight_layout()
    plt.show()
