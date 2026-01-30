# Implémentation de l'heuristique gloutonne
# Etape A : déterminer les p points (stations)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import data_extraction

def rectangle_draw(file_path,p,q,x,y,x_min,x_max,y_min,y_max):
    n , coords = data_extraction.tsp_data_extraction(file_path)

    sub_rects = []

    _, ax = plt.subplots(figsize=(10, 8))

    ax.scatter(x, y, c='red', s=20)

    main_rect = patches.Rectangle(
        (x_min, y_min),
        x_max - x_min,  # w
        y_max - y_min,  # h
        linewidth=2,
        edgecolor='blue',
        facecolor='none',
        alpha=0.5
    )
    ax.add_patch(main_rect)

    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi, yi, str(i+1), fontsize=9, ha='right')

    ax.set_title("Points TSP avec rectangle englobant")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)

    padding = 10
    ax.set_xlim(x_min - padding, x_max + padding)
    ax.set_ylim(y_min - padding, y_max + padding)

    rect_width = (x_max - x_min) / q
    rect_height = (y_max - y_min) / q

    current_rect = 0

    for k in range(0, q):
        if k == 0:  # First column
            for i in range(0, q):
                current_rect += 1

                rect_x = x_min
                rect_y = y_min + i * rect_height

                rect = patches.Rectangle(
                    (rect_x, rect_y),
                    rect_width,
                    rect_height,
                    linewidth=2,
                    edgecolor='yellow',
                    facecolor='none',
                    alpha=0.5
                )
                ax.add_patch(rect)

                centre_x = rect_x + rect_width / 2
                centre_y = rect_y + rect_height / 2
                centre = (centre_x, centre_y)

                new_elt = (centre, rect)
                sub_rects.append(new_elt)
                ax.scatter(centre[0], centre[1], marker='*',
                          c='white', edgecolor='black', s=70, linewidth=0.5)

        else:  # Subsequent columns
            compute_column_x = True
            column_x = 0  # Initialize column_x

            for i in range(0, q):
                current_rect += 1

                if i == 0:
                    color = 'red'
                else:
                    color = 'blue'

                rect_x = x_min + k * rect_width
                rect_y = y_min + i * rect_height

                rect = patches.Rectangle(
                    (rect_x, rect_y),
                    rect_width,
                    rect_height,
                    linewidth=2,
                    edgecolor=color,
                    facecolor='none',
                    alpha=0.5
                )
                ax.add_patch(rect)

                if compute_column_x:
                    column_x = rect_x + rect_width / 2
                    compute_column_x = False

                centre_x = column_x
                centre_y = rect_y + rect_height / 2
                centre = (centre_x, centre_y)

                new_elt = (centre, rect)
                sub_rects.append(new_elt)
                ax.scatter(centre[0], centre[1], marker='*',
                          c='white', edgecolor='black', s=70, linewidth=0.5)

    plt.tight_layout()
    print(f"Total rectangles created: {len(sub_rects)}")
    print(f"Expected: {q}×{q} = {q*q} rectangles")
    if plt.isinteractive():
        plt.show()
    plt.savefig('screenshots/rectangles.png')
    plt.close()
    return sub_rects