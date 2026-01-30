import math
import data_extraction
import rectangles_draw
import rectangle_affectation

import stations
import stations_visualisation

import tsp_heuristic
import metaheuristic
import formule_compacte
p = 9
q = int(math.sqrt(p))

file_name = "berlin52.tsp"


n , coords = data_extraction.tsp_data_extraction(file_name)
x = [c[0] for c in coords]
y = [c[1] for c in coords]
x_max = max(x)
x_min = min(x)
y_max = max(y)
y_min = min(y)

data_extraction.tsp_visualisation(file_name,x,y)


import time


start_heur = time.perf_counter()

sub_rects= rectangles_draw.rectangle_draw(file_name,p,q,x,y,x_min,x_max,y_min,y_max)

newCoords=coords.copy()
l = rectangle_affectation.affect_points_to_rect(newCoords,coords,sub_rects)

medium_points = [(x, y) for elt in l for x, y,id, flag in elt if flag]
print(medium_points)

print("La liste de tous les point mediums est  : \n")
print(l)

stations.draw_medium_points(l,x_min,x_max,y_min,y_max,q)

affectation_points_to_mediums = stations_visualisation.assign_points_to_station(l)

tour, gloutonne_cost = tsp_heuristic.tsp_problem_fixed(l,affectation_points_to_mediums)
print(tour)

end_heur = time.perf_counter() - start_heur
with open("timing_results.txt", "w") as f:
    f.write("Execution time for heuristic algorithm is : ")
    f.write(f"{end_heur}\n")



start_meta = time.perf_counter()

meta_tour=metaheuristic.metaheuristic(l,p,affectation_points_to_mediums,gloutonne_cost)

end_meta = time.perf_counter() - start_meta
with open("timing_results.txt", "a") as f:
    f.write("Execution time for metaheuristic algorithm is : ")
    f.write(f"{end_meta}\n")

print(coords)

start_formule_compacte = time.perf_counter()
d = formule_compacte.construire_matrice_d_distance(coords)
print(d)
stations, affectation, cycle ,n =formule_compacte.formule_compacte(d, p)
end_formule_compacte = time.perf_counter() - start_meta
with open("timing_results.txt", "a") as f:
    f.write("Execution time for formule compacte algorithm is : ")
    f.write(f"{end_formule_compacte}\n")
formule_compacte.visualiser_solution(n, stations, affectation, cycle)
