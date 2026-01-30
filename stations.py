import matplotlib.pyplot as plt
import matplotlib.patches as patches
# Visualisation des points candidats (les p mediums)

def draw_medium_points(list_points,x_min,x_max,y_min,y_max,q):

    sub_rects = []

    _, ax = plt.subplots(figsize=(10, 8))

    for i, elt in enumerate(list_points) :
      for x,y,id,is_medium in elt :
        if is_medium :
          color = 'purple'
          marker = '*'
        else :
          color = 'red'
          marker = 'o'
        ax.scatter(x, y, c=color, marker=marker, s=25)
        ax.text(x, y, str(i+1), fontsize=9, ha='right')

    rect = patches.Rectangle(
        (x_min, y_min),
        x_max - x_min, #w
        y_max - y_min, #h
        linewidth=2,
        edgecolor='blue',
        facecolor='none',
        alpha=0.5
    )
    ax.add_patch(rect)

    ax.set_title("Points TSP avec rectangle englobant")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)

    padding = 10
    ax.set_xlim(x_min - padding, x_max + padding)
    ax.set_ylim(y_min - padding, y_max + padding)

    current_rect = 0

    for k in range(0, q):


      if k == 0 :

        for i in range(0,q):
          current_rect+=1

          rect = patches.Rectangle(
            (x_min  , y_min + i * (y_max - y_min) / q),
            (x_max - x_min) / q,
            (y_max - y_min) / q,
            linewidth=2,
            edgecolor='yellow',
            facecolor='none',
            alpha=0.5
          )
          ax.add_patch(rect)
          centre = ((rect.get_x() + rect.get_width()) / 2 , (rect.get_y()+ (i+1)*rect.get_height())/2)
          new_elt = (centre, rect)
          sub_rects.append(new_elt)
          ax.scatter(centre[0] , centre[1] , marker='*', c='white', edgecolor='black', s=70, linewidth=0.5)

      else :

        compute_column_x = True


        for i in range(0,q):
          current_rect+=1

          if i == 0 :
            color = 'red'
          else:
            color = 'blue'

          rect = patches.Rectangle(
            (sub_rects[current_rect - q ][1].get_x() + sub_rects[current_rect - q][1].get_width(), y_min + i * (y_max - y_min) / q   ),
            (x_max - x_min) / q,
            (y_max - y_min) / q,
            linewidth=2,
            edgecolor='red',
            facecolor='none',
            alpha=0.5
          )
          ax.add_patch(rect)
          if compute_column_x :
            column_x = ((k+1)*rect.get_width() + rect.get_x()) / 2
            compute_column_x = False
          centre = (column_x , (rect.get_y()+ (i+1)*rect.get_height())/2)
          new_elt = (centre, rect)
          sub_rects.append(new_elt)
          ax.scatter(centre[0] , centre[1]  ,marker='*', c='white', edgecolor='black', s=70, linewidth=0.5 )

    plt.tight_layout()
    if plt.isinteractive():
        plt.show()
    plt.savefig('screenshots/stations.png')
