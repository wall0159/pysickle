#/usr/bin/python

import filter
import sys

# process args
args = sys.argv[1:]
filename = args[1]

# test file exists, test file appropriate
try:
   with open('filename'): pass
except IOError:
   print 'Oh dear.'
if filename[-6:] != '.fastq':
    except IOError
    print "this program requires a fastq file as input"

# program input and output fastqfilenames as arguments

# open the file

#iterate through all the records

    # read a record into a fastq_seq object

    # use methods to process it

    # write out the filtered fastqfile to the output
