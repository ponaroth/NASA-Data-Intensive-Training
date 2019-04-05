#!/bin/bash
#SBATCH -J test            # job name
#SBATCH -o test.o%j        # output and error file name (%j expands to jobID)
#SBATCH -n 1               # total number  requested
#SBATCH -N 1               # total number nodes requested
#SBATCH -p development     # queue (partition) -- normal, development, etc.
#SBATCH -A TG-ASC190007   # Allocation/Project name 
#SBATCH -t 00:00:45          # run time (hh:mm:ss) - 1.5 hours
#SBATCH --mail-user=jpowell@tacc.utexas.edu
#SBATCH --mail-type=begin  # email me when the job starts
#SBATCH --mail-type=end    # email me when the job finishes

date
pwd
hostname
who
module load python3
module list
python3 helloworld.py
