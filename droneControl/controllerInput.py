from djitellopy import Tello
import pygame

if a_button:
    drone.takeoff()
elif b_button:
    drone.land()
elif x_button:
    drone.emergency()
elif y_button:
    # Placeholer comment
    print("Oopsie haha")
elif dpad_up:
    drone.flip_forward()
elif dpad_down:
    drone.flip_back()
elif dpad_left:
    drone.flip_left()
elif dpad_right:
    drone.flip_right()