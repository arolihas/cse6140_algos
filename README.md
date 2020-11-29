CSE 6140 Algos

This project has multiple approximation methods for the minimum vertex cover. To run these methods make sure you have the following:

1) Download the dataset and put it into a DATA directory on the same level as the code and output folder

2) Have anaconda downloaded and run the following line:

conda create --name <env> --file requirements.txt 

3) Inside the conda environment run the following line to run the methods:

python minVertexCover.py -inst[directory of file you want to run] -alg[LS1, LS2, BnB, Approx] -time[cutoff time in seconds] -seed[random seed for LS1 and LS2 methods]