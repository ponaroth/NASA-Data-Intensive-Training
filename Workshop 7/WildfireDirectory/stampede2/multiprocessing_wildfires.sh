#!/bin/bash
#SBATCH -J wildfire_multiprocessing            # job name
#SBATCH -o out_multiprocessing.o%j             # output and error file name (%j expands to jobID)
#SBATCH -n 1                                   # total number  requested
#SBATCH -N 1                                   # total number nodes requested
#SBATCH -p development                         # queue (partition) -- skx-dev, development, etc.
##SBATCH -p skx-dev                            # remove the # character to use the Skylake queue
##SBATCH -p normal                             # remove the # character from this line and line 9 to use reservation on normal queue 
##SBATCH --res=ASC190016                       # remove the # character from this line and line 8 to use reservation on normal queue
#SBATCH -A TG-ASC190007                        # Allocation/Project name
#SBATCH -t 00:05:00                            # run time (hh:mm:ss) - 5 minutes
#SBATCH --mail-user=<INSERT YOUR EMAIL HERE>
#SBATCH --mail-type=all                      # email me if the job fails

date
pwd
hostname
who
module load python3
module list
python3 MultiprocessingWildfires.py
