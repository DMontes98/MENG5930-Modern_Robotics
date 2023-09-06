# Conditional statements
sensor_output = 135;

if sensor_output == 100
    print("Robot is in the right position")
elif sensor_output > 100:
    print("Robot is too far away")
elif sensor_output < 100 and sensor_output >= 0 :
    print("Robot is too close away")
else:
    print("Sensor Error")
