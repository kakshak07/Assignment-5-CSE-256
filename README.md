There are different files:

ibm1.py: Run this file to run IBM model 1, this file will generate an output file output_file_ibm1.out

ibm2.py: Run this file to run TBM model 2,k this file will generate an output file output_file_ibm2.out

output_file_ibm1.out: Contains results alignments using IBM model 1

output_file_ibm2.out: Contains results alignments using IBM model 2

Graphs.ipynb: This is Jupyter notebook which contains graph visualization of results obtained

misalignment.py: This file is used to check the similarity match of alignments obtained using IBM model 2 and real alignments of dev.key. This file contains thresholds of match. Using these thresholds of match we will find sentences which are perfectly aligned and which are misaligned.