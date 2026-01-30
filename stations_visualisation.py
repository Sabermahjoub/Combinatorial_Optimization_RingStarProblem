# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import math
# import matplotlib

# def euclidian_distance(centre, point) :
#   x0, y0 = centre
#   x, y = point
#   return math.sqrt((x - x0)**2 + (y-y0)**2)

# def assign_points_to_station(list_points) :
#   colors = [
#     "red",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "brown",
#     "coral",
#     "gray",
#     "olive",
#     "cyan",
#     "magenta",
#     "gold",
#     "teal",
#     "navy",
#     "pink",
#     "black"
#   ]
#   _, ax = plt.subplots(figsize=(10, 8))

#   medium_points = [(x, y) for elt in list_points for x, y,id, flag in elt if flag]
#   affectation_points_to_mediums = {}

#   # Draw the medium points
#   for id, (x, y) in enumerate(medium_points):
#     ax.scatter(x, y, c=colors[id] , marker='*', s=50)
#   for i, elt in enumerate(list_points) :
#     closest_medium = None
#     for x,y,id,is_medium in elt :
#       if not is_medium :
#         distance_to_medium = float('inf')
#         medium_color_id = -1
#         for j, (medium) in enumerate(medium_points) :
#           dist = euclidian_distance(medium, (x, y))
#           if dist < distance_to_medium :
#             distance_to_medium = dist
#             closest_medium = medium
#             medium_color_id = j
#         ax.scatter(x, y, c=colors[medium_color_id], marker='o', s=15)
#         ax.text(x, y, str(i+1), fontsize=7, ha='right')
#         affectation_points_to_mediums[(x,y,id,is_medium)] = closest_medium
#   return affectation_points_to_mediums


import matplotlib.pyplot as plt
import math


def euclidian_distance(centre, point):
    x0, y0 = centre
    x, y = point
    return math.sqrt((x - x0) ** 2 + (y - y0) ** 2)


def assign_points_to_station(list_points, filename="assignment_plot.png"):
    colors = [
        "red", "blue", "green", "orange", "purple", "brown", "coral",
        "gray", "olive", "cyan", "magenta", "gold", "teal", "navy",
        "pink", "black"
    ]

    fig, ax = plt.subplots(figsize=(10, 8))

    medium_points = [(x, y) for elt in list_points for x, y, id, flag in elt if flag]
    affectation_points_to_mediums = {}

    for i, (x, y) in enumerate(medium_points):
        ax.scatter(x, y, c=colors[i % len(colors)], marker='*', s=120, label=f"Medium {i+1}")

    for i, elt in enumerate(list_points):
        for x, y, id, is_medium in elt:
            if not is_medium:
                min_dist = float('inf')
                closest_medium = None
                color_id = -1

                for j, medium in enumerate(medium_points):
                    dist = euclidian_distance(medium, (x, y))
                    if dist < min_dist:
                        min_dist = dist
                        closest_medium = medium
                        color_id = j

                ax.scatter(x, y, c=colors[color_id % len(colors)], s=20)
                ax.text(x, y, str(i + 1), fontsize=7, ha='right')
                affectation_points_to_mediums[(x, y, id, is_medium)] = closest_medium

    # Plot styling
    ax.set_title("Assignment of Points to Nearest Medium")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)

    if plt.isinteractive():
        plt.show()
    plt.savefig('screenshots/stations_visualization.png', dpi=300, bbox_inches="tight")
    plt.close()

    return affectation_points_to_mediums
