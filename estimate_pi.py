import random


def estimate_pi(n):
    point_circle = 0
    point_total = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # x,y are dimensions of random points
        distance = x ** 2 + y ** 2
        # distance from origin to point
        if distance <= 1:
            point_circle += 1
            # if a random point is within a circle
        point_total += 1

    print(4 * point_circle / point_total)
    # scaled percentage of points in circle can estimate pi


if __name__ == "__main__":
    estimate_pi(10)
    # amount of random points used to estimate pi, higher for more accuracy
