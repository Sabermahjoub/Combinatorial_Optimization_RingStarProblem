import math
List_affectation = []


def euclidian_distance(centre, point) :
  x0, y0 = centre
  x, y = point
  return math.sqrt((x - x0)**2 + (y-y0)**2)

def determine_nearest_point_to_empty_rectangle(center, points_list):
    min_distance = float('inf')
    nearest_point = None

    for i, (x, y,id, is_medium) in enumerate(points_list):
        if is_medium : 
          continue
        else : 
          dist = euclidian_distance(center, (x, y))
          if dist < min_distance:
              min_distance = dist
              nearest_point = (x, y,id, is_medium)

    if nearest_point is not None:
        return nearest_point


def determine_nearest_point_to_center(center, set_points):
    min_distance = float('inf')
    nearest_point = None
    # nearest_index = None

    points_list = list(set_points)

    for i, (x, y,id, visited) in enumerate(points_list):
        dist = euclidian_distance(center, (x, y))
        if dist < min_distance:
            min_distance = dist
            nearest_point = (x, y,id, visited)
            # nearest_index = i

    if nearest_point is not None:
        set_points.remove(nearest_point)
        set_points.add((nearest_point[0], nearest_point[1], nearest_point[2], True))


def affect_points_to_rect(new_coords,coords,sub_rects):
    print(f"Initial points: {len(new_coords)}")
    print(new_coords)

    for i, (center, rect) in enumerate(sub_rects, start=1):

        set_points = set()
        print(f"\nProcessing rectangle {i}")
        print(f"Points before processing rect {i}: {len(new_coords)}")

        j = len(new_coords) - 1
        while j >= 0:
            x, y, id, flag  = new_coords[j]
            if (x >= rect.get_x() and x <= rect.get_x() + rect.get_width() and
                y >= rect.get_y() and y <= rect.get_height() + rect.get_y()):
                set_points.add((x, y, id, flag))
                del new_coords[j]
            j -= 1

        print(f"Points found in rectangle {i}: {len(set_points)}")
        print(set_points)

        medium_already_exists = any([is_medium is True for x, y, id, is_medium in set_points])

        # If the current rectangle is empty no points in it ! 
        if len(set_points) == 0 : 
          set_points = {determine_nearest_point_to_empty_rectangle(center,coords)}

        # If the current rectangle doesn't contain any point that is medium (so doesn't contain the first point)
        if not medium_already_exists :
          determine_nearest_point_to_center(center, set_points)

        print(f"Points in set after determine_nearest: {len(set_points)}")


        List_affectation.append(set_points)

    print(f"\nPoints left in new_coords after all rectangles: {len(new_coords)}")
    print(f"Total points in all sets: {sum(len(s) for s in List_affectation)}")

    return List_affectation
