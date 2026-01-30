import math
import pulp as pl
import matplotlib.pyplot as plt

def euclidian_distance(centre, point) :
  x0, y0 = centre
  x, y = point
  return math.sqrt((x - x0)**2 + (y-y0)**2)

def construire_matrice_d_distance(coords):
    pts = [(x, y) for (x, y, _, _) in coords]
    n = len(pts)

    d = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                d[i][j] = euclidian_distance(pts[i], pts[j])
    return d





def formule_compacte(d,p):
  n = len(d)
  s = 0
  #probleme de minimisation
  model = pl.LpProblem("formule_compact", pl.LpMinimize)

  y = pl.LpVariable.dicts("y",(range(n), range(n)),lowBound=0, upBound=1,cat="Binary")
  x = pl.LpVariable.dicts("x",((i, j) for i in range(n) for j in range(i+1, n)),lowBound=0, upBound=1,cat="Binary")
  z = pl.LpVariable.dicts("z",((i, j) for i in range(n) for j in range(n) if i != j and j != s),lowBound=0, upBound=p-1,cat="Continuous")#j n'est pas une station

  alpha = 1
  model += (alpha * pl.lpSum(d[i][j] * x[(i, j)] for i in range(n) for j in range(i+1, n))
    +  pl.lpSum(d[i][j] * y[i][j]   for i in range(n) for j in range(n))
  )

  def X(i, j):
    if i < j:
      return x[(i, j)]
    else:
      return x[(j, i)]

  model += pl.lpSum(y[i][i] for i in range(n)) == p
  for i in range(n):#chaque i ->  1 station
      model += pl.lpSum(y[i][j] for j in range(n)) == 1
  for i in range(n):
      for j in range(n):
          if i != j:
              model += y[i][j] <= y[j][j]
  #le nombre de routes de la boucle qui touchent le sommet i est égal à 2 si i est une station, sinon 0.
  for i in range(n):
      model += pl.lpSum(X(i, j) for j in range(n) if j != i) == 2 * y[i][i]

  #fixer s comme station:
  model += y[s][s] == 1
  for j in range(n):
      if j != s:
          model += y[s][j] == 0
  #contrainte5: s envoie p-1 unites
  model += pl.lpSum(z[(s, j)] for j in range(n) if j != s) == p - 1
  #contrainte6: chaque station consomme 1 unite sauf s
  for i in range(n):
      if i == s:
          continue
      inflow  = pl.lpSum(z[(j, i)] for j in range(n) if j != i)  # j -> i
      outflow = pl.lpSum(z[(i, j)] for j in range(n) if j != i and j != s)  # i -> j, pas vers s

      model += inflow == outflow + y[i][i]
  #contrainte7: pas de flot si pas de route de boucle
  for i in range(n):
      for j in range(i+1, n):
          if i != s and j != s:
              model += z[(i, j)] + z[(j, i)] <= (p - 1) * x[(i, j)]
          else:
            other = j if i == s else i #other le sommet qui n'est pas s
            model += z[(s, other)] <= (p - 1) * X(s, other)
              #else sert only a eviter d’utiliser z[*,s] qui n’existe pas
  #le flot qui part de raoot vers other est autorisé seulement si la route root—other est dans la boucle.


#resolution
  solver = pl.PULP_CBC_CMD(msg=True, timeLimit=5, gapRel=0.0)
  model.solve(solver)

  print("Status:", pl.LpStatus[model.status])
  print("Objectif:", pl.value(model.objective))

  #lire les stations (retourne que les stations y[j][j]=1)
  stations = [j for j in range(n) if y[j][j].value() > 0.5]
  print("Stations:", stations)

  #lire les affectations (i-> station)
  print("Affectations (zone -> station):")
  affectation = {}
  for i in range(n):
      for j in range(n):
          if y[i][j].value() > 0.5:
              affectation[i] = j
              print(f"  {i} -> {j}")
              break #chaque ville va à UNE SEULE station (contrainte)

  #lire les aretes de la boucle
  cycle = []
  for i in range(n):
      for j in range(i+1, n):
          if x[(i, j)].value() > 0.5: #si la route entre i et j est dans la boucle
              cycle.append((i, j)) #on ajoute l'arete

  print("Arêtes de la boucle:", cycle)
  return stations, affectation, cycle , n




def visualiser_solution(n, stations, affectation, cycle):

    pos = {}
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = math.cos(angle)
        y = math.sin(angle)
        pos[i] = (x, y)

    plt.figure(figsize=(7, 7))

    for i in range(n):
        j = affectation[i]
        if i != j:  # si ce n'est pas une station qui se sert elle-même
            xi, yi = pos[i]
            xj, yj = pos[j]
            plt.plot([xi, xj], [yi, yj], linestyle="--")

    # --- dessiner la boucle ---
    for (i, j) in cycle:
        xi, yi = pos[i]
        xj, yj = pos[j]
        plt.plot([xi, xj], [yi, yj], linewidth=3)  # épais

    for i in range(n):
        x, y = pos[i]
        if i in stations:
            plt.scatter(x, y, s=300)  # stations
        else:
            plt.scatter(x, y, s=120)  # vil
        plt.text(x + 0.05, y + 0.05, str(i), fontsize=12)

    plt.title("Stations (gros points) + Cycle (épais) + Affectations (pointillés)")
    plt.axis("equal")
    plt.axis("off")
    if plt.isinteractive():
        plt.show()
        plt.close() 
    plt.savefig('screenshots/formule_compacte.png', dpi=300, bbox_inches="tight")






