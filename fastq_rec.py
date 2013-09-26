from Bio import SeqIO
from scipy import pandas as pd

class fastq_rec:
    def __init__:
    
    def fastq(self, filename):
        '''load the fastq file and pass all the information with quality scores converted to Phred Values'''
		# hard coded to take in only illumina scores but can be extended to work with others
		for record in SeqIO.parse(filename, "fastq-illumina"):
			self.id = record.id
			self.seq = record.seq
			self.phred = record.letter_annotations["phred_quality"]
			calculate_trim_adresses(self)
			write_to_output(self)
    
    def phred_id(self):
        '''determine the encoding of the phred score, and populate the dictionary
        guessing phred type may return AmbiguousPhredError'''
		
        
    def calculate_trim_adresses(self):
        '''return the addresses at the 5' and 3' ends at which to trim the sequence'''
        # output
        self.5_addr
        self.3_addr
        
    def trim(self):
        '''use the calculated addresses to trim the fastq file'''
        
    
    
    
    
    
    
	
