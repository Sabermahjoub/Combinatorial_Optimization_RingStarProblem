
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import matplotlib
def tsp_data_extraction(file_path):
    coords = []
    n = 0
    #
    i = 0
    with open(file_path, 'r') as f:
        startReading = False
        for line in f:
            if "DIMENSION" in line.strip().upper():
                n = line.strip().split()[-1]
                continue
            if line.strip() == "NODE_COORD_SECTION":
                startReading = True
                continue
            elif line.strip() == "EOF":
                return n, coords
                break

            if startReading:
                i += 1
                parts = line.strip().split()
                if len(parts) >= 3:
                    _, x, y = parts[0], float(parts[1]), float(parts[2])
                    # If first point, then it's a medium
                    if i == 1 :
                      coords.append((x, y,i, True))
                    else :
                      coords.append((x, y,i, False))

def tsp_visualisation(file_path,x,y):

    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, c='red', s=20)
    plt.title("Points TSP")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, alpha=0.3)

    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, str(i+1), fontsize=9, ha='right')

    if plt.isinteractive():
        plt.show()
    plt.savefig('screenshots/tsplib_data.png')
    plt.close()