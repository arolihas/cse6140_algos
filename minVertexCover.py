import time
import sys
import os
import argparse
import random
# add imports for each method file here
from LocalSearch import Graph, LocalSearch1, LocalSearch2
import BranchAndBound

parser = argparse.ArgumentParser(description='Run a Local Search Algorithm for Min Vertex Cover Problem')
parser.add_argument("-inst", help='Which file to run', default='./DATA/dummy1.graph') 
parser.add_argument("-alg", help='Choose which method to run (BnB, Approx, LS1, LS2)', default="LS1", choices=["BnB", "Approx", "LS1", "LS2"])
parser.add_argument("-time", help='When to stop the run in seconds', type=int, default=600)
parser.add_argument("-seed", help='Random Seed for Local Search', type=int, default=32)
parser.add_argument("-folder", help='What folder to save', default='./Output/') 
args = parser.parse_args()

if __name__ == '__main__':
    if args.alg == "BnB":
        #run Branch and Bound
        BranchAndBound.main(args.inst, args.time, args.seed, args.folder)
    elif args.alg == "Approx": 
        #run Heuristics
        print("Nothing implemented yet")
    elif args.alg == "LS1":
        #run Decision based Local Search Framework
        if (args.inst == "all"):
            for filename in os.listdir("./DATA"): #all graphs
                if ((".graph") in filename):
                    filepath = os.path.join("./DATA", filename)
                    ls = LocalSearch1(filepath, args.time, args.seed, args.folder)
                    ls.main()
        elif (args.seed == 100): #rand seed
            for i in range(1,11):
                print(i)
                ls = LocalSearch1(args.inst, args.time, i, args.folder)
                ls.main()
        else:
            ls = LocalSearch1(args.inst, args.time, args.seed, args.folder)
            ls.main()
    elif args.alg == "LS2": 
        #run Independent Set Local Search Framework
        if (args.seed == 100): #rand seed
            for i in range(1,11):
                print(i)
                ls = LocalSearch2(args.inst, args.time, i, args.folder)
                ls.main()
        else:
            ls = LocalSearch2(args.inst, args.time, args.seed, args.folder)
            ls.main()
    