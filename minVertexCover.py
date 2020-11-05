import time
import sys
import glob
import argparse
# add imports for each method file here


parser = argparse.ArgumentParser(description='Run a Local Search Algorithm for Min Vertex Cover Problem')
parser.add_argument("--filename", "-f", help='Which file to run', default='./DATA/dummy1.graph') 
parser.add_argument("--method", help='Choose which method to run (BnB, Heuristics, LocalSearch)', default="BnB", choices=["BnB", "Heuristics", "LocalSearch"])
parser.add_argument("--cutoff_time", help='When to stop the run in seconds', type=int, default=100)
parser.add_argument("--seed", help='Random Seed for Local Search', type=int, default=32)
parser.add_argument("--test", help='Run only sample files', action='store_true', default=False)
args = parser.parse_args()

if __name__ == '__main__':
    

    # check to run testcases only
    if args.test:
        all_gr_files = glob.glob("./DATA/*.graph")
        sample_gr_files =  [pathname for pathname in all_gr_files if "dummy" in pathname or "email" in pathname or "jazz" in pathname]
        sample_sol_files = glob.glob("./DATA/ExampleSolutions/*.sol")
        print("Running all test files")

        for i in range(len(sample_gr_files)):
            print("Starting test case for " +sample_gr_files[i])
            graph_file = sample_gr_files[i]
            output_file = sample_sol_files[i]

            if args.method == "BnB":
                #run Branch and Bound
                print("Nothing implemented yet")
            elif args.method == "Heuristics": 
                #run Heuristics
                print("Nothing implemented yet")
            elif args.method == "LocalSearch": 
                #run LocalSearch
                print("Nothing implemented yet")
            

    else:
        file = args.filename
        if args.method == "BnB":
                #run Branch and Bound
                print("Nothing implemented yet")
        elif args.method == "Heuristics": 
            #run Heuristics
            print("Nothing implemented yet")
        elif args.method == "LocalSearch": 
            #run LocalSearch
            print("Nothing implemented yet")
        print(file)