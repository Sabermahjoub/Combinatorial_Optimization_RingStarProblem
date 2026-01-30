# Circular Public Transport Route Optimization

This project addresses the problem of designing a circular public transport line. It combines the **p-median problem** with the **Traveling Salesman Problem (TSP)** to optimize routes over a set of intermediate stations (medium points) and their associated point assignments.  

The **main objective** is to minimize the **overall cost**, which is a combination of:  
1. The TSP route cost (the tour through the stations).  
2. The assignment cost (connecting points to their associated stations).  

To achieve this, the project implements several **heuristics and optimization approaches**, including:  
- Greedy p-median heuristic  
- Nearest neighbor heuristic for TSP  
- 2-opt heuristic for route improvement  
- A metaheuristic with dynamic station modifications  
- A compact mathematical formulation  

The report includes detailed explanations of each method, along with their computed costs and execution times, allowing for performance comparison.  

---

## Features

This project implements the following functionalities:  
- **Euclidean distance calculation** between points  
- **Greedy TSP heuristic**  
- **2-opt heuristic** for TSP route optimization  
- **Metaheuristic** with dynamic station adjustment  
- **Compact formulation** for exact optimization  
- **Graphical visualizations** for each method (stored in `screenshots/`)  
- **Performance charts** comparing costs and execution times for all methods  

---

## Project Structure

packages/ # Contains imported libraries such as PuLP
screenshots/ # Contains screenshots of method results
berlin52.tsp # Coordinates file for 52 points
data_extraction.py
formule_compacte.py
metaheuristic.py
rectangle_affectation.py
rectangle_draw.py
tsp_heuristic.py
stations.py
stations_visualisation.py
sae.py # Main script executing all methods
Makefile # Installation, run, and cleanup commands
timing_results.txt # Execution times for each method


---

## Prerequisites

- **Python 3.8**  
- **Libraries:**  
  - `PuLP` (for optimization)  
  - `matplotlib` (for visualizations)  

> Note: In university environments without admin rights, the libraries are installed locally via the `Makefile`.  

---

## Usage

1. **Run the project:**  
```bash
make run
```

This executes all methods in sae.py. Terminal outputs show execution progress, and visualizations are saved in screenshots/.

2. Install dependencies (if needed):
If you encounter the error:
```bash
No module named PuLP
```

Run : 
```bash
make install
```

Then execute ```bash make ``` run again.

## Authors

This project was completed as part of the academic curriculum at Université Sorbonne Paris Nord – Sup Galilée, by:

MAHJOUB Mohamed Saber

MAZOUZ Erij

