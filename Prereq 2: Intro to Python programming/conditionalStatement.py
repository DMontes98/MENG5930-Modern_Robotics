# Conditional statements
joystick_in = "up"             # we first get the joystick input

if joystick_in == "right":
    print("moving 1st joint in positive direction")
elif joystick_in == "left":
    print("moving 1st joint in negative direction")
elif joystick_in == "up":
    print("moving the 2nd joint in positive direction")
elif joystick_in == "down":
    print("moving the 2nd joint in the negative direction")
else:
    print("the joystick is in the neutral position, no movement")