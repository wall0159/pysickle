#!/usr/bin/python

help_str = '''
HELP:
#> pysickle infile (phred_type) (threshold) (window_size) (outfile)
(bracketed arguments are optional)
phred_type in [fastq-illumina|fastq-solexa|fastq-sanger|fastq]

pysickle is a program to trim the 3' and 5' ends of a read based on the phred 
score. A slinding window is used to determine the cut-off points, based on the
average phred score (at that location) dropping below a user-specified 
threshold. If no output file is provided, output is written to stdout.
'''

from fastq_rec import fastq_pysickle
import sys

### ################# ###
### process arguments ### 
### ################# ###
args = sys.argv

try:
    infile    = args[1]
except:
    raise IOError("you did not specify an input file")
try:
    threshold   = args[2]
except:
    threshold   = 30
    
try:
    phred_type  = args[2] 
except:
    phred_type  = 'Illumina1.8'
    
try:        
    window_size = args[3]
except:
    window_size = 0.1 # proportion of seq length 
   
try:
    outfile = args[4]
except:
    outfile = ''

### ############## ###
### test arguments ###
### ############## ###
# test infile exists, test file appropriate
if infile[-6:] != '.fastq':
    raise IOError("this program requires a fastq file as input")


# run through the file, record-by-record, trim according to params, and spit 
# out the result
pysickle = fastq_pysickle(infile, threshold, phred_type, window_size, outfile)
pysickle.fastq()


