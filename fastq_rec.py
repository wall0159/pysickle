from Bio import SeqIO


class fastq_pysickle:
    def __init__(self,infile, threshold, phred_type, window_size, outfile):
        # add the arguments to the object for acess from other methods
        self.infile = infile
        self.threshold = threshold
        self.phred_type =phred_type
        self.window_size = window_size
        self.outfile = outfile
        # if the user has specified a filename, redirect stdout to that file
        # outfile will be an empty string if the user hasn't specified anything
        if len(self.outfile) > 0:
            sys.stdout = open(self.outfile)

    def fastq(self):
        '''load the fastq file and pass all the information with quality scores converted to Phred Values'''
		# hard coded to take in only illumina scores but can be extended to work with others
		for record in SeqIO.parse(self.infile, "fastq-illumina"):
			#self.rec = record.format("fastq-illumina")
			self.id = record.id
			self.seq = record.seq
			self.phred = record.letter_annotations["phred_quality"]
			calculate_trim_adresses(self)
			trim(self)
			write_to_output(self)


#    def phred_id(self):
#        '''determine the encoding of the phred score, and populate the dictionary
#        guessing phred type may return AmbiguousPhredError'''

        
    def calculate_trim_adresses(self, threshold):
        '''return the addresses at the 5' and 3' ends at which to trim the sequence'''
        # input
        self.phred_nums
        # use the MA filter
        filtered_numeric_quality_score = filter_on_quality()
        
        # output
        self.addr_5
        self.addr_3
        
    def trim(self):
        '''use the calculated addresses to trim the fastq file'''
        self.trimmed_seq = self.seq[self.addr_5:self.addr_3]
        self.trimmed_phred = self.phred[self.addr_5:self.addr_3]

        
    def write_to_output(self):
        '''write out this record to output (file or stdout)'''
        print(self.id)
        print(self.trimmed_seq)
        print('+')
        print(self.trimmed_phred)
    
    
    
    
    
	
