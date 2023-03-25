import pygame

pygame.init()

# Find the first joystick (controller)
joystick = None
for i in range(pygame.joystick.get_count()):
    j = pygame.joystick.Joystick(i)
    j.init()
    print(f"Joystick {i}: {j.get_name()}")
    if not joystick:
        joystick = j

if not joystick:
    print("No joystick found!")
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # Read the joystick X and Y axes
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    speed = joystick.get_axis(3)

    # Scale the X and Y axis values from -100 to 100
    x_axis = int(x_axis * 100)
    y_axis = int(y_axis * -100)
    speed = int(speed * -100)

    # Clamp the X and Y axis values to the range -100 to 100
    x_axis = max(-100, min(x_axis, 100))
    y_axis = max(-100, min(y_axis, 100))
    speed = max(-100, min(speed, 100))
    
    # Print the X and Y axis values
    print(f"X Axis: {x_axis} Y Axis: {y_axis} Speed: {speed}")
  #  print(f"Y Axis: {y_axis}")