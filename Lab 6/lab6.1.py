import numpy as np 
import matplotlib.pyplot as plt

# Create vectors for the coordinate frame
origin = np.zeros(3)
x_axis = [0,1,0]
y_axis = [-1,0,0]
z_axis = [0,0,1]
# From rotation matrix:
# rot_0_5 = rot_z_theta_1 @ rot_y_theta_2 @ rot_y_theta_3 @ rot_y_theta_4 @ eye
# [[0,-1,0],
#  [1,0,0]
#  [0,0,1]]
# the columns are the vectors

# Visualize the coordinate frame
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(*origin, *x_axis, color='r', label='X-axis')
ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()