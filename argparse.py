
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


def example_function(filename, ligands, mutant="Ne135/", resolution=2.5, optimize="Optimize", grid=1.5, completeness=95, null="  NULL  "):
    print("example datafile")

def parseArguments():
    parser = argparse.ArgumentParser(prog='python3 asgparse.py',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                     ------------------------------------------------------------------------
                                     >> The script is for educational purpose
                                     ========================================================================
                                     '''),
                                     epilog=textwrap.dedent('''\
                                     ========================================================================
                                     >>Please read instructions before start.
                                     ENJOY!!!
                                     ------------------------------------------------------------------------'''))
    # girdiğinin üzeirndekini değiştirmek için input tanımladık. terminalde -h olara çalıştır görürsün inputu
    input = parser.add_argument_group('------------------------------------------------------------------------'
                                      '\n>input')
    input.add_argument('-r', '--rep', metavar="rep.txt", type=argparse.FileType('r'), nargs='+',
                       help=textwrap.dedent("""Text file should have..............."""))
    input.add_argument('-l', '--lig', metavar="lig.TXT", type=argparse.FileType('r'), nargs='+',
                       help='Text file should have.........................')
    optional = parser.add_argument_group('------------------------------------------------------------------------'
                                         '\n>optional arguments')
    optional.add_argument('-m', '--mut', nargs='?', default="Ne135/", const=None,
                          help='The script is for educational purpose')
    optional.add_argument('-re', '--res', nargs='?', type=int, default=7.5, const=None,
                          help='The script is for educational purpose')
    optional.add_argument('-o', '--opt', nargs='?', default="Optimize", const=None,
                          help='The script is for educational purpose')
    optional.add_argument('-g', '--gr', nargs='?', type=int, default=11.5, const=None,
                          help='The script is for educational purpose')
    optional.add_argument('-c', '--com', nargs='?', type=int, default=195, const=None,
                          help='The script is for educational purpose')
    optional.add_argument('-n', '--nu', nargs='?', default="  NULL  ", const=None,
                          help='The script is for educational purpose')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseArguments()
    print(reverve_vina(sys.argv[2], sys.argv[4], args.mutant, args.resolution, args.optimize,
                       args.grid, args.completeness, args.null))
