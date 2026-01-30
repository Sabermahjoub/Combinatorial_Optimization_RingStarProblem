# Probleme du trace d’une ligne de transport public circulaire
en effet ce projet exploite le problème d'OC en combinant le probleme de voyageur de commerce "TSP" travaillé sur un ensembe de stations intermediaires (les points medium) et aussi un coût d'affectation liant les points à des stations.
Notre objectif est alors de minimiser le coût global combinant du coût de la tournée "TSP" et du coût d'affectation des points à leur stations associées.De plus, ce projet inclue un ensemble d'heuristique comme : gloutonne de p-median , heuristique du plus proche voisin, une heuristique 2-opt , une métaheuristique et la formulation compacte il sont expliquées  plus en detaille dans le rapport rédiger et on a affichier les couts de ces méthodes et le temps d'execution pour comparer entre eux et connaitre la methode la plus performante.

# Les fonctionnalités
dans le projet on a implémenté differente méthodes comme :
- une méthode pour le calcul de la distance euclidienne.
- une méthode pour l'heuristique gloutonne de la TSP
- l'heuristique 2-opt
- metaheuristique avec modif dynamique des stations
- une formulation compacte 
- une visualisation graphique pour chaque méthode qui exixte dans le dossier screenshots avec une execution du code dans le terminal
- des graphes aussi pour la visualisation des couts de chaque méthode pour savoir quelle est la meilleure et suivre leur evolution 

# Structure du projet
packages/           # contenant les imports PulP,...
screenshots/         # contenant les impages des resultats des modeles
berlin52.tsp   # fichier les coordonnees des points contenant 52 points 
data_extraction.py
formule_compacte.py
metaheuristic.py
rectangle_affectation.py
rectangle_draw.py
tsp_heuristic.py
staions.py
stations_visualisation.py
sae.py      # contenant l'execution de tous les fichier cité dessus 
Makefile    # contenant les commande d'installation d'import des bibs et le run du fichier sae et le clean du cache
timing_results.txt # un fichier texte contenant le temps d'execution de chaque modele  

Les prérequis sont python3.8 on a installé juste au niveau du projet la bib Pulp car on a pas eu le droit d'acces de l'installer sur les machine de l'universite la bibliotheque pour la visualisation de graphe matplotlib l'import de ces bibs est effectuer a travers la commande existante dans le makefile a partir du dossier packages (la partie nommée check)

de plus pour executer le projet il faut juste taper dans le terminal make run et il va executer toutes les méthodes existantes dans le fichier sae.py (dans le makefile la partie run)et l'execution sera afficher dans le terminal et les visualisations seront dans le dossier screenshots/.
Remarque : si vous avez eu un probleme pour l'import de pulp avec cet affichage dans le terminal : "No module named Pulp" il faut juste taper la commande "make install" pour l'installer dans le projet et apres lancez la commande "make run" pour l'execution.

Ce projet est réalisé dans le cadre académique dans l'Université Sorbonne Paris Nord Sup-Galilée en binome par Mazouz Erij et Mahjoub Mohamed Saber .