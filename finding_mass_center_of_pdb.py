
import datetime
import math
import statistics
import subprocess
import sys
import textwrap
import timeit
from pathlib import Path

import argparse
import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
from pymol.cgo import *
from scipy.optimize import minimize


i="2ZC6"
os.system("pdb_fetch %s > %s.pdb" % (i, i))
grid_box={}
grid=1 # how big grid box
grid_size={} # output dictionary for pdbid=Size
def grid_center(x):
    def center_protein(x):
        X1 = x[0]
        Y1 = x[1]
        Z1 = x[2]
        point1 = (X1, Y1, Z1)
        distance = []
        total_points_distance = []
        e = 0
        for pdbs in c.itertuples(index=True, name="Pandas"):
            first = c.iat[e, 0]
            second = c.iat[e, 1]
            third = c.iat[e, 2]
            e += 1
            point2 = (first, second, third)
            dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))
            distance.append(dist)
        total = sum(distance)
        total_points_distance.append(total)
        # print(total)
        # print (minimize(center(x,y,z), total))
        return total

    def objective(x):
        return center_protein(x)

    cons = ({"type": "ineq"})
    X1 = 1
    Y1 = 1
    Z1 = 1
    x0 = np.array([X1, Y1, Z1])
    sol = minimize(objective, x0, method='SLSQP', options={
        "disp": True})                  # SLSQP only solver in sight PI that can do constrained nonlinear optimization. so we are using here
    x0 = sol.x                          # BFGS method gives 19750.45700958098   4B97 proteini için.
    center_protein = sol.fun            # Nelder-Mead gives 19750.45700960077
    center_coordinate = x0              # SLSQP gives 19750.457009557023
    print("center_coordinate")          # Jacobian is required for Newton-CG method
    print(x0)                           # Jacobian is required for Newton-CG trust-region minimization
    grid_box[i] = [str(x0[0]), str(x0[1]), str(x0[2])]
    print("#################################################################")  # center of protein.
    ########################################################################################################
    ##############         To find out grid size cover all surface of the protein       ####################
    center = x0
    out_points = []
    t = 0
    for atoms in c.itertuples(index=True, name="Pandas"):
        first = c.iat[t, 0]
        second = c.iat[t, 1]
        third = c.iat[t, 2]
        t += 1
        point2 = (first, second, third)
        dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(center, point2)]))
        out_points.append(dist)
        # print(dist)
    # print("mean_out_point")  # en uzak atomun uzaklığı.
    mean_out_point = statistics.mean(out_points)
    max_out_point = max(out_points)
    median = statistics.median(out_points)
    print("mean output :", mean_out_point)
    print("max output : ", max_out_point)
    grid_sz = round(float("%d" % (grid)) * float(max_out_point))
    # if you cover all of protein surface, mutliply 2 and add 1
    if (grid_sz % 2) == 0:
        grid_sz = grid_sz + 1
    else:
        grid_sz = grid_sz
    grid_size[i] = [grid_sz]
    print("Grid sizes: \n")
    print(grid_size)
    # print(median)
    print("#################################################################")

print("\n#################################################################")
p = PDBParser()
s = p.get_structure(i, i + ".pdb")
result = []
for chains in s:
    for chain in chains:
        for residue in chain:
            for atom in residue:
                a = atom.get_coord()
                result.append(atom.get_coord())  # for dönsügünüsü [] yazdırmak lazım

c = pd.DataFrame(result)  # c :: pdb koordinatları, labellı şekilde
# print("your pdb file is readind and preparing")
print("\n#################################################################\n\n")
print("\nThe protein file in process : ")
print(i)
print("\n#################################################################")
grid_center(c)
