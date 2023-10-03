import numpy as np

################ NOTE: I know it would be easier to just check if trans(M) = M, but wanted to show the full process!


##### Matrix to check #####
matrix = np.array([[1, 0, 0],
                   [0, 0, -1],
                   [0 ,1, 0]])


#### Function Body #####
# Define Tolerance
tolerance = 1e-5

# Extract Columns
x = matrix[:, 0]
y = matrix[:, 1]
z = matrix[:, 2]

# Check Norm Constraint
norm_x = np.sqrt( x[0]**2 + x[1]**2 + x[2]**2 )
norm_y = np.sqrt( y[0]**2 + y[1]**2 + y[2]**2 )
norm_z = np.sqrt( z[0]**2 + z[1]**2 + z[2]**2 )

norm_ok = True

if (norm_x < (1-tolerance) or norm_x > (1+tolerance)):
    norm_ok = False

if (norm_y < (1-tolerance) or norm_y > (1+tolerance)):
    norm_ok = False

if (norm_z < (1-tolerance) or norm_z > (1+tolerance)):
    norm_ok = False

# Check Orthogonality Condition
dot_xy = np.dot(x, y)
dot_xz = np.dot(x, z)
dot_yz = np.dot(y, z)

dot_ok = True

if (dot_xy < -tolerance or dot_xy > tolerance):
    dot_ok = False

if (dot_xz < -tolerance or dot_xz > tolerance):
    dot_ok = False

if (dot_yz < -tolerance or dot_yz > tolerance):
    dot_ok = False

# Is it a rotation matrix?

if (norm_ok and dot_ok) :
    print("It is a Rotation Matrix")
else:
    print("It is not a Rotation Matrix")
