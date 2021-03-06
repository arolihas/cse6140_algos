import time
import sys
import os
import argparse
import random
# add imports for each method file here
from LocalSearch import Graph, LocalSearch1, LocalSearch2
import BranchAndBound
import approx

parser = argparse.ArgumentParser(description='Run a Local Search Algorithm for Min Vertex Cover Problem')
parser.add_argument("-inst", help='Which file to run', default='../DATA/dummy1.graph') 
parser.add_argument("-alg", help='Choose which method to run (BnB, Approx, LS1, LS2)', default="LS1", choices=["BnB", "Approx", "LS1", "LS2"])
parser.add_argument("-time", help='When to stop the run in seconds', type=int, default=600)
parser.add_argument("-seed", help='Random Seed for Local Search', type=int, default=32)
args = parser.parse_args()

if __name__ == '__main__':
    if args.alg == "BnB":
        #run Branch and Bound
        BranchAndBound.main(args.inst, args.time, args.seed)
    elif args.alg == "Approx": 
        #run Heuristics
        approx.measure_performance(args.inst, args.time, args.seed)
    elif args.alg == "LS1":
        #run Decision based Local Search Framework
        ls = LocalSearch1(args.inst, args.time, args.seed)
        ls.main()
    elif args.alg == "LS2": 
        #run Independent Set Local Search Framework
        ls = LocalSearch2(args.inst, args.time, args.seed)
        ls.main()
    