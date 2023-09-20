import numpy as np 
np.set_printoptions(suppress=True)
# angles in radians
theta_1 = np.deg2rad(90)
theta_2 = np.deg2rad(-45)
theta_3 = np.deg2rad(0)
theta_4 = np.deg2rad(45)

rot_z_theta_1 = np.array([[np.cos(theta_1), -np.sin (theta_1), 0],
                          [ np.sin (theta_1), np.cos(theta_1), 0],
                          [ 0, 0, 1]]) 

rot_y_theta_2 = np.array([[np.cos(theta_2), 0, np.sin (theta_2)],
                          [ 0, 1, 0],
                          [ -np.sin (theta_2), 0, np.cos(theta_2)]]) 

rot_y_theta_3 = np.array([[np.cos(theta_3), 0, np.sin (theta_3)],
                          [ 0, 1, 0],
                          [ -np.sin (theta_3), 0, np.cos(theta_3)]]) 

rot_y_theta_4 = np.array([[np.cos(theta_4), 0, np.sin (theta_4)],
                          [ 0, 1, 0],
                          [ -np.sin (theta_4), 0, np.cos(theta_4)]]) 

eye = np.array([[1,0,0],
               [0,1,0],
               [0,0,1]])

# tool frame w.r.t the base frame

rot_0_5 = rot_z_theta_1 @ rot_y_theta_2 @ rot_y_theta_3 @ rot_y_theta_4 @ eye

# print the final rotation matrix
print(rot_0_5)