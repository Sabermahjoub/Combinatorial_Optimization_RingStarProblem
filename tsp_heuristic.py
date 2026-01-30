import matplotlib.pyplot as plt
import math

def assignment_cost(points_to_mediums):
    cost = 0.0
    for pt, med in points_to_mediums.items():
        cost += euclidian_distance((pt[0], pt[1]), (med[0], med[1]))
    return cost

def euclidian_distance(centre, point):
    x0, y0 = centre
    x, y = point
    return math.sqrt((x - x0) ** 2 + (y - y0) ** 2)

def tsp_problem_fixed(list_points,affectation_points_to_mediums):
    _, ax = plt.subplots(figsize=(10, 8))
    medium_points = [(x, y, id_, _) for elt in list_points for x, y, id_, flag in elt if flag]

    if not medium_points:
        return

    unvisited = set([id_ for (_, _, id_, _) in medium_points])
    path = []

    current_id = medium_points[0][2]
    current_point = medium_points[0]

    while unvisited:
        unvisited.remove(current_id)
        path.append(current_point)

        if not unvisited:
            break

        min_dist = float('inf')
        nearest = None

        for (x, y, id_, _) in medium_points:
            if id_ in unvisited:
                dist = euclidian_distance((current_point[0], current_point[1]), (x, y))
                if dist < min_dist:
                    min_dist = dist
                    nearest = (x, y, id_, _)

        if nearest is None:
            break

        current_point = nearest
        current_id = nearest[2]

    # 2-opt optimization (fixed version)
    def get_distance(p1, p2):
        return euclidian_distance((p1[0], p1[1]), (p2[0], p2[1]))

    improved = True
    iterations = 0
    max_iterations = 1000

    while improved and iterations < max_iterations:
        improved = False
        iterations += 1

        for i in range(len(path) - 1):
            for j in range(i + 2, len(path)):
                # Don't check adjacent edges
                if j == i + 1:
                    continue

                # Get the four points involved
                # Edge 1: path[i] -> path[i+1]
                # Edge 2: path[j] -> path[(j+1) % len(path)]

                # Current configuration distance
                dist_before = (get_distance(path[i], path[i + 1]) +
                              get_distance(path[j], path[(j + 1) % len(path)]))

                # Swapped configuration distance
                dist_after = (get_distance(path[i], path[j]) +
                             get_distance(path[i + 1], path[(j + 1) % len(path)]))

                # If swap improves, reverse the segment
                if dist_after < dist_before:
                    path[i + 1:j + 1] = reversed(path[i + 1:j + 1])
                    improved = True
                    break

            if improved:
                break

    # Complete the cycle
    tour = path + [path[0]]

    # Plot
    for (x, y, id_, _) in medium_points:
        ax.scatter(x, y, c='black', marker='*', s=100, zorder=3)

    for i in range(len(tour) - 1):
        x1, y1, _, _ = tour[i]
        x2, y2, _, _ = tour[i + 1]
        ax.plot([x1, x2], [y1, y2], color='blue', linewidth=2, zorder=1)
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        # Calculate direction vector
        dx = x2 - x1
        dy = y2 - y1
        ax.annotate('',
                    xy=(mid_x + dx * 0.1, mid_y + dy * 0.1),  # Arrow tip position
                    xytext=(mid_x - dx * 0.1, mid_y - dy * 0.1),  # Arrow tail position
                    arrowprops=dict(arrowstyle='->',
                                  color='blue',
                                  linewidth=2,
                                  shrinkA=0, shrinkB=0),  # No shrinking at ends
                    zorder=2)
    for point in affectation_points_to_mediums :
      ax.scatter(point[0], point[1], c='red', marker='o', s=25, zorder=3)
      ax.plot([point[0], affectation_points_to_mediums[point][0]], [point[1], affectation_points_to_mediums[point][1]], color='gray',linestyle='--', linewidth=1, zorder=1)


    # Calculate total distance
   # total_dist = sum(get_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    tsp_cost = sum(get_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    aff_cost = assignment_cost(affectation_points_to_mediums)
    total_cost = tsp_cost + aff_cost

    plt.title(f'TSP+Assign - {len(medium_points)} points, Cost: {total_cost:.2f}')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if plt.isinteractive():
        plt.show()
    plt.savefig('screenshots/ring_star_circle.png', dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Completed {iterations} optimization iterations")
    return tour, total_cost