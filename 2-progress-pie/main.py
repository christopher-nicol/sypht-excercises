import math
import numpy as np

# Constants & Variables
radius = 50
v1 = [0, 50] # Start line segment vector
origin = [0, 0] # Origin translated to Cartesian coordinates

while True:
    T = int(input('Enter the number of points: '))

    if (1 <= T <= 1000):
        break
    else: 
        print('T must be between 1 and 1000')

# Initialise arrays that store variables of the cases
percentages = [0] * T
x_coordinates = [0] * T
y_coordinates = [0] * T
segment_angles = [0] * T


i = 0
# Taking inputs
while i < T:
    case = input(f'Enter Case {i + 1} input here (in the format [% X Y]): ')

    # Splits inputs into different arrays
    percentages[i], x_coordinates[i], y_coordinates[i] = map(int, case.split(' '))

    if (0 <= percentages[i] <= 100) and (0 <= x_coordinates[i] <= 100) and (0 <= y_coordinates[i] <= 100):
        i += 1
    else:
        print('Parameters outside of constraints (0 <= P, X, Y <= 100)')
        continue

# Computing case results
for i in range(0, T):
    # Converting coordinates to Cartesian system
    x_coordinates[i] -= 50
    y_coordinates[i] -= 50

    # Convert percentages to floats
    percentages[i] = float(percentages[i] / 100)

    # Calculate angle of the circle segment
    segment_angles[i] = percentages[i] * 360

    point = [x_coordinates[i], y_coordinates[i]]

    if percentages[i] < 0.5:
        point_angle = math.degrees(math.acos(np.dot(v1, point) / (np.linalg.norm(v1) * np.linalg.norm(point))))
    elif percentages[i] > 0.5:
        point_angle = 360 - math.degrees(math.acos(np.dot(v1, point) / (np.linalg.norm(v1) * np.linalg.norm(point))))

    point_length = math.sqrt((point[0] - origin[0])**2 + (point[1] - origin[1])**2)

    if (point_angle < segment_angles[i]) and (point_length < radius):
        print(f'Case #{i+1}: black')
    else:
        print(f'Case #{i+1}: white')