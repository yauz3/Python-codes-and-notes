
import datetime
import math
import statistics
import subprocess
import sys
import textwrap
import time
import timeit
from pathlib import Path

import argparse
import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
from pymol.cgo import *
from scipy.optimize import minimize

def time_it(func):
    def wapper (*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"The function took {(end-start)*1000} mil sec")
        return result
    return wapper()

@time_it
def example_function():
    print("example datafile")


