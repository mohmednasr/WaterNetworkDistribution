#!/usr/bin/python

#############################################################################
#                                                                           #
#  MONITEUR D'ENCHAINEMENT POUR LE CALCUL DE L'EQUILIBRE D'UN RESEAU D'EAU  #
#                                                                           #
#############################################################################

##### Pour nettoyer l'environnement Python...
##### (commande a entrer directement dans l'interpreteur)
# %reset

from numpy import random


############################################################
#####                                                  #####
#####   Le cas d'un reseau realiste de taille normale  #####
#####                                                  #####
############################################################

##### Fonctions fournies dans le cadre du projet

# Probleme realiste et structures normales
from Probleme_R   import *
from Structures_N import *

# Affichage des resultats
from Visualg import Visualg

# Optimisation
from Gradient_F  import Gradient_F
from Newton_F    import Newton_F
from Scipy_Optim import Scipy_Optim

# Verification des resultats
from HydrauliqueP import HydrauliqueP
from HydrauliqueD import HydrauliqueD
from Verification import Verification

##### Fonctions a ecrire dans le cadre du projet

# ---> Charger les fonctions associees a l'oracle du probleme,
#      aux algorithmes d'optimisation et de recherche lineaire
#
#      Exemple 1 - tester l'oracle sur le gradient a pas fixe :
#
#          from OraclePG   import OraclePG
#          from Gradient_F import Gradient_F
#
#      Exemple 2 - ecrire le gradient a pas variable :
#
#          from OraclePG   import OraclePG
#          from Wolfe      import Wolfe
#          from Gradient_V import Gradient_V
#
# ---> A modifier...
# ---> A modifier...
# ---> A modifier...

##### Initialisation de l'algorithme

# ---> La dimension du vecteur dans l'espace primal est n-md
#      et la dimension du vecteur dans l'espace dual est md
#
#      Probleme primal :
#
#          x0 = 0.1 * random.normal(size=n-md)
#
#      Probleme dual :
#
#          x0 = 100 + random.normal(size=md)
#
# ---> A modifier...
# ---> A modifier...
# ---> A modifier...

##### Minimisation proprement dite

# ---> Executer la fonction d'optimisation choisie
#
#      Exemple 1 - le gradient a pas fixe :
#
#          print()
#          print("ALGORITHME DU GRADIENT A PAS FIXE")
#          copt, gopt, xopt = Gradient_F(OraclePG, x0, 0.0005)
#
#      Exemple 2 - le gradient a pas variable :
#
#          print()
#          print("ALGORITHME DU GRADIENT A PAS VARIABLE")
#          copt, gopt, xopt = Gradient_V(OraclePG, x0, 1)
#
# ---> A modifier...
# ---> A modifier...
# ---> A modifier...

##### Verification des resultats

# ---> La fonction qui reconstitue les variables hydrauliques
#      du reseau a partir de la solution du probleme s'appelle
#      HydrauliqueP pour le probleme primal, et HydrauliqueD
#      pour le probleme dual
#
#      Probleme primal :
#
#          qopt, zopt, fopt, popt = HydrauliqueP(xopt, m, mr, md, r, pr, fd, Ar, AdI, B, q0)
#          Verification(A, qopt, zopt, fopt, popt)
#
#      Probleme dual :
#
#          qopt, zopt, fopt, popt = HydrauliqueD(xopt, m, mr, r, pr, fd, A, Ar)
#          Verification(A, qopt, zopt, fopt, popt)
#
# ---> A modifier...
# ---> A modifier...
# ---> A modifier...
