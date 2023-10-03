import math

horizontal_FOV = 80
near_plane = 2
screen_height = 768
screen_width = 1366

vertical_FOV = horizontal_FOV * (screen_height / screen_width)
right = math.tan(math.radians(horizontal_FOV / 2)) * near_plane
bottom = math.tan(math.radians(vertical_FOV / 2)) * near_plane

print(vertical_FOV)
print(right)
print(bottom)