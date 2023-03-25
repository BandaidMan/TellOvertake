import pygame

pygame.init()

# Find the first joystick
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

    # Read the joystick axes and buttons
    axes = []
    buttons = []
    for i in range(joystick.get_numaxes()):
        axes.append(joystick.get_axis(i))
    for i in range(joystick.get_numbuttons()):
        buttons.append(joystick.get_button(i))

    # Print the values
    print(f"Axes: {axes}")
    print(f"Buttons: {buttons}")
