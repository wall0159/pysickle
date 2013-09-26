#!/usr/bin/python

help_str = '''
HELP:
#> pysickle infile (threshold) (window_size) (outfile)
(bracketed arguments are optional)

pysickle is a program to trim the 3' and 5' ends of a read based on the phred 
score. A slinding window is used to determine the cut-off points, based on the
average phred score (at that location) dropping below a user-specified 
threshold. If no output file is provided, output is written to stdout.
'''

import pysickle_filter
import sys

### process arguments
args = sys.argv[1:]
infile    = args[1]
try:
    threshold   = args[2]
except:
    threshold   = 30
try:        
    window_size = args[3]
except:
    window_size = 0.1 # proportion of seq length    
output_file = args[4]

### ############## ###
### test arguments ###
### ############## ###
# test infile exists, test file appropriate
if infile[-6:] != '.fastq':
    raise IOError("this program requires a fastq file as input")
try:
    file_handle = open('infile')
except IOError:
    print 'Could not open fastq file'




# program input and output fastqinfiles as arguments

# open the file

#iterate through all the records

    # read a record into a fastq_seq object

    # use methods to process it

    # write out the filtered fastqfile to the output
