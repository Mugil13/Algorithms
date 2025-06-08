import math
import random

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest(points):
    min_dist = 99999
    closest = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = dist(points[i], points[j])
            if distance < min_dist:
                min_dist = distance
                closest = (points[i], points[j])
    return min_dist, closest

def closest_pair_dc(points):
    if len(points) <= 3:
        return brute_force_closest(points)

    sorted_points = sorted(points, key=lambda x: x[0])
    mid = len(points) // 2
    left_min_dist, left_closest = closest_pair_dc(sorted_points[:mid])
    right_min_dist, right_closest = closest_pair_dc(sorted_points[mid:])

    min_dist = min(left_min_dist, right_min_dist)
    closest = left_closest if left_min_dist == min_dist else right_closest

    mid_x = sorted_points[mid][0]
    strip = [point for point in sorted_points if abs(point[0] - mid_x) < min_dist]

    strip_min_dist, strip_closest = strip_closest_in_strip(strip, min_dist)
    if strip_min_dist < min_dist:
        min_dist = strip_min_dist
        closest = strip_closest

    return min_dist, closest

def strip_closest_in_strip(strip, min_dist):
    min_distance = min_dist
    closest = None
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            distance = dist(strip[i], strip[j])
            if distance < min_distance:
                min_distance = distance
                closest = (strip[i], strip[j])
    return min_distance, closest

def generate_random_points(n):
    points = []
    for i in range(n):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.append((x, y))
    return points

# Example usage:
num_points = 10
points = generate_random_points(num_points)
print("Randomly generated points:", points)

min_dist, closest_pair = closest_pair_dc(points)
print("Closest pair:", closest_pair, "with distance:", min_dist)