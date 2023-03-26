import pygame

pygame.init()
def discoverController():
    # Find the first joystick
    joystick = None
    for i in range(pygame.joystick.get_count()):
        j = pygame.joystick.Joystick(i)
        j.init()
        #print(f"Joystick {i}: {j.get_name()}")
        if not joystick:
            joystick = j

    if not joystick:
        print("No joystick found!")
        return None
    return joystick


def getControllerValues(joystick):
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    # Read the hat position
    hat = joystick.get_hat(0)
    # Check the hat position for each direction
    dpad_up = int(hat[1] == 1)
    dpad_down = int(hat[1] == -1)
    dpad_left = int(hat[0] == -1)
    dpad_right = int(hat[0] == 1)

    # Read the joystick X and Y axes
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    speed = joystick.get_axis(3)
    yaw = joystick.get_axis(2)

    # Read the buttons
    a_button = joystick.get_button(0)
    b_button = joystick.get_button(1)
    x_button = joystick.get_button(2)
    y_button = joystick.get_button(3)

    # Scale the X and Y axis values from -100 to 100
    x_axis = int(x_axis * 100)
    y_axis = int(y_axis * -100)
    speed = int(speed * -100)
    yaw = int(yaw * 100)

    stick_drift = 10

    if abs(x_axis) <= stick_drift:
        x_axis = 0
    if abs(y_axis) <= stick_drift:
        y_axis = 0
    if abs(speed) <= stick_drift:
        speed = 0
    if abs(yaw) <= stick_drift:
        yaw = 0
    
    # Clamp the X and Y axis values to the range -100 to 100
    x_axis = max(-100, min(x_axis, 100))
    y_axis = max(-100, min(y_axis, 100))
    speed = max(-100, min(speed, 100))
    yaw = max(-100, min(yaw, 100))
    print(f"Power: {x_axis} Yaw: {y_axis} Pitch: {speed} Roll: {yaw} D-Pad Up: {dpad_up} D-Pad Down: {dpad_down} D-Pad Left: {dpad_left} D-Pad Right: {dpad_right} A: {a_button} B: {b_button} X: {x_button} Y: {y_button}")
    return [x_axis, y_axis, speed, yaw, dpad_up, dpad_down, dpad_left, dpad_right, a_button, b_button, x_button, y_button]


controller = discoverController()
print(type(controller))


if __name__ == '__main__':
    controller = discoverController()  
    while True:
        print(getControllerValues(controller))